# 🚀 Publishing Kuya to PyPI

## What You Need

1. **PyPI Account** - Create accounts on:
   - Test PyPI: https://test.pypi.org/account/register/
   - PyPI: https://pypi.org/account/register/

2. **Build Tools** - Install required packages:
```bash
pip install build twine
```

---

## 📋 Pre-Publishing Checklist

✅ All tests pass
✅ Documentation complete
✅ README.md ready
✅ LICENSE file included
✅ Version number set
✅ Dependencies listed

---

## 🔧 Step-by-Step Publishing Guide

### Step 1: Install Build Tools
```bash
source venv/bin/activate
pip install --upgrade build twine
```

### Step 2: Build Distribution Files
```bash
cd /home/bishnups/Documents/PROJECT-COLLEGE
python -m build
```

This creates:
- `dist/kuya-0.1.0.tar.gz` (source distribution)
- `dist/kuya-0.1.0-py3-none-any.whl` (wheel distribution)

### Step 3: Test on Test PyPI (Recommended First!)
```bash
# Upload to Test PyPI
python -m twine upload --repository testpypi dist/*

# You'll be prompted for:
# Username: (your Test PyPI username)
# Password: (your Test PyPI password or token)
```

### Step 4: Test Installation from Test PyPI
```bash
# Create a new test environment
python3 -m venv test_env
source test_env/bin/activate

# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ kuya

# Test it
python -c "import kuya as ky; print('Success!')"
```

### Step 5: Upload to Real PyPI
```bash
# Once testing passes, upload to real PyPI
python -m twine upload dist/*

# Enter your PyPI credentials
```

### Step 6: Verify Installation
```bash
# Anyone can now install with:
pip install kuya

# Test it works
python -c "import kuya as ky; print('Kuya installed from PyPI!')"
```

---

## 🔐 Using API Tokens (Recommended)

Instead of passwords, use API tokens for security:

### For Test PyPI:
1. Go to https://test.pypi.org/manage/account/token/
2. Create a new API token
3. Create `~/.pypirc`:
```ini
[testpypi]
  username = __token__
  password = pypi-AgEIcHlwaS5vcmc...  # Your token
```

### For Real PyPI:
1. Go to https://pypi.org/manage/account/token/
2. Create a new API token
3. Add to `~/.pypirc`:
```ini
[pypi]
  username = __token__
  password = pypi-AgEIcHlwaS5vcmc...  # Your token
```

---

## 📝 Quick Commands Summary

```bash
# 1. Install tools
pip install --upgrade build twine

# 2. Build package
python -m build

# 3. Upload to Test PyPI (test first!)
twine upload --repository testpypi dist/*

# 4. Upload to PyPI (production)
twine upload dist/*
```

---

## 🎯 After Publishing

Once published, users can install Kuya with:

```bash
pip install kuya
```

And use it immediately:

```python
import kuya as ky

df = ky.load('data.csv')
df = ky.quick_clean(df)
df.smart_analysis()
```

---

## 🔄 Updating Kuya

When you make changes:

1. Update version in `setup.py`
2. Rebuild: `python -m build`
3. Upload new version: `twine upload dist/*`

---

## ⚠️ Important Notes

1. **Package Name** - `kuya` must be available on PyPI
   - Check: https://pypi.org/project/kuya/
   - If taken, choose another name (e.g., `kuya-data`, `kuya-analysis`)

2. **Version Numbers** - Follow semantic versioning:
   - `0.1.0` - Initial release
   - `0.1.1` - Bug fixes
   - `0.2.0` - New features
   - `1.0.0` - Stable release

3. **Cannot Delete** - Once uploaded, you can't delete versions
   - Test thoroughly on Test PyPI first!

4. **Documentation** - PyPI will use your README.md
   - Make sure it's formatted well
   - Include installation instructions

---

## 🚀 Let's Publish!

Ready to publish? Follow these commands:

```bash
cd /home/bishnups/Documents/PROJECT-COLLEGE
source venv/bin/activate

# Install build tools
pip install --upgrade build twine

# Build the package
python -m build

# Upload to Test PyPI first
twine upload --repository testpypi dist/*

# If successful, upload to real PyPI
twine upload dist/*
```

---

## 🎉 Success!

After publishing, Kuya will be available at:
- **PyPI Page:** https://pypi.org/project/kuya/
- **Installation:** `pip install kuya`
- **Anyone** in the world can now use Kuya!

---

## 📊 Monitoring

After publishing, you can:
- View download statistics
- See user feedback
- Monitor issues
- Update as needed

Your project is now part of the Python ecosystem! 🌟
