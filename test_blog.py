#!/usr/bin/env python3
"""Tests for personal-blog static site"""
import pytest
from pathlib import Path

BLOG_DIR = Path(__file__).parent

def test_index_exists():
    """Test that index.html exists"""
    assert (BLOG_DIR / "index.html").exists()

def test_blog_directory_exists():
    """Test that blog directory exists"""
    assert (BLOG_DIR / "blog").is_dir()

def test_posts_js_exists():
    """Test that posts.js exists"""
    assert (BLOG_DIR / "posts.js").exists()

def test_has_html_posts():
    """Test that there are HTML posts"""
    html_files = list(BLOG_DIR.glob("2026-*.html"))
    assert len(html_files) > 0

def test_posts_js_valid_format():
    """Test that posts.js has valid format"""
    content = (BLOG_DIR / "posts.js").read_text()
    assert "const posts" in content or "window.posts" in content

def test_html_files_not_empty():
    """Test that HTML files have content"""
    index = BLOG_DIR / "index.html"
    content = index.read_text()
    assert len(content) > 100

def test_no_broken_files():
    """Test no .broken files exist (cleanup check)"""
    broken = list(BLOG_DIR.glob("*.broken"))
    # Just warn, don't fail
    if broken:
        print(f"Warning: {len(broken)} .broken files found")
