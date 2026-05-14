---
title: The insane difficulty of reverse engineering video codecs | Lex Fridman Podcast
date: '2026-05-14'
type: youtube
category: AI/Tech
video_id: v2xe5ki4oHw
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=v2xe5ki4oHw
---

# The Insane Difficulty of Reverse Engineering Video Codecs

## Key Insights

- **Scale of complexity**: A 1 megabyte binary blob requires "order of magnitude a month of work" to reverse engineer—yet legendary reverse engineers like Costa tackled 20-30 megabyte blobs routinely
- **Pattern recognition mastery**: Reverse engineers identify DCT (Discrete Cosine Transform) and entropy coding structures by intuition and visual recognition of code patterns, often noting similarities to previously-seen codecs like Windows Media Video (WMV)
- **GoToMeeting codec preservation**: GoToMeeting used proprietary codecs stored in WMV files across versions 2, 3, 4, and 5; without specialized decoders, Windows Media Player would display black screens or only audio
- **Cross-platform obsolescence problem**: Legacy 32-bit Windows applications can't run on modern platforms (Android, iPad, RIS 5 systems), making codec reverse engineering essential for long-term video preservation
- **Archaeological analogy**: Lex Fridman describes reverse engineering as "like archaeologist with a little brush trying to reconstruct the entire human"—working from minimal signal toward complete understanding

---

## Introduction

In the world of video codecs, much of what we take for granted—our ability to watch recordings across platforms, access historical video archives, or play back meeting recordings from a decade ago—depends on a small, extraordinarily skilled community of reverse engineers. A recent discussion on the Lex Fridman Podcast delved into this rarefied world, exploring how dedicated individuals have spent years deciphering proprietary binary code to create open implementations that keep our video history accessible.

The conversation reveals a fascinating intersection of computer science, forensic analysis, and preservation. The speakers trace the evolution of codec reverse engineering from its origins in the early 2000s through the golden era of the 2010s, highlighting the remarkable personalities who drove this work and the technical challenges they overcame. What emerges is not just a technical explanation but a meditation on intellectual curiosity, the value of open standards, and the quiet heroism of maintaining our digital heritage.

This discussion carries particular relevance today as software becomes increasingly siloed within platforms. Every day, proprietary video formats from the past risk becoming unplayable as the original software becomes obsolete—making the work of these reverse engineers essential for anyone who cares about long-term digital preservation.

---

## The History and Evolution of Codec Reverse Engineering

### Origins in the 2000s

The reverse engineering of video codecs began in earnest during the 2000s, driven primarily by two proprietary ecosystems: Windows Media (WMV) and Real Media. Benjamin Larsson emerged as a key figure during this period, laying crucial groundwork for what would become a thriving community of codec archaeologists. These early pioneers faced an uphill battle—proprietary formats were deliberately obfuscated, documentation was nonexistent, and the tools available for binary analysis were far less sophisticated than what exists today.

The motivation was both practical and philosophical. On the practical side, users needed to play proprietary video formats on platforms other than those supported by the original vendors. On the philosophical side, the open-source community has long championed interoperability and the right to access one's own data without being locked into proprietary ecosystems. This tension between corporate secrecy and the public interest has defined much of the reverse engineering landscape.

### The Golden Era: The 2010s and Costa's Legacy

The 2010s marked the golden era of codec reverse engineering, characterized by increasingly ambitious projects and the emergence of truly exceptional talent. The discussion centers heavily on a legendary figure known as Costa—a Ukrainian engineer who was living in Germany at the time and harbored a deep love for Sweden. According to those who knew his work, Costa represents "one of those who are like borderline geniuses," capable of feats that seemed impossible to others in the community.

Costa's specialty was reverse engineering what he called "binary specification"—the complete technical specification derivable from analyzing a binary blob alone, without any documentation or external reference material. He would simply declare "I have a binary and I can figure all of this out," then disappear for weeks or months before returning with a working implementation. His approach was systematic yet bordering on intuition: he could look at assembly code and recognize patterns from other codecs he'd studied, making connections that eluded less experienced analysts.

