---
title: Future of holograms, brain signal playback, smell, and touch in multimedia
  software | Lex Fridman
date: '2026-05-14'
type: youtube
category: AI/Tech
video_id: S7uUtfHW6yo
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=S7uUtfHW6yo
---

# The Future of Multimedia: Holograms, Brain-Computer Interfaces, and the Evolution of VLC

**Key Insights**

- FFmpeg will likely persist 100 years from now, while VLC's survival is less certain—the distinction hinges on FFmpeg's role as fundamental infrastructure versus VLC as a consumer-facing product
- Multimedia is defined as "a digital representation of several streams for the human senses"—encompassing all sensory data, not just audio and video
- Approximately 150 contributors annually maintain VLC, with ~300 for FFmpeg; the speakers emphasize they are **maintainers** not merely contributors, responsible for accepting and integrating community work
- VLC already has a haptic plugin for 4D cinemas (with hydraulic motion systems used in theme parks), demonstrating smell and touch aren't hypothetical—they're in development now
- The standardization cycle follows a predictable pattern: five competing formats emerge → hype collapses → two or three follower companies create a standard → the market leader is pressured to adopt it

---

Jean-Baptiste Kempf, the co-founder and president of the VideoLAN project and a core developer of FFmpeg, has spent two decades building the free software that powers video playback across billions of devices. In this conversation with Lex Fridman, he tackles a question that might seem mundane at first glance but unfolds into a profound meditation on the future of human sensory experience: where is multimedia technology heading, and will the tools we use today survive alongside brain-computer interfaces, holographic displays, and sensory feeds that include smell and touch?

The interview emerges from a simple premise—whether VLC and FFmpeg will exist a century from now—but rapidly expands into territory that encompasses Neuralink, volumetric video codecs, 4D cinema infrastructure, and the architecture decisions that will determine whether these projects can absorb entirely new categories of human experience into their frameworks. What makes this conversation particularly valuable is that Kempf speaks not as a futurist or theorist, but as someone who has spent years maintaining software that processes trillions of multimedia streams daily, giving him a pragmatic perspective on what actually survives and scales versus what remains vaporware.

---

## The Question of Survival: FFmpeg, VLC, and Hundred-Year Horizons

When Fridman asks whether VLC and FFmpeg will persist a century from now, Kempf's answer is revealing in its nuance: "FFmpeg, yes. VLC, maybe." The distinction matters because it reveals the fundamental nature of these two projects. FFmpeg functions as a codec library and command-line tool—a piece of infrastructure that other software builds upon. It processes video and audio, and as long as humans consume visual and auditory media in digital form, FFmpeg remains relevant. VLC, by contrast, is an application with a user interface, a branding, a consumer presence that depends on continued development, funding, and cultural relevance. The survival of applications is far less certain than the survival of underlying libraries.

Kempf identifies what he calls "the tension inside FFmpeg"—the faction that argues the project should stick to what it does well, video and audio encoding and decoding, rather than expanding into uncertain territory. His response to this tension hinges on a redefinition of the problem. Before deciding whether to expand, you must answer the question: what is multimedia? And his answer is both simple and expansive: "Multimedia is a digital representation of several streams for the human senses." If that definition holds, then expanding beyond audio and video isn't a departure from the project's purpose—it's a fulfillment of it.

---

## Brain-Computer Interfaces and the Coming Codec Revolution

The conversation takes a dramatic turn when Kempf addresses brain-computer interfaces directly. "If you look at something like Neuralink with brain computer interfaces, it's very possible that we start to consume what multimedia means is whatever codec, whatever data that our brain wants to consume through the brain computer interfaces." This isn't speculation about distant futures—it's a technical roadmap. "You will have VLC for Neuralink," Kempf says with conviction. "And you'll have FFmpeg input format human brain. Yeah, there's going to be codecs for the brain."

The reasoning here is rooted in the fundamental purpose of codecs: compression. The human brain receives enormous amounts of information, and transmitting that information efficiently—whether from external sensors to the brain or between brains—will require compression standards as rigorous as any developed for video. The parallel to existing codecs is direct: if we need to send neural data, we'll need neural codecs, and FFmpeg and VLC will need to handle them.

What makes this vision concrete is the existing groundwork already being laid. Kempf points to emerging codec research for "point cloud" and "volumetric videos"—3D representations that capture spatial information rather than flat pixels. There's significant work on RGBD codecs, where the D stands for depth data, useful for robotics applications and immersive media. "There is a ton of codecs for compression of 3D elements," Kempf notes. "There is compression for astronomy." The architecture of these systems is being developed now, and when brain-computer interfaces become consumer products, the infrastructure will already exist to compress and decompress the data flows they require.

