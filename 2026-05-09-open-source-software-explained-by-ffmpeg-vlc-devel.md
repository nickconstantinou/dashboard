---
title: Open source software explained by FFmpeg & VLC developers | Lex Fridman Podcast
date: '2026-05-09'
type: youtube
category: AI/Tech
video_id: 1p0R-c2Lacw
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=1p0R-c2Lacw
---

# Open Source Software Explained: A Deep Dive with FFmpeg and VLC Developers

**Key Insights**

- Open source projects operate like distributed recipe-sharing: FFmpeg and VLC provide not just the final "cheesecake" but also the recipe, the oven-building instructions, and the freedom to resell modified versions—unlike proprietary software which only gives you the finished product
- FFmpeg has had 2,000-3,000 contributors since its inception, while the Linux kernel has approximately 10,000 contributors worldwide, demonstrating the massive collaborative scale these projects achieve
- Open source licenses create a "social contract" (referencing Rousseau) where the community agrees on little else besides the license terms; this contract enables community splits (forks) and eventual reunification, as seen with GCC → EGCS and KHTML → WebKit → Blink
- VLC underwent a complex relicensing process from GPL to LGPL for its libVLC core, which required obtaining agreement from thousands of contributors (some deceased), highlighting why such projects cannot simply change licenses unilaterally
- Cloud providers building billion-dollar businesses by wrapping open source tools behind APIs (without contributing back) prompted companies like Elastic and MongoDB to change their licenses, creating a tension between open source principles and commercial sustainability

---

## Introduction

When Lex Fridman sat down with the developers behind FFmpeg and VLC—two of the most foundational open source projects in modern computing—he wasn't just conducting a technical interview. He was opening a window into a philosophy that has fundamentally reshaped how software gets built, distributed, and sustained across the globe. These projects, which touch virtually every video watched and audio processed on the internet, represent something larger than their technical achievements: they embody a movement that grants unprecedented power to individuals while challenging traditional notions of intellectual property and commercial software development.

FFmpeg serves as the universal workhorse for video and audio transcoding, used everywhere from Hollywood production pipelines to smartphone apps. VLC, the media player developed by the VideoLAN project, is one of the most downloaded pieces of software in history, capable of playing virtually any format imaginable. Behind both projects sits the same fundamental question: what does it mean to truly share software? The conversation that unfolded touched on everything from chocolate cheesecake metaphors to the philosophical foundations of open source licensing, revealing how deeply these projects are woven into the fabric of modern technological infrastructure.

The timing of this discussion feels particularly relevant. As debates about AI training data, platform monopolies, and software sustainability continue to intensify, understanding how open source actually works—and why it matters—has become essential knowledge for anyone building, using, or investing in technology.

---

## The Essence of Open Source: Beyond Simple Sharing

The developers began by articulating what truly distinguishes open source from conventional software distribution. Their analogy was elegant: imagine wanting a chocolate cheesecake. In the traditional model, you walk into a bakery, pay money, and receive a finished cheesecake. You can eat it, but you have no idea how it was made, no recipe, and certainly no ability to reproduce it yourself. Open source, by contrast, hands you not just the cheesecake but the complete recipe, instructions for building the oven, and crucially—the legal freedom to modify the recipe and even sell your own version.

This distinction carries profound implications. Software, as one developer explained, is essentially "a very long recipe of small instructions." Computers aren't intelligent; they simply execute instructions incredibly fast. A typical program contains tens of billions of instructions—vastly more complex than any cooking recipe. Traditional proprietary software shields these instructions, treating them as trade secrets. Open source pulls back that curtain entirely.

The power this grants to individuals across the world represents something the developers described as "real freedom"—a democratization of capability that transcends geographical, political, and economic boundaries. Someone in a developing country can now access the same tools that power Netflix's streaming infrastructure, modify them for local needs, and contribute improvements back to a global community. This isn't hyperbole; it's the operational reality of projects like FFmpeg and VLC.

---

## The Collaborative Architecture of Open Source

The conversation revealed the remarkable scale of collaborative development these projects sustain. FFmpeg has attracted between 2,000 and 3,000 contributors since its inception—a figure that becomes more striking when you consider these aren't employees following a corporate roadmap but volunteers and professionals contributing from around the world, mostly coordinating online. The Linux kernel, which FFmpeg and VLC closely parallel in their development model, has approximately 10,000 contributors.

The mechanism behind this collaboration is worth examining. When a developer encounters a codec that doesn't work, they don't simply wait for a corporation to address it. Instead, they roll up their sleeves, implement the support themselves, and contribute it back to the project. This work benefits everyone—there's no siloed advantage, no competitive moat being built. The developers spoke of working "for the greater good," a phrase that would sound naive in a corporate context but genuinely describes the operational motivation of these communities.