The scale of Costa's work was staggering. While a 1 megabyte binary blob might require "order of magnitude a month of work" for a competent engineer, Costa routinely handled 20 to 30 megabyte blobs—effectively compressing years of work into each project. He accomplished this not through any special tooling but through an extraordinary combination of pattern recognition, persistence, and deep knowledge of how video codecs are constructed.

### The GoToMeeting Challenge

Among Costa's most notable achievements was reverse engineering the GoToMeeting codec. This was a major undertaking because GoToMeeting was "the number one feature request for a long time" in the open-source community. The speaker in the discussion had personally posted a bounty for the work, and Costa eventually stepped forward to take on the challenge.

The complete reverse engineering of GoToMeeting took approximately two months—a remarkably short timeframe given the complexity involved. When Costa explained his methodology, his approach revealed both the technical skill and the creative intuition required for such work. He described looking at the binary code and recognizing patterns: "Oh, this looked like a DCT that I used to see on WMV and so on." This ability to transfer knowledge across codec implementations—recognizing that the underlying mathematical transforms are often variations on well-established techniques—proved essential to his success.

What makes the GoToMeeting story particularly memorable is its human touch. The code Costa produced "is beautiful," according to those who reviewed it, and it's filled with inside jokes, references to the names of developers involved (including "JB," "Kemp," and "Costia" himself), and humorous comments throughout. This blend of serious technical work with playful creativity exemplifies the culture of the reverse engineering community.

---

## The Technical Process: How Codecs Are Reverse Engineered

### Locating the Decoding Module

Understanding how reverse engineering actually works requires tracing through the practical steps involved. The process begins not with the codec itself but with finding the relevant code within a much larger software ecosystem. For GoToMeeting, this meant identifying the actual video conferencing client and then locating the specific module responsible for decompression—a task that "may be easy, it may not be easy" depending on how the original software was structured.

This initial reconnaissance phase requires a combination of technical knowledge and investigative intuition. Engineers must understand the typical architecture of video software to know where to look for decompression routines, and they must have tools capable of analyzing compiled binaries to narrow down the search space.

### Dumping Raw Data for Comparison

Once the relevant module is located, the next challenge is extracting data that can serve as a reference for the reverse engineering work. The goal is to "dump the YUV data from the module"—raw video information before it's encoded or after it's decoded. This requires finding a way to hook into the module's decoding process and capture its output.

The technical approach typically involves "opening in a disassembler, trying to guess where the hooks are to incorporate that module and run that module natively to decode a sample file." This means understanding not just the codec's internal logic but also how it interfaces with the surrounding software ecosystem. The objective is to "figure out where this module is doing the decoding process and find a way to hook in and output the raw YUV data."

This raw YUV data serves as the ground truth against which the reverse engineer's work will be compared. The target is to achieve results that are "bit exact or in some cases close to bit exact" with the original implementation—a stringent requirement that means every detail of the algorithm must be correct.

### Pattern Recognition and Intuition

With raw reference data in hand, the actual reverse engineering begins. The process involves "using a lot of intuition to go and figure out, you know, where the DCT is, where's Entropy Coding." This is described as "not a rule book, but there's always a pattern of some sort" that experienced reverse engineers learn to recognize.

The intuition develops over years of working with video codecs, many of which share common structural elements despite their proprietary nature. DCT (Discrete Cosine Transform) is a fundamental building block of video compression, appearing across virtually all codecs in various forms. Similarly, entropy coding techniques (like Huffman coding or arithmetic coding) follow mathematical principles that can be recognized even when implemented in non-obvious ways.

The speaker notes that "there's always a pattern of some sort"—GoToMeeting, for instance, would "be a lot of screen codec tools" with "also different variants" across versions. Experienced reverse engineers learn to recognize these patterns quickly and adapt their approaches to each new challenge.

