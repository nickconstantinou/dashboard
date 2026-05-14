---
title: 'Andrew Wilkinson: AI Agents run my business and life'
date: '2026-05-14'
type: podcast
category: Business/Startups
video_id: 01KQT1CED6D3RCSDC8WMMBY8YE.mp3
channel: Startup Ideas Podcast
video_url: https://episode.flightcast.com/01KQT1CED6D3RCSDC8WMMBY8YE.mp3
---

<div class="key-insights">
<h2>Key Insights</h2>
<ul>
<li><strong>[33:49–35:16]</strong> <em>Personal AI Tools and Productivity Stack</em> — The guest shows his personal AI setup including a wearable camera device that records his entire day for G to ingest context. He built AI tools for inbox management that draft emails and create Instagram stories from tweets. He uses countdown timers tracking remaining summers with kids and days to live. Two OpenClaw agents run on a VPS with Ava as his personal assistant monitoring health metrics.</li>
<li><strong>[27:29–31:38]</strong> <em>AI-Driven Business Portfolio at Tiny</em> — The guest runs Tiny empire with 24 businesses and uses AI to interface with portfolio companies and their data. He trained a vector database on his family office Folly Partners and built a CFO tool showing real estate holdings, stocks, balance sheets, and portfolio rebalancing analysis. AI agents handle administrative burden that made him forget he had no laptop while running his business from Ubers.</li>
<li><strong>[22:30–23:31]</strong> <em>Financial Portfolio Tracking and Venture Investments</em> — The guest built a markdown system that aggregates all his financial data into G Brain, tracking $16M invested now worth $36M, analyzing quarterly performance, write-offs, and identifying potential issues before they become problems.</li>
<li><strong>[31:38–33:49]</strong> <em>Software Business Economics and Opportunities</em> — The guest argues software is now free and a worse business than five years ago due to AI competition and vibe coding. He suggests the real opportunity is in services, using funeral homes as an example where 20 smart operators will build their own software. For a 20-year-old vibe coder, the goal should be making $1-2M with straightforward products like Deep Personality.</li>
</ul>
<p class="signal-tags"><span class="signal-tag">personal productivity</span> <span class="signal-tag">AI tools</span> <span class="signal-tag">health monitoring</span> <span class="signal-tag">life optimization</span> <span class="signal-tag">business operations</span> <span class="signal-tag">portfolio management</span> <span class="signal-tag">family office</span> <span class="signal-tag">AI automation</span> <span class="signal-tag">finance</span> <span class="signal-tag">portfolio tracking</span></p>
</div>

<p># Key Insights

- **Productivity split is currently unfavorable**: Andrew estimates he's spending 50% of his time debugging AI agents, 30% improving them, and only 20% actually being productive—meaning the tools are still more burden than liberation for most users.
- **A support agent can now autonomously fix bugs and merge PRs**: His Deep Personality app's support agent handles tickets, escalates P0 security issues directly to the dev agent for automatic fixing, and sends pre-written responses to customers with zero human intervention.
- **Marketing agents are managing real ad budgets**: The marketing agent is hooked into PostHog for data, connected to Meta and Reddit ads accounts, handles multivariate testing, creates ad creative, and adjusts budgets—all from natural language instructions like "increase budget by $1,000."
- **"Vibe coding" enables solo product creation**: Andrew bypassed his own agency (MetaLab) to build the entire Deep Personality app himself in "a few manic days," using Claude Code to generate the 100-page personality report system, psychological assessments, and JSON scoring infrastructure in roughly 40 minutes of setup.
- **Full autonomy is 3-6 months away for basic businesses**: Andrew believes truly autonomous companies that require no human oversight are close but not here yet, noting current agents function like "genius babies" that need step-by-step instructions—comparing the current state to "Zapier Zaps that can make basic decisions."

---

# The Vibe Coding Revolution: How Andrew Wilkinson Runs His Entire Business with AI Agents

In December 2025, Andrew Wilkinson experienced what he describes as an addictive breakthrough. Unlike most people who dabbled with AI coding tools like Claude Code and Replit and found them interesting but insufficient, Wilkinson describes waking up at 3 or 4 in the morning, rolling out of bed with "a big smile on his face," and sitting in terminal with ten tabs open. He compares it to chasing a dragon—the legendary high that drug users perpetually try to recreate. The catalyst was a specific moment: traveling to Arizona for a conference, having forgotten his laptop, but realizing he'd set up an OpenClaw agent that could run his entire business from the back of Ubers. No one noticed that every single email was being written by AI. That competence, that seamlessness, became his obsession.

