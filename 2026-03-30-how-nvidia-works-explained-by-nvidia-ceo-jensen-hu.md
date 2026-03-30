---
title: "How NVIDIA works - explained by NVIDIA CEO | Jensen Huang and Lex Fridman"
date: 2026-03-30
type: youtube
category: "AI/Tech"
video_id: "ugkrQzvuaDw"
channel: "Lex Fridman"
video_url: "https://www.youtube.com/watch?v=ugkrQzvuaDw"
---

# How NVIDIA Works: Jensen Huang on Extreme Co-Design, Organizational Structure, and the AI Revolution

## Introduction

In a wide-ranging conversation with Lex Fridman, NVIDIA CEO Jensen Huang offered an unusually candid look inside the company that has become central to the artificial intelligence revolution. The discussion, which touched on everything from the physics of distributed computing to the philosophy of organizational design, revealed how NVIDIA transformed itself from a graphics card manufacturer into the backbone of modern AI infrastructure. This wasn't a product announcement or earnings call—it's a masterclass in how one of the world's most influential technology companies actually thinks about problems.

The conversation centered on a concept Huang calls "extreme co-design," a term that captures how NVIDIA has moved far beyond the traditional boundaries of chip manufacturing. Where competitors might optimize individual components, NVIDIA now designs entire systems—racks of interconnected GPUs, CPUs, memory, networking equipment, power delivery, and cooling—all optimized together. This approach, Huang explained, is not merely a competitive strategy but a mathematical necessity born from the demands of scaling AI workloads to unprecedented levels.

What makes this conversation particularly valuable is Huang's willingness to trace the reasoning behind these decisions rather than simply describing outcomes. He explained how Amdahl's Law—the fundamental limit on parallel computing speedup—dictates that you cannot simply add more computers to solve harder problems faster. Instead, you must redesign the entire stack, from algorithms down to physical infrastructure. This insight, he argued, is why NVIDIA's approach to company organization must mirror its approach to system design: both require bringing together experts from radically different disciplines and getting them to solve problems collectively rather than in silos.

## The Physics of Scaling: Why Extreme Co-Design Became Necessary

Huang opened the technical portion of the conversation by explaining why the traditional approach to computing—designing better chips and then scaling them up—has reached its limits. The fundamental problem, he explained, is that AI workloads have grown too large to fit inside a single computer, no matter how powerful that computer might be.

"When you add 10,000 computers, you'd like the system to go a million times faster," Huang said. "But if you just naively distribute the problem, you'll scale linearly—you'll only get 10,000 times faster." This gap between linear scaling and the exponential improvements AI demands forces a complete rethink of how systems are designed.

The key insight comes from Amdahl's Law, which describes how the speedup of any system is ultimately limited by the portions of the workload that cannot be parallelized. Huang illustrated this with a stark example: "If computation represents 50% of the problem, and I sped up computation infinitely, I only sped up the total workload by a factor of two." This mathematical reality means that optimizing a single component—say, the GPU—yields diminishing returns once that component stops being the bottleneck.

The solution requires what Huang calls "sharding" the entire problem across multiple dimensions. This means not just distributing the computation, but also sharding the algorithm, the pipeline, the data, and the model itself. Once you distribute the problem this way, "everything gets in the way," Huang said. The CPU becomes a problem. The GPU becomes a problem. The networking becomes a problem. The switching becomes a problem. Distributing the workload across all these computers becomes its own problem.

This is why NVIDIA has moved from chip-scale design to rack-scale design. The system now includes not just GPUs and CPUs, but high-bandwidth memory, networking chips, switches, optics, copper interconnects, power delivery systems, and cooling infrastructure. Each of these domains has world-class experts, and all of them must work together to create systems that actually achieve the scaling that modern AI requires.

## The Organizational Miracle: How 60 Reports Attack Problems Together

When Fridman asked how NVIDIA brings together specialists from such disparate fields—memory experts, CPU architects, networking engineers, optical specialists, power delivery engineers, cooling engineers—Huang's answer revealed a distinctive approach to organizational design that he clearly considers central to NVIDIA's success.

