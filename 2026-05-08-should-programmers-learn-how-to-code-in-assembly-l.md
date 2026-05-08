---
title: Should programmers learn how to code in assembly? | Lex Fridman Podcast
date: '2026-05-08'
type: youtube
category: AI/Tech
video_id: _x3JYd1KW60
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=_x3JYd1KW60
---

# Should Programmers Learn Assembly Language? A Deep Dive into Low-Level Programming

## Key Insights

- **FFmpeg requires assembly**: Many codecs in FFmpeg remain only partially assembly-optimized, creating ongoing opportunities for contributors with low-level programming skills
- **Minimal prerequisites work**: High school mathematics and C pointers are sufficient—evidence includes high schooler Daniel Kang successfully writing FFmpeg assembly code
- **LLMs fail at assembly writing**: Despite surprisingly decent comprehension, large language models "hallucinate" when generating assembly code because training data is too sparse compared to languages like Python or JavaScript
- **Itanium's hidden lesson**: Intel/HP's failed 64-bit processor achieved 6 billion operations/second but the memory bus only allowed 1.5, illustrating why manual optimization matters when CPU outpaces memory by 4×
- **Rust's 85% problem**: The speaker draws a "Esperanto vibe" parallel, noting Rust rewrites often deliver only 85-90% feature parity—the final 1% consumes 99% of development time

---

## Introduction

In a conversation that spans from the philosophical foundations of learning to the gritty realities of performance optimization, a veteran systems programmer makes the case that assembly language remains relevant—not as a daily driver, but as essential understanding for anyone who wants to truly master computing. The setting is the Lex Fridman Podcast, and the speaker is someone who has spent years maintaining some of the world's most performance-critical software: FFmpeg.

The discussion emerges from the speaker's own project—ASM-lessons—a repository designed to teach assembly programming through practicalFFmpeg problems rather than through grammar-focused instruction. This distinction becomes the central thesis: traditional assembly education fails because it treats instruction sets like foreign language syntax, when in reality, low-level programming is better learned through direct communication with real problems. The conversation ventures into territory few programming discussions dare to go—examining whether artificial intelligence can assist with assembly, what modern languages like Rust get wrong about adoption, and why understanding your computer's memory hierarchy makes you a fundamentally better programmer.

This matters because the industry has largely abandoned assembly in favor of high-level abstractions. Yet video codecs, cryptography implementations, and embedded systems still depend on hand-optimized code running at the absolute limits of hardware capability. The question isn't whether everyone should write assembly—it's whether understanding it makes you better at everything else.

---

## The Problem with How Assembly Is Currently Taught

The speaker opens with a critique that will resonate with anyone who has tried to learn assembly from traditional resources: textbooks and online courses approach instruction sets like grammar in a foreign language, walking through every instruction sequentially even when most won't be encountered in practice. "You learn a language by asking someone what their name is and you start from there and you solve real problems that you want to communicate," the speaker explains. "You don't learn sentence structure. This is the interrogative and the adverb." Yet this grammar-first approach dominates virtually all assembly instruction.

The speaker identifies a second problem equally damaging: assembly knowledge has been transmitted exclusively through apprenticeship. "Assembly is taught sort of hand-to-hand like person-to-person like blacksmithing one-by-one," the speaker observes. "That's the only logical sort of analogy and that doesn't really scale online." This means the community of assembly programmers has remained small precisely because there was no scalable pathway into the craft. Knowledge stayed locked in mentor-student relationships, passed down from "wizards" and "sages"—an image the speaker wryly embraces by wearing a wizard's hat during the discussion.

This apprenticeship model works when you have unlimited time and dedicated teachers, but it collapses when trying to build a community. The speaker notes that code contributed to X264 through these lessons came from students who had learned through the targeted, problem-first approach rather than through comprehensive instruction manuals. The contrast reveals something fundamental about how humans learn complex technical skills: we grasp concepts in service of solving problems we care about, not in isolation.

---

## ASM-Lessons: A New Approach Through FFmpeg

Rather than teaching assembly syntax from the ground up, the ASM-lessons repository takes students directly into FFmpeg's codebase, where vector-focused optimizations perform operations across multiple data points simultaneously. The approach describes registers—general purpose and vector variants—using practical examples rather than abstract reference material. It skips irrelevant instructions and focuses on what actually matters for video codec development: the kind of register manipulation and instruction scheduling that makes playback smooth at extremely low bitrates.

