---
title: "The biggest barriers to AI scaling laws - NVIDIA CEO explains | Jensen Huang and Lex Fridman"
date: 2026-04-05
type: youtube
category: "AI/Tech"
video_id: "Mf2u2b1bogE"
channel: "Lex Fridman"
video_url: "https://www.youtube.com/watch?v=Mf2u2b1bogE"
---

# The Biggest Barriers to AI Scaling Laws: Jensen Huang on Power, Supply Chains, and the Future of Computing

In a wide-ranging conversation with Lex Fridman, NVIDIA CEO Jensen Huang offered an unusually candid look at the technical, logistical, and economic forces shaping the future of artificial intelligence infrastructure. The discussion moved from the philosophical—how we overcame past computing blockers—to the deeply practical: the intricate web of suppliers, the power grid's hidden capacity, and why Huang believes the path forward is clearer than many assume. This interview, recorded during a period of unprecedented demand for AI computing, provides a rare window into how one of the world's most consequential companies thinks about scaling the infrastructure that will define the next decade of technological progress.

## The Nature of Computing Blockers: Lessons from History

Huang opened the conversation by acknowledging that humanity has a long history of believing certain technological barriers would be insurmountable—only to overcome them through innovation and determined engineering effort. Rather than dwelling on past victories, however, Huang shifted focus to what actually concerns him today as AI systems become ubiquitous and agentic architectures begin to emerge as the dominant paradigm.

The immediate answer, he explained, is compute—but not simply in the sense of having enough chips. The question is how to continue scaling while managing the enormous energy demands that such scaling requires. Power is a genuine concern, Huang acknowledged, but it is not the only one. The real challenge lies in decoupling computational growth from energy consumption through what NVIDIA calls "extreme code design"—a systematic approach to improving tokens per second per watt by orders of magnitude every single year.

To illustrate just how dramatic this progress has been, Huang offered a striking comparison. In the last ten years, if traditional Moore's Law had continued unimpeded, computing would have progressed approximately 100 times. NVIDIA, through its architectural innovations and software optimizations, has progressed and scaled up computing by a factor of one million times in that same decade. This acceleration, Huang emphasized, is not accidental but the result of deliberate, intensive engineering across every layer of the computing stack.

The economics of this progress are equally remarkable. While the price of NVIDIA's computers continues to rise—reflecting their increasing capability and the sophisticated engineering embodied in each system—the token generation effectiveness of those systems is increasing so much faster that token costs are falling by approximately an order of magnitude every year. This trajectory, Huang suggested, is the fundamental engine driving AI adoption: as inference becomes cheaper and more efficient, the economic case for embedding AI into every product and service becomes overwhelming.

## The Supply Chain as Strategic Asset

Perhaps the most revealing portion of the interview concerned Huang's relationships with NVIDIA's extensive supply chain—an ecosystem that spans from the most advanced lithography equipment manufacturers to the factories producing mundane components that nonetheless prove essential. Huang spent considerable time describing how he views these relationships not merely as vendor arrangements but as genuine partnerships requiring transparent communication, shared vision, and mutual trust.

The list of critical suppliers reads like a tour through the most sophisticated manufacturing enterprises on Earth: ASML with its extreme ultraviolet lithography machines, TSMC with its advanced packaging capabilities, and SK Hynix with its high-bandwidth memory (HBM) products. Each represents a potential bottleneck in the supply chain, a point where the entire AI scaling effort could be constrained. Yet Huang expressed remarkable confidence that these bottlenecks are being addressed systematically.

"No company in history," Huang noted, "has ever grown at a scale that we're growing while accelerating that growth." He acknowledged that this pace is "incredible" and difficult for most people to even comprehend. Yet rather than anxiety, his tone conveyed something closer to controlled excitement—the satisfaction of managing an engineering challenge that, while formidable, is ultimately tractable.

To illustrate how he manages these relationships, Huang described attending a recent event attended by hundreds of CEOs representing the entire IT industry's upstream suppliers and the downstream infrastructure industry. The purpose of gathering these executives was straightforward: Huang needed to inform them about NVIDIA's business conditions, the growth drivers in the very near future, and where the company intended to go next. This information, he explained, was essential for these CEOs to make informed decisions about their own capital investments and strategic planning.

The gathering itself was unusual—Huang could not recall another keynote event where several hundred CEOs had shown up—but it reflected a core belief in his management philosophy: that transparency and shared vision serve everyone's interests better than information hoarding or strategic ambiguity.

## The HBM Memory Bet: A Case Study in Supply Chain Leadership