---

## The Current Frontier: XR, VR, and Volumetric Video

Before reaching brain-computer interfaces, multimedia technology is already navigating the transition to spatial computing. VLC maintains a VR and XR version, and the VideoLAN team is actively working on streaming 3D XR content to devices like Apple Vision Pro and Meta Quest. "We already work on streaming 3D XR interactive low latency," Kempf explains. "There is something called volumetric video point cloud videos. So it's not stopping. And yes, at some point we will manage 3D data inside VLC and FFmpeg, right? It's obvious."

The challenge here is technical but also architectural. Volumetric video represents data fundamentally differently than traditional video—a point cloud can require enormous amounts of storage and bandwidth compared to a standard video stream. Streaming this data with low enough latency to feel responsive in XR environments requires advances in both compression algorithms and network protocols. "On Kaaza," Kempf mentions, "we also would like streaming of XR content on for the glasses who cannot have enough power or inside the Apple Vision or the Quest."

This work extends to what might seem like science fiction territory: 4D cinemas with hydraulic motion systems. VLC already has a haptic plugin—though not included in the standard release—that "transports those type of movements which is physical movements which is haptic movements, right?" These are the theme park installations with seats that move in sync with on-screen action. They're not new technology, but integrating them into a multimedia framework that can sync haptic data with video and audio streams represents a proof of concept for sensory media beyond sight and sound.

---

## Smell, Touch, and the Architecture of Future Senses

The most striking moment in the conversation comes when Fridman asks about extending multimedia to include smell. Kempf's response is immediate and confident: "Imagine there is now a way to not have a mic, but have a odor sensor and a diffuser of odors. Mhm. It will get into FFmpeg." He continues with the technical details: "Of course, your demuxer has a new track type that is basically odors, right? And you already have smell, touch." The conversation reaches an almost absurd but completely earnest conclusion: "Audio, you'll have a left and right nose track, you'll have a left and right audio pair. It's easy. Yes, of course. Stereo smell."

The humor in "stereo smell" shouldn't obscure the seriousness of the underlying architecture. The same principles that allow VLC to handle separate audio tracks for left and right speakers can be extended to handle separate olfactory channels. The demuxer—the component that separates a multimedia stream into its constituent tracks—simply needs a new track type. If the encoding standards and playback software can handle five different audio tracks for surround sound, they can handle multiple olfactory tracks for smell. The barrier isn't conceptual; it's the development of standardized formats and the hardware to produce and detect odors in sync with media.

This represents a core principle of the VideoLAN approach: build flexible architecture now, and new capabilities become extensions rather than rebuilds. "We did the demo not long ago," Kempf explains. "There were changes needed on the architecture and we did the first special audio module. When it's going to add the second one, it's going to be easy or the third one, it's going to be easy, right?" The first special audio module required architectural work; subsequent modules will slot into existing infrastructure. The same approach applies to odors or haptic feedback. The architecture must be designed to accommodate future capabilities.

---

## The Standardization Cycle and the Role of Open Source

Kempf offers a revealing analysis of how technology standards actually emerge—a pattern he describes as nearly universal across multimedia domains. "You start, it's a new topic that is like five different standards because everyone starts to do this. The hype goes down because every time the hype goes down, then people start to say, 'Well, you know what? We need to do a standard.' People because two or three companies, usually not the leader, but the two or three followers do a standard. And then we implement the standard and then it's the end of the curve, it starts to be more popular. And then the leader is kind of pressured into it because it is better to do a standard."

The example he provides is 3D audio, which followed this exact trajectory. "Six or seven years ago it was everything about 3D. You had the cardboard on Android, you had two audio formats. They all dead, right? And now it's coming back with actual use cases and we learn from the mistakes of the past standard." The cardboard reference is to Google's inexpensive VR viewer—a device that generated enormous hype but no lasting standards. The failure of those early formats created the pressure that led to the current wave of 3D audio standardization, which benefits from learning what didn't work before.

This is where Kempf frames the broader role of FFmpeg and VLC. "I lost us so many funds because so FFmpeg and VLC are pushing companies and pushing the world to standardize." The projects serve as forcing functions for standardization. When a new modality like haptic feedback or olfactory data emerges, FFmpeg and VLC implement support for the experimental formats. This implementation pressure forces the industry toward convergence on standard formats, even when major players would prefer to maintain proprietary control.

