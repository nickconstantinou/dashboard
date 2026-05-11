---
title: How AI slop is destroying open source | Lex Fridman Podcast
date: '2026-05-11'
type: youtube
category: AI/Tech
video_id: T7LEowYGWr4
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=T7LEowYGWr4
---

## Key Insights

- **Daniel Steinberg**, the sole maintainer of curl (one of the most widely deployed software components globally), has coined the term "AI slop" to describe the flood of AI-generated bug reports, fake vulnerability claims, and low-quality patches that overwhelm open source maintainers
- **The XZ security fiasco** (2024) was a deliberate social engineering attack where bad actors exploited maintainer burnout by bombarding a single maintainer with questions at odd hours until he surrendered commit access to an attacker
- **Critical internet infrastructure runs on single-digit maintainer teams**: FFmpeg's entire multimedia stack supporting modern digital infrastructure depends on roughly 10-15 core developers, while libxml (the library parsing XML across nearly every enterprise system) has essentially one aging maintainer handling thousands of security researchers' edge case reports
- **Security researcher culture clash**: Large corporations like Google deploy automated security bots that generate thousands of "crap code" reports against hobby projects, with security researchers sometimes dismissing maintainers as incompetent rather than recognizing that the 99.9999th percentile edge case is a legitimate hobby project
- **Personal cost of open source**: The speaker (Jean-Baptiste Kempf) received an anthrax-threatened death package in 2009-2010 after deciding not to maintain a PowerPC port of VLC, requiring police involvement and forcing him to develop psychological resilience as a survival mechanism

---

## Introduction

The digital infrastructure underpinning modern civilization depends on a fragile and largely invisible ecosystem: thousands of open source software projects maintained by volunteers who often receive no compensation, minimal appreciation, and increasingly, AI-generated harassment that threatens to burn out the very people keeping the internet functioning.

This conversation, set against the backdrop of the Lex Fridman Podcast, explores one of open source software's most critical yet underappreciated crises: the intersection of maintainer burnout, corporate exploitation, and the emerging threat of what the open source community has begun calling "AI slop." The discussion features Jean-Baptiste Kempf, a prominent figure in the open source multimedia community who maintains VLC and related video libraries—projects used by billions of devices worldwide but maintained by teams that can be counted on two hands.

The timing of this discussion is particularly relevant as the software industry increasingly relies on open source components while providing minimal support back to the community. From the notorious XZ security incident that nearly compromised major Linux distributions to ongoing conflicts between security researchers and hobbyist maintainers, the cracks in open source's foundation are becoming impossible to ignore. This conversation pulls no punches in examining why the people who maintain the code everyone depends on are increasingly feeling abandoned, harassed, and burned out.

---

## The AI Slop Crisis

The most immediate threat to open source maintainers discussed in this conversation isn't malicious code or corporate competition—it's the overwhelming flood of low-quality, AI-generated content that clutters issue trackers, wastes maintainers' limited time, and degrades the signal-to-noise ratio of legitimate bug reports.

Daniel Steinberg, the longtime maintainer of curl (a tool so ubiquitous that virtually every internet-connected device interacts with it daily), has been particularly vocal about what he terms "AI slop." The problem manifests in several concrete ways: automated systems and AI tools generate bug reports that describe problems that don't exist, submit patches that don't actually solve anything, and flag vulnerabilities based on pattern-matching rather than actual security analysis. When a maintainer receives fifty such reports a day, the actual legitimate issues become nearly impossible to identify.

The burden this creates is psychological as much as practical. Maintainers who volunteer their limited time to support projects used by millions must now wade through mountains of synthetic noise to find the occasional genuine signal. This isn't merely an inconvenience—it represents a fundamental shift in the volunteer experience that threatens to drive away the very people the ecosystem depends on most.

---

## The XZ Fiasco: A Case Study in Exploiting Burnout

The conversation turns to one of the most significant security incidents in recent open source history: the XZ Utils backdoor attempt of 2024. This case serves as a cautionary tale about what happens when maintainer burnout intersects with deliberate malicious activity.

XZ is a compression library used in countless Linux distributions and enterprise systems—a piece of infrastructure so embedded in modern computing that its compromise could have affected millions of servers worldwide. For years, this critical project was maintained by a single individual, a situation not uncommon in the open source world. This isolation made it vulnerable.

