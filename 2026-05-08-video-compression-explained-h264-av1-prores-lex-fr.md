---
title: 'Video compression explained: H.264, AV1, ProRes | Lex Fridman Podcast'
date: '2026-05-08'
type: youtube
category: AI/Tech
video_id: DoobVFIAssU
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=DoobVFIAssU
---

# Key Insights

- **ProRes is an "intra-only" codec** with zero temporal compression—every frame is a complete, self-contained image—which makes it ideal for editing where random seeking is required, but useless for distribution due to massive file sizes
- **B frames create a fundamental asymmetry**: decoding order differs from display order, meaning decoders must buffer future frames before they can render current ones—making the encoding process remarkably complex compared to simple frame-by-frame playback
- **Intra Refresh eliminates keyframes entirely**: by gradually building up a full frame across the stream (refreshing certain parts with each new frame), the system avoids the bandwidth spike and latency issues that come with periodic I-frames
- **YouTube handles a dual challenge** that Netflix doesn't: not only delivering content at massive scale, but also encoding user-generated videos from all sources and serving them with near-zero latency to sometimes just five viewers
- **The codec/container distinction matters**: H.264 typically lives in MP4 containers, while AV1 uses WebM containers, and ProRes has its own container format—these aren't interchangeable and affect compatibility, streaming capability, and playback performance

---

# Introduction

Video compression is the invisible infrastructure that makes modern internet streaming possible, yet for most people, it's a black box of mysterious acronyms and tradeoffs. In this episode, Lex Fridman and his guest pull back the curtain on how video compression actually works, demystifying the technologies that deliver everything from YouTube tutorials to Netflix originals to your screen. The conversation focuses on the practical realities of codec selection, the mechanics of frame prediction, and the enormous engineering effort required to serve billions of video streams reliably across vastly different devices and network conditions.

The discussion emerges from a technical foundation, starting with the most common codec and container combinations in use today. Rather than diving into abstract theory, the conversation immediately grounds itself in real-world applications—why a filmmaker chooses ProRes for editing, why streaming platforms prefer AV1, and what tradeoffs each choice entails. This practical orientation makes the technical explanations accessible while still honoring the genuine complexity underlying video compression.

What becomes clear throughout the conversation is that video compression is both a solved problem and an ongoing art form. The underlying mechanisms work with near-magical reliability—decoders from different manufacturers produce bit-for-bit identical output across the globe—yet thousands of engineers at companies like YouTube and Netflix spend their careers fine-tuning parameters for different content types. The gap between "it works" and "it works optimally" is where the real expertise lies.

---

# Key Concepts & Arguments

## The Five Major Codec-Container Combinations

The conversation opens with a practical taxonomy of the video compression landscape, identifying the top five codec-container combinations that matter in modern production. H.264 inside MP4 containers remains the workhorse standard—ubiquitous compatibility has made it the default choice for nearly two decades. AV1, the newer open codec, lives inside WebM containers and represents the industry's push toward better compression efficiency, particularly important for streaming at scale. ProRes occupies a different category entirely: it's Apple's proprietary codec designed specifically for nonlinear editing workflows, housed in its own container format optimized for fast seeking and frame-accurate editing.

The distinction between codecs and containers is more than technical pedantry—it has real implications for how video behaves in different contexts. A container encapsulates the encoded video data along with audio tracks, subtitles, and metadata, determining which players and platforms can read the file. Switching from H.264 to AV1 isn't just a quality change; it potentially requires a container change and affects which devices can play the file. This is why legacy compatibility remains H.264's strongest advantage even as newer codecs offer better compression.

## ProRes and the Intra-Only Codec Paradigm

ProRes serves as the perfect counterpoint to understand why most video codecs are built the way they are. The guest explains that ProRes was designed for Final Cut Pro as an editing codec, with one defining characteristic: it has no or very minimal temporal compression. Every frame in a ProRes file is essentially a complete JPEG-like image—there's no prediction from previous frames, no dependency chains, no temporal interpolation. This means an editor can seek to any frame instantly without needing to decode a chain of preceding frames first.

