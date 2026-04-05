---
title: "The biggest barriers to AI scaling laws - NVIDIA CEO explains | Jensen Huang and Lex Fridman"
date: 2026-04-05
type: youtube
category: "AI/Tech"
video_id: "Mf2u2b1bogE"
channel: "Lex Fridman"
video_url: "https://www.youtube.com/watch?v=Mf2u2b1bogE"
---

# The Biggest Barriers to AI Scaling Laws: Jensen Huang on Power, Supply Chains, and the Future of Compute

## Introduction

In a wide-ranging conversation that touches on everything from semiconductor physics to power grid economics, NVIDIA CEO Jensen Huang sat down with Lex Fridman to discuss the most pressing challenges facing the artificial intelligence industry as it continues its exponential growth trajectory. The discussion reveals a man at the center of the most consequential supply chain in modern technology, one who spends his time not just running a company but actively shaping the investments and strategic decisions of CEOs across the entire technology ecosystem—from TSMC and ASML to Caterpillar and beyond.

The conversation arrives at a critical inflection point in the AI industry's development. While many observers focus on the capabilities of large language models or the applications of AI agents, Huang offers a rare glimpse into the industrial infrastructure that makes everything possible—and the fundamental physical constraints that could throttle progress if not addressed. His perspective is uniquely valuable: as the architect of the GPU architecture powering the AI revolution, he sees both the demand curve stretching toward the horizon and the engineering challenges that must be solved to meet it.

What emerges from this discussion is not a story of worry or concern about bottlenecks, but rather a masterclass in supply chain leadership, long-term thinking, and the art of convincing partners to make billion-dollar investments based on a shared vision of the future. Huang describes his role as one of "informing and shaping, inspiring" the entire ecosystem—not just NVIDIA's engineers, but the hundreds of suppliers whose technologies converge into the massive computing racks that form the backbone of AI infrastructure.

## The Power Challenge: Efficiency as the Primary Lever

The conversation's central theme revolves around power consumption and energy efficiency, which Huang identifies as the most significant constraint on AI scaling going forward. This is not merely a concern about availability—though that matters too—but about the fundamental economics of computation. The question is not simply whether we can generate enough electricity, but how efficiently we can turn that electricity into intelligence.

Huang draws a striking comparison between NVIDIA's actual progress and the historical trajectory of Moore's Law. While Moore's Law would have predicted approximately 100x improvement in computing performance over the past decade, NVIDIA has managed to scale up computing by a factor of one million times during the same period. This staggering achievement was accomplished not through any single breakthrough, but through what Huang calls "extreme code design"—a comprehensive approach to optimizing how computations are performed at every level of the system.

The metric that matters most in this context is tokens per second per watt, a measure of how much useful computation can be extracted from each unit of electrical power. NVIDIA is pushing this metric to improve by orders of magnitude every single year, and Huang frames this as an economic imperative that affects the revenues of every data center operator and factory owner. "Our computer price is going up," Huang acknowledges, "but our token generation effectiveness is going up so much faster that token cost is coming down." He emphasizes that token costs are declining by approximately an order of magnitude annually—a rate of improvement that, if sustained, will make AI capabilities increasingly accessible even as the underlying hardware becomes more expensive.

This efficiency-first approach is not merely about reducing costs, however. It is about making the entire enterprise physically possible. As AI systems grow larger and more capable, their appetite for electrical power grows correspondingly. Without dramatic improvements in efficiency, the power requirements would become simply untenable, forcing a choice between capability and feasibility that no one wants to face.

## Extreme Code Design: The Engineering Philosophy

When Huang speaks of "extreme code design," he is describing a philosophy that permeates every aspect of NVIDIA's approach to hardware and software development. This is not about writing more efficient algorithms in isolation, but about rethinking the entire stack from the physics of transistors to the user experience of running inference workloads.

The conversation hints at the profound architectural changes that have enabled NVIDIA to achieve its million-fold improvement in computing performance. These changes involve co-designing hardware and software in ways that were previously unthinkable, optimizing not just for raw speed but for the specific patterns of computation that modern AI workloads require. The result is systems that can extract far more useful work from each joule of energy than previous generations could achieve.

This philosophy extends beyond NVIDIA's own products to shape how the entire supply chain thinks about the problem. When Huang discusses the decisions made by his partners at TSMC, ASML, and the memory manufacturers, he reveals a collaborative effort to push efficiency improvements at every layer—from the lithography machines that pattern silicon to the memory systems that feed data to hungry AI models.

## The Semiconductor Supply Chain: A Modern Marvel

