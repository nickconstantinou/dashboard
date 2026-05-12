---
title: What will be remembered about human civilization 1,000 years from now? | Lex
  Fridman Podcast
date: '2026-05-12'
type: youtube
category: AI/Tech
video_id: SvEKSZeeOMA
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=SvEKSZeeOMA
---

# What Will Be Remembered About Human Civilization 1,000 Years From Now?

## Key Insights

- **Dave Rice and the City University of New York** lead a dedicated archiving preservation community that sees FFmpeg as a "Rosetta Stone" enabling multimedia playback a thousand years from now
- **C programming language as a timeless medium**: FFmpeg is written in C, described as "the closest to mathematics you're probably going to get" — essentially the Latin of programming languages that will remain learnable and usable for centuries
- **The BBC Micro Doomsday failure**: The UK archived extensive content on BBC microcomputers, yet within 10-20 years, no one had the correct software to play the material — a cautionary tale demonstrating how quickly digital formats become inaccessible
- **FFV1 codec** was specifically developed by the archiving community for lossless preservation with error recovery capabilities, ensuring that if a single bit flips, only a portion of a frame is lost rather than an entire Group of Pictures (GOP)
- **Tape crisis**: There simply aren't enough working tape heads remaining worldwide to read all the archived tapes from the 1970s and 1980s, forcing archivists to make impossible decisions about what to save and what to discard

---

## Introduction

In a fascinating discussion about the preservation of human knowledge, a speaker from within the open-source multimedia community reveals the quiet heroism happening behind the scenes of digital archiving. The conversation centers on a question that seems almost impossibly large: what will future civilizations know about us? More specifically, how do we ensure that the multimedia record of our era survives long enough to be understood?

This isn't merely an academic exercise. The stakes are profound and the timeline is urgent. As the speaker notes, "People don't realize we are losing today a ton of films. There is a ton of things from the 30s, 40s, and 50s that were there is no value." The harsh reality is that entire chapters of human visual history are being silently erased—not through dramatic destruction, but through the mundane decay of obsolete formats and the brutal economics of limited resources.

The discussion situates itself within the open-source multimedia ecosystem, particularly FFmpeg, which has emerged as perhaps the most critical tool in humanity's efforts to preserve its visual heritage. This isn't just about software; it's about the intersection of mathematics, community values, and the existential question of what we owe to the future.

---

## Key Concepts & Arguments

### FFmpeg as Humanity's Digital Rosetta Stone

The speaker frames FFmpeg not merely as a software tool but as a civilizational instrument for preserving visual knowledge across millennia. The choice of C as the implementation language is deliberate and profound. "C is the closest to mathematics you're probably going to get," the speaker explains, "the closest to logic." This matters because mathematics and logical notation persist across cultures and centuries in ways that proprietary formats cannot.

The comparison to Latin is illuminating: C will become a "thing that you learn from the past, but it will still be usable in certain contexts." We still study and occasionally use Latin; similarly, C will remain readable and compilable even as more modern languages rise and fall. A thousand years from now, someone could theoretically learn C and compile the FFmpeg source code, preserving the ability to decode vast swaths of human multimedia history.

The open-source nature of FFmpeg also ensures portability across platforms. Unlike proprietary codecs that might require specific hardware or licensing arrangements, FFmpeg can be compiled and run on whatever computing infrastructure exists in the future. This matters enormously given the demonstrated fragility of digital formats. The speaker references "famously in the UK there was something called the new Doomsday Book" — an attempt to comprehensively archive material on BBC microcomputers — that became unreadable within 10-20 years when the necessary software became obsolete. "Someone had to go and reverse engineer this and that was like 20 years. Imagine that in a thousand years." The lesson is clear: formats without open, maintainable implementations are essentially time bombs.

### The Active Archiving Preservation Community

The speaker credits "someone called Dave Rice" from City University of New York as the leader of what they describe as "one of the coolest communities in open source multimedia." This community operates under severe resource constraints — "they lack budgets, but two they see the fact that archiving video is important for the world."

The community's philosophy combines technical rigor with deep respect for the actual content being preserved. "They have a deep appreciation of the content itself of the video itself," the speaker notes, explaining that this leads to "deeply understanding the thing that is to be preserved which you sometimes might not be thinking about when you're obsessing about the actual technology of the encoding." This is not merely engineering; it's a form of humanistic technical work.

The community also demonstrates remarkable generosity in sharing workflows and training. "Because it's open source, they give this away their workflows to countries who can't afford to have archiving institutions where archiving is done by volunteers." The speaker specifically mentions teaching "children in India to do FFmpeg commands." This global, educational dimension reflects "the model ethos of what we're trying to achieve."

### The FFV1 Lossless Codec and Technical Preservation Strategy

The archiving community funded the development of the FFV1 codec specifically to address archival concerns. The core issue is compression: "they're really scared about the act of compression losing things. And this could this is they have a fair point in this, you know. Yeah. If they compress too hard, it could change the view of the material. There could be something slightly different here and there."