What happened next was a sophisticated social engineering operation. Attackers systematically targeted the maintainer, overwhelming him with requests, questions, and pressure at unusual hours. The constant barrage wasn't just annoying—it was designed to exhaust him psychologically until he became willing to surrender commit access to someone else. Once the attacker had that access, they introduced a backdoor that could have given them remote code execution on millions of systems.

The speaker emphasizes that this incident represents a new category of threat: not technical vulnerabilities in code, but the weaponization of maintainer burnout itself. By driving someone to exhaustion through persistent demands, attackers can achieve what traditional hacking techniques could not. The lesson isn't just about security protocols—it's about recognizing that human factors are now primary attack vectors in open source infrastructure.

---

## The Fragile Foundation: Critical Infrastructure on Individual Shoulders

Perhaps the most visually striking portion of the discussion addresses the meme that has become a defining image of open source's precarious situation: a diagram showing the modern digital multimedia infrastructure with FFmpeg at its very bottom, holding up an impossibly complex tower of dependencies.

FFmpeg is the library that actually decodes and encodes video and audio across the internet. Every video streamed on YouTube, Netflix, or any website passes through FFmpeg at some point. Every piece of media editing software relies on it. Every transcoding operation, every format conversion, every time media travels between formats or devices, FFmpeg is there. Yet this critical infrastructure is maintained by a community of perhaps ten to fifteen dedicated developers who often receive little compensation and even less recognition.

The situation becomes even more stark when contrasted with other projects. The XZ compression library, used in far more installations than most people realize, was being maintained by essentially one person. libxml—the library that parses XML across virtually every enterprise system, handling all the complex edge cases that the XML specification requires—has effectively one aging maintainer. This person also maintains all the time zone data for essentially the entire world, a responsibility so significant and thankless that the speaker questions how anyone could maintain their mental health under such pressure.

The Google security incident mentioned in the conversation illustrates how corporations' automated tools can inadvertently create problems for these individual maintainers. Google's automated security scanners generate enormous numbers of reports against open source projects, and these reports are often sent without human review to determine whether they're legitimate concerns or AI-generated noise. Maintainers then face the burden of responding to or dismissing these reports while continuing to maintain projects that companies profit from extensively.

---

## The Security Community Divide

A significant portion of the conversation addresses a growing cultural conflict between the professional security research community and open source maintainers. This isn't merely a philosophical disagreement—it has practical consequences for how vulnerabilities are reported, fixed, and disclosed.

The speaker, who maintains several multimedia libraries, describes a disturbing pattern: when automated tools flag potential issues in open source projects, the resulting communication often dismisses maintainers as incompetent rather than recognizing the constraints they work under. Phrases like "these guys write crap code" and demands that maintainers "fix their crap code" reflect a fundamental misunderstanding of open source economics and reality.

The speaker pushes back forcefully on this characterization. The edge case that a security bot flags as a vulnerability might be the 99.9999th percentile scenario that a maintainer didn't anticipate because, as the speaker puts it, "This is a guy's hobby project decoding Star Wars games." The maintainer didn't write poor code—they wrote functional code that solved their actual problem, and the security researcher's automated tool has identified an theoretical edge case that would only matter in extraordinary circumstances.

This divide reflects broader tensions in how the software industry treats open source. Companies deploy automated security scanning at scale, generating reports that create work for volunteer maintainers without providing the resources to fix theoretical issues that may never manifest in practice. The resulting frustration on both sides erodes relationships and discourages maintainers from engaging with the professional security community.

---

## Personal Cost: What It Takes to Maintain Open Source

The most human portion of the conversation involves the speaker sharing their own experiences with abuse, threats, and the psychological toll of maintaining software used by billions of people.

Around 2009 or 2010, when Apple transitioned from PowerPC to Intel processors, the speaker made the difficult decision to stop maintaining the PowerPC port of VLC. This was a practical decision—resources were limited, development had moved to new architectures, and maintaining legacy ports diverted effort from improving the project. The decision predictably upset some users who still relied on PowerPC systems, but the speaker was unprepared for what followed.

The speaker received a package containing powder and death threats, requiring police involvement and causing significant distress to their family, particularly their mother. The package arrived during a period when anthrax threats were being taken extremely seriously, amplifying the terror of the situation. The accompanying message was explicit in its hatred, suggesting the maintainer should die and that PowerPC support should continue forever.

What makes this story significant isn't just its brutality but its aftermath. The speaker describes the incident as forging them psychologically, enabling them to handle subsequent abuse and criticism that would break less hardened maintainers. This isn't presented as a point of pride but as a troubling necessity: survival in open source maintenance increasingly requires developing psychological defenses against harassment, threats, and entitled users who view maintainers as service providers rather than human beings volunteering their time.

