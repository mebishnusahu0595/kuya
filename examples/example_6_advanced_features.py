"""
Example 6: Advanced Features - Making Kuya Extraordinary!
Demonstrates advanced data quality, transformations, and automated insights.
"""

import pandas as pd
import numpy as np
import sys
sys.path.insert(0, '/home/bishnups/Documents/PROJECT-COLLEGE')

import kuya as ky
from kuya.core import KuyaDataFrame

print("=" * 70)
print("        🌟 ADVANCED KUYA FEATURES - EXTRAORDINARY DATA ANALYSIS 🌟")
print("=" * 70)

# Create a realistic dataset with various quality issues
np.random.seed(42)

data = {
    'customer_id': [f'CUST{str(i).zfill(4)}' for i in range(1, 151)],
    'age': np.random.randint(18, 75, 150),
    'income': np.random.normal(50000, 20000, 150),
    'credit_score': np.random.randint(300, 850, 150),
    'purchase_amount': np.random.exponential(500, 150),
    'num_purchases': np.random.randint(1, 50, 150),
    'membership_level': np.random.choice(['Bronze', 'Silver', 'Gold', 'Platinum'], 150, p=[0.4, 0.3, 0.2, 0.1]),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 150),
    'satisfaction_score': np.random.uniform(1, 5, 150),
    'join_date': pd.date_range(start='2020-01-01', periods=150, freq='3D'),
}

# Add some quality issues
# 1. Missing values
indices = np.random.choice(150, 15, replace=False)
for idx in indices[:5]:
    data['income'][idx] = np.nan
for idx in indices[5:10]:
    data['satisfaction_score'][idx] = np.nan

# 2. Duplicates
data['customer_id'][10] = data['customer_id'][5]
data['customer_id'][20] = data['customer_id'][5]

# 3. Outliers
data['income'][30] = 500000  # Extreme outlier
data['income'][31] = -10000  # Invalid negative income

# 4. Constant column
data['country'] = 'USA'  # Constant

df = KuyaDataFrame(data)

print(f"\n✓ Created dataset: {df.shape[0]} customers")
print("=" * 70)

# ========== PHASE 1: DATA QUALITY ASSESSMENT ==========
print("\n\n" + "=" * 70)
print("📋 PHASE 1: ADVANCED DATA QUALITY ASSESSMENT")
print("=" * 70)

# Quality report
quality_metrics = df.quality_report()

# Detect duplicates
print("\n\n🔍 Checking for Duplicates:")
print("-" * 70)
duplicates = df.detect_duplicates(subset=['customer_id'])

# Memory optimization suggestions
print("\n\n💾 Memory Optimization:")
print("-" * 70)
dtype_suggestions = df.suggest_dtypes()

# ========== PHASE 2: AUTOMATED INSIGHTS ==========
print("\n\n" + "=" * 70)
print("🔮 PHASE 2: AUTOMATED INSIGHTS GENERATION")
print("=" * 70)

insights = df.auto_insights()

# Compare groups
print("\n\n📊 Group Comparison:")
print("-" * 70)
group_stats = df.compare_groups('membership_level', 'purchase_amount')

# ========== PHASE 3: ADVANCED TRANSFORMATIONS ==========
print("\n\n" + "=" * 70)
print("⚡ PHASE 3: ADVANCED DATA TRANSFORMATIONS")
print("=" * 70)

# Clean the data first
print("\n1. Cleaning Data:")
df_clean = df.copy()
df_clean = KuyaDataFrame(df_clean)
df_clean = df_clean.clean_missing(method='fill')
df_clean = df_clean.handle_outliers(method='iqr')

# Smart encoding
print("\n2. Smart Categorical Encoding:")
print("-" * 70)
df_encoded = df_clean.smart_encode(columns=['membership_level', 'region'])

# Normalize numeric features
print("\n3. Feature Normalization:")
print("-" * 70)
numeric_cols = ['age', 'income', 'credit_score', 'purchase_amount', 'num_purchases', 'satisfaction_score']
df_normalized = df_clean.normalize(columns=numeric_cols, method='minmax')
print(f"  Sample normalized values:")
print(df_normalized[numeric_cols].head(3))

# Create new features
print("\n4. Automated Feature Engineering:")
print("-" * 70)
df_features = df_clean.create_features()

# ========== PHASE 4: COMPREHENSIVE ANALYSIS ==========
print("\n\n" + "=" * 70)
print("📈 PHASE 4: COMPREHENSIVE ANALYSIS")
print("=" * 70)

