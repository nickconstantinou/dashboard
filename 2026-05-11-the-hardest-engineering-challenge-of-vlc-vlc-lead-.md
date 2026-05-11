---
title: The hardest engineering challenge of VLC - VLC lead developer explains | Lex
  Fridman Podcast
date: '2026-05-11'
type: youtube
category: AI/Tech
video_id: Iodc7-1MgSM
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=Iodc7-1MgSM
---

## Key Insights

- **500+ plugins** make up VLC's core architecture, including FFmpeg, hardware decoders for Intel/Nvidia/AMD GPUs, and third-party drivers — much of this code isn't actually VLC's own
- **Sandbox isolation at gigabit speeds** is the core engineering challenge: unlike web browsers processing 5-10MB, VLC must process hundreds of megabits per second of video data while maintaining strict security boundaries
- **Crash-based exploitation** is a primary threat model — malware (ransomware, botnets) commonly exploits program crashes, and VLC's extensive third-party code surface makes this especially concerning
- **Process splitting** is the solution being implemented: separating VLC into isolated processes for decoding, demuxing, and filtering — so when one crashes (like a Chrome tab), the entire application survives
- **The puzzle filter** started as a math teacher's Bezier curve teaching tool in South France, was merged into VLC in 2010, and 5 years later a user complained 256 pieces was "too simple" — prompting JB to push it to 65,536 pieces

---

## Introduction

In this conversation from the Lex Fridman Podcast, Jean-Baptiste Kempf — the lead developer of VLC Media Player — explains one of the most technically challenging aspects of maintaining software used by hundreds of millions of people: security sandboxing for a multimedia application. The discussion reveals why a seemingly straightforward security feature becomes a profound engineering problem when you need to process high-bandwidth video data while preventing malicious actors from exploiting the complex web of plugins, drivers, and third-party code that makes VLC so capable.

The conversation spans beyond pure security into the fascinating psychology of software development at scale — exploring how features designed for one purpose find unexpected utility, and how millions of users guarantee that even the most obscure capabilities will find devoted users. Kempf's insights offer a rare glimpse into the mindset required when your code runs on a substantial percentage of the world's computers.

---

## The Architecture Challenge: Why Sandboxing VLC Is Hard

VLC operates as what developers call a "core with around 500 plugins." This architecture is both VLC's greatest strength and its most significant security liability. The plugins handle everything from decoding various media formats through FFmpeg, to supporting new protocols, applying video filters, and interfacing with the increasingly complex hardware architectures found in modern computers.

When you play a video in VLC, you're threading through a chain of components that calls your hardware decoders — whether that's Intel, Nvidia, or AMD GPUs — which in turn communicate with their respective drivers. All of this runs through FFmpeg for format handling. The problem is that any of these components could contain security vulnerabilities. A bug might exist in a shader, in VLC itself, in FFmpeg, or in your GPU driver, and any of them could cause a crash.

Here's where the security implications become serious. When a program crashes, malicious actors can potentially exploit that crash to run arbitrary code on your machine. This technique is commonly demonstrated in web browser exploitation and PDF-based attacks. While multimedia files are less frequently targeted, Kempf emphasizes that it absolutely could happen. The result could be ransomware encrypting your files or your computer being recruited into a botnet — real consequences for real users.

The fundamental challenge is that VLC, unlike mobile applications, runs on your desktop machine with access to everything. When you download and run Adobe software or any other program, it has the same access to your documents that you do. The security goal is to isolate potentially vulnerable code so that even when it fails catastrophically, it cannot be leveraged to compromise the rest of the system.

---

## The Sandbox Paradox

The obvious solution seems to be sandboxing — running VLC in a restricted environment where it cannot access your files, network, or system resources unless explicitly permitted. Mobile applications already do this by default; iOS and Android enforce sandboxing as a fundamental security model.

However, VLC faces a unique problem that makes simple sandboxing nearly useless: it legitimately needs access to almost everything. To play a video file, it needs to read files. To display video, it needs GPU access. To handle network streams, it needs network access. To decode media, it needs access to hardware decoders and their associated drivers. If you create a sandbox and then punch holes in it for every required permission, you've defeated the entire purpose of the sandbox. A program with access to everything is, by definition, not sandboxed.

This creates the core engineering paradox that makes sandboxing VLC so difficult. You cannot simply wrap the entire application in a single security boundary because the application legitimately needs to communicate with external resources at a fundamental level.

---

## The Solution: Process Isolation at Scale

The approach VLC is implementing involves splitting the application into multiple specialized processes, each running in its own sandbox. Specifically, the development team is separating the decoding pipeline into distinct components: demuxing (separating audio and video streams), decoding (converting compressed data into raw frames), and filtering (applying effects like color correction or the puzzle transform).

This architecture mirrors how Google Chrome handles stability and security. When a Chrome tab crashes — and tabs crash frequently — it crashes in isolation. The user sees a "Rethink" button, the tab restarts, and the entire browser continues functioning. No single webpage's failure can bring down the browser or compromise the user's other tabs. VLC is attempting to bring this same resilience to multimedia playback.

The critical challenge is that Chrome processes text and HTML — small amounts of data for each web page. VLC processes video data at hundreds of megabits per second, sometimes multiple streams simultaneously. The inter-process communication overhead required to maintain security boundaries while moving gigabits of data per second creates significant performance and complexity challenges. This isn't a simple architectural change; it's a fundamental rethinking of how the application handles data flow while maintaining strict security boundaries.

This remains an active research area for the VLC team. They're working on finding the right balance between security isolation and the performance requirements that users expect from a multimedia player. The goal is a system where even if your GPU driver crashes while processing a malformed video file, the rest of your system — and your video playback session — remains secure and operational.

---

## The Unexpected Users Problem

