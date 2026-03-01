#!/bin/bash
# Pre-commit hook for personal-blog
echo "🧪 Running tests..."

pytest test_blog.py -v --tb=short

if [ $? -ne 0 ]; then
    echo "❌ Tests failed!"
    exit 1
fi

echo "✅ Tests passed!"
exit 0