What makes Wilkinson uniquely qualified to share this inside look is his position as both a serial entrepreneur and the founder of MetaLab, a significant design and development agency. He's seen how traditional software development works. He's also the type of person who buys and starts businesses as a hobby, accumulating the administrative burden that comes with SaaS companies—support tickets, accounting, and what he calls "very boring rote types of tasks." Instead of delegating this work to his agency or hiring teams, Wilkinson went all-in on building autonomous systems. This episode represents the first time he's sharing his exact setup publicly: the tools, the frustrations, the failures, and the jaw-dropping successes.

---

# Vibe Coding: Building a 100-Page Personality Report in Days

The story begins with Wilkinson's personal life. He wanted to build a custom GPT project for his relationship with his girlfriend—the kind of tool where they'd input their dynamics and get insights into recurring conflicts. He asked ChatGPT which psychological tests would be most valuable, received a list of fifteen different assessments, and then turned to Claude Code with a simple request: build a multiple-choice test interface with scoring, export everything to JSON. The process took about forty minutes.

Both partners completed the assessments, uploaded their JSON files, and asked the AI to analyze the data without any context about who they were. The result was startling. The AI nailed every single fight they have, every recurring issue at home. "Our jaws just dropped," Wilkinson recalls. The power of aggregated psychological testing, synthesized by AI, was undeniable.

Instead of taking this to a development team or his own agency, Wilkinson decided to productize it himself. He calls this approach "vibe coding"—a term that captures the feeling of coding by intuition and mood rather than formal training. Using the Hollywood screenwriting analogy he employs, Wilkinson explains why this matters: brilliant screenwriters have incredible ideas, but between the script and the finished film stand 100 people, $50 million in financing, and countless middlemen. Every layer between vision and execution compromises creativity. Vibe coding removes those layers. You think it, you write it, you iterate with AI, and you ship it. No one misinterprets your vision. No one has gaps in their expertise that create friction between design and development.

In a few manic days, Wilkinson built Deep Personality—an app where users complete a 40-minute personality assessment and receive a 100-page report written in the style of Robert Greene. The report covers archetypes (his is "the blazing architect"), superpowers, kryptonite, ideal career paths, relationship compatibility, ADHD indicators, OCD tendencies, attachment styles, and internal family systems analysis. The depth is extraordinary: a single AI-generated document that would take a human therapist hours to produce, delivered instantly.

---

# The Agent Architecture: Three Bots Running a SaaS Company

With the product built, Wilkinson faced the eternal entrepreneur's problem: starting something exciting but dreading the maintenance phase where you have to hire people, manage them, and deal with the organizational overhead. His solution was characteristically direct: build agents to do everything.

The Deep Personality stack uses Harbor, a friend-built agent management platform (available at github.com/geekforbrains/harbor) that serves as a visual harness for running multiple AI agents simultaneously. Wilkinson explains that OpenClaw alone wasn't quite deterministic enough and lacked visual tracking—what he needed was something closer to a visual org chart where he could see every agent's status at a glance. Harbor provides that interface, with agents connected to their knowledge bases, databases, and environment variables.

**The Support Agent** handles customer inquiries with near-complete autonomy. It either resolves tickets directly or, when a technical issue arises, escalates to the dev agent. For P0 security vulnerabilities—a critical bug or breach—the dev agent automatically fixes the issue and merges the pull request without human approval. For everything else, Wilkinson wakes up to pre-merged code and template emails explaining the fixes. "Support is not a job very, very soon," he predicts with confidence.

**The Marketing Agent** is where Wilkinson sees the most exciting potential. It's integrated with PostHog for product analytics and connected directly to Meta and Reddit advertising accounts. The agent conducts multivariate testing on ad creative, manages budgets based on natural language instructions ("increase budget by $1,000" or "approve this SEO project"), and generates new ad variations autonomously. The current revenue sits around $20,000, but Wilkinson's eyes light up when discussing the trajectory: "What happens when we give it a $100,000/month ad budget and find the ads and creative that actually work?"

**The Dev Agent** handles bug fixes, feature requests, and code maintenance. It monitors the codebase, responds to issues, and merges improvements—all while Wilkinson focuses his attention elsewhere.

---

# The Honest Reality: Debugging a Genius Baby

Wilkinson's enthusiasm is palpable, but he tempers it with remarkable candor about the current limitations. The 50/30/20 split—half debugging, 30% improving, 20% productive—reveals the actual cost of this autonomy. "It's like the classic productivity treadmill," he admits. The tools work, but they require constant babysitting, refinement of prompts, and debugging of edge cases that human employees would handle intuitively.

The fundamental problem is context window limitations. Wilkinson draws an analogy to the movie *Memento*: current AI models have the memory of someone with anterograde amnesia. They can hold a conversation, but they can't maintain coherent long-term awareness without extensive system prompts and knowledge base setups. He believes that when context windows expand to 5-10 million tokens, running entire companies becomes genuinely feasible. For now, you're managing something like "a super genius who has Alzheimer's"—brilliant in bursts, but requiring constant reorientation.

