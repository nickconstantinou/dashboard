---
title: The best programmers in the world have contributed to FFmpeg | Lex Fridman
  Podcast
date: '2026-05-12'
type: youtube
category: AI/Tech
video_id: -bRqc8CP4t8
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=-bRqc8CP4t8
---

# The Best Programmers in the World Have Contributed to FFmpeg: Inside the Open Source Multimedia Revolution

**Key Insights**

- FFmpeg runs on an estimated **hundreds of millions to nearly a billion CPUs simultaneously** worldwide, making every single CPU instruction matter at extraordinary scale
- Multimedia programming operates under severe real-time constraints requiring **perfect execution within 16 milliseconds per frame** — missing one frame destroys visual quality with no recovery option
- Andrew Kelly, creator of the Zig programming language, **learned to code through FFmpeg development** before building his own system programming language, illustrating FFmpeg's role as a finishing school for elite programmers
- The speaker argues FFmpeg is "**the best school ever of programming**" because contributors receive code reviews from the most seasoned programmers who scrutinize every line and demand excellence
- Understanding computer architecture — including CPU pipelining, SIMD operations, ALU functionality, and IO systems — remains essential for multimedia work, a depth many modern software engineers lack

---

## Introduction

Jean-Baptiste Kempf has spent years at the intersection of open source software and multimedia technology, leading projects that billions of people use daily without ever knowing the names. In a conversation that delves into the philosophy behind open source contribution, Kempf reveals what truly drives the remarkable developers who have built tools like FFmpeg and VLC into the backbone of modern video processing. His insights cut through the typical narratives about open source motivation, revealing a complex interplay between passion, technical excellence, and the unique demands of real-time multimedia programming.

The conversation centers on a question that many ask but few answer satisfyingly: what compels some of the world's most talented programmers to contribute countless hours to projects that, for most contributors, will never directly compensate them financially? The answer, according to Kempf, lies not in altruism or idealism but in something more fundamental — a love for the work itself, combined with an environment that demands and rewards excellence in ways few other coding contexts can match.

## The Three Engines of Open Source Motivation

Kempf describes three distinct phases that keep developers engaged with FFmpeg and the broader multimedia open source ecosystem. The first engine is simply that video is cool. This sounds almost too simple to be profound, yet Kempf emphasizes that the personal connection to the subject matter matters enormously. Many contributors arrived in the community because they loved watching anime and wanted to understand how video encoding actually worked. When people ask Kempf how to get started in open source, his answer never wavers: work on something you love.

For Kempf himself, that passion manifests in his love of movies. He describes watching the same films repeatedly, even when his wife finds it exasperating, because the technical problem of video reproduction remains endlessly fascinating to him. This personal investment transforms what could be merely a job into something sustainable over decades.

The second engine is excellence. Working in FFmpeg and VLC exposes developers to the most demanding programming environment many will ever encounter. Code reviews are conducted by some of the most experienced programmers in the world, people who will examine every line of submitted code and explain precisely why it falls short of perfect. This creates what Kempf describes as the best programming education available anywhere — not because of formal curricula, but because of the relentless pressure for quality from peers who genuinely care about the craft.

The third engine is impact. When you explain to your grandmother that you work on software that lets her watch videos on her laptop, she understands. This stands in stark contrast to the many software jobs that involve building invoice portals for utility companies — work that pays bills but fails to create the kind of tangible, human connection that makes labor meaningful. FFmpeg and VLC sit at the end of hundreds of millions of devices worldwide, and contributors can point to that reach with genuine pride.

## FFmpeg as a Finishing School for Elite Programmers

The technical demands of multimedia programming are unlike almost any other domain. When you write code for FFmpeg, you are not operating in an environment where occasional sloppiness can be tolerated or recovered from gracefully. The constraints are absolute: you have 16 milliseconds to decode and display a single frame. Miss that deadline and you have destroyed the visual experience for the viewer, with no mechanism to catch up later.

This creates a forcing function for excellence that few other environments replicate. Unlike game engines, where occasional dropped frames might be noticed but tolerated, video playback is unforgiving. And unlike many modern programming contexts that abstract away hardware details behind layers of interpretation, multimedia code must understand precisely how computers work at the most fundamental level.