Perhaps the most fascinating portion of the conversation concerns the intricate web of relationships that enables modern AI computing. Huang reveals that each NVIDIA Blackwell rack contains 1.3 million components—a staggering number that reflects the impossible complexity of what has become humanity's most sophisticated manufactured product. These components come from approximately 200 suppliers across the Verubin rack architecture, each contributing essential pieces to a system that must work flawlessly at scales ranging from individual chips to city-block-sized data centers.

Huang's role in this ecosystem extends far beyond that of a typical CEO. He describes spending considerable time briefing the CEOs of his suppliers on the dynamics that will drive growth in the coming years, helping them understand where the market is going so they can make informed decisions about capital investments. This is not a passive sharing of information—it is active persuasion, the cultivation of shared vision across organizations that must coordinate their multi-billion dollar investments without any formal authority linking them.

The conversation reveals a particularly compelling example from approximately three years ago. At that time, HBM (High Bandwidth Memory) was used scarcely, limited primarily to supercomputers and specialized applications. Huang believed it would become mainstream for data centers, and he worked to convince several DRAM industry CEOs to invest heavily in building HBM manufacturing capacity. Initially, the idea sounded "ridiculous," Huang admits, but several CEOs trusted his vision and made the investments. Today, those decisions look prescient, with HBM memories alongside LPDDR5 and other memory types recording their best years in history—remarkable achievements for companies that are themselves 45 years old.

The same dynamic applied to low-power cell phone memories like LPDDR, which Huang wanted to adapt for use in supercomputers and data centers. The idea of using "cell phone memory for supercomputers" seemed odd at first, but Huang explained the technical reasoning, and the volumes proved the wisdom of the approach. This ability to see connections across seemingly disparate domains—to recognize that cell phone memory economics could solve data center problems—is a hallmark of Huang's approach to technology strategy.

## The MVLink 72 Revolution: Moving Manufacturing Upstream

A significant shift in NVIDIA's architecture came with the introduction of MVLink 72 and the transition to rack-scale computing. Historically, NVIDIA shipped its DGX systems as components that were assembled inside customer data centers. The MVLink 72 architecture changed this model fundamentally, shipping fully assembled supercomputers weighing two to three tons per rack, complete with all the integration and testing that previously occurred at the customer's facility.

Huang explains the reasoning behind this change: the density of MVLink 72 systems made in-field assembly "impossible." But the implications extended far beyond logistics. By moving supercomputer integration into the supply chain, NVIDIA also had to move the power requirements for building and testing those systems upstream. A 50-gigawatt deployment of AI supercomputers, if manufactured in one week, requires the supply chain to have access to one gigawatt of power just for the manufacturing and testing process.

This architectural decision forced Huang to engage with his manufacturing partners in new ways. He found himself flying to meet suppliers and explaining, with "pictures and first principles reasoning," why they needed to invest in new capabilities. He would describe the coming inflection point for inference, explain why the market would be large, and then ask these partners to commit billions of dollars to capacity expansions. "I give them every opportunity to question me," Huang notes, "and I spend time to explain things to people." The result, he suggests, is that by the time these conversations conclude, there is "no what to do"—his partners understand the logic so completely that the investment decision becomes obvious.

## Supply Chain Confidence: No Sleepless Nights

What strikes Huang's interviewer most is the CEO's apparent lack of anxiety about the supply chain challenges that would keep most executives awake at night. ASML and its EUV lithography machines, TSMC and its advanced packaging capabilities, SK Hynix and high bandwidth memory—these are all potential bottlenecks that would seem to demand constant vigilance. Yet Huang seems remarkably unconcerned.

The explanation lies in the relationships he has built and the information-sharing mechanisms he has established. "I told them what I needed, they understood what I need," Huang explains. "They told me what they're going to go do, and I believe in what they're going to do." This is not naive optimism—it is the result of years of building trust, being transparent about forecasts and plans, and maintaining the kind of credibility that makes bold promises believable.

Huang also describes attending industry events surrounded by "the entire right hand side" of the technology industry. Practically every major upstream IT company CEO and downstream infrastructure CEO was present, not as audience members but as participants in a shared conversation about where the industry is heading. These gatherings serve as coordination mechanisms, allowing Huang to share his perspective on "business conditions now, the growth drivers in the very near future, what's happening, and where we are going to go next"—all information that his partners need to make their own investment decisions.

## The Power Grid Opportunity: Excess Capacity hiding in Plain Sight

The conversation concludes with a topic that Huang clearly finds energizing: the untapped potential of existing power grid infrastructure. The current electrical grid, he explains, is designed for worst-case conditions—those few days in winter and summer when extreme weather creates peak demand. The rest of the time, the grid operates at approximately 60% of its rated capacity. "99% of the time our power grid has excess power," Huang observes, "and they're just sitting idle."

