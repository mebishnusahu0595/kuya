# Kuya Project Structure

```
PROJECT-COLLEGE/
│
├── kuya/                          # Main package directory
│   ├── __init__.py               # Package initialization
│   ├── core.py                   # KuyaDataFrame (extended Pandas)
│   ├── clean.py                  # Data cleaning utilities
│   ├── eda.py                    # Exploratory data analysis
│   ├── viz.py                    # Visualization helpers
│   └── io.py                     # File input/output with auto-detection
│
├── examples/                      # Example scripts
│   ├── README.md                 # Examples documentation
│   ├── example_1_cleaning_eda.py # Basic cleaning and EDA
│   ├── example_2_visualization.py # Visualization examples
│   ├── example_3_file_io.py      # File I/O operations
│   ├── example_4_outliers.py     # Outlier detection
│   ├── example_5_complete_workflow.py # Complete analysis workflow
│   └── sample_data/              # Generated sample data files
│
├── venv/                         # Virtual environment (ignored in git)
│
├── setup.py                      # Installation configuration
├── README.md                     # Main documentation
├── QUICKSTART.md                 # Quick start guide
├── LICENSE                       # MIT License
└── test_kuya.py                  # Quick test script

```

## Module Descriptions

### Core Package (`kuya/`)

#### `__init__.py`
- Package entry point
- Imports all main components
- Displays welcome message

#### `core.py`
- `KuyaDataFrame`: Extended Pandas DataFrame
- Integrates all Kuya methods into one convenient class
- Provides seamless access to cleaning, EDA, and visualization

#### `clean.py`
- `KuyaCleaner`: Data cleaning utilities
- Methods:
  - `clean_missing()`: Handle missing values
  - `fix_dtypes()`: Auto-convert data types
  - `handle_outliers()`: Detect and remove outliers (IQR/Z-score)
  - `standardize_columns()`: Normalize column names

#### `eda.py`
- `KuyaEDA`: Exploratory data analysis
- Methods:
  - `summary()`: Comprehensive data summary
  - `check_missing()`: Missing value analysis
  - `unique_summary()`: Unique value counts
  - `correlation_report()`: Correlation analysis with insights

#### `viz.py`
- `KuyaViz`: Visualization utilities
- Methods:
  - `quick_plot()`: Multi-type plotting (bar, scatter, line, etc.)
  - `plot_histogram()`: Enhanced histogram with statistics
  - `corr_heatmap()`: Correlation heatmap
  - `pairplot()`: Pairwise feature visualization

#### `io.py`
- File I/O utilities
- Functions:
  - `load()`: Smart file loading with format auto-detection
  - `save()`: Smart file saving with format auto-detection
- Supports: CSV, Excel, JSON, Parquet, TSV

---

## Installation Files

### `setup.py`
- Package metadata
- Dependencies specification
- Installation configuration

### `requirements.txt` (auto-generated)
- pandas >= 1.3.0
- numpy >= 1.20.0
- matplotlib >= 3.3.0
- seaborn >= 0.11.0
- scipy >= 1.7.0
- openpyxl >= 3.0.0

---

## Documentation Files

### `README.md`
- Complete project documentation
- Feature descriptions
- Installation instructions
- Usage examples
- Future roadmap

### `QUICKSTART.md`
- Quick installation guide
- Basic usage examples
- Common patterns
- Tips and tricks

### `LICENSE`
- MIT License
- Open source and free to use

---

## Testing

### `test_kuya.py`
- Quick verification script
- Tests all major components
- Validates installation

---

## Examples Directory

Contains 5 comprehensive examples demonstrating:
1. Basic data cleaning and EDA
2. Visualization capabilities
3. File I/O operations
4. Outlier detection and handling
5. Complete real-world analysis workflow

Each example is self-contained and runnable independently.

---

## Virtual Environment

### `venv/` (not tracked in git)
- Isolated Python environment
- Contains all dependencies
- Activated with: `source venv/bin/activate`

---

## Key Design Principles

1. **Simplicity**: One-line commands for common tasks
2. **Consistency**: Same behavior across all datasets
3. **Clarity**: Human-readable function names
4. **Extensibility**: Easy to add new features
5. **Integration**: Works seamlessly with Pandas

---

## Development Workflow

```bash
# 1. Setup
cd PROJECT-COLLEGE
python3 -m venv venv
source venv/bin/activate
pip install -e .

# 2. Test
python test_kuya.py

# 3. Try examples
python examples/example_1_cleaning_eda.py

# 4. Develop
# Edit files in kuya/
# Changes immediately available (editable install)

# 5. Test again
python test_kuya.py
```

---

This structure makes Kuya:
- Easy to understand
- Simple to maintain
- Ready to extend
- Professional and production-ready
