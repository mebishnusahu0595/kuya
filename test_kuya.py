"""
Quick Test Script for Kuya
Run this to verify your Kuya installation works correctly.
"""

import sys
sys.path.insert(0, '/home/bishnups/Documents/PROJECT-COLLEGE')

print("=" * 60)
print("🧪 KUYA QUICK TEST")
print("=" * 60)

try:
    print("\n1. Testing imports...")
    import kuya as ky
    from kuya.core import KuyaDataFrame
    from kuya.clean import KuyaCleaner
    from kuya.eda import KuyaEDA
    from kuya.viz import KuyaViz
    from kuya.io import load, save
    print("   ✓ All imports successful!")

    print("\n2. Testing KuyaDataFrame creation...")
    import pandas as pd
    data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    df = KuyaDataFrame(data)
    print(f"   ✓ Created KuyaDataFrame with shape {df.shape}")

    print("\n3. Testing clean methods...")
    df = df.standardize_columns()
    print("   ✓ standardize_columns() works!")

    print("\n4. Testing EDA methods...")
    df.check_missing()
    print("   ✓ check_missing() works!")

    print("\n5. Testing I/O...")
    import tempfile
    import os
    with tempfile.TemporaryDirectory() as tmpdir:
        test_path = os.path.join(tmpdir, 'test.csv')
        ky.save(df, test_path)
        df_loaded = ky.load(test_path)
        print(f"   ✓ save() and load() work! Loaded shape: {df_loaded.shape}")

    print("\n" + "=" * 60)
    print("✅ ALL TESTS PASSED!")
    print("Kuya is installed and working correctly!")
    print("=" * 60)

except Exception as e:
    print("\n" + "=" * 60)
    print("❌ TEST FAILED!")
    print(f"Error: {str(e)}")
    print("=" * 60)
    import traceback
    traceback.print_exc()
