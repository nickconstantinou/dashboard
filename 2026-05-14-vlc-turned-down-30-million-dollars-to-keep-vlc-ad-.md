---
title: VLC turned down $30+ million dollars to keep VLC ad-free | Lex Fridman Podcast
date: '2026-05-14'
type: youtube
category: AI/Tech
video_id: W37rNcA2yPU
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=W37rNcA2yPU
---

# Key Insights

- **Refused "dozens of millions"** to keep VLC ad-free — JB calculates he could have become a multi-millionaire "on the beach" but deemed monetization "not moral"
- **VideoLAN/VLC predates YouTube by roughly 10 years** — the Network 2000 project launched in 1995-1996, when main computers were 486 DX processors at 33 MHz and having a fifth TV channel was "a big deal"
- **Token ring networking** (sponsored by IBM and 3Com) created inherent latency problems that made video games unplayable, driving students to seek faster solutions
- **Open source took 3 years to negotiate** — both the university and student developers initially wanted to monetize the MPEG-2 decoders before eventually agreeing to release VideoLAN as free software
- **Student self-governance model** at École Centrale Paris created the unique environment where VLC emerged — all campus facilities (electricity, radio, TV, supermarket) were managed by 22-year-old students who "needed to run your campus, else you don't have electricity"

---

# How VLC Refused $30+ Million to Stay Free: The Story Behind the World's Most Popular Media Player

In the world of open-source software, few stories carry the legendary status of VLC media player and its creator, Jean-Baptiste Kempf. The tale has become something of an internet meme — a wizard-like figure in a VLC hat repeatedly turning down tens of millions of dollars to keep the software free, ad-free, and open source. On a recent appearance on the Lex Fridman Podcast, Kempf pulled back the curtain on this decision, tracing it not just to principle, but to an unlikely origin story rooted in 1980s French engineering education, token ring networks, and a bold experiment in video streaming that predated YouTube by nearly a decade.

The conversation begins with the legend itself — the Reddit meme that has circulated for years showing Kempf as a wizard refusing mountains of money. But as Kempf explains with characteristic directness, the meme understates the reality. "Yes, it is true," he confirms. "I refused dozens of millions of dollars. Yes, several times." The offer wasn't hypothetical — companies approached VLC repeatedly with substantial deals, and each time, Kempf said no. His reasoning combines principled idealism with self-aware pragmatism: "I did not do it because I thought it was not moral and it was not the right thing to do... I work for the greater good. I work for people." But he adds a crucial nuance — he also didn't feel "completely legitimate" to make such a decision unilaterally, and that hesitation speaks to the deeper story of how VLC came to exist in the first place.

---

## The Origins: A Campus Run by Students

To understand VLC's commitment to free software, you need to understand where it was born: École Centrale Paris, one of France's elite engineering schools. The institution occupies a unique position in French higher education — outside the traditional university system, accessible only after students spend two grueling years mastering mathematics and physics to gain admission. The school itself has a fascinating history tied to Gustave Eiffel himself, who attended the original institution. When the school attempted to relocate from central Paris to Clermont-Ferrand after World War II, alumni revolted, purchased land south of Paris, and established a self-governing campus unlike anything else in France.

What made this campus remarkable was its radical decentralization. "Everything on the campus was managed by students," Kempf explains. "The university did nothing, right? So, uh, radio, uh TV, uh supermarket, uh library, um defining who was going to into which rooms, um everything was managed by the students." This wasn't theoretical co-governance — it was practical necessity. "You're 22 and you need to run your campus, else you don't have electricity, right?" This hands-on education in infrastructure, negotiation, and communal responsibility would become the crucible in which VLC was forged.

---

## Token Ring and the Problem of Latency

The technological catalyst came in the 1980s, when École Centrale Paris became one of the first campuses in Europe to deploy a computer network — primarily sponsored by IBM and 3Com using token ring technology. Token ring represents a nearly forgotten chapter in networking history. Unlike modern Ethernet or WiFi, where devices connect through routers and can communicate relatively freely, token ring created a literal physical ring. "When you want to send a message, you talk to your neighbor who's going to put the message to the next one who's going to put the things to the next one," Kempf describes. "Everyone is linked um it's type really a ring."

The fundamental problem with this architecture was latency. Every computer on the network had to examine every passing message: "Open the message, see if it's okay, is it for me? No, it's not. And then send it back like a token which is traveling around the ring." For basic tasks like telnet and email in the 1980s, this was acceptable. But by 1994 and 1995, when games like Doom and Duke Nukem arrived, token ring's inherent delays became catastrophic. "You have li- high latency video games, basically you die, right?" Students approached the university administration for a network upgrade — and were rebuffed.

---

## The Network 2000 Experiment: Video Streaming in 1995

The rejection came with a caveat: the campus wasn't technically university property. It was managed by the nonprofit alumni association. "The campus is not ours. You manage it," the administration told them. "So so so do something."

