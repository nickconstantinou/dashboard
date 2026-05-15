---
title: I built my own wordpress with Astro and CloudCannon
date: '2026-05-15'
type: youtube
category: Tech
channel: Fireship
video_url: https://www.youtube.com/watch?v=A8pzHn0i5PA
video_id: A8pzHn0i5PA
---

# Building a WordPress Alternative with Astro and CloudCannon: A Complete Guide

**Title: I built my own WordPress with Astro and CloudCannon**

---

## Key Insights

- **[10:04]** Astro is positioned as a JavaScript web framework optimized for content-driven websites, capable of serving as a full WordPress replacement while allowing clients to edit content visually without writing code

- **[20:07]** Astro ships zero JavaScript by default, implementing "Astro Island" architecture where JavaScript loads only where specifically needed (e.g., add-to-cart buttons) — unlike Next.js or Gatsby which ship JavaScript throughout

- **[30:11]** Core Web Vitals performance shows Astro ranking "astronomically high" compared to Next.js, Gatsby, and WordPress, with enterprise adoption by Google, Unilever, Cloudflare, Netlify, and OpenAI

- **[40:15]** CloudCannon provides a visual editor interface where non-technical clients can modify pages and blogs directly, including titles, descriptions, images, drafts, tags, alt image text, and component visibility toggles

- **[50:18]** The developer-client workflow creates a bidirectional sync: client visual edits commit to Git as code changes, while developer code changes reflect in the visual editor simultaneously

---

## Introduction

In a time when website builders and content management systems dominate the web development landscape, a surprising challenger has emerged that promises to deliver WordPress-level functionality without sacrificing the developer experience that technical teams crave. In this comprehensive tutorial, content creator Hitesh walks viewers through an innovative approach to building content-driven websites using Astro — a JavaScript framework that has quietly been adopted by some of the world's largest technology companies — paired with CloudCannon's visual editing capabilities.

The premise is deceptively simple: what if you could give clients the intuitive, what-you-see-is-what-you-get editing experience they demand while keeping developers firmly in control of the codebase through traditional Git workflows? This video addresses a fundamental tension that has plagued web development for years — the disconnect between what clients want (visual control over their content) and what developers prefer (code-centric management with version control). Hitesh demonstrates that this perceived trade-off is actually a false dichotomy, and that both needs can be elegantly satisfied through the strategic combination of Astro's island architecture and CloudCannon's visual editing platform.

The video promises to be "one of the most fun" tutorials viewers will encounter, with Hitesh emphasizing that despite the seemingly complex technology involved, everything will remain code-centric. "Developers love to write code," he explains, "but client doesn't understand code. They want still prefer the WYSIWYG editor." This tutorial bridges that gap completely.

---

## Understanding Astro: Beyond the Basics

### What Makes Astro Different

Astro describes itself as "a web framework for content-driven websites," but this simple description barely scratches the surface of what the framework actually delivers. Hitesh takes viewers through the Astro website, demonstrating that the framework has been adopted by major enterprises including Google, Unilever, Cloudflare, Netlify, and OpenAI — companies that typically have exacting standards for the tools they integrate into their technology stacks.

The framework's primary differentiator lies in its performance philosophy. Unlike React-based frameworks such as Next.js, which ship JavaScript to the browser by default, Astro operates on a radically different principle: by default, Astro ships literally zero JavaScript to the client. This approach, which Hitesh describes as "astro island" architecture, represents a fundamental rethinking of how web applications should deliver content.

The island metaphor is particularly apt. Imagine a vast ocean of static HTML — fast-loading, cacheable, and requiring no runtime processing — punctuated by isolated islands of interactivity where JavaScript is actually needed. On an e-commerce website, for instance, the homepage of a product listing might require no JavaScript whatsoever since it displays the same content to every visitor. Even when a user clicks through to view a specific product, most of that page remains static. Only specific elements — the add-to-cart button, the buy-now functionality, interactive image galleries — actually require JavaScript to function. Astro's architecture identifies these islands automatically and loads JavaScript only for those specific components, resulting in dramatically faster page loads and superior Core Web Vitals scores.

### Performance That Speaks for Itself