On the question of fully autonomous companies—the kind Pulsia and similar services are now selling—Wilkinson is skeptical but not dismissive. "You cannot run a fully autonomous company right now," he states flatly. The companies selling that dream are "selling a dream." Support, marketing, and basic dev tasks? Yes. Product strategy, vision, and nuanced decision-making? Not yet. His timeline estimate of three to six months for basic autonomous businesses feels optimistic, but he's clearly watching the space closely.

---

# The Strategic Vision: Why Vibe Coding Beats Traditional Development

For entrepreneurs and business builders, Wilkinson's comparison between vibe coding and traditional agency work offers a framework worth examining. He doesn't dismiss the value of skilled teams—he runs one of the best-known agencies in tech. But for his own projects, the friction of collaboration outweighs the benefits.

Consider the typical product team: a designer who excels at visual design but struggles with frontend implementation, a frontend developer who doesn't understand backend constraints, a copywriter who works in isolation from technical reality, and a product manager translating between visionaries and executors. Every handoff introduces interpretation error, delay, and misalignment. Vibe coding eliminates handoffs. Wilkinson designs, codes, writes, and ships. When he needs help, he prompts an AI. The vision flows directly to execution.

The psychological dimension matters too. "The worst part about business is people," Wilkinson says, and he's not being cynical—he's being practical. Employees are unreliable, don't share your exact vision, require management overhead, and have bounded expertise. AI agents are always available, always aligned with their instructions (when properly prompted), and can handle multiple disciplines without friction. The tradeoff is upfront investment in learning to prompt effectively and debugging the occasional hallucination.

---

# Key Takeaways for Builders and Business Owners

**1. Start with vibe coding for personal projects before enterprise systems.** Wilkinson built Deep Personality as both a product and a proof of concept for his agent infrastructure. By testing the stack on something he cared about, he learned the capabilities and limitations organically. His recommendation: find a project you care about and build it yourself with AI tools before trying to retrofit autonomy into an existing business.

**2. Support is the lowest-risk entry point for AI autonomy.** The support agent "works basically perfectly," in Wilkinson's words, because customer service tickets follow patterns. A marketing agent requires brand understanding and creative judgment. A dev agent requires code review and security awareness. But support responses are templatable, escalate logically, and when they fail, the failure is visible and correctable. If you're adding one AI employee to your business, start with support.

**3. Current agents need explicit, step-by-step instructions—not delegation.** The gap between "hire a CEO agent and delegate everything" and "write a 200-line system prompt explaining every workflow" is enormous. Wilkinson emphasizes that you cannot say "check your email and reply appropriately." You must say "check your email every fifteen minutes, read each message, determine if it's a support inquiry or sales inquiry, and for support inquiries, use this knowledge base to draft a response." The future is delegation; the present is instruction.

**4. Visual agent management tools are becoming essential infrastructure.** OpenClaw is text-based; Harbor adds the GUI that makes multi-agent systems comprehensible. If you're running more than two or three agents, you need visual oversight—a dashboard that shows which agents are running, what they've done, and where they're stuck. This space is rapidly evolving, and tools like Harbor, Paperclip, and others are racing to make agent orchestration accessible to non-engineers.

**5. The $100k/month ad budget test will determine what's possible.** Wilkinson's most exciting claim is the potential to give a marketing agent a massive budget and let it optimize autonomously. This is the real test: can an AI agent not just manage a $1,000/month test but run a serious growth budget with appropriate judgment? His belief that this will work within months represents a high-conviction bet that advertising—traditionally a human creative discipline—is ripe for automation.

---

# Who This Episode Is For

This content is essential viewing for **founders, solo entrepreneurs, and small business operators** who are curious about leveraging AI but haven't yet built autonomous systems into their operations. If you've experimented with ChatGPT and Claude but haven't felt the "chasing the dragon" moment Wilkinson describes—the moment where AI genuinely handles something competently without you watching—this episode will show you exactly what's possible with current tools and honest assessment of their limitations.

Product managers and tech leads at companies considering AI integration will benefit from Wilkinson's candid breakdown of what works (support automation, ad management) versus what doesn't (complex product decisions, vision-setting). His framing of agents as "genius babies" versus autonomous CEOs offers a realistic mental model for what's achievable today versus what's aspirational.

Finally, anyone interested in the trajectory of autonomous businesses—the promises being sold by Pulsia and similar services—should watch Wilkinson's skeptical but engaged analysis. He's not a Luddite dismissing the technology, nor is he a true believer ignoring the current messiness. He's a pragmatist who has built the infrastructure, shipped the product, and is running real revenue through AI systems. His honesty about the 50% debugging time is as valuable as his enthusiasm about the marketing agent's potential.</p>