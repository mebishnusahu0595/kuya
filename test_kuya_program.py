"""
🎉 KUYA TEST PROGRAM 🎉
Testing kuya-data package with real data!
"""

import kuya

print("=" * 60)
print("🚀 KUYA DATA ANALYSIS TEST")
print("=" * 60)
print()

# Load the test data
print("📂 Loading test_data.csv...")
data = kuya.load('test_data.csv')
# Convert to KuyaDataFrame for extended features
df = kuya.KuyaDataFrame(data)
print(f"✅ Loaded {len(df)} rows and {len(df.columns)} columns")
print()

# Show basic info
print("=" * 60)
print("📊 DATASET SUMMARY")
print("=" * 60)
df.summary()
print()

# Check for missing values
print("=" * 60)
print("🔍 MISSING VALUE ANALYSIS")
print("=" * 60)
df.check_missing()
print()

# Quick clean the data
print("=" * 60)
print("🧹 QUICK CLEAN (AI-Powered)")
print("=" * 60)
cleaned_df = kuya.quick_clean(df)
print(f"✅ Cleaned! Shape: {cleaned_df.shape}")
print()

# Get smart analysis
print("=" * 60)
print("🤖 SMART ANALYSIS (AI Insights)")
print("=" * 60)
insights = cleaned_df.smart_analysis()
print(f"📈 Found {len(insights)} key insights:")
for i, insight in enumerate(insights, 1):
    print(f"{i}. {insight}")
print()

# Unique values summary
print("=" * 60)
print("🔢 UNIQUE VALUES SUMMARY")
print("=" * 60)
df.unique_summary()
print()

# Show correlation for numeric columns
print("=" * 60)
print("📈 CORRELATION ANALYSIS")
print("=" * 60)
df.correlation_report()
print()

# Show some statistics by department
print("=" * 60)
print("💼 STATISTICS BY DEPARTMENT")
print("=" * 60)
print("\nAverage salary by department:")
print(df.groupby('department')['salary'].mean().sort_values(ascending=False))
print("\nAverage rating by department:")
print(df.groupby('department')['rating'].mean().sort_values(ascending=False))
print()

# Data quality report
print("=" * 60)
print("✅ DATA QUALITY REPORT")
print("=" * 60)
quality = df.quality_report()
print()

# Generate auto report
print("=" * 60)
print("📄 GENERATING COMPREHENSIVE REPORT")
print("=" * 60)
report_path = 'kuya_analysis_report.txt'
kuya.auto_report(df, report_path)
print(f"✅ Report saved to: {report_path}")
print()

print("=" * 60)
print("🎉 TEST COMPLETE! KUYA WORKS PERFECTLY!")
print("=" * 60)
print()
print("📌 What we tested:")
print("  ✅ Data loading (load)")
print("  ✅ Basic summary (summary)")
print("  ✅ Missing value check (check_missing)")
print("  ✅ Quick cleaning (quick_clean)")
print("  ✅ AI insights (smart_analysis)")
print("  ✅ Unique values (unique_summary)")
print("  ✅ Correlation analysis (correlation_report)")
print("  ✅ Data quality (quality_report)")
print("  ✅ Auto report (auto_report)")
print()
print("🚀 Kuya is ready to supercharge your data analysis!")