"My direct staff is 60 people," Huang said. "I don't have one-on-ones with them because it's impossible. You can't have 60 people on your staff if you're going to get work done, and so you still have 60 reports." This isn't a management technique designed for efficiency in the traditional sense. Instead, it's a structural decision that reflects how the company must operate.

The key insight is that extreme co-design of computers requires an organization that practices extreme co-design of its own work. When you're designing a system where power delivery affects cooling decisions, which affects networking layout, which affects the algorithms you can use, you cannot have siloed teams working independently. "No conversation is ever one person," Huang explained. "We present a problem and all of us attack it, because we're doing extreme co-design, and literally the company is doing extreme co-design all the time."

This means that even discussions focused on specific components like cooling or networking are attended by everyone on staff. The memory expert hears the cooling discussion. The CPU architect hears the networking discussion. "They can contribute," Huang said. "'This doesn't work for power distribution. This doesn't work for memory. This doesn't work for this.'" And if someone who should be contributing tunes out, Huang will call them out directly: "Hey, come on, let's get in here."

The underlying philosophy, Huang explained, is that a company should be designed as "the machinery, the mechanism, the system that produces the output—and that output is the product that we like to create." The architecture of the company should reflect the environment in which it exists. Since NVIDIA's products require integrating across multiple engineering disciplines, the company's internal structure must mirror that integration.

This approach extends to hiring. Almost all of Huang's 60 direct reports have at least a foot in engineering. They are experts in their domains—memory, CPUs, optics, GPU architecture, algorithms—but they are also expected to understand enough about adjacent fields to contribute to cross-disciplinary discussions. The goal is to create what Huang calls "generalists who are also deep specialists"—people who can see across the entire stack while also having deep expertise in one area.

## The Evolution of NVIDIA: From Gaming GPUs to AI Factories

Huang walked Fridman through the strategic arc that brought NVIDIA from its origins as a graphics accelerator company to its current position designing "AI factories"—systems that produce artificial intelligence as their primary output. This evolution, he explained, was neither accidental nor inevitable. It required finding "that really narrow path step by step" that expanded NVIDIA's aperture of computing without abandoning its core specialization.

The journey began with the recognition that specialized accelerators face a fundamental tension: they are incredibly efficient for their specific task, but their narrow market reach limits their research and development capacity, which ultimately limits their impact on computing as a whole. "The better computing company we become, the worse we become as a specialist," Huang said. "The more of a specialist, the less capacity we have to do overall computing." Finding the path that maintains specialization while expanding capability required multiple strategic moves over many years.

The first step was the programmable pixel shader, which introduced programmability into graphics processing. The second was adding FP32 (32-bit floating point) support to shaders—a decision that turned out to be transformative because it made the GPU compliant with standards familiar to general-purpose computing programmers. "All of the people who were working on stream processors and other types of data flow processors discovered us," Huang said. "They said, 'All of a sudden we might be able to use this GPU that's incredibly computationally intensive, and it's now compliant, so I can take my software that I was writing on CPUs and use the GPU for that.'"

This led to CUDA (Compute Unified Device Architecture), NVIDIA's parallel computing platform that allows developers to use GPUs for general-purpose computing. But CUDA itself was just the latest step in a gradual expansion of what NVIDIA considered its domain.

## The Pivotal Decision: CUDA on GeForce

Huang identified the decision to put CUDA on GeForce—NVIDIA's consumer graphics cards—as the critical strategic turning point that made NVIDIA's transformation possible. This decision, he explained, was made at a time when NVIDIA could not afford it, and it cost the company enormous amounts of profit.

"We put CUDA on GeForce, and that was a strategic decision that was very, very hard to do because it cost the company enormous amounts of our profits, and we couldn't afford it at the time," Huang said. "But we did it anyways because we wanted to be a computing company."

The reasoning was architectural rather than immediate. A computing company needs a computing architecture that is compatible across all of its chips. By putting CUDA on GeForce—bringing it to the mass-market consumer product rather than keeping it only on expensive professional hardware—NVIDIA ensured that CUDA would have a large installed base of developers who could write software for the platform. This developer ecosystem, built over years before the deep learning revolution, became the foundation for NVIDIA's AI dominance.

