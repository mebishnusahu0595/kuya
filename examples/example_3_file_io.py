"""
Example 3: File I/O Operations
Demonstrates Kuya's smart loading and saving capabilities.
"""

import pandas as pd
import numpy as np
import sys
import os
sys.path.insert(0, '/home/bishnups/Documents/PROJECT-COLLEGE')

import kuya as ky
from kuya.core import KuyaDataFrame

print("=" * 60)
print("Example 3: File I/O Operations")
print("=" * 60)

# Create sample data directory
data_dir = '/home/bishnups/Documents/PROJECT-COLLEGE/examples/sample_data'
os.makedirs(data_dir, exist_ok=True)

# Create sample dataset
print("\n📝 Creating sample dataset...")
data = {
    'employee_id': range(1, 21),
    'name': [f'Employee {i}' for i in range(1, 21)],
    'department': np.random.choice(['Sales', 'Marketing', 'IT', 'HR'], 20),
    'salary': np.random.randint(40000, 120000, 20),
    'experience_years': np.random.randint(1, 15, 20),
    'performance_score': np.random.uniform(3.0, 5.0, 20).round(2),
}

df = KuyaDataFrame(data)
print(f"✓ Created dataset: {df.shape[0]} rows × {df.shape[1]} columns")

# Save in different formats
print("\n\n💾 STEP 1: SAVING DATA IN MULTIPLE FORMATS")
print("=" * 60)

# Save as CSV
csv_path = os.path.join(data_dir, 'employees.csv')
ky.save(df, csv_path)

# Save as Excel
excel_path = os.path.join(data_dir, 'employees.xlsx')
ky.save(df, excel_path)

# Save as JSON
json_path = os.path.join(data_dir, 'employees.json')
ky.save(df, json_path)

# Load data back
print("\n\n📂 STEP 2: LOADING DATA WITH AUTO-DETECTION")
print("=" * 60)

# Load CSV
print("\n1. Loading CSV file:")
df_csv = ky.load(csv_path)
print(df_csv.head(3))

# Load Excel
print("\n2. Loading Excel file:")
df_excel = ky.load(excel_path)
print(df_excel.head(3))

# Load JSON
print("\n3. Loading JSON file:")
df_json = ky.load(json_path)
print(df_json.head(3))

# Demonstrate full workflow
print("\n\n🔄 STEP 3: COMPLETE WORKFLOW (LOAD → CLEAN → ANALYZE → SAVE)")
print("=" * 60)

# Load
df = ky.load(csv_path)

# Add some missing values for demonstration
df.loc[2, 'salary'] = np.nan
df.loc[5, 'performance_score'] = np.nan

# Convert to KuyaDataFrame
df = KuyaDataFrame(df)

# Clean
print("\n🧹 Cleaning data...")
df = df.clean_missing(method='fill')
df = df.standardize_columns()

# Analyze
print("\n📊 Analyzing data...")
df.summary()

# Save cleaned version
cleaned_path = os.path.join(data_dir, 'employees_cleaned.csv')
ky.save(df, cleaned_path)

print("\n\n" + "=" * 60)
print("✨ Example 3 completed successfully!")
print(f"📁 All files saved in: {data_dir}")
print("=" * 60)

# List created files
print("\n📋 Created files:")
for file in os.listdir(data_dir):
    file_path = os.path.join(data_dir, file)
    size_kb = os.path.getsize(file_path) / 1024
    print(f"  • {file} ({size_kb:.2f} KB)")