Hitesh walks viewers through performance comparisons that paint a compelling picture. The data shows Astro achieving rankings that he describes as "astronomically high" compared to established players like Next.js, Gatsby, and WordPress. This isn't merely marketing hyperbole — the framework has been independently benchmarked and consistently delivers superior results in real-world scenarios.

The implications for marketing websites are particularly significant. Hitesh makes a crucial observation that many development teams overlook: "Please keep your marketing website separate from your application website. Your marketing team needs fast iteration, visual editors, and all these things." Marketing teams operate on different timelines than software developers, often needing to make rapid changes to website copy, colors, or layouts for A/B testing or campaign adjustments. When marketing must file tickets with development for every minor change, the organization loses agility. Astro, combined with CloudCannon, solves this organizational problem by giving marketing teams direct control over their content without sacrificing the performance benefits that technical teams demand.

### Content-Driven Website Examples

To help viewers understand what qualifies as a "content-driven website," Hitesh provides concrete examples beyond the obvious blog and documentation scenarios. Property listing websites, he explains, are primarily content-driven — their content remains largely static while only occasional new listings are added. Listing websites in general, even without the real estate focus, tend to be more static than dynamic. Even e-commerce sites, which many developers would classify as highly dynamic, are "majorly static" according to Hitesh, with most of the content (product descriptions, images, specifications) remaining constant across user sessions. Only specific interactive elements like shopping cart functionality and checkout flows require dynamic JavaScript processing.

---

## The Developer-Client Workflow Revolution

### How CloudCannon Transforms the Editing Experience

The true power of the Astro and CloudCannon combination emerges when Hitesh demonstrates the actual editing interface. The visual editor provided by CloudCannon allows non-technical users to modify website content through a familiar WYSIWYG interface — the same kind of editing experience that made WordPress the dominant force in content management. Users can move their cursor anywhere on the page and modify text directly, with changes reflected immediately in the preview.

The interface extends far beyond simple text editing. On the left-hand side of the editor, users gain access to metadata controls including titles, descriptions, images, draft status, tags, and alt image text — essentially every piece of structured content that developers would typically manage through front matter or database entries. Hitesh demonstrates editing blog posts, showing how users can navigate to any blog, access the visual editor, and modify any aspect of the content without touching a single line of code.

What makes this particularly powerful is the ability to edit not just blog posts, but regular pages throughout the website. Hitesh navigates to an "about" page within the demo and demonstrates how every component on that page — text elements, images, buttons, team information — remains fully editable through the visual interface. Even the visibility of components can be toggled, allowing clients to show or hide specific elements without requiring developer intervention.

### The Bidirectional Sync Magic

Perhaps the most elegant aspect of this workflow is the synchronization between developer code and client edits. Hitesh explains that when clients make changes through the visual editor, those modifications automatically commit to the Git repository as code changes. This means the codebase always reflects the current state of the website, and developers can review, modify, or revert client changes through standard Git workflows.

Conversely, when developers push code changes to the repository, those modifications immediately appear in the visual editor. This bidirectional synchronization creates a seamless workflow where neither party needs to worry about their changes overwriting or conflicting with the other's work. The system handles the technical complexity of keeping these two paradigms in harmony, allowing each team to work in their preferred environment.

This approach resolves one of the most persistent tensions in web development: the desire for visual editing versus the need for code-based control. "Whatever the client updates, that goes in our code," Hitesh explains, "whatever we update as the code goes to the client." Both parties benefit from this arrangement — developers maintain the control and predictability they need, while clients receive the intuitive editing experience they prefer.

---

## Building the WordPress Equivalent

### What Can Be Achieved

Hitesh doesn't shy away from making bold claims about what viewers can build using this technology. "You can actually go ahead and build almost like a WordPress equivalent website with just Astro," he states definitively. The implications are significant: by leveraging Astro's performance characteristics and CloudCannon's editing capabilities, developers can create websites that match or exceed WordPress's usability for content editors while delivering vastly superior performance characteristics.

