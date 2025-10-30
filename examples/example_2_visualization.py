"""
Example 2: Data Visualization
Demonstrates Kuya's visualization capabilities.
"""

import pandas as pd
import numpy as np
import sys
sys.path.insert(0, '/home/bishnups/Documents/PROJECT-COLLEGE')

import kuya as ky
from kuya.core import KuyaDataFrame
import matplotlib.pyplot as plt

# Create sample dataset for visualization
print("=" * 60)
print("Creating Sample Sales Dataset for Visualization...")
print("=" * 60)

np.random.seed(42)

data = {
    'region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'product': np.random.choice(['Product A', 'Product B', 'Product C'], 100),
    'sales': np.random.randint(1000, 10000, 100),
    'profit': np.random.randint(100, 2000, 100),
    'customer_satisfaction': np.random.uniform(3.0, 5.0, 100),
    'units_sold': np.random.randint(10, 200, 100),
    'price': np.random.uniform(50, 500, 100),
}

# Add some correlation
data['revenue'] = data['sales'] * 1.2 + np.random.normal(0, 100, 100)
data['cost'] = data['sales'] * 0.7 + np.random.normal(0, 80, 100)

df = KuyaDataFrame(data)
print(f"\n✓ Created dataset with {df.shape[0]} rows and {df.shape[1]} columns")

# Example 1: Bar plot
print("\n\n📊 Visualization 1: Bar Plot - Sales by Region")
print("=" * 60)
df.quick_plot('bar', x='region', y='sales', title='Average Sales by Region')

# Example 2: Scatter plot
print("\n\n📊 Visualization 2: Scatter Plot - Sales vs Profit")
print("=" * 60)
df.quick_plot('scatter', x='sales', y='profit', title='Sales vs Profit Relationship')

# Example 3: Histogram
print("\n\n📊 Visualization 3: Histogram - Sales Distribution")
print("=" * 60)
df.plot_histogram('sales', bins=20)

# Example 4: Box plot
print("\n\n📊 Visualization 4: Box Plot - Sales by Product")
print("=" * 60)
df.quick_plot('box', x='product', y='sales', title='Sales Distribution by Product')

# Example 5: Correlation heatmap
print("\n\n📊 Visualization 5: Correlation Heatmap")
print("=" * 60)
df.corr_heatmap()

# Example 6: Pairplot (for selected columns)
print("\n\n📊 Visualization 6: Pairplot - Key Metrics")
print("=" * 60)
df.pairplot(columns=['sales', 'profit', 'customer_satisfaction', 'units_sold'])

print("\n\n" + "=" * 60)
print("✨ Example 2 completed successfully!")
print("All visualizations generated!")
print("=" * 60)