The framework underpinning these lessons is called X86 Inc, written by Laurent, who previously worked on X264. This framework abstracts away some of the tedium around different calling conventions—the rules governing how functions pass parameters and return values—allowing students to focus on the algorithmic challenges rather than bookkeeping. Students have successfully submitted patches to X264 using this approach, with contributors explicitly citing the lessons as their entry point into low-level programming.

The speaker emphasizes that prerequisites are deliberately minimal: high school mathematics and a solid understanding of pointers in C. "Not even C really is pointers," the speaker clarifies. This accessibility challenges the mystique that has grown around assembly programming—the belief that only elite programmers with decades of experience can work at this level. Daniel Kang, a high schooler, stands as concrete proof that the barriers to entry have been artificially high, not inherently so.

The motivation extends beyond pedagogy. "It's really about trying to get this dying art to continue because we've shown it's possible with David to produce something amazing," the speaker says, referencing a collaborator whose FFmpeg contributions demonstrate the heights achievable through careful assembly optimization. The implication is clear: if no one learns assembly, the codebases that depend on it will eventually rot, and the ecosystem of performance-critical software will suffer.

---

## The Beauty of Assembly: Flying a Spitfire

When the conversation turns to what assembly programming actually feels like, the speaker's language becomes almost reverential. "Some of this assembly language is really beautiful," the speaker says. "It's kind of like flying a Spitfire. It's really aviation at its purest but also pushing the aircraft beyond what the designer thought was possible."

This metaphor captures something essential about low-level programming: the directness of the interface. "It's really you and the processor. There's nothing in between. It's you and the joystick of the cockpit and you move that joystick and it's physically connected to the ailerons." When writing assembly, there are no runtime interpreters, no garbage collectors waking up at inconvenient moments, no abstract virtual machines. The programmer speaks directly to silicon.

The beauty emerges specifically from constraint. FFmpeg contributors sometimes "abuse" instructions—using operations designed for one purpose (cryptography, for instance) to accomplish entirely different tasks. This creative misuse of hardware reveals the hardware designers' assumptions, finds the gaps between their mental model and reality, and exploits those gaps for performance gains. The speaker describes this as both art and engineering, a form of expression that happens to run at billions of cycles per second.

The Spitfire comparison also captures the physicality of manual optimization. Aircraft pilots of that era could feel every control surface through mechanical linkages. Modern assembly programmers similarly feel the cache misses, the pipeline stalls, the branch mispredictions—though through profiling tools rather than physical vibration. The abstraction layers that make programming easier also make it harder to understand what's actually happening inside the machine.

---

## Can LLMs Help Write Assembly?

The question of artificial intelligence's role in low-level programming yields an unexpected answer: LLMs understand more assembly than expected but cannot yet generate it reliably. "They have more of an understanding than I expected but they are still—I've asked it questions and it still goes and starts making modifications and then I go 'is it bit exact?' No, fix it—and then it just goes and does the same thing."

The fundamental problem is data scarcity. Stack Overflow contains millions of questions and answers for mainstream languages, giving LLMs abundant training material. Assembly programming communities, however, are tiny by comparison, and much relevant knowledge exists in private repositories or undocumented tribal wisdom. "There is not enough data to train on," the speaker explains flatly. "This is the biggest issue."

This creates a paradox: the domain where AI assistance would be most valuable—where errors are subtle and consequences severe—is precisely where current AI capabilities are weakest. Bit-exactness matters in codec development in ways that are difficult to verify automatically. A single wrong bit can corrupt an entire video frame, and the debugging process requires understanding not just the algorithm but the microarchitectural details of how the CPU executes it.

The speaker's experience with Itanium, a now-extinct processor architecture developed by Intel and HP for the ill-fated transition to 64-bit computing, illustrates why assembly remains resistant to automation. "Those were processors who had a ton of computing power to do floats FMAs which is similar to what we need now for LLMs," the speaker explains. "You could pack three operations per line that could be loaded. So basically you had an output of basically 6 billion of operation per seconds. But the memory bus only allowed 1.5, right? So you CPU was four times faster."

This bandwidth asymmetry required programmers to manually orchestrate memory reuse, register allocation, and instruction scheduling in ways that no compiler could manage automatically. The techniques required understanding the complete pipeline from application logic through memory hierarchy to actual silicon execution—and they were developed through painstaking individual experimentation rather than accumulated documentation. This knowledge exists more in people's heads than in any searchable corpus.

---

## Understanding Architecture Makes Better Programmers

