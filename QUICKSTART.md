# 🚀 Quick Start Guide - Kuya

## Installation

### Step 1: Navigate to the project directory
```bash
cd /home/bishnups/Documents/PROJECT-COLLEGE
```

### Step 2: Create and activate a virtual environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

### Step 3: Install Kuya
```bash
pip install -e .
```

---

## Basic Usage

### 1. Import Kuya
```python
import kuya as ky
from kuya.core import KuyaDataFrame
```

### 2. Load Data
```python
# Auto-detect file format and load
df = ky.load('your_data.csv')  # Works with .csv, .xlsx, .json, .parquet

# Or convert existing DataFrame
import pandas as pd
df = pd.read_csv('data.csv')
df = KuyaDataFrame(df)
```

### 3. Clean Your Data
```python
# Standardize column names (Customer Name → customer_name)
df = df.standardize_columns()

# Fix data types automatically
df = df.fix_dtypes()

# Handle missing values
df = df.clean_missing(method='fill', value=0)
# or
df = df.clean_missing(method='drop')

# Remove outliers
df = df.handle_outliers(method='iqr')
```

### 4. Explore Your Data
```python
# Get comprehensive summary
df.summary()

# Check missing values
df.check_missing()

# See unique value counts
df.unique_summary()

# Analyze correlations
df.correlation_report()
```

### 5. Visualize
```python
# Quick plots
df.quick_plot('bar', x='category', y='sales')
df.quick_plot('scatter', x='age', y='income')

# Histogram with statistics
df.plot_histogram('price')

# Correlation heatmap
df.corr_heatmap()

# Pairplot for relationships
df.pairplot()
```

### 6. Save Results
```python
# Auto-detect format from extension
ky.save(df, 'cleaned_data.csv')
ky.save(df, 'output.xlsx')
ky.save(df, 'results.json')
```

---

## Complete Example

```python
import kuya as ky
from kuya.core import KuyaDataFrame

# 1. Load data
df = ky.load('sales_data.csv')

# 2. Clean it
df = df.standardize_columns()
df = df.fix_dtypes()
df = df.clean_missing(method='fill', value=0)
df = df.handle_outliers(method='iqr')

# 3. Explore it
df.summary()
df.correlation_report()

# 4. Visualize it
df.plot_histogram('sales')
df.corr_heatmap()

# 5. Save it
ky.save(df, 'cleaned_sales.csv')
```

---

## Running Examples

Try the included examples to see Kuya in action:

```bash
# Make sure you're in the virtual environment
source venv/bin/activate

# Run examples
python examples/example_1_cleaning_eda.py
python examples/example_2_visualization.py
python examples/example_3_file_io.py
python examples/example_4_outliers.py
python examples/example_5_complete_workflow.py
```

---

## Quick Test

Run the test script to verify everything works:

```bash
python test_kuya.py
```

You should see:
```
✅ ALL TESTS PASSED!
Kuya is installed and working correctly!
```

---

## Tips & Tricks

### Chain Operations
```python
df = (df
    .standardize_columns()
    .fix_dtypes()
    .clean_missing(method='fill')
    .handle_outliers()
)
```

### Work with Specific Columns
```python
# Clean only specific columns
df = df.clean_missing(method='fill', value=0, columns=['age', 'salary'])

# Check outliers in specific columns
df = df.handle_outliers(method='iqr', columns=['price', 'quantity'])
```

### Different Plot Types
```python
df.quick_plot('bar', x='category', y='sales')      # Bar chart
df.quick_plot('scatter', x='age', y='income')      # Scatter plot
df.quick_plot('box', x='category', y='price')      # Box plot
df.quick_plot('violin', x='category', y='score')   # Violin plot
df.quick_plot('pie', x='category')                 # Pie chart
df.quick_plot('line', x='date', y='revenue')       # Line chart
```

---

## Need Help?

- 📖 Read the full [README.md](README.md)
- 📂 Check the [examples/](examples/) directory
- 💡 Review example scripts for detailed use cases

---

**Happy data analysis! 📊✨**
