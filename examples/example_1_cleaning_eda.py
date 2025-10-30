"""
Example 1: Basic Data Cleaning and EDA
Demonstrates Kuya's cleaning and exploratory analysis features.
"""

import pandas as pd
import numpy as np
import sys
sys.path.insert(0, '/home/bishnups/Documents/PROJECT-COLLEGE')

import kuya as ky
from kuya.core import KuyaDataFrame

# Create sample messy dataset
print("=" * 60)
print("Creating Sample Messy Dataset...")
print("=" * 60)

data = {
    'Customer Name': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown', 'Charlie Wilson', 
                      'David Lee', 'Emma Davis', 'Frank Miller', 'Grace Taylor', 'Henry Anderson'],
    'Age': [25, 30, np.nan, 45, 35, 28, np.nan, 50, 38, 42],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
             'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'Purchase Amount': [100.50, 250.75, 75.25, np.nan, 180.00, 
                        220.50, 95.75, 310.25, 175.50, 200.00],
    'Product Category': ['Electronics', 'Clothing', 'Electronics', 'Food', 'Clothing',
                        'Electronics', 'Food', 'Electronics', 'Clothing', 'Food'],
    'Rating': [4.5, 5.0, 3.5, 4.0, np.nan, 4.8, 3.8, 5.0, 4.2, 4.6],
    'Date': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19',
             '2024-01-20', '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24']
}

df = KuyaDataFrame(data)
print(f"\n✓ Created dataset with {df.shape[0]} rows and {df.shape[1]} columns")
print("\n" + "=" * 60)

# Step 1: Check the original messy data
print("\n🔍 STEP 1: INSPECTING ORIGINAL DATA")
print("=" * 60)
print(df.head())

# Step 2: Check missing values
print("\n\n🔍 STEP 2: CHECKING MISSING VALUES")
print("=" * 60)
df.check_missing()

# Step 3: Standardize column names
print("\n\n🧹 STEP 3: STANDARDIZING COLUMN NAMES")
print("=" * 60)
df = df.standardize_columns()

# Step 4: Fix data types
print("\n\n🧹 STEP 4: FIXING DATA TYPES")
print("=" * 60)
df = df.fix_dtypes()

# Step 5: Clean missing values
print("\n\n🧹 STEP 5: CLEANING MISSING VALUES")
print("=" * 60)
df = df.clean_missing(method='fill', value=df.select_dtypes(include=[np.number]).mean())

# Step 6: Get comprehensive summary
print("\n\n📊 STEP 6: COMPREHENSIVE DATA SUMMARY")
print("=" * 60)
df.summary()

# Step 7: Unique values summary
print("\n\n📊 STEP 7: UNIQUE VALUES ANALYSIS")
print("=" * 60)
df.unique_summary()

# Step 8: Correlation analysis
print("\n\n📊 STEP 8: CORRELATION ANALYSIS")
print("=" * 60)
df.correlation_report()

print("\n\n" + "=" * 60)
print("✨ Example 1 completed successfully!")
print("=" * 60)
