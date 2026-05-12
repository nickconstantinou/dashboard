---
title: 'Fast robot teleoperation (at ultra-low 8ms latency): Kyber explained | Lex
  Fridman Podcast'
date: '2026-05-12'
type: youtube
category: AI/Tech
video_id: Y6mjiS00Y-0
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=Y6mjiS00Y-0
---

# Fast Robot Teleoperation at Ultra-Low 8ms Latency: Kyber Explained

## Key Insights

- **Kyber achieves 7ms end-to-end latency** (Windows to Windows or Windows to Mac), with a target of 4ms glass-to-glass—equivalent to 240Hz refresh, enabling control of fast-moving systems like drones and robotic arms.
- **The platform uses a single UDP socket** to multiplex video, audio, and control data (mouse, keyboard, gamepad) while maintaining precise synchronization across multiple streams—a critical advantage over TCP-based solutions that suffer from "end-of-line" latency problems.
- **Clock drift synchronization is the core engineering challenge**: When recording from multiple cameras (5-6 on a robot), GPS, and sensors, timestamps must remain coherent for AI training data; Kyber addresses this using techniques borrowed from MPEG-TS broadcasting.
- **Forward error correction (FEC)** over-transmits a small percentage of data, allowing the receiver to reconstruct missing packets without the latency penalty of TCP acknowledgment loops—essential for long-distance teleoperation over the public internet.
- **The demo at CES Las Vegas** controlled a 3D-printed rover with a telescopic arm from France using only a webcam and minimal server hardware, demonstrating practical feasibility of intercontinental robot teleoperation.

---

## 1. Introduction

The gap between human reaction time and machine response has always been the fundamental bottleneck in remote control systems. Whether operating a surgical robot across continents, piloting a drone in hostile environments, or training AI models through teleoperation, the delay between intention and action determines not just user experience but outright feasibility. Jean-Baptiste Kempf, a veteran of video encoding with deep roots in the VLC media player ecosystem and MPEG standardization, has been working on this problem for years—first as CTO of a cloud gaming startup, and now through his new venture, Kyber.

Kyber represents a fundamental reimagining of how we transmit control signals and video feedback for interactive, real-time applications. Unlike traditional streaming solutions optimized for passive viewing—where milliseconds of delay are merely annoying—Kyber targets applications where latency directly determines whether a system works or fails. The platform is built as an SDK that enables developers to create applications for robot teleoperation, drone control, remote vehicles, and even cloud gaming with unprecedented low-latency performance. The core innovation lies not in any single technology but in the holistic integration of encoding optimization, network protocol design, and precise temporal synchronization across multiple data streams.

What makes this approach particularly compelling is the convergence of several technological trends: increasingly powerful edge computing, advances in neural video codecs, and the growing importance of teleoperation for training robotic AI systems. As companies race to develop general-purpose robots capable of performing useful tasks in unstructured environments, the ability to collect high-quality training data through remote operation has become a critical differentiator. Kyber addresses this need directly.

---

## 2. Key Concepts & Arguments

### The Latency Problem in Interactive Applications

The speaker traces the evolution of video transmission from file encoding through streaming services to the emerging category of interactive applications. Each stage has placed different demands on the underlying technology: early video work prioritized compression efficiency and quality, streaming added requirements for consistent bandwidth and buffer management, but interactive control introduces an entirely different constraint structure. When you're controlling a robot arm, piloting a drone, or playing a cloud-rendered video game, every millisecond of delay between your input and the system's response creates a compounding problem. Your control inputs must reach the machine quickly, the machine's sensor feedback must return to you even more quickly, and your brain must process this feedback and issue new commands—all within a tight enough loop to maintain stability.

The speaker draws a compelling parallel to autonomous vehicles: even though Waymo's system is largely autonomous, when edge cases occur—the 1% of situations the AI cannot handle—human operators must take over remotely. This handoff requires not just adequate latency but latency low enough that the human can maintain situational awareness and react appropriately. A delay of even 50-100ms can transform a smooth intervention into a collision.

