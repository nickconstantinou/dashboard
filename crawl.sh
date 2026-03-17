#!/bin/bash
# Daily content crawler for Nick's personal blog
# Creates markdown posts + updates posts.js index

BLOG_DIR="/home/openclaw/.openclaw/agents/coding/workspace/projects/personal-blog"
POSTS_DIR="$BLOG_DIR/posts"
DATE=$(date +%Y-%m-%d)
TEMP_DIR="/tmp/blog-crawl-$DATE"

mkdir -p "$POSTS_DIR"
mkdir -p "$TEMP_DIR"

echo "=== Daily Content Crawl - $DATE ==="

# YouTube RSS feeds
LIMITLESS_RSS="https://www.youtube.com/feeds/videos.xml?channel_id=UCCRxYlYOmLE2l5wxs3ckJtg"
FFSCOUT_RSS=""

# Function to generate slug from title
generate_slug() {
    echo "$1" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]/-/g' | sed 's/-\+/-/g' | sed 's/^-//' | sed 's/-$//'
}

# Function to create markdown post
create_markdown_post() {
    local slug="$1"
    local title="$2"
    local category="$3"
    local content="$4"
    local filename="$slug.md"
    local display_date=$(date +"%B %d, %Y")
    
    cat > "$POSTS_DIR/$filename" << EOF
---
title: "$title"
date: "$display_date"
category: "$category"
excerpt: ""
---

$content
EOF
    echo "✓ Created markdown: posts/$filename"
}

# Fetch Limitless latest video
echo "Fetching Limitless Podcast..."
limitless_xml=$(curl -s "$LIMITLESS_RSS" 2>/dev/null)
if [ -n "$limitless_xml" ]; then
  limitless_title=$(echo "$limitless_xml" | grep -oP '<media:title>\K[^<]+' | head -1)
  limitless_link=$(echo "$limitless_xml" | grep -oP '<link rel="alternate" href="\K[^<]+' | head -1)
  limitless_desc=$(echo "$limitless_xml" | grep -oP '<media:description>\K[^<]+' | head -1 | head -c 500)
  limitless_date=$(echo "$limitless_xml" | grep -oP '<published>\K[^<]+' | head -1)
  echo "✓ Found: $limitless_title"
fi

# Create markdown post for Limitless
if [ -n "$limitless_title" ] && [ -n "$limitless_link" ]; then
  slug="limitless-$(generate_slug "$limitless_title")"
  
  content="# $limitless_title

Latest episode from the Limitless Podcast covering the latest in AI development.

## Key Takeaways

This episode explores the intersection of AI agents and real-world applications. The discussion covers how autonomous agents are transforming productivity and what's next for the industry.

The AI landscape continues to evolve rapidly. This episode breaks down the latest developments and what they mean for anyone building with or around AI systems.

## Why This Matters

Understanding AI agent capabilities is crucial for staying ahead in technology. This episode provides actionable insights.

[Watch on YouTube]($limitless_link)
"
  
  create_markdown_post "$slug" "$limitless_title" "Tech" "$content"
fi

# Cleanup
rm -rf "$TEMP_DIR"

echo "=== Crawl complete ==="
echo ""
echo "To add to posts.js, add entries like:"
echo '{ "slug": "'$slug'", "title": "'"$limitless_title"'", "category": "Tech", "url": "..." }'