The video includes a complete code repository available for free in the description, allowing viewers to build upon Hitesh's foundation rather than starting from scratch. This repository demonstrates not only the technical implementation but also the organizational patterns that make this workflow successful in practice. Based on this foundation, viewers can build various types of websites — from simple marketing sites to complex e-commerce platforms with full WordPress-level functionality.

### Setup and Getting Started

The tutorial begins with the familiar `npm create Astro` command that most JavaScript developers will recognize from their experience with other frameworks. Hitesh walks through the setup process, demonstrating that Astro's developer experience follows established conventions rather than requiring teams to learn entirely new workflows. This approachability is intentional — Astro is designed to be accessible to developers who already know React, Vue, or other JavaScript frameworks, allowing teams to leverage existing skills rather than requiring extensive retraining.

The framework allows developers to use their existing knowledge of React, Vue, and other popular frameworks directly within Astro components, meaning the transition for teams already working with these technologies is relatively frictionless. A developer comfortable with React can write React components within an Astro project and deploy them with the same confidence they'd have in a pure React application.

---

## Detailed Takeaways

**Understanding the Island Architecture Philosophy**

Astro's approach to web development represents a philosophical shift from the "hydrate everything" mentality that has dominated JavaScript frameworks. By shipping zero JavaScript by default and loading it only for specific interactive components, Astro forces developers to be intentional about where client-side processing is actually needed. This mindset leads to better-performing websites and more thoughtful architecture decisions. For developers coming from React backgrounds where JavaScript is omnipresent, this requires unlearning certain habits, but the performance benefits make the adjustment worthwhile.

**Separating Marketing and Application Concerns**

Hitesh's observation about keeping marketing websites separate from application websites addresses an organizational problem that often gets overlooked in technical discussions. Marketing teams and development teams have fundamentally different needs, timelines, and skill sets. Marketing requires rapid iteration and visual control; development requires stability, predictability, and code-based workflows. By choosing tools that serve each team's needs appropriately, organizations can avoid the bottlenecks that occur when marketing must wait for development tickets to be processed simply to change a button color or update a headline.

**The Power of Visual Editing for Clients**

Not every client has the technical sophistication to work with code, and forcing them to do so often leads to frustration, mistakes, or expensive developer time for simple tasks. CloudCannon's visual editor bridges this gap by providing a familiar editing experience — the same kind of interface that made WordPress so popular among non-technical users. By giving clients direct control over their content, organizations free developers to focus on features and improvements rather than content updates.

**Git-Based Workflows Provide Safety and Accountability**

When client edits commit directly to Git alongside developer changes, the entire history of the website becomes traceable and reversible. If a client makes an unwanted change, it can be identified and reverted through standard Git workflows. If a developer introduces a regression, the same mechanisms apply. This auditability provides peace of mind for both parties and creates a clear chain of custody for every modification to the website.

**Performance Is Non-Negotiable for Modern Websites**

Google's emphasis on Core Web Vitals as a ranking factor has made page performance a business-critical concern rather than merely a technical nicety. Astro's architectural approach to shipping zero JavaScript by default creates websites that load faster, rank higher, and provide better user experiences than JavaScript-heavy alternatives. For content-driven websites where the content rarely changes, this performance advantage compounds over time as more content accumulates.

---

## Who This Is For

This tutorial serves developers and technical decision-makers who need to build content-driven websites while satisfying client demands for visual editing capabilities. Freelance web developers working with non-technical clients will find particular value in this approach, as it reduces the support burden of handling content update requests. Development agencies building marketing websites or content platforms for clients benefit from giving those clients direct control over their content without sacrificing code quality or performance.

Technical leads evaluating frameworks for marketing websites should pay close attention to Astro's performance characteristics and the CloudCannon integration. Organizations struggling with the tension between developer workflows and marketing team autonomy will find the bidirectional sync between code and visual editing particularly compelling.

For developers already working with React, Vue, or similar frameworks, Astro offers an accessible entry point into the island architecture paradigm. The ability to use existing component knowledge within Astro projects means teams can adopt this technology incrementally without requiring a complete rewrite of their component libraries.

Even for developers who don't anticipate needing client-facing visual editing, understanding Astro's approach to performance optimization provides valuable perspective on building faster, more efficient websites regardless of the framework ultimately chosen.