Huang offered a particularly vivid example of how this philosophy translates into concrete action. Approximately three years ago, he found himself trying to convince several DRAM industry CEOs that high-bandwidth memory (HBM)—at the time used scarcely, almost exclusively in supercomputers—would become mainstream memory for data centers in the future.

The initial reaction, Huang recalled with a smile, was skepticism. "At first it sounded ridiculous," he admitted. HBM was specialized, expensive, and had a narrow application domain. The idea that it would become standard equipment in commercial data centers seemed implausible. Yet several of these CEOs believed in Huang's vision and decided to invest in building HBM memory production capacity.

Another example involved low-power memories originally designed for cell phones. Huang wanted to adapt LPDDR5 memory—standard equipment in smartphones—for use in supercomputers and data centers. The combination seemed incongruous: cell phone memory for supercomputers. But Huang explained the technical rationale, and today HBM4 and LPDDR5 represent two of the highest-volume memory products in history, with all three memory types (DDR, HBM, and LPDDR) experiencing record years.

These are not minor companies, Huang emphasized—these are 45-year-old semiconductor giants with deep engineering expertise and well-honed skepticism about novel claims. That they chose to follow NVIDIA's lead, investing billions in new production facilities based on Huang's predictions, speaks to both his persuasive abilities and the trust he has cultivated over decades of working relationships.

## The Verubin Rack: Complexity at Scale

The conversation turned to the technical details of NVIDIA's Blackwell architecture, specifically the Verubin rack system that represents the company's current flagship offering. Each Verubin rack contains 1.3 million components—1.3 million individual parts that must be sourced, manufactured, tested, and assembled with extraordinary precision. These components come from approximately 200 different suppliers, each specializing in a particular piece of the puzzle.

When Fridman noted that this complexity might frighten some observers—how does such a fragile-looking supply chain actually work?—Huang agreed that the depth of science, engineering, and manufacturing involved is remarkable. "It's just feels scary how intricate the supply chain is, how many components there are," he acknowledged. "But it works somehow."

The key to making it work, Huang explained, is treating each potential bottleneck not as an insurmountable problem but as a coordination challenge that can be addressed through clear communication and collaborative planning. "I'm doing all the things necessary to [address them]," he said, noting that once he has personally verified that a concern is being addressed, he can set it aside and focus on the next challenge.

## From DGX1 to NVLink72: The Architecture Revolution

Huang walked Fridman through the evolution of NVIDIA's computing architecture, from the original DGX1 systems—which customers received as components and assembled in their own data centers—to the current NVLink72 rack-scale computing approach, where entire supercomputers are built in the supply chain and shipped as complete units weighing two or three tons per rack.

This shift was not merely logistical but reflected fundamental changes in how AI workloads are designed and executed. The density achievable with NVLink72 made in-data-center assembly impossible—the systems simply contained too many components, required too much power, and demanded too precise integration to be assembled piecemeal in the field.

The implications for the supply chain were profound. When NVIDIA decided to build supercomputers in manufacturing facilities rather than in customer data centers, it had to account for the enormous power requirements of that manufacturing process. Huang presented a revealing hypothetical: if you wanted to build 50 gigawatts of supercomputers that would eventually run simultaneously, and manufacturing each batch of that capacity took one week, then each week the supply chain would need to provision a gigawatt of power just to build and test those systems before shipment.

This example illustrated why Huang's supplier relationships matter so much. He has to fly to Taiwan, visit TSMC's facilities, and explain not just what NVIDIA needs today but what it will need months or years in the future, why those needs will arise, and how suppliers can prepare. Only with this information can suppliers make the multi-billion-dollar capital investment decisions required to stay ahead of demand.

The persuasion process, Huang explained, is not a sales pitch but a collaborative reasoning exercise. "I give them every opportunity to question me," he said, describing how he spends time explaining the technical and market dynamics to people, reasoning about them in first principles, and drawing diagrams to illustrate the logic. "By the time I'm done with them, there's no doubt what to do."

## The Power Grid's Hidden Capacity

When Fridman pressed Huang on the energy challenge—the question of where all the electricity for AI systems will come from—Huang offered a perspective that reframed the problem entirely. The existing power grid, he explained, is designed for worst-case conditions with significant safety margins: a few days of extreme winter cold, a few days of extreme summer heat, and other extreme weather scenarios.

"This 99% of the time, we're nowhere near the worst case condition," Huang said. The grid is "probably running around 60% of peak" during normal operations. This means that 99% of the time, the power grid has excess capacity sitting idle—generation, transmission, and distribution infrastructure that exists precisely because we need it during peak periods but otherwise goes underutilized.