This "intra-only" approach makes ProRes files large but functionally ideal for editing. When you're scrubbing through a timeline or making frame-accurate cuts, you need instant random access to any frame. Temporal compression breaks this property—seeking to frame 1,247 might require decoding frame 1,246 first, and that frame might depend on 1,245, creating a chain of dependencies that slows down editing tools. ProRes trades storage efficiency for access speed, making the right choice for its specific use case.

## Understanding IPB Frames: The Building Blocks of Video Compression

The heart of video compression lies in the concept of frame types, and the conversation dedicates substantial time to explaining how I-frames, P-frames, and B-frames work together to achieve compression efficiency. I-frames (also called key frames) are complete frames—essentially JPEG images that contain everything needed to render that moment in the video. They're the anchors from which other frames derive.

P-frames (predicted frames) work by identifying blocks in the previous frame that haven't changed and only encoding the differences. The guest uses a concrete example: if you're watching a person standing still with a still background, the P-frame might say "use blocks 5, 7, and 42 from the previous I-frame, and here's the new information for block 23 where the speaker's mouth is moving." This dramatically reduces the data needed compared to encoding each frame completely.

B-frames (bi-predicted frames) take this logic further by allowing references to frames in both directions—past and future. This is the conceptually mind-blowing part: to decode a B-frame, the decoder must first receive and buffer the future frame it depends on, then work backward to reconstruct the current frame. The decoding order differs from the display order. An encoder producing a B-frame must be sophisticated enough to look ahead and decide which future frame would best help compress the current one.

## Group of Pictures and Encoding Parameters

The default Group of Pictures (GOP) in FFmpeg is typically around 250 frames—roughly 10 seconds at 24 or 25 frames per second. This means the first frame is an I-frame, and then 249 frames of P and B predictions follow before the next I-frame. Longer GOPs mean smaller file sizes (more compression efficiency) but slower seeking and higher error propagation if a frame is corrupted. Shorter GOPs give faster random access at the cost of compression efficiency.

The conversation explores the numerous parameters available in modern encoding: resolution, frame rate, codec selection, bitrate versus quality tradeoffs, constant bitrate versus constant quality modes, quantization parameters, GOP length, and number of B-frames. FFmpeg provides access to nearly all of these, giving users granular control that professional encoders at major streaming platforms exploit extensively.

## Intra Refresh: Eliminating Keyframes Altogether

One particularly clever technique the guest mentions is "intra refresh," used extensively in real-time communication systems. Instead of sending periodic I-frames that create visible quality steps and consume extra bandwidth, the encoder gradually builds up a complete frame across many packets over time. Each frame refreshes certain parts of the image, and over the course of a second or so, the entire frame gets refreshed. This eliminates the jarring quality dip when an I-frame hits and smooths out bandwidth usage, making it ideal for video calls and live streaming where consistent latency matters more than periodic full-frame accuracy.

## The Industry Behind the Sliders

A significant portion of the conversation addresses the human infrastructure behind video compression. Thousands of engineers at YouTube, Netflix, Meta, and other platforms don't write new codecs—they optimize the parameters for specific content types. A theatrical movie has different optimal settings than a smartphone video or a screen recording. Movies have consistent quality, controlled lighting, and known aspect ratios. Phone videos have variable lighting, camera shake, and diverse content. Screen recordings have sharp edges, text, and minimal noise. Each requires different encoding approaches.

YouTube's scale presents unique challenges: not only must they serve billions of viewers, but they must also ingest and encode uploads from millions of sources, then serve the resulting adaptive streams with minimal latency to sometimes just a handful of viewers. Unlike Netflix's broadcast model where one encode serves millions of simultaneous viewers, YouTube must handle long-tail content watched by five people in different countries on different devices, all requiring different quality levels and formats.