This isn't utopian idealism. It's practical engineering economics. When thousands of people can contribute to a shared foundation without negotiating licensing fees or NDAs, the result is an accumulation of expertise and capability that no single company could match. Each contributor solves problems relevant to their own needs while simultaneously solving problems for thousands of others. The Linux kernel powering billions of devices and the FFmpeg library handling trillions of video streams exist because this collaborative model works.

---

## Understanding Open Source Licensing: The Legal Architecture

A substantial portion of the discussion focused on licensing—the legal framework that makes open source possible and defines its boundaries. The developers outlined the major categories with nuance that exceeded typical oversimplifications.

**Permissive licenses** like MIT, BSD, and Apache grant users broad freedom. Take the code, modify it, use it in proprietary software, ship it commercially—the original authors typically ask only for attribution. These licenses dominate in JavaScript ecosystems and BSD-based operating systems. The developers noted that some permissive licenses require attribution while others don't, creating subtle differences developers must understand when selecting components for commercial projects.

**Copyleft licenses** impose additional requirements: if you modify and redistribute the code, you must contribute your changes back to the community under the same license. This creates a viral effect ensuring the commons remains open. The strength varies—LGPL (Lesser GPL) permits linking without requiring full GPL terms, making it popular for libraries; MPL (Mozilla Public License) occupies middle ground; GPL represents strong copyleft; AGPL extends GPL to cover network usage, preventing companies from running open source code on servers without releasing their modifications.

The developers emphasized that open source licenses operate within copyright law rather than outside it. "Public domain" doesn't actually exist worldwide—many jurisdictions lack mechanisms for dedicating work to public ownership. Every open source license is fundamentally a copyright license, granting specific permissions while retaining others. This legal foundation is why GPL-compliant forks can diverge and reunite: the license permits modification and redistribution, creating a legally enforceable commons.

---

## The Social Contract: Community Governance in Open Source

One of the most intellectually rich parts of the conversation concerned the concept of open source licenses as "social contracts"—a deliberate reference to Rousseau. The developers observed that the community around a project often agrees on very little beyond the license terms. People from radically different backgrounds—different religions, different political systems, different economic circumstances—collaborate precisely because the license defines the rules of engagement.

