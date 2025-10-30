# Kuya Examples

This directory contains example scripts demonstrating Kuya's capabilities.

## Available Examples

### 1. Basic Data Cleaning and EDA (`example_1_cleaning_eda.py`)
Learn how to:
- Clean missing values
- Standardize column names
- Fix data types
- Get comprehensive summaries
- Analyze unique values and correlations

**Run it:**
```bash
python examples/example_1_cleaning_eda.py
```

---

### 2. Data Visualization (`example_2_visualization.py`)
Learn how to:
- Create quick plots (bar, scatter, box, etc.)
- Generate histograms with statistics
- Plot correlation heatmaps
- Create pairplots

**Run it:**
```bash
python examples/example_2_visualization.py
```

---

### 3. File I/O Operations (`example_3_file_io.py`)
Learn how to:
- Load data with auto-format detection
- Save data in multiple formats (CSV, Excel, JSON)
- Execute complete load → clean → save workflows

**Run it:**
```bash
python examples/example_3_file_io.py
```

---

### 4. Outlier Detection (`example_4_outliers.py`)
Learn how to:
- Detect outliers using IQR method
- Remove outliers from datasets
- Compare data before and after cleaning
- Visualize the impact of outlier removal

**Run it:**
```bash
python examples/example_4_outliers.py
```

---

### 5. Complete Real-World Workflow (`example_5_complete_workflow.py`)
A comprehensive example showing:
- Full e-commerce sales analysis
- Data inspection and cleaning
- Exploratory analysis
- Multiple visualizations
- Business insights extraction
- Results export

**Run it:**
```bash
python examples/example_5_complete_workflow.py
```

---

## Running All Examples

To run all examples in sequence:

```bash
python examples/example_1_cleaning_eda.py
python examples/example_2_visualization.py
python examples/example_3_file_io.py
python examples/example_4_outliers.py
python examples/example_5_complete_workflow.py
```

---

## Requirements

Make sure Kuya is installed before running examples:

```bash
cd /home/bishnups/Documents/PROJECT-COLLEGE
pip install -e .
```

---

## Output

Examples will:
- Print informative messages to console
- Generate visualizations (matplotlib windows)
- Create sample data files in `examples/sample_data/` directory

---

Enjoy exploring Kuya! 🎉