The decision reflects a pattern in Huang's thinking: he evaluates strategic choices not by their immediate financial impact but by their effect on long-term capability and ecosystem development. CUDA on GeForce was expensive in the short term, but it created the conditions for everything that followed. The developers who learned CUDA on gaming GPUs brought their skills to professional computing, and when the deep learning era arrived, NVIDIA had the only platform with a mature ecosystem of GPU computing developers.

## Key Takeaways

**The diminishing returns of component optimization:** As AI systems scale, the traditional approach of optimizing individual components yields less and less improvement. Huang's explanation of Amdahl's Law reveals why NVIDIA had to move from chip design to system design—the bottleneck shifts continuously, and only by optimizing the entire stack can you continue to achieve meaningful performance improvements. This insight applies beyond hardware: any organization or system that reaches significant scale will eventually face similar constraints where individual optimization stops delivering proportional results.

**Organizational structure must mirror product architecture:** Huang's description of his 60-person staff and the company's "attack problems together" approach reflects a deep principle: the structure that creates integrated products must itself be integrated. Traditional corporate hierarchies with narrow functional silos cannot produce systems where power delivery, cooling, networking, and algorithms are co-optimized. The organization itself must be designed for the cross-disciplinary collaboration that the product requires. This suggests that companies pursuing ambitious technical goals should evaluate whether their internal structure matches the structure of the problems they're trying to solve.

**Long-term platform thinking creates unexpected advantages:** The decision to put CUDA on GeForce demonstrates how investing in platform development—even when it's unprofitable in the short term—can create decisive advantages years later. NVIDIA's AI dominance today rests on the developer ecosystem built during the CUDA era, which existed because NVIDIA chose to bring its computing platform to the mass market rather than keeping it exclusive and expensive. For organizations considering platform investments, this suggests that the measure of success is not immediate ROI but the size and engagement of the developer or user community that forms around the platform.

**The tension between specialization and generality is navigable:** Huang traced a path that allowed NVIDIA to maintain its specialized optimization capabilities while expanding into broader computing applications. This wasn't a single decision but a series of deliberate steps—programmable shaders, FP32 support, CUDA—that each preserved core capabilities while extending reach. The key was finding "that really narrow path" that expanded aperture without abandoning specialization. Organizations facing similar tensions might benefit from thinking about expansion as a sequence of steps rather than a single leap, each building on the capabilities established by previous moves.

**Experts must remain engaged across disciplinary boundaries:** Huang emphasized that in his organization, specialists in one domain are expected to contribute to discussions outside their primary expertise. The memory expert participates in cooling discussions; the CPU architect weighs in on networking. This cross-pollination of expertise is what enables the kind of integrated design that gives NVIDIA its competitive advantage. It requires not just structural arrangements but a culture where experts feel empowered to contribute outside their domain and are expected to do so by leadership.

## Who This Conversation Is For

This discussion between Jensen Huang and Lex Fridman will be most valuable for technology leaders, engineers, and entrepreneurs trying to understand how one of the world's most consequential technology companies approaches problems. If you're building systems that involve scaling, distributed computing, or cross-disciplinary design, Huang's explanations of why traditional approaches fail and how NVIDIA addresses those failures offer directly applicable insights.

Product managers and strategy executives will find particular value in Huang's discussion of platform strategy and the long-term thinking required to build ecosystems. The CUDA on GeForce story is a case study in how short-term financial sacrifice can create conditions for long-term market dominance, and Huang's framework for thinking about the relationship between specialization and market reach applies broadly to any company trying to expand its scope.

Finally, anyone interested in organizational design will benefit from Huang's candid description of how NVIDIA structures its leadership team and runs its meetings. The idea that organizational structure should reflect the structure of the problems being solved—that a company making integrated systems must itself be organized for integration—is a principle that extends far beyond the technology industry.

What makes this conversation particularly valuable is Huang's willingness to explain not just what NVIDIA does, but why it does it and how it thinks about the underlying principles. This isn't marketing material or public relations; it's a detailed account of the reasoning behind decisions that shaped the modern AI landscape. For readers willing to engage with that reasoning seriously, it offers insights that go well beyond NVIDIA's specific products to fundamental questions about how complex systems should be designed and organized.