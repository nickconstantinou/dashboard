---
title: How controversy on Twitter/X helps solve problems | Lex Fridman Podcast
date: '2026-05-13'
type: youtube
category: AI/Tech
channel: Lex Fridman
video_url: https://www.youtube.com/watch?v=1vJyN6cQuF8
video_id: 1vJyN6cQuF8
---

# Key Insights

- **[1:05]** **VLC for Android serves ~100 million users**, yet VideoLAN lacked any mechanism to resolve a Play Store bug for over a year—until a public "spicy tweet" threatened to stop distribution entirely, forcing Google Android engineers to finally engage directly.
- **[2:10]** **VLC ranks among the top 10 most-used software on Windows**, yet VideoLAN is excluded from Microsoft's ISV contact programs—unlike Spotify or Adobe—leaving the project without enterprise support channels and dependent on social media pressure tactics.
- **[3:16]** **FFmpeg's young contributors have written more assembly code than Google engineers combined**, as one response to a critic noted; Ruikai Peng was just 16 years old when submitting security fixes that shamed professional "security researchers."
- **[4:21]** **Edward Wong began contributing at age 14** through Google Summer of Code, stayed with VideoLAN for three years, and exemplified a contrast to the security community by quietly fixing a development-branch vulnerability in three days without publicizing it as a critical CVE.
- **[5:26]** **Twitter/X controversy measurably increased donations** to both FFmpeg and VideoLAN—not to sustainability levels (still insufficient for one full-time developer), but enough to meaningfully raise both public awareness and technical engagement with these critical open-source projects.

---

# Introduction

In an era when social media increasingly feels like a source of division rather than progress, a counterintuitive insight emerges from the open-source world: the controversies and "spicy tweets" that unfold on platforms like Twitter and X can actually catalyze real-world solutions to technical problems. This was the central theme explored in a Lex Fridman Podcast conversation featuring developers from the VideoLAN and FFmpeg projects, the creators of two of the most widely-used pieces of software most people have never heard of.

The discussion revealed a striking paradox at the heart of open-source sustainability. VLC media player, which likely runs on a significant portion of the world's computers and mobile devices, is technically sophisticated enough to be among the top 10 most-used applications on Windows—yet the organization behind it operates with fewer resources and less institutional access than major tech corporations. FFmpeg, the multimedia framework that powers everything from video streaming to film production, handles video conversion for countless applications yet depends on a small team of unpaid volunteers.

What makes this conversation particularly compelling is how the speakers demonstrated that strategic controversy on social media has become an unlikely but effective tool for small open-source projects to cut through bureaucratic indifference and force accountability from trillion-dollar corporations. The episode also served as a celebration of grassroots contribution, showcasing how teenagers and young developers have quietly built and maintained infrastructure that the professional tech industry relies upon daily.

---

# The Power of Strategic Controversy

## Weaponized Visibility: How Drama Gets Results

The conversation opened with an admission that might seem cynical to outsiders but reads as pragmatic necessity to those familiar with open-source maintenance: some of the "spicy tweets" and public drama have actually produced positive results. Donations have increased substantially following controversies, and while they still fall short of funding even a single full-time developer, the visibility gains have been substantial on both awareness and technical levels.

Jean-Baptiste Kempf, one of the project's primary voices, explained that Twitter and X serve their purpose precisely because they create visibility that "snowballs." When large companies ignore polite inquiries or support tickets, a well-crafted public announcement can force attention from engineers who otherwise have no obligation to engage with small open-source projects.

The VLC Android Play Store situation provided a concrete case study. For more than a year, the VideoLAN team could not release updates to VLC for Android because of a bug in Google's Android Play Store infrastructure. With approximately 100 million people using that application, the issue affected a massive user base—but no amount of standard communication channels yielded a response from Google. The solution, as described with audible resignation, was to post a "very spicy tweet" announcing that VideoLAN was going to stop distributing VLC for Android entirely. Only then did someone from Android actually engage in substantive discussion with the team.

A parallel situation occurred with Microsoft's Windows Store. The same pattern emerged: years of trying standard channels, culminating in a public threat to halt distribution, followed by actual Microsoft engagement. These weren't preferred methods—the speaker made clear they would rather have professional relationships with these companies—but they were the only approaches that worked.

