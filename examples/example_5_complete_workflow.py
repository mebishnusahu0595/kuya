"""
Example 5: Complete Real-World Analysis Workflow
Demonstrates a complete data analysis workflow using Kuya.
"""

import pandas as pd
import numpy as np
import sys
sys.path.insert(0, '/home/bishnups/Documents/PROJECT-COLLEGE')

import kuya as ky
from kuya.core import KuyaDataFrame

print("=" * 70)
print("         🎯 COMPLETE REAL-WORLD ANALYSIS WORKFLOW")
print("=" * 70)
print("\nScenario: Analyzing E-commerce Sales Data")
print("=" * 70)

# Create realistic e-commerce dataset
np.random.seed(42)

n_records = 200

data = {
    'Order ID': [f'ORD{str(i).zfill(5)}' for i in range(1, n_records + 1)],
    'Customer Name': [f'Customer {i}' for i in range(1, n_records + 1)],
    'Product Category': np.random.choice(['Electronics', 'Clothing', 'Home & Garden', 
                                          'Sports', 'Books'], n_records),
    'Product Price': np.random.uniform(10, 500, n_records).round(2),
    'Quantity': np.random.randint(1, 10, n_records),
    'Discount %': np.random.choice([0, 5, 10, 15, 20, 25], n_records),
    'Shipping Cost': np.random.uniform(5, 50, n_records).round(2),
    'Customer Age': np.random.randint(18, 70, n_records),
    'Customer Rating': np.random.uniform(1, 5, n_records).round(1),
    'Order Date': pd.date_range(start='2024-01-01', periods=n_records, freq='D'),
}

# Calculate total amount
data['Total Amount'] = (data['Product Price'] * data['Quantity'] * 
                        (1 - data['Discount %']/100) + data['Shipping Cost'])

# Add some missing values to make it realistic
indices_to_null = np.random.choice(range(n_records), 15, replace=False)
for idx in indices_to_null[:5]:
    data['Customer Rating'][idx] = np.nan
for idx in indices_to_null[5:10]:
    data['Customer Age'][idx] = np.nan
for idx in indices_to_null[10:15]:
    data['Discount %'][idx] = np.nan

df = KuyaDataFrame(data)

print(f"\n✓ Created e-commerce dataset: {df.shape[0]} orders")
print("=" * 70)

# PHASE 1: DATA INSPECTION
print("\n\n" + "=" * 70)
print("📋 PHASE 1: DATA INSPECTION")
print("=" * 70)

print("\n📄 First few records:")
print(df.head())

print("\n\n🔍 Checking for issues:")
df.check_missing()

# PHASE 2: DATA CLEANING
print("\n\n" + "=" * 70)
print("🧹 PHASE 2: DATA CLEANING")
print("=" * 70)

# Standardize column names
df = df.standardize_columns()

# Fix data types
df = df.fix_dtypes()

# Handle missing values
df = df.clean_missing(method='fill')

# Remove outliers
df = df.handle_outliers(method='iqr')

print("\n✓ Data cleaning completed!")

# PHASE 3: EXPLORATORY ANALYSIS
print("\n\n" + "=" * 70)
print("📊 PHASE 3: EXPLORATORY ANALYSIS")
print("=" * 70)

# Comprehensive summary
df.summary()

# Unique values
print("\n")
df.unique_summary()

# Correlation analysis
print("\n")
df.correlation_report()

# PHASE 4: VISUALIZATIONS
print("\n\n" + "=" * 70)
print("📈 PHASE 4: VISUALIZATIONS")
print("=" * 70)

print("\n1. Sales by Product Category")
df.quick_plot('bar', x='product_category', y='total_amount')

print("\n2. Price Distribution")
df.plot_histogram('product_price', bins=30)

print("\n3. Customer Age vs Rating")
df.quick_plot('scatter', x='customer_age', y='customer_rating')

print("\n4. Correlation Heatmap")
df.corr_heatmap()

# PHASE 5: KEY INSIGHTS
print("\n\n" + "=" * 70)
print("💡 PHASE 5: KEY INSIGHTS")
print("=" * 70)

# Calculate key metrics
total_revenue = df['total_amount'].sum()
avg_order_value = df['total_amount'].mean()
total_orders = len(df)
avg_rating = df['customer_rating'].mean()

# Revenue by category
revenue_by_category = df.groupby('product_category')['total_amount'].sum().sort_values(ascending=False)

print(f"\n📊 Business Metrics:")
print(f"  • Total Revenue: ${total_revenue:,.2f}")
print(f"  • Average Order Value: ${avg_order_value:.2f}")
print(f"  • Total Orders: {total_orders:,}")
print(f"  • Average Customer Rating: {avg_rating:.2f}/5.0")

print(f"\n💰 Revenue by Category:")
for category, revenue in revenue_by_category.items():
    pct = (revenue / total_revenue) * 100
    print(f"  • {category}: ${revenue:,.2f} ({pct:.1f}%)")

# Age demographics
age_groups = pd.cut(df['customer_age'], bins=[0, 25, 35, 45, 55, 100], 
                    labels=['18-25', '26-35', '36-45', '46-55', '56+'])
age_distribution = age_groups.value_counts().sort_index()

print(f"\n👥 Customer Age Distribution:")
for age_group, count in age_distribution.items():
    pct = (count / len(df)) * 100
    print(f"  • {age_group}: {count} customers ({pct:.1f}%)")

# PHASE 6: SAVE RESULTS
print("\n\n" + "=" * 70)
print("💾 PHASE 6: SAVING RESULTS")
print("=" * 70)

# Save cleaned data
output_path = '/home/bishnups/Documents/PROJECT-COLLEGE/examples/sample_data/ecommerce_cleaned.csv'
ky.save(df, output_path)

# Save insights as a summary report
insights_df = pd.DataFrame({
    'Metric': ['Total Revenue', 'Avg Order Value', 'Total Orders', 'Avg Rating'],
    'Value': [f'${total_revenue:,.2f}', f'${avg_order_value:.2f}', 
              f'{total_orders:,}', f'{avg_rating:.2f}/5.0']
})

insights_path = '/home/bishnups/Documents/PROJECT-COLLEGE/examples/sample_data/ecommerce_insights.csv'
ky.save(insights_df, insights_path)

print("\n\n" + "=" * 70)
print("✨ COMPLETE WORKFLOW FINISHED SUCCESSFULLY!")
print("=" * 70)
print("\n🎉 You've successfully:")
print("  ✓ Loaded and inspected data")
print("  ✓ Cleaned missing values and outliers")
print("  ✓ Performed exploratory analysis")
print("  ✓ Generated visualizations")
print("  ✓ Extracted key insights")
print("  ✓ Saved results for reporting")
print("\n" + "=" * 70)