## Historical Context: From Browser Plugins to WebAssembly

The conversation ends with an interesting historical note about Google Video, an early predecessor to YouTube that used the VLC plugin to run inside Internet Explorer—actually executing VLC code within the browser. This contrasts sharply with the modern approach of compiling FFmpeg to WebAssembly, a JavaScript-compatible format that runs in the browser's sandboxed virtual machine. Today, the full power of FFmpeg's video processing can run client-side in a web browser, representing a complete inversion of the historical plugin architecture.

---

# Detailed Takeaways

**The codec you choose depends entirely on your workflow stage, not just quality preferences.** ProRes exists because editing requires instantaneous random access to any frame, which temporal compression fundamentally prevents. Choosing ProRes for distribution would create unwieldy file sizes; choosing H.264 for editing would create sluggish seeking. The "best" codec depends on whether you're creating, editing, or distributing content. Understanding this distinction helps professionals make appropriate choices and prevents amateurs from making costly ones.

**B-frames reveal the encoder's hidden intelligence.** The ability of B-frames to reference future frames means the encoding process requires looking ahead, analyzing potential frame sequences, and making predictions about which reference frames would minimize the eventual bitrate. The decoder appears to simply play back what it receives, but the encoder performs substantial computational analysis to produce that sequence. This asymmetry explains why encoding takes much longer than playback and why codec implementations require extensive testing to ensure different encoders produce compatible streams.

**The ecosystem achieves something remarkable: bit-exact reproducibility across manufacturers.** The guest notes that decoders from different manufacturers produce bit-for-bit identical output from the same input stream. This interoperability is essential for a global video infrastructure where content encoded on one continent must play identically on devices manufactured elsewhere. Achieving this requires extensive specification work, conformance testing, and quality assurance—it's a quiet achievement underlying all modern video.

**Streaming at scale requires solving the long-tail problem, not just the popular content problem.** YouTube serves videos watched by five people with the same infrastructure that serves videos watched by fifty million. This means their encoding and delivery systems must handle every conceivable content type, viewer count, device capability, and network condition. The complexity isn't in serving popular content—it's in doing so efficiently for millions of videos that might never go viral but must still be available instantly when someone finds them.

**Professional encoding is an art form informed by content analysis.** The discussion about optimizing parameters for different content types—movies versus phone videos versus screen recordings—highlights that encoding isn't a mechanical process. An engineer optimizing encoding for a Hollywood film brings different assumptions than one optimizing for user-generated content: film has consistent cinematography, controlled lighting, and known scene cuts; phone video has variable quality, motion blur, and noise; screen recordings have sharp text, limited color variation, and specific motion patterns. Each requires different parameter tuning, and understanding these differences is a specialized professional skill.

---

# Who This Is For

This content is essential viewing for software engineers, video engineers, and technical decision-makers who work with video in any form—whether building streaming platforms, developing playback systems, creating video editing tools, or simply trying to choose the right export settings in Final Cut Pro or DaVinci Resolve. The explanation of IPB frames and codec-container combinations provides mental models that help debugging and decision-making, even if you're not implementing codecs yourself.

For product managers and technical leads at streaming companies or video platforms, the discussion about optimization as a profession and YouTube's scale challenges offers valuable context about where engineering investments should focus. Understanding that "codec work" and "encoding parameter optimization" are distinct specializations helps with hiring decisions and resource allocation.

For journalists and analysts covering the streaming industry, the technical grounding provided here helps contextualize industry moves—like the push toward AV1 adoption or Apple's ProRes investments—without requiring deep technical expertise. The historical note about Google Video and the evolution toward WebAssembly provides useful perspective on how browser video has changed over time.

General viewers who find themselves frustrated by video quality or buffering will gain appreciation for the engineering complexity underlying their streaming experience, though the primary value here is for those with technical roles.