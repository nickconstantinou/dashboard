---
title: "I built a real 29 dollar per month SAAS with Insforge"
date: 2026-04-02
type: youtube
category: "Tech"
video_id: "gxYcGipGCYA"
channel: "Fireship"
video_url: "https://www.youtube.com/watch?v=gxYcGipGCYA"
---

# How I Built a $29/Month SAAS Product Using AI: A Real-Time Experiment with Infisforge

## The Frustration That Sparked a Business Idea

The modern internet is built on a fragile foundation of interconnected services, and the cracks are showing more frequently than ever. In a candid video that reads more like a developer's diary than a polished tutorial, content creator [Name Redacted] walks viewers through the genesis of a potentially profitable SAAS idea—one born directly from the frustration of watching billion-dollar platforms fail their users with inconsistent, incomplete, or entirely absent status pages.

The creator opens by acknowledging the turbulent state of the technology landscape, noting that "things are not looking that great with the uptime these days." Recent months have seen Gemini suffer significant outages, Anthropic's Claude platform experience disruptions, and Supabase go down repeatedly—all while their own status pages fail to provide timely or accurate information to affected users. The situation has become so unreliable that the creator humorously notes they've seen Twitter itself go dark without any official communication, and GitHub—whose entire existence depends on developer trust—occasionally fails to update even its own status page when problems arise.

This led to a pivotal realization: what if the monitoring responsibility shifted from companies self-reporting their issues to independent third parties tracking uptime and downtime? The creator articulates this vision clearly, explaining that the core value proposition would be simple but powerful—"what if somebody else actually monitors that, or at least I can monitor my own uptimes and downtimes and all of these things?" This insight—turning the passive frustration of outages into an active business opportunity—becomes the foundation for everything that follows.

## The Business Case for Downtime Monitoring

Beyond personal frustration, the creator provides compelling market validation for this SAAS concept. They highlight the acquisition of Okla by Accenture, the company that owns Downdetector and Speedtest—two services that have become go-to resources for millions of users experiencing connectivity issues. The creator emphasizes that these applications succeed not because they're technologically revolutionary, but because they perform a single function reliably over extended periods: "we can technically build a SAAS and can sell it," they observe, noting that even a simple speed test tool, if built and maintained consistently, can become valuable infrastructure.

The timing for this venture appears particularly auspicious. Existing competitors in the uptime monitoring space charge significant fees for what many consider basic functionality. The creator references services like Uptime Robot, which charges $7 per month for a solopreneur plan allowing just 10 monitors with 60-second monitoring intervals. Additional features like HTTP port monitoring, keyword monitoring, API monitoring, and UDP monitoring typically require increasingly expensive tiers. The creator asks rhetorically, "can we build a system which can solve this problem, at least have as simple, uh, on this?"

The business model seems straightforward: offer reliable, independent monitoring at a price point that democratizes access for indie developers, small businesses, and solopreneurs who currently find enterprise monitoring solutions prohibitively expensive. If the platform can maintain accuracy and uptime—embodying the very reliability it promises to track in others—it would occupy a unique position in the market.

## Introducing Infisforge: The AI-Native Backend

The technical foundation for this project comes from Infisforge, an open-source backend platform that the creator describes as "the backend built for agentic AI-native application development" and positions as a Supabase alternative. The project has already garnered significant community attention, with nearly 1,900 stars on its repository, indicating robust interest in the platform.

What makes Infisforge particularly compelling for this use case is its deployment philosophy. The creator highlights that the platform offers one-click Docker deployment, meaning users can host the entire infrastructure wherever they choose: "everything is under my control," the creator notes, appreciating the sovereignty this provides over their data and infrastructure. This self-hosting capability addresses a common concern in the SAAS world—vendor lock-in—while still providing the conveniences of modern backend-as-a-service functionality.

The AI-native aspect of Infisforge proves crucial to this experiment. Rather than treating AI as an add-on feature, the platform appears designed from the ground up to support AI-driven development workflows. This alignment with the creator's approach—using AI assistance as a primary development partner rather than a mere autocomplete tool—creates a cohesive technical and philosophical framework for the project.

## The Experimental Approach: Building with Cursor and MCP

Perhaps the most innovative aspect of this project isn't the SAAS concept itself, but the methodology employed to build it. The creator commits to an unscripted, real-time experiment: using Cursor, an AI-powered code editor, to build the entire downtime detector application without writing code themselves. "I have no script for this video, no existing code," they explain. "I want to see that can AI build this whole thing for me. If it fails, you're going to see this. If this succeeds, on how much level it succeeds, you're going to see all of that."

The technical setup involves connecting Cursor to Infisforge through MCP (Model Context Protocol), which allows the AI agent to access tools and context from the backend platform. The creator walks through the installation process, noting that Infisforge detected their environment and automatically configured API keys and base URLs: "It even sets my API key and the base URL. Love that." The setup loads 17 tools including fetch documentation capabilities, SDK docs access, templates, metadata functions, and standard CRUD operations—giving the AI agent comprehensive access to build and modify the application.

