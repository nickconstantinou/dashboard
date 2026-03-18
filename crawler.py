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

def load_posts_json():
    """Load existing posts from posts.json"""
    try:
        with open('posts.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Could not load posts.json: {e}")
    return []

def save_posts_json(posts):
    """Save posts to posts.json"""
    # Sort by date (newest first)
    posts.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=2)
    
    print(f"✓ Updated posts.js with {len(posts)} posts")

def crawl_sources():
    """Crawl various sources - add your sources here"""
    new_posts = []
    
    # Test post - demonstrates the system works
    new_posts.append(create_markdown_post(
        "test-post-ada",
        "Testing the New Blog Architecture",
        "Tech",
        """# Testing the New Blog Architecture

This is a test post to verify the markdown blog system is working correctly.

## What Changed

1. Posts are now stored as markdown files
2. Index is minimal JSON
3. Clicking a post loads markdown dynamically

## How It Works

- `posts.js` contains the index (title, date, slug)
- `posts/*.md` contains the full content
- JavaScript fetches and renders markdown on click

## Next Steps

Add real content sources to the crawler!
"""
    ))
    
    return new_posts

def auto_categorize(title):
    """Auto-categorize based on title keywords"""
    title = title.lower()
    
    if 'fpl' in title or 'fantasy' in title or 'captain' in title or 'gw' in title:
        return 'FPL'
    elif 'ai' in title or 'tech' in title or 'claude' in title or 'coding' in title or 'software' in title or 'nvidia' in title or 'google' in title or 'openai' in title:
        return 'Tech'
    elif 'business' in title or 'startup' in title or 'money' in title or 'million' in title or 'invest' in title:
        return 'Business'
    elif 'sport' in title or 'training' in title or 'workout' in title or 'health' in title:
        return 'Sports'
    else:
        return 'Blog'

def main():
    """Main entry point"""
    os.makedirs(POSTS_DIR, exist_ok=True)
    
    print("=== Blog Crawler ===")
    
    # Crawl for new content
    new_posts = crawl_sources()
    
    # Load existing posts
    existing_posts = load_posts_json()
    
    # Add new posts (avoid duplicates by slug)
    existing_slugs = {p.get('slug') for p in existing_posts}
    
    for post in new_posts:
        if post['slug'] not in existing_slugs:
            # Auto-categorize new posts
            if 'category' not in post:
                post['category'] = auto_categorize(post['title'])
            existing_posts.append(post)
            print(f"Added: {post['title']}")
    
    # Re-categorize all posts (in case title keywords changed)
    for post in existing_posts:
        post['category'] = auto_categorize(post.get('title', ''))
    
    # Save updated posts
    if new_posts:
        save_posts_json(existing_posts)
    else:
        print("No new posts to add")
    
    print("=== Done ===")

if __name__ == "__main__":
    main()