Students took this challenge to an unexpected place — the offices of Bull, a major French technology company. They met with the company's CIO, who made a prediction that would shape VLC's future: "The future of video is satellite." While that forecast would prove partially wrong in the long term, the insight was transformative for 1995. The CIO proposed something elegant: instead of installing individual satellite dishes and decoders for each of the 1,500 students on campus, why not deploy a single massive dish, one central decoder, and stream video directly over the campus network?

This required an extremely fast network — ATM technology running at 155 megabits per second, among the fastest in Europe at the time. The students built the project, calling it Network 2000. "Everything is futuristic," Kempf laughs. "It's called 2000." The demonstration, however, was barely functional. "It's completely hacked. It crashes after 45 seconds. That's okay. The demo is 40 seconds. It leaks memory. That's okay. They put 64 megabyte of RAM instead of the age of 16 you have." The technical foundation was fragile, but the concept worked — and it was arguably the world's first video streaming experiment over a local area network.

---

## Birth of VideoLAN: The Real VLC Origin

Six months to a year after Network 2000 concluded, two new students arrived with a revolutionary idea: what if this technology wasn't limited to a single French engineering campus? What if anyone could stream video over a local network? They created the VideoLAN project. One of its founders, Christophe Massiot, remains a close friend of Kempf's to this day.

At this point, VLC didn't exist yet — VideoLAN was a server solution for network streaming, not a consumer media player. More significantly, the project wasn't open source. It took approximately three years of negotiation before the school agreed to release the code freely. The resistance came from multiple directions. The university wanted to protect intellectual property. Students who had worked on the original MPEG-2 decoders wanted potential monetization. "Because the university wanted to get some because of the IP and copyright of the students wanted to basically monetize these MPEG-2 decoders," Kempf explains.

The irony is striking: the culture that would eventually produce one of the world's most successful open-source projects initially resisted the very concept of free software. But persistence won out, and VideoLAN eventually became the open-source project that would eventually transform into VLC media player.

---

## Why Refuse the Money? The Philosophy of Free Software

Returning to the $30+ million question, Kempf's reasoning goes deeper than simple idealism. He describes his work as serving "the greater good" — a phrase he returns to multiple times. But he also expresses a specific discomfort with unilateral control over decisions that affect millions of users. "I did not feel that I'm completely legitimate to do that," he says, acknowledging that the project belongs to its community of users and contributors, not just to him.

This philosophy has practical consequences. VLC runs on an incredibly diverse range of hardware and software platforms — from latest-generation iPhones to ancient Android devices no longer receiving updates, from Windows and macOS to Linux and obscure Unix variants. "We want to support everything," Kempf has said in other contexts. Commercial interests would inevitably push toward profit-maximizing decisions: focusing on popular platforms, adding premium features, or introducing advertising. VLC's independence means it can optimize for universality rather than revenue.

---

## The Modern Context: VLC in 2024

VLC's refusal to monetize stands in stark contrast to virtually every other piece of software that has achieved similar scale. Streaming platforms have proliferated with advertising and subscription models. Media players have bundled spywares and bloatware. The browser landscape has consolidated around ad-supported Chromium derivatives.

Yet VLC, now downloaded over four billion times, remains exactly what it was in 2001: free, open source, and ad-free. The VideoLAN organization that maintains it operates through donations, grants, and the passionate work of volunteers. Kempf himself continues to contribute actively, still active on Reddit where his "Good morning" comments can gather 24,000 upvotes.

The choices made by those Network 2000 students in 1995 — to prioritize access over control, community over profit — have created software that bridges technological gaps across the global south, enables media accessibility on aging hardware, and provides a reliable fallback when streaming platforms fail or geo-restrict content. VLC's success demonstrates that open-source software can achieve commercial-scale adoption without compromising its founding principles.

---

## Who Should Care About This Story

**Software developers and tech entrepreneurs** will find in VLC's history a powerful counterargument to the assumption that successful software must monetize. The project demonstrates that open-source sustainability is possible through community, grants, and principle — not advertising or venture capital.

**Open-source advocates and digital rights activists** will appreciate the concrete details of how VideoLAN navigated IP negotiations, university bureaucracy, and the early open-source movement's growing legitimacy in the 1990s.

**Anyone who uses VLC** — which is to say, nearly everyone who has ever watched a video on their computer — gains a richer understanding of the software's values and origins. In an era of increasing surveillance capitalism and platform lock-in, VLC represents an alternative model: technology built for human use rather than human extraction.

**Students and educators** will find in the École Centrale Paris story an inspiring model of experiential learning. The self-governing campus wasn't just a quirky administrative structure — it was the crucible that produced Network 2000, VideoLAN, and ultimately VLC. When 22-year-olds are responsible for real infrastructure, they rise to the occasion in ways traditional curricula cannot match.

The legend of VLC's refused millions is more than a tech meme. It's a case study in how principled decisions compound over decades into something genuinely transformative — software used by billions of people, controlled by no corporation, and free forever.