This insight has profound implications for AI infrastructure planning. Rather than viewing power availability as a scarce resource requiring massive new investment in generation capacity, the AI industry could potentially capture significant value by intelligently scheduling workloads to coincide with periods of excess grid capacity. Data centers could be designed with this flexibility in mind, running compute-intensive training jobs during off-peak hours while scaling back during the rare moments of true peak demand.

Huang frames this as an opportunity for the entire industry to think more creatively about the relationship between computation and electricity. The grid's design includes margins for reliability that, when properly understood, reveal substantial headroom for growth. This perspective transforms the power challenge from an absolute constraint into a scheduling and optimization problem—one that could be solved with the same kind of systems thinking that has enabled NVIDIA to achieve its other efficiency gains.

## Detailed Takeaways

### 1. Efficiency Improvements Are the Primary Defense Against Scaling Limits

The lesson from NVIDIA's experience is that efficiency gains can far outpace the pessimistic predictions of those who see physical constraints as insurmountable walls. When Huang states that tokens per second per watt are improving by orders of magnitude annually, he is describing an engineering culture that refuses to accept constraints as permanent. The implication for any organization working with AI is that the economics of intelligence will continue to improve dramatically, making capabilities that seem expensive today potentially trivial within a few years. This suggests that waiting for costs to drop may be less valuable than building expertise and infrastructure now, while also investing in efficiency improvements.

### 2. Supply Chain Leadership Requires Vision and Persuasion, Not Just Contracts

Huang's description of his role reveals a truth about modern technology leadership that extends far beyond NVIDIA. The most valuable executives are not those who can negotiate the best contract terms, but those who can articulate a compelling vision of the future and convince partners to invest based on that vision. When asked to commit billions of dollars to capacity expansions, suppliers need to believe that the demand will materialize—and that belief is built through relationships, transparency, and demonstrated insight. Any leader involved in complex supply chains should study how Huang builds this credibility and maintains the trust that makes billion-dollar commitments feel reasonable rather than reckless.

### 3. Architectural Decisions Have Implications That Cascade Throughout the Industry

The shift to rack-scale computing with MVLink 72 was not merely an internal NVIDIA optimization—it had profound implications for manufacturing partners, power requirements, and the entire structure of how AI infrastructure gets built and deployed. When making architectural decisions, leaders must think systemically about how those choices affect the ecosystem around them. This requires a different kind of planning than traditional product development, one that considers not just what is optimal for a single company but what is sustainable and achievable across the entire value chain.

### 4. Power Grid Utilization Is an Untapped Resource That Deserves Serious Attention

The observation that 99% of the time the power grid operates below capacity should change how the industry thinks about AI's energy footprint. Rather than accepting the narrative of inevitable power shortages, there is significant opportunity to redesign workloads and infrastructure to take advantage of existing excess capacity. This could reduce the pressure for new generation investment, lower costs, and improve sustainability. Leaders planning AI infrastructure should consider workload scheduling flexibility as a design criterion, not just raw compute capacity.

### 5. Cross-Domain Thinking Reveals Opportunities Hidden in Plain Sight

The most valuable insights often come from recognizing connections between seemingly unrelated domains. The decision to apply cell phone memory technology to supercomputers, or to borrow efficiency techniques from one workload to benefit another, demonstrates the value of bringing diverse perspectives together. Organizations that encourage their teams to look across traditional boundaries—to ask what mobile computing can teach data centers, or what scientific computing can teach consumer applications—will find opportunities that siloed thinking misses entirely.

## Who This Is For

This conversation is essential listening for technology executives and investors trying to understand the industrial realities underlying the AI boom. While most media coverage focuses on model capabilities and application potential, Huang's discussion reveals the physical and economic infrastructure that makes those capabilities possible. Understanding these constraints—and how NVIDIA is addressing them—is crucial for anyone making strategic decisions about AI investments, infrastructure planning, or technology partnerships.

Product managers and engineers building AI systems will find particular value in Huang's discussion of architectural evolution and the importance of co-designing hardware and software for specific workload characteristics. The insights about efficiency optimization, memory technology choices, and system integration offer a masterclass in the kind of systems thinking that separates adequate solutions from transformative ones.

Finally, leaders in any industry that depends on complex supply chains should pay attention to Huang's description of his role in shaping partner investments. The ability to build shared vision across organizational boundaries, to persuade without authority, and to maintain the credibility that makes bold commitments believable—these are skills that transfer across industries and applications. Whether you are building AI systems or consumer products, the principles of ecosystem leadership that Huang describes will determine who captures value in increasingly connected markets.