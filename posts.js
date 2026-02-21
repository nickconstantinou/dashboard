const posts = [
  { date: "February 21, 2026", category: "AI", title: "Lex Fridman: OpenClaw Podcast with Peter Steinberger", excerpt: "Lex interviews the OpenClaw creator on the viral AI agent phenomenon.", tags: ["AI", "OpenClaw", "Podcast"], url: "2026-02-21-lex-fridman-openclaw.html" },
  // February 21
  { date: "February 21, 2026", category: "AI", title: "Apple AI Wearables, Grok vs Lovable, Google I/O", excerpt: "Latest AI news: Apple enters wearables race, xAI targets Lovable, Google I/O dates announced.", tags: ["AI", "News", "Apple"], url: "2026-02-21-ai-secret-daily.html" },
  { date: "February 21, 2026", category: "AI", title: "The Smartest AI Investment Isn't NVIDIA: Toto", excerpt: "Limitless explores why Japanese toilet maker Toto might be a surprising AI winner.", tags: ["AI", "Investing", "Podcast"], url: "2026-02-21-limitless-toto-nvidia.html" },
  
  // February 20
  { date: "February 20, 2026", category: "AI", title: "MiniMax M2.5: The $1/Hour AI Model", excerpt: "80.2% on SWE-Bench, matches Opus 4.6 speed, costs $1/hour.", tags: ["AI", "Tech"], url: "2026-02-20-minimax-m2-5.html" },
  { date: "February 20, 2026", category: "AI", title: "AI Secret: The Daily AI News Source You Need", excerpt: "Discovered an AI newsletter that's better than most.", tags: ["AI", "News"], url: "2026-02-20-ai-secret-daily.html" },
  { date: "February 20, 2026", category: "Tech", title: "How AI Is Breaking the SaaS Business Model", excerpt: "Fireship breaks down why recent AI updates are crushing SaaS economics.", tags: ["AI", "SaaS"], url: "2026-02-20-ai-breaking-saas.html" },
  { date: "February 20, 2026", category: "AI", title: "Naval: On Artificial Intelligence", excerpt: "Naval's latest thinking on AI.", tags: ["AI", "Philosophy"], url: "2026-02-20-naval-on-ai.html" },
  { date: "February 20, 2026", category: "AI", title: "Head of Claude Code: What Happens After Coding Is Solved", excerpt: "Boris Cherny discusses how AI is transforming software engineering.", tags: ["AI", "Coding"], url: "2026-02-20-claude-code-future-coding.html" },
  { date: "February 20, 2026", category: "Tech", title: "NanoClaw - A Different Approach", excerpt: "Analyzing a lightweight alternative to OpenClaw.", tags: ["Tech", "AI"], url: "2026-02-20-nanoclaw-analysis.html" },
  { date: "February 20, 2026", category: "AI", title: "We Used OpenClaw for a Week", excerpt: "An honest review of using OpenClaw for a week straight.", tags: ["AI", "OpenClaw"], url: "2026-02-20-openclaw-week-honest.html" },
  { date: "February 20, 2026", category: "AI", title: "This AI Agent Made $41K in a Week!", excerpt: "How an OpenClaw agent generated real revenue.", tags: ["AI", "Agents"], url: "2026-02-20-ai-agent-41k.html" },
  
  // February 19
  { date: "February 19, 2026", category: "FPL", title: "FPL GW27 Tips & Strategy", excerpt: "Gameweek 27 analysis with captain picks.", tags: ["FPL", "Football"], url: "2026-02-19-fpl-gw27-tips.html" },
  { date: "February 19, 2026", category: "AI", title: "AI News Roundup: DeepMind's Moral AI", excerpt: "Latest developments in AI safety.", tags: ["AI", "News"], url: "2026-02-19-ai-news-roundup.html" },
  { date: "February 19, 2026", category: "AI", title: "Limitless: AI News Summary", excerpt: "Latest AI news from the Limitless podcast.", tags: ["AI", "News"], url: "2026-02-19-ai-limitless.html" },
  // February 18
  { date: "February 18, 2026", category: "AI", title: "Meta Acquires Limitless", excerpt: "What the acquisition means for the AI assistant landscape.", tags: ["AI", "News"], url: "2026-02-18-meta-acquires-limitless.html" },
  { date: "February 18, 2026", category: "Science", title: "Huberman: How Women Should Train", excerpt: "Key insights on training optimization for women.", tags: ["Science", "Training"], url: "2026-02-18-huberman-women-training.html" },
  { date: "February 18, 2026", category: "FPL", title: "FPL Captain Strategy", excerpt: "Analyzing the best captain choices.", tags: ["FPL", "Football"], url: "2026-02-18-fpl-captain-strategy.html" },
  { date: "February 18, 2026", category: "AI", title: "AI Trends 2026", excerpt: "Key trends shaping the AI landscape.", tags: ["AI", "Trends"], url: "2026-02-18-ai-trends-2026.html" },
  { date: "February 18, 2026", category: "Tech", title: "Greg Isenberg's Directory Playbook", excerpt: "How to build directory businesses.", tags: ["Business", "Marketing"], url: "2026-02-18-greg-isenberg-directory.html" },
];

// Auto-render posts when page loads
document.addEventListener('DOMContentLoaded', function() {
  const container = document.getElementById('posts-list');
  if (container && posts) {
    container.innerHTML = posts.map(post => `
      <a href="${post.url}" class="post">
        <p class="post-meta">${post.date} • ${post.category}</p>
        <h2>${post.title}</h2>
        <p>${post.excerpt}</p>
        <div class="tags">${post.tags.map(t => `<span class="tag">${t}</span>`).join('')}</div>
      </a>
    `).join('');
  }
});
