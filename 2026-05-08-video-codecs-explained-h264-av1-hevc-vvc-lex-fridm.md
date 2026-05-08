---
title: 'Video codecs explained: H.264, AV1, HEVC, VVC | Lex Fridman Podcast'
date: '2026-05-08'
type: youtube
category: AI/Tech
video_id: _jjJCurqm7c
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=_jjJCurqm7c
---

## Video Codecs Explained: Understanding H.264, AV1, HEVC, and VVC

**Key Insights:**
- Video codecs achieve **100x to 1000x compression** by identifying and removing redundant visual information that humans wouldn't notice if missing
- Compression is inherently **asymmetric** — encoding requires orders of magnitude more compute than decoding because a single file is compressed once but viewed countless times
- Modern codecs like AV1, AV2, and VVC are not single algorithms but **collections of tools** that dynamically adapt based on content type (screen share, animation, live video)
- Two fundamental types of redundancy exist: **spatial** (same-color regions within a single frame) and **temporal** (unchanged elements across consecutive frames)
- Codec design involves fundamental trade-offs: more complex encoding enables easier viewing, while faster encoding shifts computational burden to the client side

---

### Introduction

Video compression sits at the invisible foundation of modern digital life. Every Netflix show streamed, every YouTube video watched, every Zoom call conducted relies on codec technology that transforms billions of pixels into manageable data packets. Yet for most users, the underlying mechanics remain a black box — even as the debate between H.264, HEVC, AV1, and emerging standards like VVC shapes everything from streaming quality to bandwidth costs.

This conversation dives deep into the engineering reality of video codecs, exploring not just what they are but how they fundamentally work. The discussion centers on compression as a mathematical problem of identifying what information humans won't notice if removed — and leveraging that principle to shrink video files by orders of magnitude. The speaker, an engineer working on these technologies, walks through the core concepts of redundancy removal, the asymmetric nature of encoding versus decoding, and how modern codec standards have evolved into sophisticated, content-adaptive systems rather than monolithic algorithms.

For anyone working in streaming, video production, software development, or anyone curious about the infrastructure powering digital media, understanding these principles reveals why certain formats dominate in different contexts and what trade-offs engineers and companies face when choosing compression standards.

---

### Understanding Video Codec Fundamentals

At its core, a video codec exists to solve a straightforward problem: video is just a massive grid of RGB pixel values repeating at 24, 30, or 60 times per second. A single minute of 1080p video at 30 frames per second contains approximately 150 million individual pixel values — before any compression. The goal of any codec is to reduce this data by factors of 100x, 200x, or even 1000x while maintaining visual quality.

The mechanism behind this reduction relies on redundancy. Video contains enormous amounts of information that doesn't actually convey new visual content. Consider a typical interview setup: the background behind the speaker remains static — perhaps black or a simple color — for the entire conversation. Rather than storing that same background pixel value hundreds or thousands of times across frames, the codec can simply state "this region is unchanged from the previous frame" or even "this region uses the same value across the entire picture."

The same principle applies temporally. When a camera pans across a landscape, the clouds in the sky remain relatively constant frame to frame. The sky doesn't need to be redrawn completely for every single frame — the codec can identify these static elements and reference them efficiently rather than recomputing them. This temporal redundancy removal is one of the most powerful techniques in video compression.

The compression process is fundamentally asymmetric by design. Encoding video requires comparing pixels across frames, analyzing spatial patterns, and making complex decisions about what information to keep and what to discard. This computational work happens once per video file. Decoding, however, must happen every time a viewer watches that file. A video uploaded to YouTube might be viewed millions of times, so the codec design prioritizes making decoding as efficient as possible even if encoding requires dramatically more computational resources.

This asymmetry explains why live streaming applications often face different challenges than on-demand video services. A live broadcast needs to encode in real-time — every frame must be processed within the time budget before it's scheduled to display. This constraint means live encoders often cannot use the most sophisticated compression techniques, potentially resulting in lower quality or higher bitrates for the same visual fidelity compared to non-real-time encoding where hours of computation can be applied to a single minute of video.

---

### The Dual Challenge of Spatial and Temporal Redundancy

Understanding redundancy requires examining both spatial and temporal dimensions. Spatial redundancy exists within a single frame — a clear blue sky stretching across half the image contains millions of pixels that are essentially identical. Rather than storing the exact RGB value for each pixel, the codec can identify that this region is uniformly blue and store only the color value and the region boundaries.

Temporal redundancy spans across multiple frames. When watching a movie, the set design, furniture, and background elements remain constant even as actors move through the scene. The codec can reference these unchanged elements from previous frames rather than retransmitting the identical data. The more sophisticated the codec, the further back in frame history it can look to find matching data, and the more clever its algorithms for identifying partial matches even when content has shifted slightly.

The practical limitation is computational power. Comparing every pixel in the current frame against pixels in the previous 200 frames across a 4K resolution means processing billions of comparisons per second. The codec must balance compression efficiency against the time and resources required to perform the analysis. More aggressive compression typically requires more computational work during encoding — a trade-off that may be worthwhile for content that will be viewed many times but impractical for real-time applications.

This is why the engineering field focuses heavily on developing faster algorithms and more efficient techniques that can achieve better compression with less computational overhead. Each generation of codec design advances on this frontier, finding mathematical shortcuts and intelligent heuristics that identify redundancy more effectively without requiring exhaustive searches.

