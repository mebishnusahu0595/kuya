"""
Test Advanced Kuya Features
"""

import sys
sys.path.insert(0, '/home/bishnups/Documents/PROJECT-COLLEGE')

import pandas as pd
import numpy as np
from kuya.core import KuyaDataFrame
from kuya.advanced import quick_clean, smart_analysis, auto_report

print("=" * 60)
print("🧪 TESTING ADVANCED KUYA FEATURES")
print("=" * 60)

# Create test data
np.random.seed(42)
data = {
    'Customer Name': ['John Doe', 'Jane Smith', 'Bob Johnson', None, 'Charlie Wilson'],
    'Age': [25, 30, np.nan, 45, 1000],  # Has outlier
    'City': ['New York', 'LA', 'Chicago', 'Houston', 'Phoenix'],
    'Sales': [100, 250, 75, np.nan, 180],
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Rating': [4.5, 5.0, 3.5, 4.0, np.nan]
}

df = pd.DataFrame(data)

print("\n1. Testing quick_clean()...")
try:
    cleaned_df = quick_clean(df)
    print(f"✓ quick_clean() works! Shape: {cleaned_df.shape}")
except Exception as e:
    print(f"✗ quick_clean() failed: {e}")

print("\n2. Testing smart_analysis()...")
try:
    df_test = KuyaDataFrame(df)
    insights = df_test.smart_analysis()
    print(f"✓ smart_analysis() works! Found {len(insights)} insights")
except Exception as e:
    print(f"✗ smart_analysis() failed: {e}")

print("\n3. Testing auto_report()...")
try:
    report_path = '/tmp/kuya_test_report.txt'
    auto_report(df, output_path=report_path, format='txt')
    print(f"✓ auto_report() works! Report saved to {report_path}")
except Exception as e:
    print(f"✗ auto_report() failed: {e}")

print("\n" + "=" * 60)
print("✅ ADVANCED FEATURES TEST COMPLETE!")
print("=" * 60)