Contributors who work in FFmpeg must understand CPU pipelining, the operation of SIMD (Single Instruction, Multiple Data) instruction sets, how the Arithmetic Logic Unit actually functions, and how IO systems behave. They must write assembly code when necessary, optimizing individual instructions for specific CPU architectures. When debates arise about which assembly call to use, contributors might argue about whether one approach costs three CPU cycles more than another on particular processor generations — and that three-cycle difference matters when you're executing it billions of times per second across a billion devices.

Kempf uses Andrew Kelly as a concrete example of this phenomenon. Kelly, who went on to create the Zig programming language, was first an FFmpeg developer. He learned to be an excellent programmer through the FFmpeg school, then applied those skills to building his own contribution to the programming language landscape. This pattern — FFmpeg as a proving ground where elite programmers develop skills they later apply elsewhere — is not coincidental. The environment simply doesn't allow mediocrity.

## The Scale of Responsibility

FFmpeg's reach creates both pressure and pride. The project is likely one of the biggest CPU users in the world, running on hundreds of millions of devices as users speak. Every instruction the codebase executes matters, multiplied across that enormous installed base. A one-cycle optimization in critical video decoding paths translates into massive cumulative savings across billions of CPU-hours of daily usage.

This scale also creates accountability. When your code runs on nearly every video playback scenario on earth, you cannot hide behind abstraction layers or blame infrastructure when things go wrong. You have nowhere to hide, as Kempf puts it. Your code stands exposed to scrutiny from the entire open source community, and any failures become immediately visible.

Yet this same scale creates the ultimate validation. Contributors can point to their work as directly enabling billions of people to watch video content, manipulate media files, and experience digital media in countless ways. When asked what they do, the answer resonates with almost everyone they meet. There is something uniquely satisfying about building infrastructure that the world depends on without realizing it.

## The Passion Project Acceleration

The conversation touches on a broader truth about open source development in the software world. John Collison's observation that "the world is a museum of passion projects" captures something essential about why open source works so well in software specifically. A passion project in the physical world — opening a cafe, for instance — requires navigating building codes, finding locations, managing supply chains, and countless other practical obstacles that slow iteration and limit reach. The network effects are inherently bounded by geography and physical constraints.

Software passion projects face no such limitations. A developer can build something interesting, and if it provides genuine value, the network effects can spread globally within hours. Contributors from anywhere can participate. The cost of copying and distributing software approaches zero. This means that passion projects in software can achieve impact that physical passion projects simply cannot match, creating a virtuous cycle where talented people are drawn to open source precisely because their work can matter so broadly.

## Who Should Pay Attention to This Discussion

This conversation offers particular value to software developers considering open source contribution for the first time. Kempf's advice about working on something you love rather than chasing perceived prestige or financial opportunity runs counter to much conventional career guidance, yet his reasoning is grounded in deep understanding of what sustains long-term engagement. The developers who thrive in open source are those who find genuine joy in their work, not those treating it as a stepping stone to something else.

For engineering managers and technical leaders, the discussion illuminates what makes open source communities function. The peer review culture, the emphasis on excellence, and the pride in tangible impact are not accidental — they are features carefully embedded in how projects like FFmpeg operate. Creating those conditions deliberately in commercial development environments could yield similar benefits.

Technology investors and founders might also find value in understanding how elite programmers actually develop their skills. The path from FFmpeg contributor to language creator (as with Andrew Kelly and Zig) suggests that deep technical excellence comes from working on problems with genuine constraints, not from abstract study or safe corporate environments. Companies seeking to hire genuinely elite programmers might consider what they can learn from communities that produce them.

Finally, anyone curious about the invisible infrastructure underlying modern digital life stands to gain appreciation for the human effort behind tools they use constantly. FFmpeg is not merely software — it is a living project maintained by passionate contributors who chose to work on something they love and developed extraordinary skills in the process. Understanding that story enriches appreciation for the digital infrastructure that increasingly mediates human experience.