His criticism of Dolby crystallizes this point. "It used to be an amazing company doing tons of great things with amazing engineers. They defined what sound was. And now it's mostly lawyers and licensing things. They're closing stuff off. They're trying to make money off of licensing. They don't innovate as much as they did." The contrast is between a company that defined standards through technical excellence and one that now extracts value through legal restrictions. For Kempf, open source projects serve a counterbalancing function—they provide implementations that work without licensing fees, creating competitive pressure that keeps proprietary standards from strangling innovation.

---

## The Maintainer's Perspective: Why Community Architecture Matters

Throughout the conversation, Kempf emphasizes a distinction that illuminates how large open source projects actually function: he and his colleagues are **maintainers**, not merely contributors. "We are not the contributors, we are the maintainers. Right? So we maintain for everyone." This means their primary role isn't writing code—they're integrating code written by others, ensuring that the contributions from approximately 150 annual VLC contributors and 300 FFmpeg contributors actually work together and don't break existing functionality.

The maintenance burden is enormous. "If you're a contributor to FFmpeg or VLC, it feels stressful. Like it's just looking at Twitter, it's like it's a huge amount of work to make it work on all these different operating systems. It's an incredible effort." The speakers acknowledge that working on foundational multimedia infrastructure can feel overwhelming—the endless flow of new formats, devices, and use cases creates a maintenance backlog that never clears. But the architecture decisions they've made allow the project to absorb this complexity. The key is designing systems flexible enough to incorporate new modalities without requiring complete rebuilds.

This architectural flexibility is why Kempf can confidently predict that "I think that's inevitable"—the integration of brain waves, haptic feedback, and olfactory data into multimedia frameworks. Not because the specific technologies are predetermined, but because the architecture is designed to absorb new human senses as they become digitally representable. The question isn't whether multimedia will expand to include new sensory modalities; it's whether the standards and infrastructure will be open and accessible or controlled by licensing regimes. FFmpeg and VLC exist to ensure the former outcome.

---

## Detailed Takeaways

**The definition of multimedia determines its future scope.** When Kempf reframes multimedia as "a digital representation of several streams for the human senses," he's not just being expansive—he's establishing a framework that justifies extending software from video to VR to neural interfaces. If you accept this definition, then smell codecs, haptic tracks, and brain wave compression aren't departures from the project's purpose; they're completions of it.

**Open source projects serve as standardization forcing functions.** By implementing experimental formats without licensing restrictions, projects like FFmpeg and VLC create competitive pressure that forces proprietary players toward standardization. This means the existence of open source multimedia infrastructure has an outsized effect on how industries evolve—it makes standardization more likely and reduces the ability of market leaders to extract licensing rents.

**Architectural flexibility is more valuable than current capabilities.** The value of VLC and FFmpeg isn't that they handle video formats you use today; it's that they're designed to easily absorb new track types, new codecs, and new sensory modalities. The first special audio module required significant architectural work, but "when it's going to add the second one, it's going to be easy." This reveals that long-term sustainability of infrastructure depends on building for extensibility rather than optimizing for current use cases.

**Standardization follows a predictable pattern that open source can accelerate.** The cycle of hype, fragmentation, standardization, and adoption appears across 3D audio, VR, and likely brain-computer interfaces. Open source projects insert themselves at the standardization phase—implementing formats when they emerge and pressuring proprietary players to adopt them. Understanding this cycle helps predict where FFmpeg and VLC will appear next.

**Maintainer roles are fundamentally different from contributor roles.** With 150 VLC and 300 FFmpeg contributors annually, the challenge isn't generating new code—it's integrating contributions without breaking existing functionality. This suggests that the bottleneck for open source infrastructure projects is rarely individual contribution; it's the coordination and maintenance capacity of a small core team.

---

## Who This Is For

This conversation is essential for software engineers working on multimedia systems, compression algorithms, or extended reality applications. The architectural decisions Kempf discusses provide a roadmap for building systems that can absorb new modalities without requiring complete rebuilds. Understanding why the VideoLAN team made specific architectural choices—and how they define the scope of their project—offers guidance for anyone building multimedia infrastructure.

It's also valuable for technology strategists and investors trying to understand which technologies will achieve standardization and which will fragment into proprietary dead ends. Kempf's analysis of the standardization cycle provides a framework for predicting which formats will gain adoption and which will require additional cycles of development before achieving market traction.

Finally, for anyone interested in brain-computer interfaces or sensory media beyond audio and video, this conversation provides a grounded, practical perspective on what the path from current technology to those futures actually looks like. It's not about predicting specific products but understanding the infrastructure that must be built—and is already being built—to support the next generation of human-computer interaction.