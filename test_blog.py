#!/usr/bin/env python3
""": Automated GitHub Actions test for personal-blog HTML validation"""
import os
import re
from pathlib import Path

def test_html_files():
    """Validate all HTML files in directory"""
    html_files = Path('.').glob('*.html')
    
    for html_file in html_files:
        content = html_file.read_text()
        
        # Test 1: Basic HTML structure
        assert '<!DOCTYPE html>' in content or '<html' in content, f"{html_file}: Invalid HTML structure"
        
        # Test 2: Title exists
        assert '<title>' in content, f"{html_file}: Missing title"
        
        # Test 3: UTF-8 encoding
        assert 'UTF-8' in content, f"{html_file}: Missing UTF-8 declaration"
        
        # Test 4: Semi-reasonable content length (not empty)
        assert len(content) > 500, f"{html_file}: Too short (empty?)"
        
        print(f"✅ {html_file} validated")

def test_repo_structure():
    """Test basic repository structure"""
    assert Path('index.html').exists(), "Missing index.html"
    assert Path('.github/workflows').exists(), "Missing CI workflow"

if __name__ == "__main__":
    test_repo_structure()
    test_html_files()
    print("🚀 All validations passed!")