## The Liability of Being Small

What emerges from this discussion is a counterintuitive reality about influence in the tech industry. VLC is almost certainly one of the top 10 most-used applications on Windows in terms of install base and daily active users. Yet VideoLAN is not part of Microsoft's Independent Software Vendor (ISV) programs, meaning they have no designated point of contact, no enterprise support channel, and no formal pathway for raising critical issues.

The speaker noted this disparity explicitly: "Adobe, Spotify has a point of contact. I don't have that." The implication was stark—companies that likely serve fewer direct users have institutional relationships that VideoLAN, despite its ubiquitous presence, cannot access. This creates a strange paradox where popularity does not translate into support infrastructure.

The only leverage available to such projects, then, becomes public pressure. By creating situations where silence becomes more costly than engagement—where not responding invites negative attention that snowballs across social networks—small projects can occasionally force the attention they need. It's an uncomfortable dynamic that requires embracing drama and controversy, but for projects with no other mechanisms, it becomes survival strategy.

---

# The Unseen Labor of Open Source

## Rebuilding the Airplane While Flying It

Beyond the immediate corporate dynamics, the conversation served as a meditation on the nature of open-source contribution and maintenance. The speakers highlighted the work of developers like Andreas Rünhardt and Anton Kern, whose massive refactorings and rewrites of FFmpeg's threading systems changed nothing from the user's standpoint—the output files remain exactly the same—yet represented engineering efforts comparable to "rebuilding the airplane while it's in the air."

This distinction matters because it captures something fundamental about the invisible labor sustaining digital infrastructure. Users benefit from faster encoding, better compatibility, and improved reliability without necessarily knowing that these improvements came from unpaid volunteers working late nights on thankless tasks. The code functions identically from a distance, but the engineering underneath has been continuously renewed and improved by people who receive neither recognition nor compensation commensurate with their contribution.

Christian Garcia's comment that "there's a teenager running this account" (referring to the FFmpeg Twitter/X presence) prompted responses that highlighted the project's age diversity. The speakers pointed out that teenagers have contributed thousands of lines of assembly code to FFmpeg over the years, prompting one response noting that "teenagers have written more assembly in FFmpeg than Google engineers." This isn't hyperbole but observation—the project has historically attracted talented young developers willing to invest significant effort in low-level, complex work.

## A Gallery of Young Contributors

The speakers enumerated several examples to illustrate this point. Daniel Kang received a shoutout for contributions dating back years. Ruikai Peng was specifically highlighted as having been just 16 years old when making contributions to FFmpeg—and notably, some of those contributions involved finding and fixing security issues that professional "security researchers" had publicized as dramatic CVEs rather than addressing quietly.

In the VLC project, one of the oldest contributors is "Felix," who handles all Mac and iOS development. Felix started working on VLC at age 16. Edward Wong was even younger—14 years old—when he participated in Google Summer of Code and Code-in programs, eventually staying with VideoLAN for three years and writing significant amounts of assembly code for x264, VLC, and FFmpeg.

What unites these examples is the explicit absence of barriers. The speakers emphasized that FFmpeg and VideoLAN "don't care who you are, where you're from, what you do"—only that you can write code. The pathway is straightforward: learn C from the K&R book, learn assembly, and contribute. No college degree required, no professional credentials needed, no age restrictions beyond basic legal considerations.

## The Contrast with Security Theater

A particularly pointed critique emerged when contrasting these young contributors with parts of the professional security community. The speakers acknowledged that "not all security people do this," but observed that "there is a portion of the security community that likes to hype themselves up by creating drama."

The example given was Edward Wong's approach versus the alarmist pattern: when Wong discovered a vulnerability in development (not yet in any release), he simply fixed it in Git within three days. He did not create a CVE, did not assign it a frightening priority score, and did not announce it as a critical discovery. By contrast, the speakers noted, other security researchers might happily hype such a finding as a CVE 8.0 or higher, treating it as a major emergency even when it affected code no user would ever encounter.

This contrast illuminates something about incentives in different parts of the tech ecosystem. Young contributors like Wong are motivated by the satisfaction of solving problems and improving software. Others seem motivated by the visibility and credibility that dramatic security disclosures provide. Both approaches produce fixes, but only one builds community and trust.