FFV1 is a lossless codec designed for fast software-based encoding. But the innovation extends beyond compression ratios. "They can prove mathematically that it's lossless," the speaker explains. The codec also includes sophisticated error recovery capabilities: "if they store on tapes or other hard disks, I lose some bits. I need to recover quickly. I can't lose a whole GOP because I've lost the bit." The system is designed so that bit errors affect only "a portion of a given frame" rather than corrupting larger temporal windows.

The funding for this development came from the community itself: "They funded GPU encoding in FFmpeg to make FFV1 encode faster." This is a remarkable example of a small but dedicated community investing resources to solve a problem that the broader market has no incentive to address.

### The Race Against Time and Formats

The speaker paints a sobering picture of the current state of media preservation. "People don't realize we are losing today a ton of films. There is a ton of things from the 30s, 40s, and 50s." The crisis extends to analog and digital tape formats from later decades: "tape 70s and 80s there's tape and there's not enough tape heads in the world to read all the tapes."

This creates what the speaker calls "huge moral hazard" — the impossible obligation to decide what gets preserved when everything cannot be. "They have to decide what they want to archive and throw away the rest of the tapes." No algorithm or principle can make this truly manageable; it remains an ongoing tragedy of lost information.

The work of preservation is also a form of archaeological discovery. "There's a lot of value in archiving all that footage and then over time finding the gems that we don't know are there." The speaker uses the metaphor of "needle in a haystack": "Hey, there was something in that corner that we just didn't know." Lossless archiving makes this discovery possible retroactively; lossy compression might discard exactly the detail that future researchers find significant.

### The Transition Point from Scarcity to Slop

Perhaps the most striking observation is the framing of our current era as a critical transition point. "We are drowning in AI slop. This stuff needs to be important and archived well. What was the what was life like?" The speaker suggests that capturing the 20th century in the 21st century is "essential because it feels like a transition point. Where we went from scarcity of data to slop. Yeah. Oceans of slop."

This framing elevates the archival community's work from mere technical maintenance to historical importance. The question is not simply "how do we preserve files" but "how do we document humanity at the precise moment when the ratio of signal to noise fundamentally shifts?" Future generations looking back at our era will need to distinguish the authentic record from the generated noise — and the archival decisions made now will determine whether that's even possible.

---

## Detailed Takeaways

**The Imperative of Open, Maintainable Formats**: The BBC microcomputer example demonstrates that proprietary formats are inherently fragile over long time horizons. What appears "modern" and "standard" today may be completely unreadable in decades. FFmpeg's open-source nature and its basis in the enduring C language create genuine longevity. Organizations and individuals creating digital archives today should prioritize formats with open specifications and widely available implementations, even if proprietary alternatives offer better current performance or convenience.

**Lossless Compression Protects Unknown Value**: The archiving community's insistence on mathematical losslessness isn't perfectionism — it's recognizing that future significance can't be predicted. "You compress away because some little thing oh wow, there's something there." The details discarded by lossy compression may include exactly what future researchers need. This suggests that any archive with uncertain future use cases should lean toward lossless or near-lossless formats, accepting higher storage costs as insurance against information loss.

**Technical Expertise and Content Understanding Must Combine**: The archivists "have specialist advice" and "know things on video that we don't." They understand "in the 1950s colorimetry was done like this on this certain type of tape." This deep content knowledge informs technical decisions — you can't preserve something properly if you don't understand what makes it meaningful. Any serious archival effort should include not just engineers but content specialists who understand the historical and aesthetic significance of the material being preserved.

**Community-Driven Preservation Fills Market Gaps**: The archival community operates with "limited funds" yet has accomplished remarkable things because they combine genuine expertise with "deep appreciation" for the material. This suggests that preservation cannot be left entirely to market forces; it requires communities of practice organized around values rather than profit. Supporting these communities — through funding, contributions, or simply awareness — may be among the most impactful ways to ensure the long-term survival of human cultural heritage.

**The Clock Is Already Running**: The tape preservation crisis is not hypothetical — "there are not enough tape heads in the world to read all the tapes" right now. This means the window for action is already narrow. Every year of delay potentially results in irrecoverable losses. Organizations holding legacy media should treat preservation as urgent rather than routine, recognizing that the economic and technical window for digitization is finite.

---

## Who This Is For

This discussion is essential for anyone responsible for institutional, corporate, or personal digital preservation — particularly those dealing with video or multimedia archives that may span decades. Archivists and librarians will find validation and inspiration in the community-focused approach described, as well as specific technical guidance on codec selection and error recovery strategies.

Software developers working in multimedia will gain crucial perspective on why certain constraints matter. Understanding the archival use case explains why lossless codecs and error recovery exist — not as academic features but as practical necessities for preserving humanity's visual memory.

Additionally, anyone making decisions about long-term storage — from family video preservation to enterprise document management — will benefit from understanding the "transition point" framing. The principle of prioritizing formats with longevity and open implementations applies at every scale.

Finally, this discussion speaks to anyone who has ever wondered what future civilizations will know about our time. It provides both a diagnosis of the current crisis and a model for what can be done about it — combining technical rigor with humanistic concern for the meaning of what we're preserving.