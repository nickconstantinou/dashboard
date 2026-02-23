const posts = [
  {
    "date": "February 23, 2026",
    "category": "Test",
    "title": "Test Post from Crawler",
    "excerpt": "This is a test post from the new content crawler",
    "tags": [
      "Test"
    ],
    "url": "2026-02-23-test.html"
  },
  {
    "date": "February 23, 2026",
    "category": "Tech",
    "title": "Tech Roundup",
    "excerpt": "Latest Tech videos",
    "tags": [
      "Tech"
    ],
    "url": "2026-02-23-tech-roundup.html"
  },
  {
    "date": "February 23, 2026",
    "category": "Tech",
    "title": "I Built a Vibe Translator - AI Battle",
    "excerpt": "Testing the content crawler end-to-end",
    "tags": [
      "Tech"
    ],
    "url": "2026-02-23-i-built-a-vibe-translator-one-idea-4-frontend-stac.html"
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