### Handling Multiple Versions and Variants

A particularly challenging aspect of codec reverse engineering is dealing with multiple versions and variants of the same codec. GoToMeeting existed in versions 2, 3, 4, and 5, each potentially using slightly different encoding approaches. The reverse engineer must identify "what all the different flavors are" and develop implementations that handle each variant correctly.

The discussion notes that sometimes "a soap form for example is actually a collection of different approaches and toolkits within that codec cuz often it grows naturally." As proprietary software evolves, developers make architectural decisions that may introduce inconsistencies or new approaches. The reverse engineer must untangle this organic growth and produce implementations that work across all the variants users might encounter.

A key challenge is "finding the sample that gets you kind of somewhere to start without having to implement 10 different other things." The choice of which sample to analyze first can dramatically affect the difficulty of the overall project. A well-chosen sample might reveal the core algorithms quickly, while a poorly-chosen one might require building substantial infrastructure before making progress.

---

## The Community of Reverse Engineers

### Assembly Language Masters

The discussion distinguishes between two types of exceptional engineers in the video codec world: reverse engineers who decipher proprietary algorithms, and assembly language programmers who implement those algorithms with maximum performance. Both groups are described as "amazing," and the best work emerges from collaboration between them.

The speaker mentions Loren Merritt as an exemplar of the assembly language tradition. Merritt was associated with the University of Washington and became famous for his work on x264, the open-source H.264 encoder. He "made everything great and fast doing a ton of assembly"—a testament to the importance of low-level optimization in achieving competitive video encoding performance.

### The Culture of Humility

An interesting psychological observation emerges from the discussion: "I've gotten a chance to speak to some of the developers, some of the assembly language level people, and they all always make everything sound like it's kind of easy." This creates "a kind of humility" that might mislead observers into underestimating the difficulty of the work.

The explanation offered is that "the level of what's required to do this stuff is so high that everything else seems easy, I guess." When you're working at the frontier of difficulty, problems that would seem impossible to outsiders appear routine. This psychological adaptation is both a survival mechanism and a genuine reflection of expertise—after years of solving impossible problems, they become the baseline against which other challenges are measured.

### The Joke-Filled Code of Costa

Among the cultural artifacts of this community, Costa's code stands out for its humor and personality. While producing functionally correct and elegant implementations, he populated his work with "a ton of JB right, my name and Kemp and Costia jokes inside the code." This playful approach reflects a broader culture in which engineers invest personal meaning in their work rather than treating it as mere corporate output.

The code's readability and documentation also made it valuable for others in the community—jokes and all, it served as both a functional implementation and an educational resource for those learning the craft.

---

## Why This Work Matters: Preservation and Accessibility

### The Cross-Platform Problem

The discussion emphasizes why reverse engineering proprietary codecs serves essential purposes beyond technical curiosity. The core problem is obsolescence: "GoToMeeting.exe for Windows 32 bits" represents a format that may be inaccessible on modern platforms. As the speaker notes, "I'm on Android, I'm on an iPad, I'm somewhere else"—modern users may need to access historical recordings on devices and operating systems that can't run legacy Windows software.

This problem extends far beyond GoToMeeting. Every proprietary video format ever created faces this existential risk. The original software may become unmaintained, the company that created it may go out of business, or the hardware and operating systems it requires may become obsolete. Without reverse engineering efforts, the videos encoded in these formats become permanently inaccessible.

### The Exceptional Utility to Humanity

The speaker frames codec reverse engineering as "exceptionally useful for humanity"—a phrase that might seem hyperbolic until one considers the scope of the problem. Organizations worldwide have recorded meetings, conferences, educational content, and personal memories in proprietary formats that are now at risk. Every month that passes without action increases the volume of irrecoverable video content.

The work becomes even more critical as "there are tons of files we need to support for the future." This isn't a solved problem with a finite scope—new proprietary formats continue to proliferate, and each one represents potential future data loss if it isn't eventually reverse engineered.

