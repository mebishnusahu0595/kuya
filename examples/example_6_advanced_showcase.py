"""
Example 6: Advanced Features Showcase
Demonstrates Kuya's extraordinary advanced capabilities.
"""

import sys
sys.path.insert(0, '/home/bishnups/Documents/PROJECT-COLLEGE')

import pandas as pd
import numpy as np
import kuya as ky
from kuya.core import KuyaDataFrame

print("=" * 70)
print("        ✨ KUYA ADVANCED FEATURES SHOWCASE ✨")
print("=" * 70)

# Create a realistic messy dataset
np.random.seed(42)

data = {
    'Customer ID': range(1001, 1101),
    'Customer Name': [f'Customer {i}' for i in range(100)],
    'Age': np.concatenate([np.random.randint(18, 70, 95), [150, 200, 5, 180, 190]]).astype(float),  # Has outliers
    'City': np.random.choice(['New York', 'LA', 'Chicago', 'Houston', 'Phoenix'], 100),
    'Product Category': np.random.choice(['Electronics', 'Clothing', 'Home'], 100),
    'Purchase Amount': np.random.uniform(50, 1000, 100),
    'Quantity': np.random.randint(1, 10, 100),
    'Customer Rating': np.random.uniform(1, 5, 100),
    'Member Since': pd.date_range(start='2020-01-01', periods=100, freq='W'),
}

# Add some realistic problems
data['Age'][::10] = np.nan  # 10% missing
data['Purchase Amount'][::15] = np.nan  # ~7% missing
data['Customer Rating'][:5] = [100.0, 200.0, -50.0, 300.0, -100.0]  # Invalid ratings (outliers)

df = pd.DataFrame(data)

print(f"\n📊 Created realistic dataset: {df.shape[0]} customers")
print("=" * 70)

# ============================================================================
# FEATURE 1: ONE-COMMAND CLEANING
# ============================================================================
print("\n\n" + "=" * 70)
print("🚀 FEATURE 1: ONE-COMMAND SMART CLEANING")
print("=" * 70)

print("\nBefore: Dataset has missing values, outliers, and messy column names")
print(f"Shape: {df.shape}")
print(f"Missing values: {df.isnull().sum().sum()}")

cleaned_df = ky.quick_clean(df)

print(f"\n✅ After: Dataset is production-ready!")

# ============================================================================
# FEATURE 2: DATA QUALITY ASSESSMENT
# ============================================================================
print("\n\n" + "=" * 70)
print("🔍 FEATURE 2: COMPREHENSIVE DATA QUALITY REPORT")
print("=" * 70)

df_kuya = KuyaDataFrame(df)
quality_metrics = df_kuya.quality_report()

# ============================================================================
# FEATURE 3: SMART ANALYSIS WITH AI-LIKE INSIGHTS
# ============================================================================
print("\n\n" + "=" * 70)
print("🤖 FEATURE 3: AI-POWERED SMART ANALYSIS")
print("=" * 70)

insights = cleaned_df.smart_analysis()

# ============================================================================
# FEATURE 4: AUTOMATED INSIGHTS GENERATION
# ============================================================================
print("\n\n" + "=" * 70)
print("💡 FEATURE 4: AUTOMATED INSIGHTS")
print("=" * 70)

auto_insights = cleaned_df.auto_insights()

# ============================================================================
# FEATURE 5: INTELLIGENT ENCODING
# ============================================================================
print("\n\n" + "=" * 70)
print("🎯 FEATURE 5: SMART ENCODING FOR MACHINE LEARNING")
print("=" * 70)

print("\nOriginal categorical columns:")
print(cleaned_df.select_dtypes(include=['object']).columns.tolist())

encoded_df = cleaned_df.smart_encode()

print(f"\n✅ Encoded! New shape: {encoded_df.shape}")
print(f"All columns are now numeric and ML-ready!")

# ============================================================================
# FEATURE 6: NORMALIZATION
# ============================================================================
print("\n\n" + "=" * 70)
print("📊 FEATURE 6: DATA NORMALIZATION")
print("=" * 70)

print("\nBefore normalization - Age column sample:")
print(cleaned_df['age'].head())

normalized_df = cleaned_df.normalize(columns=['age', 'purchase_amount'], method='minmax')

print("\nAfter MinMax normalization - Age column sample:")
print(normalized_df['age'].head())
print("Values are now scaled between 0 and 1!")

# ============================================================================
# FEATURE 7: AUTO REPORT GENERATION
# ============================================================================
print("\n\n" + "=" * 70)
print("📝 FEATURE 7: AUTOMATED REPORT GENERATION")
print("=" * 70)

# Generate text report
txt_report = ky.auto_report(cleaned_df, 
                            output_path='/tmp/kuya_customer_analysis',
                            format='txt')

# Generate HTML report
html_report = ky.auto_report(cleaned_df,
                             output_path='/tmp/kuya_customer_analysis',
                             format='html')

print(f"\n✅ Generated beautiful reports!")
print(f"   📄 Text: {txt_report}")
print(f"   🌐 HTML: {html_report}")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n\n" + "=" * 70)
print("🎉 SHOWCASE COMPLETE!")
print("=" * 70)

print("\n✨ What You Just Witnessed:")
print("  1️⃣  One-command cleaning (quick_clean)")
print("  2️⃣  Comprehensive quality assessment")
print("  3️⃣  AI-powered smart analysis")
print("  4️⃣  Automated insight generation")
print("  5️⃣  Intelligent categorical encoding")
print("  6️⃣  Multiple normalization methods")
print("  7️⃣  Automated report generation (TXT & HTML)")

print("\n💡 Kuya makes you 10x faster at data analysis!")
print("   Less typing, more thinking. Less boring, more insights!")

print("\n" + "=" * 70)
print("🚀 Ready to analyze your own data?")
print("   Try: python examples/example_5_complete_workflow.py")
print("=" * 70)