The creator deliberately grants extensive autonomy to their AI assistant, explaining their philosophy: "People are giving their entire life to Claude Code. I can at least give my agents the autonomy to act on behalf of me." This hands-off approach serves a dual purpose: it tests the limits of current AI-assisted development tools while providing viewers with an authentic demonstration of what these systems can accomplish without heavy human intervention.

## Project Architecture and Feature Vision

The project takes shape with the creator establishing a new Infisforge project named "down detector," selecting the nearest region for deployment. The interface includes polished touches like animations for event selection, demonstrating that even the infrastructure setup process has been thoughtfully designed.

The creator draws inspiration from Infisforge's template library, examining a Reddit clone example to understand the platform's conventions for building community-based discussion systems with threaded conversations. However, they quickly pivot to their specific requirements, sketching out the core features needed for a downtime monitoring service. The vision centers on tracking "the downtime status of any endpoint, actually any endpoint" using Infisforge as the backend.

The creator begins enumerating requirements, starting with authentication: "first of all, it should be login." This fundamental feature acknowledges that a professional SAAS product needs user accounts, potentially with different access tiers for free and paid users. The planning phase involves the AI agent fetching documentation, pulling up relevant technical references, and outlining concrete development steps before diving into implementation.

## Understanding the Infisforge Platform Economics

Before proceeding with development, the creator explores Infisforge's pricing structure, which reflects a thoughtful approach to serving different user segments. The free tier at $0 per month includes $1 of AI model credits, providing enough resources for experimentation and small projects. This democratizes access to AI-native backend capabilities, allowing developers to test the platform before committing financially.

The $25 per month plan offers $10 in model credits monthly along with substantially higher limits: 100,000 monthly active users, 8GB storage, and 25GB bandwidth allocations. The creator shrewdly observes that "if any of the SAS has 100,000 active users, they are making way way more than $25"—a reminder that the pricing targets early-stage projects and growing applications, not established platforms with massive user bases.

The creator commits to testing the application on the free tier initially, with a willingness to upgrade if the product gains traction: "if our SAAS works good, I'll be—I'll not hesitate to upgrade this and sell it even." This pragmatic approach minimizes financial risk while keeping the door open for monetization if the concept proves viable.

## Key Insights and Takeaways

**The Power of Solving Your Own Frustrations**: The creator demonstrates a valuable entrepreneurial principle—that personal pain points often represent underserved market opportunities. By identifying a genuine need (reliable, independent status monitoring) and combining it with frustration at current solutions (expensive, self-reported, unreliable), they constructed a business concept with built-in market validation.

**AI-Native Development Tools Are Reaching Practical Viability**: The experiment with Cursor and Infisforge represents a significant test of current AI development capabilities. The 17 tools loaded through MCP, the automatic environment detection, and the ability to plan and execute development tasks suggest that AI assistants have evolved beyond simple code suggestions into genuine development partners capable of handling substantial workflow components.

**Open Source Infrastructure Creates New Entrepreneurship Pathways**: Infisforge's positioning as a self-hostable, open-source Supabase alternative demonstrates how the modern development ecosystem enables individuals to build and scale SAAS products without accepting the constraints—or costs—of traditional backend providers. This shift lowers barriers to entry for technical entrepreneurs while preserving flexibility and data sovereignty.

**Documentation and Tooling Quality Matter**: The seamless integration between Infisforge and Cursor, featuring automatic configuration and comprehensive tool access, highlights how developer experience directly impacts adoption. Products that reduce friction in the development process—whether through excellent documentation, intuitive APIs, or thoughtful integrations—will capture developer mindshare in an increasingly crowded market.

## Who This Content Serves

This video and the resulting insights will prove most valuable for **indie developers and solo entrepreneurs** considering their first SAAS product. The creator's transparent, unfiltered approach—showing both successes and inevitable setbacks—provides realistic expectations for what AI-assisted development can accomplish today.

**Technical founders** exploring backend infrastructure choices will find the Infisforge deep-dive particularly useful, as the creator evaluates the platform's capabilities, pricing, and developer experience firsthand. The discussion of self-hosting versus managed solutions addresses a common architectural decision point.

**Anyone curious about AI-assisted coding** will benefit from watching the methodology unfold. Rather than marketing claims about AI capabilities, viewers witness an authentic experiment with real obstacles and solutions, providing a nuanced understanding of current AI development tool limitations and strengths.

Finally, **developers experiencing frustration with unreliable internet services** will appreciate the validation of their concerns and the demonstration that those frustrations can transform into viable business concepts. The video validates that sometimes the best SAAS ideas come not from chasing trends, but from fixing the broken things we encounter in daily digital life.