The conversation makes a broader argument for low-level literacy independent of whether anyone actually writes assembly professionally. "I believe it's necessary to understand assembly language even if you don't do it much to understand what's going on inside your computer," the speaker asserts, "and that will make you a better programmer."

The mechanism operates through the memory hierarchy. Understanding assembly forces confrontation with the reality of registers—L1, L2, and L3 cache levels—and how data moves between them and main memory. "RAMs, SSDs, disk and so on—which are very important because then you have a good programming culture that will make you a better programmer." Programmers who understand these hierarchies make different design choices: they pre-fetch data, they structure access patterns to maximize cache hits, they batch operations to reduce memory traffic.

This understanding changes how one thinks about performance generally. A programmer who has manually managed register allocation develops intuition about when allocation matters and when compilers handle it adequately. Someone who has felt the pain of cache misses develops habits around data structure design that pay dividends even in garbage-collected languages. The abstraction layers don't disappear, but their costs become visible.

The speaker connects this to the Rust discussion that follows, suggesting that languages which promise to eliminate entire categories of errors can paradoxically worsen performance intuition. If memory safety errors are prevented automatically, programmers lose motivation to understand why those errors occur—which means they miss opportunities to write code that the runtime would handle inefficiently even if safely.

---

## Rust's Esperanto Problem

The conversation shifts to Rust, and the speaker's assessment is blunt: "I think it's valuable what they're doing in terms of memory safety as a concept. Can it achieve some of the speed up that assembly achieves? No, not by hand. I think that's a given. C potentially but I see it very—it has a very big Esperanto vibe about it."

The Esperanto comparison cuts to the heart of the critique. Esperanto was designed as a universal second language—logically structured, easy to learn, politically neutral. It never achieved mainstream adoption despite linguistic elegance because natural languages evolve to solve real problems and accumulate millions of speakers who have built culture around them. Rust, the speaker suggests, suffers from similar overconfidence in design purity over practical integration with existing ecosystems.

"It's like we're going to solve this and we're doing this in a particular way. Meaning it's a bit too utopian? There's a lot of focus on the self-importance rather than solving real world problems." The speaker draws a parallel to the Sinclair C5, an electric vehicle designed by Sir Clive Sinclair that was technologically interesting but practically useless. "I think the community doesn't quite understand that in order to get people to move, you have to build something that's as good as—if not better than—what you have now."

The specific complaint centers on incomplete rewrites. Projects like coreutils written in Rust achieve perhaps 85-90% of the original feature set, and this gap consumes disproportionate effort. "That last 1% takes 99% of the time," the speaker notes, referencing a formulation often attributed to Elon Musk about prototypes versus production. The irony is that this principle—which explains why startups can move faster than incumbents—applies equally to rewrites. The easy parts are easy; the hard parts reveal that the original implementers understood their domains in ways that aren't always documented.

This doesn't mean Rust is worthless. Memory safety as a concept matters enormously, and languages that enforce it correctly eliminate entire vulnerability classes. But the speaker suggests the community needs to reckon with practical constraints: programmers won't abandon tools that work for tools that promise to be better while delivering less.

---

## Who This Discussion Is For

This conversation serves several audiences differently. **Systems programmers** already comfortable with C will find validation for their low-level instincts plus practical encouragement to maintain assembly literacy even as they work primarily in higher-level languages. The discussion of memory hierarchy and register allocation provides vocabulary for explaining to others why the choices systems programmers make matter.

**FFmpeg contributors and aspiring codec developers** will find the most direct value in understanding the ASM-lessons approach and the X86 Inc framework. The speaker makes clear that opportunities exist—many codecs remain only partially optimized—and that the pathway to contributing has been deliberately cleared of unnecessary obstacles.

**Language designers and advocates** will encounter uncomfortable questions about their approaches. Whether one agrees with the speaker's assessment of Rust or not, the underlying logic about adoption barriers and the cost of incomplete rewrites deserves serious engagement. Anyone building tools meant to displace existing solutions should reckon with why the existing solutions won.

**Programmers in general** will benefit from understanding why low-level literacy matters even without writing assembly professionally. The memory hierarchy discussion provides mental models that improve programming in any language, and the warning about abstraction's cost applies everywhere.

Finally, **those curious about programming philosophy** will appreciate the Spitfire metaphor and the broader argument about directness versus abstraction. The speaker makes a case that computing has progressively hidden its substrate, and that understanding the substrate makes you better at working with abstractions—even if you never throw away the abstractions entirely.