### UDP vs. TCP: Why Protocol Design Matters

Kyber's architecture deliberately chooses UDP over TCP for its core transport mechanism, and the reasoning reveals deep understanding of network characteristics. TCP's reliability guarantees come at a cost: when packets are lost, the protocol must wait for acknowledgment before retransmission, and this round-trip time becomes a floor on minimum achievable latency. For file downloads or video streaming, this is acceptable—buffering can absorb variability. But for interactive control, that buffering is unacceptable.

The UDP-based approach in Kyber trades reliability for speed. Packets are sent continuously without waiting for acknowledgment, meaning the system never stalls waiting for network round-trips. However, this creates a new challenge: what happens when packets are lost? The answer lies in forward error correction. Kyber over-transmits a small percentage of redundant data—typically a few percent of total bandwidth—that allows the receiver to reconstruct missing packets locally without requesting retransmission. This elegant solution sidesteps the latency penalty of TCP's acknowledgment loops while still providing robust error handling, crucial for applications like drone control where packet loss could mean loss of the aircraft.

### Multi-Stream Synchronization and Clock Drift

Perhaps the most technically sophisticated aspect of Kyber is its approach to temporal synchronization across heterogeneous data streams. Modern robotic systems don't just have one camera—they might have two, five, or ten cameras plus GPS, IMU sensors, force sensors, and more. When training AI models on this data, temporal coherence is essential: the video frames from different cameras must be precisely timestamped relative to each other, and those timestamps must remain accurate across extended recording sessions.

The problem is that clocks drift. A computer's internal clock might run slightly fast or slow relative to an external reference, and over time this drift compounds. Existing solutions work adequately for single-camera setups but break down when synchronizing multiple independent streams. The speaker explains that Kyber applies techniques developed for MPEG-TS broadcasting to track and compensate for clock drift in real-time. When a Kyber stream is recorded for later playback—critical for training robotic AI systems—users can be confident that the data remains temporally coherent regardless of recording duration. This means AI models trained on Kyber recordings will see consistent, accurate sensor data rather than corrupted timestamps that could teach incorrect associations.

### The Architecture of Ultra-Low Latency Encoding

Achieving 4ms glass-to-glass latency requires optimization at every stage of the pipeline. The speaker describes a target where the encoder itself takes only 4 milliseconds to compress a frame, which represents an enormous engineering challenge. Current systems achieve approximately 3.5 milliseconds on Nvidia hardware encoders, meaning most of the budget is consumed before a single bit crosses the network.

The speaker's approach emphasizes minimizing local latency as much as network latency. Even with perfect networking, an encoder that adds 20ms of delay makes achieving end-to-end goals impossible. This is why Kyber works closely with encoder optimization, borrowing techniques from both traditional video encoding and emerging neural approaches. The decoder side shows similar optimization: current implementations achieve around 2 milliseconds on Intel hardware. The remaining milliseconds must cover network transit time, which varies based on distance and network conditions.

### Practical Applications and Use Cases

Kyber targets a diverse range of applications united by their latency requirements. Teleoperation of humanoid robots for both direct control and data collection for AI training represents a major focus area. Remote drones—potentially for defense or inspection applications—require the low latency necessary for stable flight control. Remote vehicles and rovers, demonstrated at CES with a France-to-Las Vegas control link, show the system's practical capability. Remote surgery and other medical applications where experts cannot be physically present but must maintain precise control. Even cloud gaming, where the speaker previously worked, benefits from the same optimizations.

The speaker articulates a clear vision: "the goal of Kyber is to make distance disappear, because it's either projection of skills or projection of power." This captures the essential value proposition—enabling human operators to extend their capabilities across arbitrary distances without degradation from latency. For robotic AI training specifically, Kyber enables the collection of high-quality, temporally coherent sensor data that current solutions cannot provide reliably.

### Integration with Modern AI Systems

The discussion emphasizes that Kyber is not just about human teleoperation but also about enabling AI systems to control multiple machines. As robotic systems become more capable, the transition from human teleoperation to AI-in-the-loop control becomes natural: humans supervise and intervene when needed, but AI handles routine operations. This hybrid architecture requires the same low-latency guarantees as direct human control, since AI systems may need to respond to novel situations faster than their training covered.