---

# Detailed Takeaways

## Strategic Visibility as an Engineering Tool

The most immediately applicable insight concerns the use of public platforms for technical problem-solving. When institutional channels fail and when the scale of your user base grants you no automatic access to corporate attention, strategic public communication becomes a viable alternative. This doesn't mean随意制造 drama—it means understanding that visibility creates accountability, and that sometimes the only way to get Google's attention for a critical bug is to announce you're stopping distribution of software 100 million people use.

For technical leaders and open-source maintainers, this suggests a counterintuitive skill: knowing when to go public, how to craft messages that will generate appropriate response, and understanding the social dynamics of platforms like Twitter/X well enough to predict how announcements will travel. It's a form of communication engineering as much as traditional technical skill.

## The Sustainability Paradox of Ubiquity

VLC being top-10 most-used software on Windows while lacking basic corporate support relationships reveals a fundamental paradox in tech industry economics. Wide adoption does not automatically translate into institutional recognition, support contracts, or sustainability pathways. The software everyone depends on is often maintained by people with fewer resources and less institutional power than their user base might assume.

This has implications for how the industry thinks about open-source sustainability. It's not enough to point to billions of users and call that success if the people maintaining that infrastructure cannot earn a living from it. The conversation suggests that new models—perhaps involving mandatory corporate contributions, government funding for critical infrastructure, or novel organizational structures—are needed to align the benefits of ubiquitous open-source with the costs of maintaining it.

## Age Diversity as a Feature, Not an Anomaly

The celebration of teenage contributors should not be read as suggesting that open-source projects should rely on exploited youth labor. Rather, it demonstrates what becomes possible when barriers to contribution are genuinely lowered. The projects that attract young contributors are often those that offer interesting technical challenges, welcoming communities, and merit-based recognition—qualities that professional development environments don't always provide.

For organizations hoping to develop talent pipelines, FFmpeg and VideoLAN offer a model: create interesting problems, remove bureaucratic barriers, and talented people will come regardless of age or credentials. The key is ensuring that this openness doesn't become a mechanism for extracting free labor, but rather a genuine pathway where contributors receive value proportionate to what they provide.

## Distinguishing Real Fixes from Performance Art

The contrast between quiet, efficient fixes and dramatic CVE creation offers a useful framework for evaluating security disclosures. The question to ask is not "how severe is this vulnerability?" but "who benefits from this disclosure being public, and how?" Security researchers who find genuine issues in released software and disclose them responsibly provide valuable service. Those who find issues in development code, assign them maximum severity scores, and create public drama around them are performing security rather than practicing it.

For organizations receiving security reports, this suggests screening disclosures through a lens that accounts for the incentives of the reporter. Not all CVEs represent genuine risk to users—some represent efforts to build reputation through manufactured urgency.

---

# Who This Is For

This conversation will prove most valuable to several distinct audiences. Open-source project maintainers and contributors will find both validation and practical strategy for navigating the difficult terrain between producing critical infrastructure and maintaining financial sustainability. The discussion of Twitter/X as a tool for corporate engagement offers specific tactical advice that, while uncomfortable, has demonstrated effectiveness.

Technology industry professionals who use open-source software without thinking about its maintenance will gain appreciation for the invisible labor underlying their daily tools. Understanding that VLC has no Microsoft support contract, that FFmpeg developers work unpaid, and that teenagers contribute significant portions of the code running on millions of devices can shift how individuals and companies think about their obligations to open-source communities.

Aspiring developers, particularly those who feel excluded by traditional pathways into the tech industry, will find a message of genuine possibility. The speakers explicitly rejected credentialism and offered a clear pathway: learn C from K&R, learn assembly, and contribute to world-class projects. The age diversity of FFmpeg's contributor base demonstrates that these pathways are real, not theoretical.

Finally, technology industry executives and investors should pay attention to the sustainability paradox articulated in this discussion. The current situation—where top-10 Windows software cannot get Microsoft to return emails—is not a stable equilibrium. At some point, critical open-source infrastructure will fail in ways that create pressure for new models of support. Companies that recognize this and develop proactive relationships with critical open-source projects will fare better than those that wait until public drama forces engagement.