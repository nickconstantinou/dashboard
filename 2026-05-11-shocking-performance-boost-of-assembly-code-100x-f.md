---
title: 'Shocking performance boost of assembly code: ~100x faster than C code | Lex
  Fridman Podcast'
date: '2026-05-11'
type: youtube
category: AI/Tech
video_id: IUo0UwZOaRw
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=IUo0UwZOaRw
---

## Key Insights

- **62x performance gain**: Handwritten assembly achieves 62x speedup over C-compiled code for the same functions, demonstrating that modern compilers cannot match human-optimized SIMD code
- **240,000 lines of handwritten assembly**: The "David" AV1 decoder represents one of the largest pure assembly codebases in existence—larger than FFmpeg's entire 100,000-line assembly corpus across all codecs
- **SIMD parallelization**: Single Instruction Multiple Data allows one instruction to process 16 elements simultaneously, ideal for pixel grid operations in video decoding
- **3 billion devices depend on this code**: David powers AV1 playback for 30% of Netflix traffic and 50% of YouTube, running on devices without hardware AV1 decoders
- **"Every cycle matters" philosophy**: The team achieves 720p decoding on 1-2 CPU cores by counting every computational cycle, enabling software playback where hardware decoders don't exist

---

## Introduction

In the world of software development, a persistent assumption has held that compiled C code is "fast enough" for most applications. A conversation between Lex Fridman and developers behind the VideoLAN project—creators of the ubiquitous VLC media player and contributors to FFmpeg—challenges this assumption with startling evidence. The discussion reveals how handwritten assembly code, particularly using SIMD (Single Instruction Multiple Data) techniques, can achieve performance gains that dwarf what modern compilers produce, sometimes reaching 62 times faster execution than equivalent C code.

This isn't merely an academic exercise in optimization. The VideoLAN team's assembly work underpins video playback on billions of devices worldwide, including software AV1 decoding for major streaming platforms like Netflix and YouTube. The "David" project—a fully software-based AV1 decoder—demonstrates that with meticulous cycle-counting and SIMD optimization, it's possible to achieve real-time 720p video decoding on just one or two CPU cores, opening the doors for hardware-constrained environments that lack dedicated AV1 decoder chips.

## The Lost Art of Assembly Programming

The conversation begins with a framing that frames assembly optimization as a "lost art"—a craft that modern software development has largely abandoned in favor of higher-level languages and compiler-based solutions. The speakers, who have started companies around the FFmpeg/VLC ethos of low-level programming, explain that most commercial development simply writes functionality in C and considers the job done, accepting that compiled code is "fast." The evidence presented, however, suggests this acceptance is premature.

When asked to explain what assembly programming actually is and why it matters, the speakers describe how writing assembly means communicating directly with the processor using its native instruction set. In contrast, when developers write in languages like C, a compiler translates that code into assembly language and machine code instructions on the developer's behalf. This translation process introduces inefficiency because the compiler must generate code that works generally, rather than code optimized for a specific computational pattern.

The speakers highlight a particular flavor of assembly used extensively in FFmpeg called SIMD—Single Instruction Multiple Data. This technique fundamentally changes how computation happens by allowing a single instruction to operate on multiple data elements simultaneously. For scalar assembly (the alternative), working with numbers means processing each element individually: adding five to ten requires one add instruction for one result. With SIMD, the same operation can process a vector containing sixteen different numbers simultaneously, with a single instruction adding five to all sixteen elements at once.

The implications for video processing are profound. Video frames consist of pixel grids, and operations like color conversion, scaling, and filtering must be applied across thousands or millions of pixels. SIMD's parallel processing capability means what would require millions of sequential operations can instead be accomplished with a fraction of the instructions, yielding the dramatic speedups observed.

## Beyond Intrinsics: Why Handwritten Assembly Wins

A significant portion of the conversation addresses a debate that has apparently consumed the development community for two years: whether handwritten assembly truly outperforms intrinsics and compiler auto-vectorization. Intrinsics are C functions that behave similarly to assembly instructions, allowing developers to invoke SIMD operations through a C syntax that the compiler then translates into assembly. The key difference is that with intrinsics, the compiler allocates CPU registers (temporary storage for computational values) automatically, removing direct control from the programmer.

The speakers maintain a controversial position: intrinsics and compiler optimization cannot match handwritten assembly because the compiler's register allocation and instruction selection, while improved, still cannot match human judgment about which instructions best exploit the specific computational patterns in video codecs. The evidence is empirical—hundreds of examples demonstrating handwritten assembly's superior performance—but this stance has generated substantial pushback from developers who believe modern compilers have solved these optimization challenges.

The speakers note that even contributors to the Alliance for Open Media (the consortium behind AV1, including Google, Netflix, Amazon, and Mozilla) initially believed the AV1 format was "so complex, it must be done in hardware to do decoding." The VideoLAN team's response, undertaken with developers including Ronald, Henrik, and Martin, was to create an extremely capable software decoder anyway—recognizing that hardware adoption would take time and that devices without AV1 decoder chips needed alternatives.

## The David Project: Scale and Achievement