# Calculate business metrics
print("\n💰 Business Metrics:")
print("-" * 70)
total_revenue = df_clean['purchase_amount'].sum()
avg_customer_value = total_revenue / df_clean['customer_id'].nunique()
avg_satisfaction = df_clean['satisfaction_score'].mean()

print(f"  • Total Revenue: ${total_revenue:,.2f}")
print(f"  • Average Customer Value: ${avg_customer_value:,.2f}")
print(f"  • Average Satisfaction: {avg_satisfaction:.2f}/5.0")
print(f"  • Customer Retention: {(avg_satisfaction/5*100):.1f}%")

# Segment analysis
print("\n\n🎯 Customer Segmentation:")
print("-" * 70)
for level in ['Bronze', 'Silver', 'Gold', 'Platinum']:
    segment = df_clean[df_clean['membership_level'] == level]
    if len(segment) > 0:
        avg_spend = segment['purchase_amount'].mean()
        avg_freq = segment['num_purchases'].mean()
        count = len(segment)
        print(f"  • {level:10} | Customers: {count:3} | Avg Spend: ${avg_spend:8,.2f} | Avg Frequency: {avg_freq:5.1f}")

# Correlation insights
print("\n\n🔗 Key Correlations:")
print("-" * 70)
corr = df_clean[numeric_cols].corr()
print("Top 5 strongest correlations:")
# Get unique correlations
corr_pairs = []
for i in range(len(corr.columns)):
    for j in range(i+1, len(corr.columns)):
        corr_pairs.append((corr.columns[i], corr.columns[j], corr.iloc[i, j]))
corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)
for col1, col2, val in corr_pairs[:5]:
    print(f"  • {col1:<20} ↔ {col2:<20}: {val:6.3f}")

# ========== PHASE 5: VISUALIZATION ==========
print("\n\n" + "=" * 70)
print("📊 PHASE 5: ADVANCED VISUALIZATIONS")
print("=" * 70)

print("\nGenerating visualizations...")

# Distribution analysis
df_clean.plot_histogram('purchase_amount')
df_clean.plot_histogram('satisfaction_score')

# Group comparison
df_clean.quick_plot('box', x='membership_level', y='purchase_amount')

# Correlation heatmap
df_clean.corr_heatmap()

# ========== PHASE 6: ACTIONABLE RECOMMENDATIONS ==========
print("\n\n" + "=" * 70)
print("💡 PHASE 6: ACTIONABLE RECOMMENDATIONS")
print("=" * 70)

print("\n🎯 Strategic Recommendations:\n")

recommendations = []

# Based on quality score
if quality_metrics['score'] < 80:
    recommendations.append("1. Data Quality: Improve data collection processes to reduce missing values and errors")

# Based on satisfaction
if avg_satisfaction < 3.5:
    recommendations.append("2. Customer Experience: Focus on improving satisfaction scores (currently low)")
elif avg_satisfaction >= 4.0:
    recommendations.append("2. Customer Experience: High satisfaction scores - leverage for testimonials and referrals")

# Based on membership distribution
bronze_pct = (df_clean['membership_level'] == 'Bronze').sum() / len(df_clean) * 100
if bronze_pct > 50:
    recommendations.append("3. Membership Growth: Large Bronze segment - create upgrade campaigns")

# Based on regional performance
regional_revenue = df_clean.groupby('region')['purchase_amount'].sum()
top_region = regional_revenue.idxmax()
bottom_region = regional_revenue.idxmin()
recommendations.append(f"4. Regional Strategy: Focus growth efforts in {bottom_region} region (learn from {top_region})")

# Based on correlations
if corr.loc['num_purchases', 'satisfaction_score'] > 0.5:
    recommendations.append("5. Retention: Strong correlation between purchases and satisfaction - focus on repeat customers")

for rec in recommendations:
    print(f"  {rec}")

# ========== FINAL SUMMARY ==========
print("\n\n" + "=" * 70)
print("✨ ANALYSIS COMPLETE!")
print("=" * 70)

print(f"""
📊 Summary Statistics:
   • Customers Analyzed: {len(df_clean):,}
   • Data Quality Score: {quality_metrics['score']:.1f}/100
   • Total Revenue: ${total_revenue:,.2f}
   • Average Satisfaction: {avg_satisfaction:.2f}/5.0
   • Insights Generated: {len(insights)}
   • Recommendations: {len(recommendations)}

🎉 You've unlocked the full power of Kuya's advanced features!
""")

print("=" * 70)
