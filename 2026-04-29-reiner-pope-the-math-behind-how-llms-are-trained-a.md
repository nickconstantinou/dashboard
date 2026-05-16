---
title: Reiner Pope – The math behind how LLMs are trained and served
date: '2026-04-29'
type: podcast
category: AI/Tech
channel: Dwarkesh Podcast
video_url: https://api.substack.com/feed/podcast/195859978/26c19662ae988720a5c793e5f1acbf55.mp3
---

## Introduction

The economics of AI inference—why faster responses cost more, why API pricing structures work the way they do, and what limits AI progress—are fundamentally determined by a handful of mathematical relationships that play out on GPU hardware. In a rare technical deep-dive, Reiner Pope, CEO of Maddox (a chip startup) and former TPU architecture lead at Google, walked through the core mathematics of how large language models are actually trained and served at scale.

The format was deliberately pedagogical: a blackboard lecture designed to make the invisible economics of AI infrastructure visible. Rather than describing these relationships abstractly, Pope built them up from first principles using roofline analysis—a standard technique in hardware architecture that examines the two fundamental bottlenecks any computation faces: how fast you can move data (memory bandwidth) versus how fast you can compute on that data (compute throughput).

This analysis matters because it reveals why the AI industry behaves the way it does. The pricing tiers offered by services like Claude Code and Codex, which charge 6× the price for 2.5× the streaming speed, are direct consequences of batch scheduling and the memory-compute tradeoff. Understanding these mechanics transforms AI from an opaque technology into a predictable engineering system governed by quantifiable constraints.

---

## The Two Fundamental Constraints: Memory and Compute

The foundation of the analysis rests on a simple but powerful insight: any inference run must satisfy two lower bounds simultaneously. The time to complete an inference cannot be faster than the time required to move the necessary data from memory into the compute units, nor can it be faster than the time required to actually perform the mathematical operations on that data. The actual runtime is the maximum of these two constraints, not their sum, because a well-designed system will keep both the memory and compute pipelines busy.

On the compute side, the dominant operation is matrix multiplication—running each token through the weight matrices of a neural network. For a model like DeepSeek v3, which has approximately 37 billion "active" parameters (the weights touched for each new token) out of 700 billion total parameters, the compute time scales linearly with the batch size. Pope expressed this mathematically as the batch size multiplied by the number of active parameters, divided by the GPU's compute throughput measured in floating-point operations per second. The key caveat is that attention computation, while present, is typically negligible compared to the weight matrix multiplications and can be ignored for back-of-envelope calculations.

On the memory side, the story is more complex because two distinct memory operations must occur for each inference. First, all of the model's total parameters—not just the active ones—must be fetched from high-bandwidth memory into the compute units. This is a constant cost per inference regardless of batch size. Second, the system must fetch the KV cache for every element in the batch. The KV cache (Key-Value cache) represents the model's internal representation of all prior tokens in the conversation, and it must be re-fetched for each batch element because each user has a unique conversational history. This cost scales linearly with both batch size and context length, making it the most variable component of memory traffic.

The KV cache deserves particular attention because it reveals how autoregressive decoding actually works. When generating text token by token, the model must attend to all previously generated tokens through this cached representation. Each new token requires a full forward pass through every layer of the network, but the attention mechanism specifically involves looking up the stored representations of prior tokens. This lookup is fundamentally a memory-bandwidth operation rather than a compute operation, which is why it appears in the memory time equation rather than the compute time equation.

---

## Latency Versus Batch Size: The Shape of the Tradeoff

With the fundamental equations established, Pope moved to visualizing how runtime changes as a function of batch size. This analysis directly explains why "fast mode" services can offer lower latency at premium prices.

The graph plots time on the vertical axis against batch size on the horizontal axis. The compute time component is a straight line starting from the origin—doubling the batch doubles the compute time. The weight fetch time is a horizontal line, representing a constant overhead that doesn't change with batch size. The KV fetch time is another line starting from the origin, but with a different slope determined by context length and the size of each token's cache representation.

