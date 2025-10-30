"""
Example 4: Outlier Detection and Handling
Demonstrates Kuya's outlier detection capabilities.
"""

import pandas as pd
import numpy as np
import sys
sys.path.insert(0, '/home/bishnups/Documents/PROJECT-COLLEGE')

import kuya as ky
from kuya.core import KuyaDataFrame

print("=" * 60)
print("Example 4: Outlier Detection and Handling")
print("=" * 60)

# Create dataset with outliers
np.random.seed(42)

# Normal data
normal_data = {
    'temperature': np.random.normal(25, 5, 95),
    'humidity': np.random.normal(60, 10, 95),
    'pressure': np.random.normal(1013, 5, 95),
    'wind_speed': np.random.normal(15, 5, 95),
}

# Add outliers
outlier_data = {
    'temperature': [100, 120, -50, 150, 200],  # Extreme temperatures
    'humidity': [150, 200, -10, 180, 190],     # Invalid humidity
    'pressure': [1200, 1300, 800, 1400, 700],  # Extreme pressure
    'wind_speed': [100, 150, 200, 120, 180],   # Extreme wind speeds
}

# Combine
data = {key: list(normal_data[key]) + list(outlier_data[key]) 
        for key in normal_data.keys()}

df = KuyaDataFrame(data)

print(f"\n✓ Created dataset with {df.shape[0]} rows (including 5 outliers)")

# Step 1: Initial summary
print("\n\n📊 STEP 1: INITIAL DATA SUMMARY (WITH OUTLIERS)")
print("=" * 60)
df.summary()

# Step 2: Visualize data with outliers
print("\n\n📊 STEP 2: VISUALIZING DATA WITH OUTLIERS")
print("=" * 60)
print("Generating histograms...")
df.plot_histogram('temperature')
df.plot_histogram('humidity')

# Step 3: Detect outliers using IQR method
print("\n\n🔍 STEP 3: REMOVING OUTLIERS (IQR METHOD)")
print("=" * 60)
df_cleaned_iqr = df.handle_outliers(method='iqr', threshold=1.5)

# Step 4: Summary after outlier removal
print("\n\n📊 STEP 4: DATA SUMMARY AFTER OUTLIER REMOVAL")
print("=" * 60)
df_cleaned_iqr.summary()

# Step 5: Visualize cleaned data
print("\n\n📊 STEP 5: VISUALIZING CLEANED DATA")
print("=" * 60)
print("Generating histograms for cleaned data...")
df_cleaned_iqr = KuyaDataFrame(df_cleaned_iqr)
df_cleaned_iqr.plot_histogram('temperature')

# Step 6: Comparison
print("\n\n📊 STEP 6: BEFORE & AFTER COMPARISON")
print("=" * 60)
print("\nBefore outlier removal:")
print(df.describe().round(2))
print("\nAfter outlier removal:")
print(df_cleaned_iqr.describe().round(2))

print("\n\n" + "=" * 60)
print("✨ Example 4 completed successfully!")
print("Outliers detected and removed successfully!")
print("=" * 60)