This license-driven governance enables something remarkable: community splits and reunifications without destroying the project. The developers cited historical examples. GCC (the GNU Compiler Collection) experienced a fork into EGCS (Eric Geographic's Compiler Collection) in the 1990s, which eventually replaced the original as the community rallied around the superior implementation. More recently, KHTML—a rendering engine developed by KDE—forked into WebKit (adopted by Apple), which then forked into Blink (adopted by Google). Each fork was legal, each produced valuable innovation, and the ecosystem as a whole benefited.

These forks don't represent failure—they represent the system working as designed. The license permits divergence, enabling experimentation without requiring consensus. When the experiment succeeds, the broader community benefits. When it doesn't, participants can return or start new experiments. This evolutionary mechanism is fundamentally different from how proprietary software develops, where a single corporation controls the direction and forks are either forbidden or legally complicated.

---

## The VLC Relicensing Saga: Why Changing Courses Is Hard

The conversation included a detailed discussion of VLC's journey from GPL to LGPL—a process that illuminated why open source projects cannot simply adapt their licenses when circumstances change. The developers explained that relicensing required obtaining agreement from every contributor to the affected code. For a project with thousands of contributors spanning decades, many of whom are no longer reachable—and some no longer alive—this presented a nearly insurmountable challenge.

This practical reality explains why most successful open source projects maintain their initial licensing choices indefinitely. The Linux kernel remains GPL v2. Apache and MIT projects don't suddenly switch to GPL. Once thousands of people have contributed under specific terms, those terms become effectively permanent. Any change requires what the developers described as "all of their agreement," which is logistically impossible for large, long-running projects.

The developers drew a contrast with situations where projects can change: smaller projects with fewer contributors, or situations where a company owns the copyright and can unilaterally modify terms (as happened with companies like Redis and MongoDB in recent years). But community-driven projects face different constraints entirely.

---

## The Commercial Paradox: Building Fortunes on Open Source

A particularly thorny topic addressed the relationship between open source and commercial enterprise. The developers acknowledged that companies can—and do—build billion-dollar甚至 trillion-dollar businesses on open source foundations, typically by wrapping functionality behind proprietary APIs or services without contributing meaningful changes back to the upstream projects.

This phenomenon has created significant tension. The developers mentioned cloud providers specifically—companies that run FFmpeg, VLC, and other open source tools in their data centers, profit from the convenience they provide, and contribute nothing back. This "wrapper economy" troubled them, representing a one-way extraction from commons others maintain.

The discussion touched on how some companies have responded by changing licenses. Elasticsearch and MongoDB, among others, moved from open source licenses to proprietary ones to prevent cloud providers from monetizing their work without permission. The developers noted this phenomenon without passing explicit judgment, though the contrast with FFmpeg and VLC—projects that maintained their open source commitment despite these pressures—seemed intentional.

FFmpeg and VLC's approach reflects a philosophical commitment: the license exists to enable the community, not to extract value from it. Even when commercial interests could profit by restricting access, the developers chose to preserve the freedom the original license provided. This long-term perspective—prioritizing community sustainability over short-term revenue—distinguishes these projects from more commercially motivated open source endeavors.

---

## Real-World Impact: From Hollywood to Handhelds

The conversation wouldn't have been complete without grounding these concepts in concrete applications. FFmpeg powers video processing across countless platforms—it's in smartphones, streaming services, professional editing software, and web browsers. The format support that makes VLC capable of playing virtually any media file exists because thousands of contributors added codecs over decades. Each contribution benefited everyone immediately.

The developers painted a picture of a global infrastructure built on shared foundation rather than proprietary lock-in. When a researcher in Germany improves audio encoding, that improvement appears in every FFmpeg installation worldwide within days. When a company in Korea needs support for a new format, they can implement it themselves rather than waiting for a vendor's roadmap. This interoperability and accessibility define the open source advantage in practical terms.

---

## Detailed Takeaways

**Takeaway 1: Open source licensing choices are effectively permanent for community-driven projects.** Once thousands of contributors have given code under specific terms, changing those terms requires unanimous consent that's practically impossible to obtain. Organizations choosing open source infrastructure must evaluate licensing carefully at the outset, as the choice will likely define the project's legal framework indefinitely.

**Takeaway 2: Forks represent the system working correctly, not failing.** The ability for projects like GCC, WebKit, and others to split and eventually reunite demonstrates the strength of open source governance. This evolutionary mechanism enables experimentation without requiring consensus, allowing innovation to occur faster and more diversely than proprietary development allows. Organizations should view forks as healthy ecosystem behavior rather than fragmentation.

**Takeaway 3: The distinction between permissive and copyleft licensing affects downstream obligations.** MIT, BSD, and Apache licenses permit proprietary commercial use with minimal restrictions, making them popular for commercial projects. GPL and LGPL require reciprocal contribution, protecting the commons at the cost of limiting certain commercial uses. Projects choosing open source components must understand these implications for their own products and distribution models.

**Takeaway 4: The "wrapper economy" creates unsustainable dynamics that have prompted license changes from major projects.** Companies like Elasticsearch and MongoDB changed their licenses specifically to prevent cloud providers from monetizing their work without contributing back. This trend suggests the original open source licenses didn't adequately anticipate modern cloud business models, and organizations building on open source should evaluate the sustainability of their dependencies accordingly.

**Takeaway 5: Open source enables global meritocracy where anyone can contribute to foundational infrastructure.** The 2,000-3,000 FFmpeg contributors and 10,000+ Linux kernel contributors span countries, economic backgrounds, and professional contexts. This accessibility means organizations can not only consume open source but actively shape the tools they depend on—a capability that would be impossible with proprietary alternatives controlled by single vendors.

---

## Who This Is For

This conversation holds particular value for **software developers and technical leaders** evaluating open source components for commercial or infrastructure projects. The discussion provides essential context for making informed licensing decisions, understanding the sustainability of dependencies, and recognizing the legal and philosophical frameworks underlying projects they likely already use.

**Startup founders and product managers** will find the commercial tension discussion especially relevant. Understanding why some projects relicensed and what that means for long-term usage rights can inform decisions about which open source foundations to build upon and what backup plans to maintain.

**Technology investors and executives** benefit from understanding how open source creates and captures value. The discussion of the "wrapper economy" and its tensions illuminates dynamics affecting industries from cloud computing to AI infrastructure.

**Policy makers and legal professionals** working on intellectual property, technology regulation, or platform economics will find the social contract discussion valuable for understanding how community-driven development actually functions—a perspective often missing from regulatory discussions about technology.

For anyone who has ever pressed play on a video, converted an audio file, or benefited from software that "just worked" across formats, this conversation reveals the human infrastructure making that capability possible—and the philosophical choices sustaining it.