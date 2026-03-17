#!/usr/bin/env python3
"""
Blog crawler - fetches content and creates markdown posts
Auto-updates posts.js index
"""

import os
import json
import re
import subprocess
from datetime import datetime

BLOG_DIR = "/home/openclaw/.openclaw/agents/coding/workspace/projects/personal-blog"
POSTS_DIR = f"{BLOG_DIR}/posts"
POSTS_JS = f"{BLOG_DIR}/posts.js"

def generate_slug(title):
    """Generate URL-friendly slug from title"""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug[:50]  # Limit length

def create_markdown_post(slug, title, category, content):
    """Create a markdown post file"""
    filename = f"{slug}.md"
    filepath = f"{POSTS_DIR}/{filename}"
    
    date_str = datetime.now().strftime("%B %d, %Y")
    
    frontmatter = f"""---
title: "{title}"
date: "{date_str}"
category: "{category}"
excerpt: ""
---

{content}
"""
    
    with open(filepath, 'w') as f:
        f.write(frontmatter)
    
    print(f"✓ Created: {filename}")
    return {
        "date": date_str,
        "title": title,
        "excerpt": "",
        "category": category,
        "url": f"{slug}.html",
        "slug": slug
    }

def load_posts_js():
    """Load existing posts from posts.js"""
    try:
        with open(POSTS_JS, 'r') as f:
            content = f.read()
            # Extract JSON array
            match = re.search(r'(?:var|const) posts = (\[[\s\S]*\]);?', content)
            if match:
                return json.loads(match.group(1))
    except Exception as e:
        print(f"Could not load posts.js: {e}")
    return []

def save_posts_js(posts):
    """Save posts to posts.js"""
    # Sort by date (newest first)
    posts.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    js_content = f"""// Post index - minimal metadata for cards
// Full content available in /posts/{{slug}}.md
const posts = {json.dumps(posts, indent=2)};
"""
    
    with open(POSTS_JS, 'w') as f:
        f.write(js_content)
    
    print(f"✓ Updated posts.js with {len(posts)} posts")

def crawl_sources():
    """Crawl various sources - add your sources here"""
    new_posts = []
    
    # Example: Add a manual post
    # new_posts.append(create_markdown_post(
    #     "my-new-post",
    #     "My New Post Title",
    #     "Tech",
    #     "Post content in markdown..."
    # ))
    
    return new_posts

def main():
    """Main entry point"""
    os.makedirs(POSTS_DIR, exist_ok=True)
    
    print("=== Blog Crawler ===")
    
    # Crawl for new content
    new_posts = crawl_sources()
    
    # Load existing posts
    existing_posts = load_posts_js()
    
    # Add new posts (avoid duplicates by slug)
    existing_slugs = {p.get('slug') for p in existing_posts}
    
    for post in new_posts:
        if post['slug'] not in existing_slugs:
            existing_posts.append(post)
            print(f"Added: {post['title']}")
    
    # Save updated posts
    if new_posts:
        save_posts_js(existing_posts)
    else:
        print("No new posts to add")
    
    print("=== Done ===")

if __name__ == "__main__":
    main()
