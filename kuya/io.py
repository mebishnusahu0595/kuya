"""
Input-Output Module
Smart file loading and saving with automatic format detection.
"""

import pandas as pd
import os


def load(path, **kwargs):
    """
    Auto-detects and reads CSV, Excel, JSON, or Parquet files.
    
    Parameters:
    -----------
    path : str
        File path to load
    **kwargs : additional arguments passed to the appropriate pandas reader
    
    Returns:
    --------
    pd.DataFrame
        Loaded DataFrame
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ File not found: {path}")
    
    # Get file extension
    _, ext = os.path.splitext(path)
    ext = ext.lower()
    
    print(f"📂 Loading file: {os.path.basename(path)}")
    
    try:
        if ext == '.csv':
            df = pd.read_csv(path, **kwargs)
            print(f"✓ Loaded CSV file: {df.shape[0]} rows × {df.shape[1]} columns")
        
        elif ext in ['.xlsx', '.xls']:
            df = pd.read_excel(path, **kwargs)
            print(f"✓ Loaded Excel file: {df.shape[0]} rows × {df.shape[1]} columns")
        
        elif ext == '.json':
            df = pd.read_json(path, **kwargs)
            print(f"✓ Loaded JSON file: {df.shape[0]} rows × {df.shape[1]} columns")
        
        elif ext == '.parquet':
            df = pd.read_parquet(path, **kwargs)
            print(f"✓ Loaded Parquet file: {df.shape[0]} rows × {df.shape[1]} columns")
        
        elif ext == '.tsv':
            df = pd.read_csv(path, sep='\t', **kwargs)
            print(f"✓ Loaded TSV file: {df.shape[0]} rows × {df.shape[1]} columns")
        
        elif ext == '.txt':
            # Try to detect delimiter
            with open(path, 'r') as f:
                first_line = f.readline()
            if '\t' in first_line:
                df = pd.read_csv(path, sep='\t', **kwargs)
            else:
                df = pd.read_csv(path, **kwargs)
            print(f"✓ Loaded text file: {df.shape[0]} rows × {df.shape[1]} columns")
        
        else:
            raise ValueError(f"❌ Unsupported file format: {ext}")
        
        # Quick data info
        memory_mb = df.memory_usage(deep=True).sum() / 1024**2
        print(f"💾 Memory usage: {memory_mb:.2f} MB")
        
        return df
    
    except Exception as e:
        print(f"❌ Error loading file: {str(e)}")
        raise


def save(df, path, index=False, **kwargs):
    """
    Saves DataFrame in the appropriate format based on file extension.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to save
    path : str
        File path to save to
    index : bool, default=False
        Whether to write row index
    **kwargs : additional arguments passed to the appropriate pandas writer
    
    Returns:
    --------
    None
    """
    # Get file extension
    _, ext = os.path.splitext(path)
    ext = ext.lower()
    
    # Create directory if it doesn't exist
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        print(f"📁 Created directory: {directory}")
    
    print(f"💾 Saving file: {os.path.basename(path)}")
    
    try:
        if ext == '.csv':
            df.to_csv(path, index=index, **kwargs)
            print(f"✓ Saved as CSV: {df.shape[0]} rows × {df.shape[1]} columns")
        
        elif ext in ['.xlsx', '.xls']:
            df.to_excel(path, index=index, **kwargs)
            print(f"✓ Saved as Excel: {df.shape[0]} rows × {df.shape[1]} columns")
        
        elif ext == '.json':
            df.to_json(path, **kwargs)
            print(f"✓ Saved as JSON: {df.shape[0]} rows × {df.shape[1]} columns")
        
        elif ext == '.parquet':
            df.to_parquet(path, index=index, **kwargs)
            print(f"✓ Saved as Parquet: {df.shape[0]} rows × {df.shape[1]} columns")
        
        elif ext == '.tsv':
            df.to_csv(path, sep='\t', index=index, **kwargs)
            print(f"✓ Saved as TSV: {df.shape[0]} rows × {df.shape[1]} columns")
        
        else:
            # Default to CSV
            csv_path = path + '.csv'
            df.to_csv(csv_path, index=index, **kwargs)
            print(f"⚠️  Unknown extension, saved as CSV: {csv_path}")
        
        # File size
        file_size = os.path.getsize(path if ext else csv_path) / 1024**2
        print(f"📦 File size: {file_size:.2f} MB")
    
    except Exception as e:
        print(f"❌ Error saving file: {str(e)}")
        raise
