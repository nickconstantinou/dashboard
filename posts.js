const posts = [
  {
    "date": "February 20, 2026",
    "category": "AI",
    "title": "MiniMax M2.5: The $1/Hour AI Model",
    "excerpt": "80.2% on SWE-Bench, matches Opus 4.6 speed, costs $1/hour.",
    "tags": ["AI", "Tech"],
    "url": "2026-02-20-minimax-m2-5.html"
  },
  {
    "date": "February 20, 2026",
    "category": "AI",
    "title": "AI Secret: The Daily AI News Source You Need",
    "excerpt": "Discovered an AI newsletter that's better than most.",
    "tags": ["AI", "News"],
    "url": "2026-02-20-ai-secret-daily.html"
  },
  {
    "date": "February 20, 2026",
    "category": "Tech",
    "title": "How AI Is Breaking the SaaS Business Model",
    "excerpt": "Fireship breaks down why recent AI updates are crushing SaaS economics.",
    "tags": ["AI", "SaaS"],
    "url": "2026-02-20-ai-breaking-saas.html"
  },
  {
    "date": "February 20, 2026",
    "category": "AI",
    "title": "Naval: On Artificial Intelligence",
    "excerpt": "Naval's latest thinking on AI—from vibe coding to the English programming language.",
    "tags": ["AI", "Philosophy"],
    "url": "2026-02-20-naval-on-ai.html"
  },
  {
    "date": "February 20, 2026",
    "category": "AI",
    "title": "Head of Claude Code: What Happens After Coding Is Solved",
    "excerpt": "Boris Cherny discusses how AI is transforming software engineering.",
    "tags": ["AI", "Coding"],
    "url": "2026-02-20-claude-code-future-coding.html"
  },
  {
    "date": "February 20, 2026",
    "category": "Tech",
    "title": "NanoClaw - A Different Approach",
    "excerpt": "Analyzing a lightweight alternative to OpenClaw.",
    "tags": ["Tech", "AI"],
    "url": "2026-02-20-nanoclaw-analysis.html"
  },
  {
    "date": "February 20, 2026",
    "category": "AI",
    "title": "We Used OpenClaw for a Week",
    "excerpt": "An honest review of using OpenClaw for a week straight.",
    "tags": ["AI", "OpenClaw"],
    "url": "2026-02-20-openclaw-week-honest.html"
  },
  {
    "date": "February 19, 2026",
    "category": "AI",
    "title": "AI News Roundup",
    "excerpt": "The latest AI developments from the past week.",
    "tags": ["AI", "News"],
    "url": "2026-02-19-ai-news-roundup.html"
  },
  {
    "date": "February 18, 2026",
    "category": "Tech",
    "title": "Greg Isenberg's Directory Playbook",
    "excerpt": "How to build directory businesses that compound.",
    "tags": ["Business", "Marketing"],
    "url": "2026-02-18-greg-isenberg-directory.html"
  }
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