The "David" AV1 decoder emerges as the centerpiece example of what handwritten assembly optimization enables. The project contains approximately 30,000 lines of C code paired with 240,000 lines of handwritten assembly—a ratio that illustrates just how much optimization work goes beyond the algorithmic logic. For context, the entire FFmpeg codebase contains roughly 100,000 lines of assembly across all codecs combined; David's single codec has more than double that amount of hand-optimized assembly code.

The project philosophy centers on the motto "every cycle matters"—an approach that acknowledges the cumulative impact of micro-optimizations across billions of decodes. Because David is embedded in VLC and various software AV1 playback stacks, and because AV1 adoption is accelerating (now accounting for 30% of Netflix's video traffic and 50% of YouTube's), the decoder runs on an estimated 3 billion devices. Optimizations that might seem trivial at the individual playback level compound into massive computational savings at this scale.

The concrete achievement is that David achieves real-time 720p video decoding using only one or two CPU cores. This means devices without hardware AV1 decoders—which currently includes most consumer electronics—can still play AV1 video smoothly through software alone. The efficiency comes from the cycle-counting approach: instead of accepting that software decoding requires heavy CPU utilization, the team ensured every instruction contributed to the result and no computational cycles were wasted.

## The Cross-Platform Challenge

Beyond the assembly optimization itself, the speakers discuss operational challenges in maintaining projects of this scope. VLC is notable for its extraordinary cross-platform support, running on everything from Windows XP (still supported in current releases) through Windows 11, Mac OS versions from 10.7 onward, iOS from version 9 through the latest, numerous Linux distributions, BSD, Solaris, and even OS/2 (which apparently has approximately ten users worldwide, one of whom maintains VLC support).

This breadth of support creates significant development headaches. For iOS 9 support, the team has needed to construct what they describe as a "Frankenstein version" of Xcode, mixing components from multiple SDK versions to enable compilation for a platform Apple no longer supports in its development tools. The effort reflects a broader philosophy: not forcing users to purchase new hardware when their existing devices can handle the workload if software is optimized correctly.

The speakers note the satisfaction of receiving messages from users who continue using devices like the original iPad 2 for video playback, appreciating that the software enables this continued utility rather than obsolescence. This connects to the assembly optimization theme: performance improvements aren't just about speed but about resource efficiency and device longevity.

## Detailed Takeaways

**Compiler trust has limits in performance-critical applications.** While modern C compilers produce reasonably optimized code for general purposes, specialized tasks like video decoding reveal that human-optimized assembly consistently outperforms compiler output by substantial margins. The 62x improvement measured in FFmpeg functions demonstrates that accepting "fast enough" code leaves significant performance on the table. For applications where every cycle matters—embedded systems, real-time video processing, high-frequency trading—handwritten assembly remains not just viable but necessary.

**SIMD transforms the economics of parallel computation.** The ability to process 16 elements with a single instruction isn't merely a technical detail; it represents a fundamental shift in what's achievable with limited computational resources. This is why a software decoder can achieve 720p real-time playback on 1-2 cores—the parallelization via SIMD multiplies the effective throughput of each cycle. Developers working with data-parallel problems should investigate SIMD techniques as a first-order optimization, not an afterthought.

**Cross-platform support requires extraordinary engineering commitment.** Maintaining support for operating systems spanning decades (Windows XP to Windows 11) and even obscure platforms (OS/2) demands creative problem-solving and resource allocation that most commercial software teams would abandon. The payoff is serving users who cannot or will not upgrade their hardware—a market segment that becomes more significant as devices last longer and economic pressures encourage device longevity.

**Performance optimization is also an environmental and social issue.** The speakers frame optimization not just as a technical exercise but as a stance against planned obsolescence and e-waste. When software runs efficiently on old hardware, users needn't replace functional devices. This perspective positions assembly optimization as partly an ethical choice: each cycle saved in video decoding contributes to reduced computational waste and extended device lifespans.

**Community-driven projects can outperform corporate efforts.** The VideoLAN team, described as a "very small team," maintains broader operating system support than Microsoft, Google, or Apple—with far fewer resources. This demonstrates that focused engineering effort, particularly when motivated by open-source principles rather than commercial cycles, can achieve results that corporate development models struggle to match.

---

## Who This Is For

This discussion benefits software engineers and technical leaders working on performance-critical applications, particularly in multimedia, embedded systems, or real-time computing domains. Video codec developers and those working with data-parallel workloads will find the SIMD discussion and optimization philosophy directly applicable. System programmers interested in understanding how modern compilers compare to human optimization will gain perspective on the limits of automated code generation.

More broadly, the conversation serves anyone interested in understanding the practical limits of software optimization and the engineering philosophy behind widely-used open-source infrastructure. The AV1 codec and its software implementation represent a significant technological transition underway in internet video delivery—understanding how and why software decoding works at scale provides insight into the invisible infrastructure shaping media consumption worldwide.

For managers and technical decision-makers, the discussion illustrates that accepting "fast enough" code has costs, and that optimization investments yield compounding returns at scale. The contrast between a small open-source team and corporate giants on cross-platform support also suggests organizational models that enable focused, mission-driven engineering outperform bureaucratic development structures for certain technical challenges.