Beyond the technical architecture discussion, Kempf shares a revealing story that illustrates something profound about building software for hundreds of millions of people: every feature, no matter how seemingly useless, will find dedicated users.

The puzzle filter in VLC transforms your video into a jigsaw puzzle. You can click and drag pieces, shuffle them around, reassemble the image. It's the kind of feature that sounds gimmicky — something to show off the API rather than genuinely useful. And by most measures, it is useless. Who actually uses this?

According to Kempf, someone does. The filter was originally created by a high school math teacher in the South of France who was teaching his students about Bezier curves — the mathematical basis for curved lines in computer graphics. The code was clean and the feature was merged into VLC in 2010. Five years later, Kempf received an email from someone who complained that the puzzle was "too simple."

The existing implementation supported a maximum of 16 by 16 pieces — 256 individual puzzle pieces. This user loved watching movies and wanted to assemble puzzles while watching. For them, 256 pieces wasn't a feature limit; it was an insult. The user pushed back, explaining that they loved the feature but found the complexity insufficient for their needs.

Kempf's response was to commit a change that increased the maximum to 256 by 256 — 65,536 pieces. The commit is publicly visible online as evidence of this interaction. The lesson here isn't just about the puzzle filter; it's about what happens when your software has hundreds of millions of users. Any feature, no matter how specialized, finds someone who depends on it in ways you never anticipated.

---

## The ASCII Art Feature: Debugging at Scale

The ASCII art output in VLC provides another example of unexpected utility. VLC can display video in pure ASCII characters — green text characters on a black background approximating the image. It's visually striking but seems like a novelty.

Kempf explains the actual use case. Network engineers debugging complex multicast networks face a genuinely difficult problem: verifying that video streams are being properly distributed across thousands of routers and network segments. Traditional debugging involves examining packet headers, log files, and statistical data — time-consuming and error-prone processes.

With VLC's ASCII output, an engineer can SSH into a router, run the headless version of VLC on a video stream, and immediately see the output as colored text. If the image appears all black, the stream isn't arriving. If it's all green, something is wrong with color handling. The visual nature of the output provides instant feedback that would take much longer to diagnose through traditional logging and inspection methods.

This use case requires running VLC without any graphical interface, through command-line interfaces on remote systems. It's a far cry from the typical consumer experience but exactly the kind of capability that network infrastructure teams rely on. The ASCII art mode isn't a toy; it's a legitimate debugging tool for a specific professional audience.

---

## The Scale Reality

Throughout the conversation, the underlying theme is what happens when software reaches true mass adoption. VLC doesn't have thousands of users or even millions — it has hundreds of millions. With that scale comes certainties that smaller projects never encounter.

Every feature, no matter how obscure, will be discovered by someone. Every bug will be encountered by someone. Every limitation will eventually feel too restrictive to someone. The puzzle filter having a maximum of 256 pieces wasn't a problem for the vast majority of users, but for one particular user who loved assembling puzzles while watching films, it was a genuine problem that warranted a direct complaint to the lead developer.

This reality shapes how VLC approaches development. Features that might seem frivolous — like puzzle filters and ASCII art rendering — aren't really frivolous when you understand that they serve real users with legitimate needs. The question isn't whether a feature is universally useful; it's whether anyone, somewhere, will depend on it. With hundreds of millions of users, the answer is almost always yes.

---

## Detailed Takeaways

**Takeaway 1: Security boundaries require rethinking when performance demands are extreme.** Traditional sandboxing models designed for low-bandwidth applications don't translate directly to multimedia processing. The VLC team is essentially pioneering new approaches to maintaining security isolation while handling gigabit-per-second data throughput. This work has implications beyond VLC — any application requiring high-bandwidth inter-process communication while maintaining security boundaries can learn from their research.

**Takeaway 2: Complexity creates attack surface that cannot be ignored.** VLC's strength — support for 500+ plugins, integration with multiple hardware platforms, compatibility with countless codecs — is simultaneously its security weakness. Every line of code from third parties represents a potential vulnerability. The sandboxing project exists precisely because VLC cannot control the security of every component it relies upon.

**Takeaway 3: Scale changes the calculus of feature development.** When your user base is in the hundreds of millions, even features serving 0.001% of users serve more people than most software serves in total. The puzzle filter serves a tiny fraction of users, but that fraction represents tens of thousands of people. The economic and practical case for maintaining such features is strong.

**Takeaway 4: Headless operation is an underrated capability.** The ability to run VLC from command line without any graphical interface serves professional use cases that consumer-facing features never anticipate. Network debugging, automated testing, and server-side media processing all benefit from applications that can run without display infrastructure.

**Takeaway 5: Isolation enables resilience without sacrificing capability.** The Chrome tab model demonstrates that users will accept more granular crash experiences if the overall experience remains stable. VLC's move toward process isolation accepts that individual components might fail more visibly while ensuring the overall application remains robust. Users don't need every feature to always work; they need the application to remain reliable.

---

## Who This Is For

This discussion is particularly valuable for software engineers working on complex desktop applications, security engineers evaluating sandboxing strategies for high-performance systems, and technical product managers trying to understand the hidden costs of maintaining software at scale. The insights about how "useless" features serve real users and how third-party integration creates unmanageable attack surfaces apply broadly to any project involving complex dependencies.

Open source maintainers will find the discussion especially resonant — the challenges of securing code you don't control while serving a global user base with unpredictable usage patterns are universal experiences. The puzzle filter story in particular serves as a useful reminder about the relationship between software scale and user expectations.

General technology enthusiasts will appreciate the window into how software they likely use every day navigates seemingly invisible but critically important engineering challenges. Understanding why features take time to implement, why updates sometimes seem slow, and why certain security properties are genuinely difficult to achieve provides useful context for interpreting software development news and announcements.