#!/bin/bash
# Daily content crawler for Nick's personal blog
# Run at 7am daily

BLOG_DIR="/home/openclaw/openclaw-workspace/personal-blog"
DATE=$(date +%Y-%m-%d)

echo "=== Daily Content Crawl - $DATE ==="

# Source URLs to fetch
SOURCES=(
  "https://www.limitless.ai/featured"
  "https://therundown.ai"
  "https://news.ycombinator.com"
)

# Fetch and summarize each source
for url in "${SOURCES[@]}"; do
  echo "Fetching: $url"
  content=$(curl -s "https://r.jina.ai/$url" 2>/dev/null)
  
  if [ -n "$content" ]; then
    echo "✓ Got content from $url"
  else
    echo "✗ Failed: $url"
  fi
done

# Create daily summary
cat > "$BLOG_DIR/$DATE-daily-digest.html" << EOF
---
title: Daily Digest - $DATE
date: $DATE
---

# Daily Digest - $DATE

## AI News

## FPL Updates

## What's New

EOF

echo "=== Crawl complete ==="
echo "Created: $DATE-daily-digest.html"