### From Reverse Engineering to Open Source

A satisfying outcome of many reverse engineering projects is their eventual incorporation into open-source ecosystems. The discussion mentions that Kieran (or Kan), one of the participants, "has done some reverse engineering at the time, actually led to the open sourcing of that work." This trajectory—from proprietary binary to open implementation—represents the democratization of access to information.

Once a codec is reverse engineered and an open implementation is created, it can be maintained by the community indefinitely, compiled for any platform, and integrated into any software. This transforms a perishable proprietary advantage into a permanent public good.

---

## The Archaeological Metaphor

Perhaps the most evocative description of reverse engineering comes when Lex Fridman draws an analogy to archaeology. The process, he explains, is "mindblowing" and "crazy"—like working as "an archaeologist with a little brush trying to reconstruct the entire human." The metaphor captures both the scale of the challenge and the delicacy required.

An archaeologist working with fragmentary remains has limited signal: broken bones, scattered artifacts, partial structures. Similarly, a reverse engineer sees only compiled machine code—human intention and algorithm design translated into opaque binary patterns. The skill lies in "start inferring basics" from these fragments, building up a coherent picture from indirect evidence.

The comparison also highlights the irreversibility of the task. An archaeologist can never know for certain whether their reconstruction is correct; a reverse engineer has more objective tests (bit-exact output) but faces the same fundamental challenge of inferring design intent from implementation artifacts. And like archaeology, codec reverse engineering is fundamentally about preserving knowledge for future generations—rescuing meaning from the decay of time.

---

## Key Takeaways

### 1. Reverse Engineering Requires Both Systematic Methodology and Intuition-Based Pattern Recognition

The process isn't purely analytical—it demands years of accumulated experience to recognize DCT patterns, entropy coding structures, and codec-specific implementation choices. Beginners should focus on studying known codecs thoroughly before attempting reverse engineering, building up the pattern library they'll need to recognize in proprietary binaries.

### 2. The Scale of Binary Blobs That Can Be Reverse Engineered Is Staggering to Outsiders but Routine for Experts

While a 1 megabyte binary might require a month of work for most engineers, experts like Costa routinely handled 20-30 megabyte blobs. This isn't magic—it's the result of deep expertise that compresses the time required for each incremental analysis task. Understanding this magnitude helps set realistic expectations for project timelines and resource requirements.

### 3. Cross-Platform Preservation Is an Ongoing Crisis That Requires Constant Vigilance

Every proprietary format ever created represents potential future data loss. Organizations should audit their video archives now to identify proprietary formats that might become inaccessible, and support open-source codec development to ensure future reversibility of current proprietary formats.

### 4. The Human Element in Technical Work Produces More Durable Results

Costa's joke-filled, well-documented code demonstrates that technical work infused with personality serves better as both a functional implementation and an educational resource. The culture of making code readable—jokes included—creates artifacts that train the next generation of reverse engineers.

### 5. The Community of Codec Engineers Operates with a Characteristic Humility That Obscures Their Exceptional Abilities

Those who work at the frontier of difficulty naturally make their work seem routine, which can mislead observers about the actual difficulty involved. This has implications for hiring (don't judge candidates solely by how easily they explain things), project planning (build in substantial time buffers), and community building (recognize and celebrate exceptional contributors).

---

## Who This Is For

This discussion is essential listening for software engineers working with video processing, media archivists concerned with long-term preservation, open-source community leaders interested in understanding the sociology of technical communities, and anyone who has ever wondered how proprietary video formats become accessible across platforms. It offers particular value to those considering entering the video codec field, providing both a realistic view of the challenges involved and inspiring examples of what's achievable with sufficient dedication.

For technical audiences, the discussion provides concrete details about reverse engineering methodology that can inform approach to similar challenges. For non-technical audiences, it offers a window into a hidden world where a small group of dedicated engineers has quietly preserved vast amounts of our video heritage through intellectual curiosity and persistence.