Taking the maximum of these curves produces a characteristic shape: at very small batch sizes, the constant weight fetch time dominates, creating a plateau of minimum latency. As batch size grows, the KV fetch line eventually crosses above this plateau, and then finally the compute line takes over as the dominant constraint. This reveals the first key insight about latency: there exists a fundamental lower bound on how fast any inference can complete, determined by the time required to read all model parameters from memory at full bandwidth utilization.

The crossover points between these regimes are particularly important. At the exact point where the KV fetch slope matches the compute slope, the system is simultaneously memory-bound and compute-bound—an ideal operating point where neither hardware resource is wasted. Pope described this as the "Goldilocks zone" for a given context length. Moving away from this optimal context length causes the system to become severely underutilized: if context length doubles but the architecture remains fixed, the KV fetch time doubles, potentially pushing the system far into memory-bound territory where compute sits idle waiting for data.

This is where model architecture choices become consequential. Dense attention, where every token attends to every other token, scales the KV fetch time linearly with context length. Sparse attention mechanisms, which some frontier labs have implemented (Pope specifically cited DeepSeek's published work), scale this cost much more favorably—approximately with the square root of context length rather than linearly. This architectural difference can dramatically affect the cost and feasibility of serving long contexts.

---

## The Economics of Cost Per Token

Understanding latency is necessary but not sufficient for explaining AI economics. The more revealing analysis examines cost per token—how much a provider must charge to cover their GPU rental costs while serving a particular request.

Cost, in this framework, is simply the GPU rental rate multiplied by the inference time. For a provider paying approximately $2 per hour per GPU, a 20-millisecond inference consumes only a tiny fraction of a second's worth of rental cost. However, the key question is how many tokens are produced during that inference time, which is determined by the batch size. Dividing the runtime by the batch size gives the cost per token.

When this division is performed on the three components of runtime, the shapes transform dramatically. The compute time, which was linear in batch size, becomes a constant—the cost per token from compute doesn't change with batch size because both the numerator and denominator scale together. The KV fetch time behaves similarly, also becoming a constant when divided by batch size. But the weight fetch time, which was constant in runtime, becomes a hyperbola (1/B) when expressed as cost per token. This mathematical transformation reveals the economic engine behind AI inference pricing.

At batch size equal to one, the weight fetch cost approaches infinity in the cost-per-token graph—each user's request must pay the full cost of reading the entire model from memory, an unamortized expense that makes single-user serving economically devastating. As batch size grows, this cost drops precipitously. By the time a batch reaches modest sizes, the weight fetch cost becomes negligible compared to the constant compute and KV fetch costs. Eventually, at sufficiently large batch sizes, the system becomes purely compute-limited, and cost per token reaches its theoretical minimum.

This analysis immediately explains the fast mode pricing observed in the wild. Services like Claude Code and Cursor offering 6× faster streaming at 6× the price are simply refusing to batch the user with others. At the artificially low batch size enforced by "I want my answer immediately," the system operates in the portion of the curve where weight fetch costs remain high, and the amortized efficiency gains from large batches are abandoned. The user's willingness to pay a premium directly purchases freedom from batch scheduling.

---

## The Optimal Batch Size and the Hardware Constant

Having established the shapes of the latency and cost curves, Pope derived the specific batch size at which a system transitions from memory-limited to compute-limited operation. This calculation yields practical guidance for infrastructure design.

Setting memory time equal to compute time and ignoring the KV fetch term for clarity, the equation reduces to a relationship between model parameters (total and active), hardware parameters (memory bandwidth and compute throughput), and batch size. Rearranging to isolate the hardware terms on one side produces a dimensionless constant that represents the fundamental character of modern GPU architectures.

Pope explained that when compute throughput is expressed in operations per second and memory bandwidth in bytes per second, these can be made commensurable by accounting for the data type being used. For FP4 computation, where each value occupies half a byte, the ratio becomes approximately 300 on current GPUs. This means modern accelerators can perform roughly 300 floating-point operations per byte of memory bandwidth—a ratio that has grown as hardware has evolved but remains a fundamental constraint.

Solving the equation with this constant yields the critical batch size where compute and memory are balanced. Pope noted that this optimal batch size is "not particularly sensitive to model architecture," meaning the same mathematical relationships hold across different model designs. The absolute value of the optimal batch depends on the ratio of active to total parameters (smaller for mixture-of-experts models, larger for dense models), but the framework remains consistent.

This is the mathematical basis for understanding why inference providers batch aggressively: the economics of weight fetch amortization create enormous incentives to fill GPU capacity. A provider serving a single user at a time pays roughly 1,000 times more per token than one serving a fully-optimized batch. The entire API pricing structure reflects this reality, with base prices implicitly assuming reasonable batch utilization.

---

## Implications for AI Progress and Architecture

Beyond explaining current pricing, the mathematical framework illuminates why AI is progressing the way it is and suggests where future improvements must come from.

The lower bound on latency—determined by the time required to read model weights from memory—establishes a floor that cannot be crossed by algorithmic improvements alone. To make inference faster, either the weights must be reduced (through better compression, quantization, or architectural efficiency) or the memory bandwidth must be increased (through hardware improvements). This explains why memory bandwidth remains a critical metric for AI accelerators and why advances in memory technology directly translate to inference speedups.

The context-length sensitivity of dense attention reveals a vulnerability in current architectures. As context windows grow toward hundreds of thousands of tokens, the linear scaling of KV fetch creates mounting inefficiency. The move toward sparse attention, mixture-of-experts architectures, and other architectural innovations can be understood as attempts to bend this curve—to achieve longer contexts without proportional increases in memory traffic.

Pope hinted at additional techniques beyond batch optimization. Speculative decoding and multi-token prediction represent alternative approaches to the latency-cost tradeoff, potentially achieving some of the benefits of larger batches without requiring multiple users to wait together. These methods generate multiple candidate tokens in parallel and verify them sequentially, amortizing the cost of weight fetches across more tokens generated per computation.

---

## Detailed Takeaways

**The Cost of Immediacy is Exponential, Not Linear**: When you pay premium prices for fast mode, you're not paying a small premium for scheduling priority. You're paying to escape the batch optimization that makes inference economically viable. At batch size one, weight fetch costs dominate and are completely unamortized. The fast mode customer is effectively subsidizing their own inefficiency, which is why the pricing multiplier (6× for 2.5× speed) appears asymmetric—it's capturing the full cost of abandoning batching, not merely adding a priority fee.

**Memory Bandwidth is the Bottleneck That Hardware Cannot Easily Solve**: While compute throughput has grown dramatically through Moore's Law and domain-specific accelerators, memory bandwidth improvements have been more modest. The ratio of compute to memory bandwidth (~300:1) means that simply making chips faster doesn't solve the memory bottleneck for inference. This is why model compression, weight pruning, and architectures that reduce memory traffic (like sparse attention) are strategically important—they attack the fundamental constraint.

**Context Length Creates Discrete Cost Regimes**: A system optimized for 32K context will have dramatically different cost characteristics than one optimized for 128K context. Moving from optimal to suboptimal context length doesn't cause gradual degradation—it causes a discrete transition from balanced operation to memory-bound operation where compute utilization drops significantly. This explains why providers may charge nonlinear premiums for very long contexts: the infrastructure must be re-optimized for the new operating point.

**The Math Predicts Infrastructure Winners**: Companies that solve the batching problem most effectively—maintaining high utilization while keeping latency acceptable—will have structural cost advantages. This includes both the batching algorithms that pack users efficiently and the architectural choices that maximize the batch sizes at which compute dominates. The race to build AI infrastructure is partly a race to optimize these mathematical relationships.

---

## Who This Is For

This content is essential for anyone making decisions about AI infrastructure, whether as a founder building products on top of LLM APIs, an engineer evaluating inference providers, an investor assessing AI infrastructure companies, or a technical product manager pricing AI features. The ability to distinguish genuine efficiency differences from pricing theater requires understanding the underlying math.

For practitioners, the framework provides concrete guidance: when evaluating whether a premium AI service is worth paying for, the question becomes whether you're getting the efficiency of batch optimization (at lower latency tiers) or paying for the privilege of avoiding it (at premium tiers). For infrastructure builders, the equations reveal what metrics actually matter—memory bandwidth utilization and compute utilization, not just aggregate throughput numbers.

Even for those who will never implement roofline analysis themselves, understanding that latency and cost are governed by these specific mathematical relationships transforms AI from an unpredictable technology into a manageable engineering domain where progress can be planned and priced rationally.