The speaker also reflects on the lack of positive feedback despite VLC being used billions of times. For years, they had no mechanism to receive gratitude until discovering the Twitter account that occasionally posts thank-you messages. Now, when they encounter someone expressing appreciation on Reddit or elsewhere, they screenshot and share it with their team through their Signal to IRC communication— IRC being the communication protocol the VideoLAN community still uses daily because, as the speaker notes, "there's no tracking, there's nothing." This small moment of validation illustrates how starved maintainers often are for acknowledgment that their work matters.

---

## The Path Forward: Recognition and Support

The conversation concludes with a call for fundamental changes in how society treats open source maintainers—not just financially, though that matters, but spiritually and psychologically as well.

The speaker argues that human civilization runs on the work of people who maintain open source projects, often without adequate compensation and frequently with abusive treatment from users and corporations alike. The image of FFmpeg holding up modern media infrastructure while receiving minimal thanks encapsulates a relationship that is fundamentally unsustainable.

What open source maintainers need isn't just money (though financial support is genuinely important). They need recognition that their work is valuable, that their time has worth, and that they are not servants obligated to respond to every request. They need the professional security community to engage as partners rather than demanding compliance. They need corporations to recognize that their profits depend on infrastructure maintained by volunteers and to contribute accordingly. And they need users to understand that the software they rely on exists because specific human beings chose to dedicate their lives to building and maintaining it.

The speaker's conclusion is clear: we need to celebrate the people who step up to maintain critical infrastructure, often without recognition, often without payment, and often under difficult conditions. These are the humans whose invisible labor makes modern digital civilization possible—and their continued well-being is essential to that civilization's survival.

---

## Detailed Takeaways

**Maintainer burnout is an attack surface, not just a personal problem.** The XZ incident demonstrated that psychological exhaustion is a legitimate security vulnerability. Organizations and projects should recognize that overworked, isolated maintainers create exploitable conditions. This means funding multiple maintainers where possible, establishing succession plans, and treating workload sustainability as a security measure.

**AI-generated content is creating a crisis in open source quality control.** The flood of synthetic bug reports and patches isn't merely annoying—it threatens to overwhelm the signal-detection capabilities that keep open source projects functional. Projects need better tools for filtering AI-generated content and communities need to establish norms about appropriate use of AI in reporting issues.

**Critical infrastructure has single points of failure that receive insufficient attention.** FFmpeg, libxml, curl, time zone databases—these are all maintained by handfuls of people, often one. The industry treats this as acceptable risk while profiting extensively from this infrastructure. Companies should fund not just specific features but the sustainability and security of the entire projects they depend on.

**The security research community's automated approach damages relationships with maintainers.** While automated vulnerability scanning has legitimate uses, the current approach often creates burden without value. Security researchers should consider whether their automated reports represent genuine risks to actual users or theoretical edge cases that would never manifest in practice—and maintainers should feel empowered to set boundaries about the types of reports they're willing to engage with.

**Positive reinforcement is urgently needed.** Most maintainers receive only criticism, never gratitude. The speaker's joy at discovering a Twitter account that occasionally posts thank-you messages illustrates how starved the community is for acknowledgment. Users should proactively thank maintainers, companies should highlight dependencies on open source in marketing materials, and the industry should celebrate maintainers the way it celebrates developers of proprietary software.

---

## Who This Is For

This conversation is essential listening for anyone who develops, funds, or depends on software in any industry—but particularly for three audiences.

**Software engineers and developers** who use open source dependencies will gain essential perspective on the human costs of their dependency choices. Understanding that the library they import with a single line of code represents years of volunteer labor under often difficult conditions changes how one should think about contributing upstream, reporting issues, and expressing gratitude.

**Technology executives and decision-makers** at companies that profit from open source infrastructure will encounter uncomfortable truths about the extractive relationship many organizations have with open source communities. The conversation makes clear that sustainable open source requires investment, not just consumption, and that the current model is approaching collapse.

**Open source maintainers and contributors** will find validation and solidarity in hearing someone articulate the frustrations, threats, and burnout that often feel isolating. The speaker's candor about their own experiences may help maintainers recognize patterns in their own work and feel less alone in facing them.

For all three audiences, the core message is the same: the invisible infrastructure of modern computing runs on human beings who deserve recognition, support, and sustainable working conditions. The alternative—continued burnout, abandoned projects, and compromised infrastructure—is a threat to everyone.