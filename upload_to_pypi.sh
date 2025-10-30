#!/bin/bash

# 🚀 Kuya Package Upload Script
# This script helps you upload your package to PyPI

set -e  # Exit on error

echo "🎨 Kuya Package Upload Tool"
echo "=============================="
echo ""

# Check if in correct directory
if [ ! -f "setup.py" ]; then
    echo "❌ Error: setup.py not found. Are you in the project directory?"
    exit 1
fi

# Activate virtual environment
if [ ! -d "venv" ]; then
    echo "❌ Error: Virtual environment not found"
    exit 1
fi

echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Check if dist/ exists
if [ ! -d "dist" ]; then
    echo "⚠️  dist/ directory not found. Building packages..."
    python -m build
fi

echo ""
echo "📦 Available packages in dist/:"
ls -lh dist/
echo ""

# Menu
echo "Choose upload destination:"
echo "1) Test PyPI (recommended for first upload)"
echo "2) Production PyPI"
echo "3) Check packages only (no upload)"
echo "4) Clean and rebuild"
echo "5) Exit"
echo ""

read -p "Enter choice [1-5]: " choice

case $choice in
    1)
        echo ""
        echo "🧪 Uploading to Test PyPI..."
        echo "You'll need your Test PyPI API token"
        echo "Get it from: https://test.pypi.org/manage/account/token/"
        echo ""
        twine upload --repository testpypi dist/*
        echo ""
        echo "✅ Upload complete!"
        echo ""
        echo "Test installation with:"
        echo "pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple kuya-data"
        ;;
    
    2)
        echo ""
        echo "🚀 Uploading to Production PyPI..."
        echo "You'll need your PyPI API token"
        echo "Get it from: https://pypi.org/manage/account/token/"
        echo ""
        read -p "Are you sure? This can't be undone! (yes/no): " confirm
        if [ "$confirm" = "yes" ]; then
            twine upload dist/*
            echo ""
            echo "🎉 Upload complete! Your package is now live!"
            echo ""
            echo "Install it with:"
            echo "pip install kuya-data"
            echo ""
            echo "View it at:"
            echo "https://pypi.org/project/kuya-data/"
        else
            echo "❌ Upload cancelled"
        fi
        ;;
    
    3)
        echo ""
        echo "🔍 Checking packages..."
        twine check dist/*
        echo ""
        echo "✅ Package validation complete!"
        ;;
    
    4)
        echo ""
        echo "🧹 Cleaning old builds..."
        rm -rf dist/ build/ *.egg-info kuya_data.egg-info
        echo "✅ Cleaned!"
        echo ""
        echo "📦 Building new packages..."
        python -m build
        echo ""
        echo "✅ Build complete!"
        twine check dist/*
        ;;
    
    5)
        echo "👋 Goodbye!"
        exit 0
        ;;
    
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "=============================="
echo "Done! 🎉"