The synchronization features become particularly valuable here. When training reinforcement learning models or behavior cloning systems, the quality of training data determines ceiling performance. Temporal inconsistencies in sensor streams—frames that are actually from different moments but appear simultaneous—would corrupt the training signal and limit model capabilities. Kyber's approach ensures that multi-camera, multi-sensor recordings remain coherent even across long sessions, enabling high-quality datasets for the next generation of robotic AI.

---

## 3. Detailed Takeaways

**Latency is measured end-to-end, not component-by-component.** Achieving 7ms total latency (and targeting 4ms) requires optimizing the entire pipeline: encoder performance, network protocol, decoder speed, and clock synchronization. Systems that optimize only one component while neglecting others will fail to reach practical latency goals. The speaker notes that the Nvidia hardware encoder alone consumes 3.5ms of the budget, leaving minimal margin for network transit.

**UDP with forward error correction provides the best latency-reliability tradeoff for interactive applications.** Traditional approaches using TCP introduce round-trip latency that compounds with packet loss. UDP eliminates waiting for acknowledgments but requires error correction to handle lost packets. Kyber's FEC approach sends redundant data that allows reconstruction without retransmission, achieving reliability without latency penalties. This is fundamentally different from adaptive bitrate streaming, which prioritizes quality over responsiveness.

**Clock synchronization across heterogeneous sensors is a solved problem with the right approach.** Multi-camera robot recordings require nanosecond-level temporal accuracy across all sensors, but clocks drift over time. Kyber applies techniques from MPEG-TS broadcasting to continuously track and compensate for drift, ensuring recordings remain temporally coherent regardless of duration. This matters critically for AI training, where corrupted timestamps would produce poorly generalizing models.

**Single-socket architectures simplify deployment and improve reliability.** Rather than managing multiple connections for video, audio, and control data, Kyber multiplexes everything over a single UDP socket. This reduces connection management overhead, simplifies firewall configuration for enterprise deployments, and ensures all data streams remain synchronized. The approach trades some theoretical bandwidth efficiency for practical deployment simplicity.

**Human-in-the-loop teleoperation is becoming essential for both deployment and training of robotic systems.** Direct teleoperation enables expert operators to extend their skills to remote locations, but it also provides the highest-quality training data for AI systems. When robots are trained on data collected through Kyber, they learn from temporally coherent, high-frequency sensor streams that capture the full complexity of real-world manipulation. This positions teleoperation not as a temporary stepping stone to full autonomy but as a permanent component of robust robotic systems.

---

## 4. Who This Is For

Kyber's target audience spans several distinct groups. **Robotics researchers and companies** building manipulation systems will find immediate value in the ability to collect high-quality training data through teleoperation, while also benefiting from the platform for direct remote control applications. **Autonomous vehicle developers** face similar teleoperation needs when their systems encounter edge cases beyond their operational design domain. **Drone operators** seeking reliable control over long distances, including military and inspection applications, will appreciate the FEC-based reliability. **Cloud gaming companies** can leverage the latency optimizations for competitive gaming experiences, though the gaming market is more price-sensitive than the robotics market.

For developers building applications where human operators control machines in real-time, Kyber offers a turnkey solution that handles the complex engineering of ultra-low latency video and control transmission. For researchers collecting robotic training data, the platform provides the temporal coherence necessary for high-quality datasets. The SDK approach means integration requires defining the right interfaces rather than rebuilding core networking and encoding infrastructure from scratch.

The underlying technologies—UDP transport, forward error correction, clock synchronization, encoder optimization—represent significant engineering investments. By packaging these into an accessible SDK, Kyber democratizes access to capabilities that previously required specialized expertise in video encoding, network protocol design, and real-time systems. This positions the platform as infrastructure for the emerging teleoperation economy, where human operators extend their capabilities across arbitrary distances to control machines in dangerous, remote, or simply inconvenient locations.