This insight suggests that the AI energy challenge is not, at least initially, about building new power plants but about better utilizing existing infrastructure. If data centers can be located where excess capacity exists, or if AI workloads can be scheduled during off-peak hours, a great deal of AI computing could be powered without new generation capacity.

## The Art of Shared Vision: Leadership in Uncertain Times

Throughout the interview, Huang returned repeatedly to the theme of building shared views of the future with partners and employees alike. This is not merely good business practice, he suggested, but a core part of his job: "part of my job is to inform and shape, inform and shape, inspire, inspire, inspire."

This leadership philosophy extends beyond NVIDIA's own walls. By informing the supply chain about where technology is going, Huang is in a real sense "manifesting the supply chain of the future." He is not simply responding to market forces but actively shaping them, creating the conditions for the infrastructure he needs by helping others see the same opportunities he sees.

The confidence that pervades Huang's comments about bottlenecks and supply chain challenges is not bravado but the product of extensive personal engagement with every link in the chain. He knows what TSMC can do and what it is planning to do. He knows what ASML is building. He knows what the memory manufacturers are investing in. And crucially, they know what he needs and why.

"Do you worry about certain bottlenecks?" Fridman asked at one point, pressing specifically on ASML tooling and TSMC packaging capacity. "Are you worried about how fast it could scale?"

"No," Huang replied, with the calm certainty of someone who has put in the work to earn that certainty. "Because I told them what I needed, they understood what I need. They told me what they're going to go do, and I believe in what they're going to do."

## Key Insights

**First, energy efficiency improvements are outpacing even the most aggressive historical benchmarks.** While Moore's Law might have delivered 100x improvement over a decade, NVIDIA has achieved 1,000,000x improvement in the same timeframe. The implication is profound: token costs are falling by approximately an order of magnitude annually, meaning that economic constraints on AI deployment are dissolving faster than many realize. Organizations should plan for a world where inference costs are trivial compared to today, not as a distant possibility but as an imminent reality within the next few years.

**Second, supply chain relationships have become a form of competitive advantage that cannot be easily replicated.** Huang's ability to convince DRAM manufacturers to invest billions in HBM production three years before it became obviously necessary, or to shift memory architectures for supercomputers, reflects decades of trust-building. Companies seeking to compete in AI infrastructure cannot simply purchase their way into similar relationships—they must earn them through consistent transparency, technical credibility, and demonstrated commitment to partners' success.

**Third, the power grid constraint is more tractable than commonly assumed.** The 99% figure Huang cited—that the grid operates at roughly 60% of peak 99% of the time—suggests substantial headroom for additional computing load without new generation capacity. This reframes the energy debate: rather than asking "where will we get the power," the more relevant question may be "how do we better utilize what we already have?" For data center operators, this suggests strategic advantages for locations with strong grid infrastructure but variable demand profiles.

**Fourth, manufacturing and computing are becoming increasingly intertwined.** The shift from assembling systems in data centers to building complete supercomputers in supply chain facilities represents a fundamental change in where computation happens. This vertical integration of manufacturing and deployment creates new logistical challenges—the need for gigawatt-scale power at manufacturing facilities being one example—but also enables architectural innovations impossible under the old model.

**Fifth, leadership in fast-moving technology requires active vision-sharing.** Huang's description of his supplier engagement process—reasoning from first principles, drawing pictures, spending hours ensuring understanding—stands in contrast to typical executive behavior. The lesson is not merely that transparency is valuable but that genuine persuasion requires investment. Leaders who expect partners to make billion-dollar bets based on minimal explanation will not build the trust necessary for true partnership.

## Who Should Read This

This conversation will be most valuable for technology executives and investors seeking to understand the infrastructure underpinnings of the AI revolution. If you are making decisions about AI strategy, data center investments, or technology partnerships, Huang's perspective on where bottlenecks actually exist—and more importantly, where they do not—provides essential context for planning.

Product managers and engineers working on AI systems will benefit from the technical depth regarding efficiency improvements and architecture evolution. Understanding that token costs are falling by an order of magnitude annually should inform how you design products and position pricing.

Policy analysts and energy planners will find Huang's power grid observations particularly relevant. His reframing of the energy question from "new capacity" to "utilization" may be controversial but deserves serious consideration given his direct involvement in building the facilities that will consume significant power.

For general readers seeking to understand the forces shaping AI's future, the interview offers a rare glimpse into how one of the most consequential companies in the technology sector thinks about the challenges and opportunities ahead. The combination of technical depth, strategic vision, and personal candor makes this conversation an unusually valuable window into the minds shaping our technological future.