---

### Modern Codec Architecture: Tools, Not Single Algorithms

Perhaps the most significant evolution in recent codec design is the shift from monolithic algorithms to collections of tools. Standards like H.264, HEVC, and VP9 represented discrete encoding approaches with defined specifications. Modern standards like AV1, AV2, and VVC have fundamentally changed this architecture.

These newer codecs function as frameworks containing dozens or hundreds of specialized compression tools. When encoding a screen-sharing session, the codec activates tools optimized for sharp text edges, flat color regions, and minimal temporal change. When encoding a fast-paced action sequence, different tools engage to handle rapid motion and complex textures. When processing animation with large areas of solid color and limited detail variation, yet another toolset proves most effective.

This adaptive approach requires sophisticated content analysis during the encoding process. The codec must identify what type of content it is processing and select the appropriate combination of tools to achieve the best results. This analysis itself consumes computational resources, adding to the encoding complexity, but it enables superior results across the diverse range of content that modern video applications handle.

Consider a typical Zoom call: the video might switch between a talking head, a screen-sharing presentation, and perhaps a video clip. A codec built on a single algorithm would treat all of this content the same way, compromising quality or efficiency in at least some scenarios. A tool-based codec like AV1 can recognize when screen-sharing begins and reconfigure its encoding strategy to better handle sharp text edges and flat backgrounds, then seamlessly adapt again when the presenter plays a video within their shared screen.

---

### Trade-offs in Codec Design

Designing a codec requires fundamental decisions about where to place computational burden. The fundamental question is whether to make encoding more complex with simpler decoding, or simpler encoding with more complex decoding.

High-quality on-demand video streaming often favors complex encoding. Netflix or YouTube can afford to spend hours encoding a single video file using sophisticated algorithms that maximize compression efficiency. Their millions of users then benefit from smaller file sizes and lower bandwidth requirements while decoding remains straightforward enough for mobile devices and smart TVs to handle in real-time.

Live streaming applications face opposite constraints. Encoding must complete in real-time — typically within 16 milliseconds for 60fps content or 33 milliseconds for 30fps content. This time budget may not allow for the most sophisticated compression techniques. Instead, the codec design might favor simpler encoding that completes quickly, shifting computational complexity to the decoder side. This approach requires viewer devices to work harder but ensures that live broadcasts don't fall behind.

Broadcast and telecommunications applications introduce additional requirements around error resilience. When video transmits over UDP networks — as commonly happens in video conferencing and broadcast applications — packets can be lost or arrive out of order. Codecs designed for these use cases must enable viewers to join an ongoing stream and begin decoding from the middle, rather than requiring them to wait for the beginning. The codec must also gracefully handle missing data, using techniques that allow the decoder to estimate or approximate lost information rather than failing entirely when packets don't arrive.

These diverse requirements explain why no single codec dominates all applications. Different use cases prioritize different characteristics, and codec designers make different trade-offs to serve different markets. The evolution from single-algorithm codecs to tool-based frameworks represents a response to this diversity, enabling a single standard to adapt across applications by selecting appropriate tools rather than compromising on a fixed algorithm.

---

### Detailed Takeaways

**The mathematical foundation of compression is human perception.** Codec engineers don't simply reduce data randomly — they leverage knowledge about what visual information humans notice versus ignore. Colors that are nearly identical, fine texture details, and rapid motion blur all fall below perception thresholds that codecs exploit to eliminate information without subjective quality loss.

**Codec selection depends heavily on your specific use case.** If you're streaming live sports, real-time encoding constraints dominate your decisions. If you're building a video-on-demand library, you can invest in encoding complexity to maximize quality and minimize storage costs. If you're designing a video conferencing tool, error resilience and low-latency decoding become critical priorities. Understanding your primary use case guides codec selection.

**The era of single codec algorithms is ending.** AV1, VVC, and similar standards are frameworks that adapt to content rather than fixed approaches. Organizations adopting these codecs need encoding pipelines that can analyze content and select appropriate tools — not just encode using a single algorithm with fixed parameters.

**Encoding investment compounds across viewership.** The computational cost of encoding a video is paid once, while the benefits of smaller file sizes and reduced bandwidth are enjoyed by every viewer. This asymmetry justifies significant investment in encoding complexity for popular content, where small improvements in compression efficiency translate to substantial savings at scale.

**Redundancy removal operates across two dimensions simultaneously.** Effective compression must identify both spatial redundancy within frames and temporal redundancy across frames. Sophisticated algorithms exploit both dimensions, looking backward through frame history to find references for unchanged content while also efficiently representing intra-frame patterns that repeat across spatial regions.

---

### Who This Is For

This discussion serves software engineers working with video infrastructure, streaming service developers choosing codec strategies, video production professionals seeking to understand encoding trade-offs, and technical decision-makers evaluating compression standards for their applications. The content provides foundational understanding for anyone evaluating codec choices — whether comparing H.264 versus AV1 for a streaming platform, designing video conferencing systems, or building content delivery infrastructure.

The value lies in understanding not just what different codecs do, but why they make different engineering trade-offs. This framework enables informed decisions about which standards serve specific applications best and helps anticipate how codec evolution will affect video infrastructure choices in the coming years.