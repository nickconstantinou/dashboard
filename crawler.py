#!/usr/bin/env python3
"""
Blog crawler - fetches content from YouTube RSS and creates markdown posts
Auto-updates posts.json index with auto-categorization
"""

import os
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime

BLOG_DIR = "/home/openclaw/.openclaw/agents/coding/workspace/projects/personal-blog"
POSTS_DIR = f"{BLOG_DIR}/posts"
POSTS_JSON = f"{BLOG_DIR}/posts.json"

# Content sources
YOUTUBE_CHANNELS = [
    # Tech/AI
    {"id": "UCXgGY0wkgOzynnHvSEVmE3A", "name": "Fireship", "category": "Tech"},
    {"id": "UCxoRKax_0vHaulMbceZtAwA", "name": "My First Million", "category": "Tech/Business"},
    {"id": "UCJIfeSCssxSC_Dhc5s7woww", "name": "Lex Fridman", "category": "Tech"},
    {"id": "UCBJycsmduvYEL83R_U4JriQ", "name": "MKBHD", "category": "Tech"},
    # FPL
    {"id": "UC8043oOKTB4uP8Nq15Kz6bg", "name": "Planet FPL", "category": "FPL"},
    {"id": "UCGJ8-xqhOLwyJNuPMsVoQWQ", "name": "FPL Blackbox", "category": "FPL"},
    {"id": "UCkk58co4Qe1A1GFRPVziSGQ", "name": "Who got the assist", "category": "FPL"},
    {"id": "UCtIPFexB6PLKNNl0XH3SKKw", "name": "FPL Wire", "category": "FPL"},
    {"id": "UC72QokPHXQ9r98ROfNZmaDw", "name": "FPL Focal", "category": "FPL"},
    {"id": "UCcPWnCj5AKC19HaySZjb25g", "name": "FPL Harry", "category": "FPL"},
]

RSS_FEEDS = [
    {"url": "https://feeds.transistor.fm/technology-brother", "name": "TBPN", "category": "Tech"},
    {"url": "https://feeds.simplecast.com/dHoohVNH", "name": "Lex Fridman", "category": "Tech"},
    {"url": "https://feeds.megaphone.fm/HS2300184645", "name": "My First Million", "category": "Business"},
    {"url": "https://www.fantasyfootballscout.co.uk/feed", "name": "Fantasy Football Scout", "category": "FPL"},
]

MAX_VIDEOS_PER_CHANNEL = 2

def generate_slug(title):
    """Generate URL-friendly slug from title"""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug[:50]

def fetch_youtube_channel(channel_id, channel_name, category, max_results=2):
    """Fetch latest videos from YouTube channel RSS"""
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    
    try:
        result = subprocess.run(
            ['curl', '-s', url],
            capture_output=True, text=True, timeout=30
        )
        xml = result.stdout
        
        # Parse XML with namespace
        root = ET.fromstring(xml)
        
        # Find all entries
        entries = root.findall('.//{http://www.w3.org/2005/Atom}entry')
        
        posts = []
        for entry in entries[:max_results]:
            # Get video ID
            video_id_elem = entry.find('.//{http://www.youtube.com/xml/schemas/2015}videoId')
            video_id = video_id_elem.text if video_id_elem is not None else ''
            
            # Get title
            title_elem = entry.find('{http://www.w3.org/2005/Atom}title')
            title = title_elem.text if title_elem is not None else ''
            
            # Get published date
            published_elem = entry.find('{http://www.w3.org/2005/Atom}published')
            published = published_elem.text[:10] if published_elem is not None else ''
            
            slug = generate_slug(f"{published}-{channel_name}-{title}")
            
            posts.append({
                'date': published,
                'title': f"{title} | {channel_name}",
                'url': f"{slug}.html",
                'slug': slug,
                'category': category,
                'video_id': video_id,
                'source': 'youtube'
            })
        
        print(f"✓ {channel_name}: {len(posts)} videos")
        return posts
        
    except Exception as e:
        print(f"✗ {channel_name}: {e}")
        return []

def fetch_rss_feed(url, name, category, max_results=2):
    """Fetch latest from RSS feed"""
    try:
        result = subprocess.run(
            ['curl', '-s', url],
            capture_output=True, text=True, timeout=30
        )
        xml = result.stdout
        
        root = ET.fromstring(xml)
        entries = root.findall('.//item')
        
        posts = []
        for entry in entries[:max_results]:
            title = entry.find('title').text
            # Try to get date
            pub_date = entry.find('pubDate')
            if pub_date is not None:
                # Parse RFC 2822 date
                from email.utils import parsedate_to_datetime
                try:
                    dt = parsedate_to_datetime(pub_date.text)
                    date = dt.strftime('%Y-%m-%d')
                except:
                    date = datetime.now().strftime('%Y-%m-%d')
            else:
                date = datetime.now().strftime('%Y-%m-%d')
            
            slug = generate_slug(f"{date}-{name}-{title}")
            
            posts.append({
                'date': date,
                'title': f"{title} | {name}",
                'url': f"{slug}.html",
                'slug': slug,
                'category': category,
                'source': 'rss'
            })
        
        print(f"✓ {name}: {len(posts)} posts")
        return posts
        
    except Exception as e:
        print(f"✗ {name}: {e}")
        return []

def crawl_sources():
    """Crawl all sources"""
    new_posts = []
    
    print("=== Crawling YouTube ===")
    for ch in YOUTUBE_CHANNELS:
        posts = fetch_youtube_channel(ch['id'], ch['name'], ch['category'], MAX_VIDEOS_PER_CHANNEL)
        new_posts.extend(posts)
    
    print("\n=== Crawling RSS ===")
    for feed in RSS_FEEDS:
        posts = fetch_rss_feed(feed['url'], feed['name'], feed['category'], MAX_VIDEOS_PER_CHANNEL)
        new_posts.extend(posts)
    
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

def load_posts_json():
    """Load existing posts"""
    try:
        with open(POSTS_JSON, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Could not load posts.json: {e}")
    return []

def save_posts_json(posts):
    """Save posts to JSON"""
    posts.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    with open(POSTS_JSON, 'w') as f:
        json.dump(posts, f, indent=2)

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
            post['category'] = auto_categorize(post['title'])
            existing_posts.append(post)
            print(f"Added: {post['title'][:50]}...")
    
    # Re-categorize all posts
    for post in existing_posts:
        post['category'] = auto_categorize(post.get('title', ''))
    
    # Save updated posts
    if new_posts:
        save_posts_json(existing_posts)
        print(f"\n✓ Total posts: {len(existing_posts)}")
    else:
        print("No new posts to add")
    
    print("=== Done ===")

if __name__ == "__main__":
    main()
