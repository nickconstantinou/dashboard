---
title: Hire a team of AI Agents
date: '2026-05-08'
type: podcast
category: Business/Startups
video_id: 01KR40FZPM416A55PB2XRMP5D2.mp3
channel: Startup Ideas Podcast
video_url: https://episode.flightcast.com/01KR40FZPM416A55PB2XRMP5D2.mp3
---

<p># Key Insights

- **Nebula uses sub-agent architecture to solve AI memory problems**: Rather than relying on a single AI with persistent memory (like Hermes's self-learning loop), Nebula handles this by creating specialized agents with explicit goals that get embedded into the system prompt each time, preventing context drift and information loss.

- **Model selection is cost-driven**: For routine tasks like scanning emails and Slack, Imran uses **Quen 3.6 Plus** instead of Opus or Sonnet—he emphasizes this is "probably a waste of money and resources" because identifying blocked team members is "a very basic task" that even older LLMs can handle.

- **Composable integrations via Composio**: Nebula's OAuth connections to tools like Gmail, Slack, Google Calendar, Linear, Jira, and others are managed through Composio, making setup significantly easier than manually configuring tools like Hermes or OpenClaw, which require more technical expertise.

- **Public agent sharing enables cloning**: Nebula's new sharing feature allows users to publish agents with anonymized connections—recipients can clone the agent and adapt it to their own tool stack (e.g., adding Telegram instead of Slack).

- **Chief of staff = executive optimization engine**: Imran frames the role as "optimizing the executive to make decisions"—handling calendar management, message filtering, project status tracking, and unblocking team members so executives focus only on decisions.

---

# Introduction

The concept of an AI chief of staff has been pitched countless times by tech companies and productivity influencers, but most implementations fall flat when rubber meets road. Either they require significant technical setup, cost a fortune in API calls, or simply don't integrate meaningfully with the tools busy professionals actually use. In this episode, Imran returns to explain how to build a functioning AI chief of staff using Nebula, an agent creation and deployment platform that abstracts away much of the technical complexity that makes other solutions impractical for time-constrained business users.

The timing matters enormously. In 2026, knowledge workers are drowning in a sea of Slack messages, emails, meetings, and project management tools—yet the core job of an executive remains simple: make decisions. Everything surrounding that decision-making—sorting through noise, identifying what needs attention, tracking project statuses, unblocking team members—represents pure overhead that could theoretically be automated. Imran makes the case that for "all the boring stuff that a normal chief of staff wouldn't actually want to do," there is now no reason a human should be doing it at all.

Unlike previous technical deep-dives on similar platforms, this demonstration prioritizes accessibility over power-user features. Imran and the host walk through building real agents step-by-step, from connecting integrations to configuring goals to sharing finished agents publicly. The goal isn't to impress developers—it's to show a busy founder, executive, or professional exactly what they can have working in their own workflow by the end of the video.

---

# The Agent Architecture: Think Humans, Not Software

Imran opens by establishing a conceptual framework that will guide the entire demonstration: the most effective way to think about AI agents is as virtual team members with specific roles, goals, and tool access. This mirrors how actual organizations function, where a project manager uses Jira and Confluence, a coordinator manages calendars, and an executive assistant handles communications.

In Nebula, each agent is defined by three core components: a system prompt (essentially the agent's personality and instructions), explicit goals that define what success looks like, and integrations that connect to external tools like Gmail, Slack, Linear, or Jira. This modularity is crucial because it solves the memory problem that plagues monolithic AI systems. Rather than expecting one AI to remember everything across complex, multi-step workflows, each agent maintains sharp focus on its defined purpose. When invoked, the agent's goals and context are fed directly into its prompt, ensuring consistent behavior without the drift that occurs in systems relying on long-context windows.

This approach also maps naturally onto existing workflows. Professionals already think in terms of roles and responsibilities—why should AI automation be any different? Imran notes that this paradigm feels intuitive because "there are certain people who have certain goals inside a company, and in order to achieve those goals, they use a certain set of tools." Agents work exactly the same way, just without the overhead of onboarding, management, and salaries.

---

# Why Nebula Over Hermes or OpenClaw?

The host presses Imran on a critical distinction: previous episodes covered Hermes (an autonomous AI assistant framework) and OpenClaw, so why use Nebula for this chief of staff demonstration? Imran is characteristically direct. Hermes and OpenClaw still require technical comfort with terminals, manual model configuration, and regular updates. For the "extremely busy" professional who already has a business or demanding job, spending hours configuring a private AI server defeats the purpose of automation.

Nebula's value proposition is speed to working automation. The interface resembles familiar communication tools—it looks like Slack, with channels representing different agents rather than different teammates. This reduces the cognitive overhead of learning an entirely new paradigm. Someone can log in, connect their Gmail and Slack via OAuth, define an agent's goals, and have it running within minutes rather than hours.

The platform also handles the tedious work of API integrations through Composio, which provides "best in class bridges" to common tools. Connecting Gmail, Slack, Google Calendar, Linear, Jira, and dozens of other services requires only clicking through OAuth prompts rather than hunting for API documentation and managing authentication tokens. Imran specifically cites this as an advantage for non-technical users who want automation without engineering support.

That said, Imran acknowledges the tradeoffs. Power users who enjoy tinkering and want maximum cost control will still prefer more technical setups—Nebula charges for convenience and accessibility. There's also an emerging trend toward local deployment for compliance or data sovereignty reasons, which Nebula is reportedly addressing with upcoming features.

---

# Building the Blockage Radar Agent

The demonstration begins with the most immediately practical use case: identifying team members who are blocked and waiting on action from their leader. The host articulates the pain precisely—"you get a lot of messages every single day... you need to execute, but you also need to unblock the people that are actually executing on your behalf." A chief of staff would naturally handle this triage, and an AI can do the same.

The process starts by querying Nebula's existing agent to research what a chief of staff actually does, generating a framework that includes strategic planning, agenda management, cross-functional alignment, and project coordination. This research becomes the foundation for building targeted agents that handle each function.

To create the Blockage Radar, the host connects Gmail and Slack directly through Nebula's integration panel—clicking through OAuth prompts rather than writing any code. The agent is configured with a simple goal: scan emails and Slack messages, identify any team members waiting on a response or decision, and surface those blockages in a daily briefing. The agent appears in the left sidebar immediately and begins processing in the background.

Imran takes a moment to defend his use of SuperWhisper for voice input, noting that speech-to-text can reach "150 words per minute" while even fast typists struggle to match that. This represents the host's own personal automation philosophy: wherever possible, eliminate manual data entry in favor of faster modalities.

The Blockage Radar agent uses Quen 3.6 Plus rather than premium models like Opus. Imran explains this choice pragmatically: the task is identifying blocked threads, not performing complex reasoning. "I think that's probably a waste of money and resources," he says of using state-of-the-art models for routine filtering. Premium models should be reserved for "coding or tasks that required deep thinking." This cost-awareness reflects a mature approach to AI deployment—using the right tool for each task rather than defaulting to the most expensive option.

The agent produces a sample briefing showing emails waiting on response, Slack messages requiring attention, and a summary of blockages. Imran notes that two years ago, generating this report every morning represented "a job that you would hire someone to do"—now it runs automatically on a configurable schedule.

---

# Cross-Functional Alignment and Project Status Tracking

Moving to the next chief of staff function, Imran outlines an agent that monitors project health across the entire organization. The agent connects to Jira or Linear (depending on the team's preference), Confluence for documentation, plus email and Slack, and produces a daily status report covering three timeframes: work completed yesterday, planned work for today, and any projects at risk of falling behind schedule.

This directly maps to what Imran calls "the job description of a project manager." Rather than paying someone to attend status meetings and compile reports, the agent automatically aggregates data across all project management tools and surfaces the information an executive needs to make decisions. If someone is blocked on a legal review, the agent pulls that from email. If a sprint is behind, it pulls that from Jira. The executive gets a unified view without manually checking five different systems.

When asked about connecting alternative tools—like Linear instead of Jira—the answer is straightforward: search for the tool in the integrations panel, click add, and authenticate via OAuth or API key. The same applies for communication tools like WhatsApp, which Imran's own team uses for customer messaging. The agent architecture doesn't care which specific tools are used; it simply connects to whatever the user specifies and operates within those constraints.

---

# The Sharing Economy for Agents

One of Nebula's most distinctive features is the ability to share agents publicly. Rather than sharing skill files, CLI configurations, or documentation that requires technical knowledge to deploy, users can publish an agent with anonymized connections. Anyone with the URL can "clone this agent" and import it into their own Nebula workspace, then modify the integrations, goals, and tools to match their own workflow.

This creates a marketplace of working automation templates. A marketing executive might share an agent that connects HubSpot, Gmail, and LinkedIn to surface leads needing follow-up. A product manager might share one that monitors Linear and customer feedback channels. Rather than starting from scratch, users browse shared agents, find ones close to their needs, and remix them.

Imran expresses genuine excitement about this capability: "I think that's super powerful" because it bridges the gap between "people sharing skill files" or "CLIs" and actually usable automation. The distinction matters—most AI tool sharing requires technical sophistication to implement, while Nebula's approach allows anyone to deploy working automation with a single click, then customize as needed.

---

# The Memory Problem and Sub-Agent Solutions

A persistent challenge in AI automation is maintaining coherent memory across complex, multi-step workflows. Imran addresses this directly by contrasting Nebula's approach with Hermes's self-learning loop. In systems that rely on a single AI managing everything, context windows eventually fill, important details get dropped, and behavior becomes inconsistent over time.

Nebula handles this structurally rather than algorithmically. By segmenting all automation needs into discrete sub-agents with explicit, defined goals, the system avoids the memory problem entirely. When an agent runs, its goals and context are freshly embedded into its system prompt—there's no reliance on the AI remembering from previous conversations or sessions. This is architecturally simpler than building self-learning loops, and for most use cases, equally effective.

The tradeoff is that complex, multi-step workflows may require more explicit orchestration. If a task spans multiple agents, someone needs to define that workflow. But for the targeted automation most professionals need—daily briefings, status updates, message filtering—individual agents with clear goals work beautifully without any cross-agent orchestration complexity.

---

# Detailed Takeaways

**1. Model selection should match task complexity, not default to the most expensive option.** Imran's deliberate choice of Quen 3.6 Plus for the Blockage Radar agent reflects a mature automation philosophy: simple filtering tasks don't require frontier models. Premium models like Opus or Sonnet should be reserved for tasks involving coding, nuanced reasoning, or complex analysis. Running everything on state-of-the-art models is "probably a waste of money and resources" and increases latency without improving results. Build an intuition for which tasks genuinely require deep thinking versus pattern matching, and allocate model budgets accordingly.

**2. The sub-agent architecture solves real engineering problems while improving reliability.** Rather than building one monolithic AI to handle everything, break automation into focused agents with specific goals, tools, and contexts. This prevents memory degradation, reduces context drift, and makes debugging straightforward—you can test each agent independently. It also mirrors how teams actually function, making the system intuitive to design and maintain. When designing your own automation, start by identifying distinct roles rather than trying to build one AI that does everything.

**3. Tool connectivity determines real-world utility more than AI sophistication.** Imran emphasizes that Nebula's advantage over technical alternatives isn't superior AI—it's easier integration with the tools professionals actually use. A brilliant AI that can't connect to Gmail, Slack, and project management tools is useless for practical automation. When evaluating any agent platform, prioritize the integrations available and the ease of setup. OAuth connections that complete in seconds versus API key configuration that takes hours will determine whether your automation actually gets built and used.

**4. Shared agents democratize automation by eliminating the "starting from scratch" problem.** The ability to clone working agents, customize them for your specific tool stack, and potentially share your modifications back creates a positive-sum ecosystem. Rather than each professional spending hours building the same type of agent from documentation, the community can iterate on proven templates. This is particularly valuable for non-technical users who would otherwise be locked out of automation entirely. Seek out agent sharing communities relevant to your industry and workflow.

**5. The executive's job is decision-making; everything else is overhead that can be automated.** Imran's framing crystallizes the value proposition: "the job of an executive is to make decisions... everything around that is what a chief of staff's job is." Identify every task you do that isn't making a decision—filtering messages, compiling status reports, checking project dashboards—and recognize these as automation candidates. The more precisely you can define a task that doesn't require your unique judgment, the more confidently you can hand it to an AI agent.

---

# Who This Is For

This content targets **busy professionals, founders, executives, and knowledge workers** who want meaningful AI automation but lack technical backgrounds or the time to become system administrators. If you've tried setting up AI tools before and bounced off terminal commands, API documentation, or configuration files, Nebula represents a meaningful reduction in friction. The interface is designed for people who want automation working in minutes, not weeks.

The demonstration particularly resonates with **managers and team leads** responsible for coordinating work across multiple functions. The Blockage Radar agent solves a universal pain point: knowing what your team needs from you without spending hours manually scanning every channel and inbox. Similarly, the project status agent replaces tedious manual check-ins with automated aggregation.

**Solo founders and small team leaders** may find the most immediate value—there's no budget for a chief of staff, but the work still needs doing. Building these agents provides the organizational leverage that previously required hiring, at a fraction of the cost. The shared agent marketplace offers templates that non-technical users can deploy without building from scratch.

However, **highly technical users who enjoy tinkering** or organizations with strict data residency requirements may prefer more flexible platforms. Imran acknowledges that power users who want maximum control over costs and configuration will find Nebula constraining. Similarly, enterprises requiring on-premise deployment need to verify Nebula's compliance capabilities before committing.</p>