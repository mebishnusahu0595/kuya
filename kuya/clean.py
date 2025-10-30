"""
Data Cleaning Module
Handles messy data like missing values, outliers, and column standardization.
"""

import pandas as pd
import numpy as np
import re


class KuyaCleaner:
    """Data cleaning utilities for Kuya."""
    
    def __init__(self, df):
        """
        Initialize cleaner with a DataFrame.
        
        Parameters:
        -----------
        df : pd.DataFrame
            The DataFrame to clean
        """
        self.df = df
    
    def clean_missing(self, method='drop', value=None, columns=None):
        """
        Drop or fill missing values automatically.
        
        Parameters:
        -----------
        method : str, default='drop'
            'drop' to remove rows with missing values
            'fill' to fill missing values
            'ffill' for forward fill
            'bfill' for backward fill
        value : any, optional
            Value to use when method='fill'
        columns : list, optional
            Specific columns to clean. If None, applies to all columns
        
        Returns:
        --------
        pd.DataFrame
            Cleaned DataFrame
        """
        from kuya.core import KuyaDataFrame
        df_copy = self.df.copy()
        target_cols = columns if columns else df_copy.columns
        
        if method == 'drop':
            df_copy = df_copy.dropna(subset=target_cols)
            print(f"✓ Dropped rows with missing values. New shape: {df_copy.shape}")
        elif method == 'fill':
            # Only fill numeric columns with mean by default
            numeric_cols = df_copy.select_dtypes(include=[np.number]).columns.tolist()
            target_numeric = [col for col in target_cols if col in numeric_cols]
            target_non_numeric = [col for col in target_cols if col not in numeric_cols]
            
            if value is not None:
                df_copy[target_cols] = df_copy[target_cols].fillna(value)
                print(f"✓ Filled missing values with {value}")
            else:
                # Fill numeric with mean
                if target_numeric:
                    for col in target_numeric:
                        df_copy[col] = df_copy[col].fillna(df_copy[col].mean())
                    print(f"✓ Filled {len(target_numeric)} numeric columns with mean")
                # Fill non-numeric with mode
                if target_non_numeric:
                    for col in target_non_numeric:
                        if df_copy[col].mode().shape[0] > 0:
                            df_copy[col] = df_copy[col].fillna(df_copy[col].mode()[0])
                    print(f"✓ Filled {len(target_non_numeric)} non-numeric columns with mode")
        elif method == 'ffill':
            df_copy[target_cols] = df_copy[target_cols].fillna(method='ffill')
            print("✓ Forward filled missing values")
        elif method == 'bfill':
            df_copy[target_cols] = df_copy[target_cols].fillna(method='bfill')
            print("✓ Backward filled missing values")
        else:
            raise ValueError("method must be 'drop', 'fill', 'ffill', or 'bfill'")
        
        return KuyaDataFrame(df_copy)
    
    def fix_dtypes(self):
        """
        Auto-convert columns to numeric, datetime, etc.
        
        Returns:
        --------
        pd.DataFrame
            DataFrame with corrected data types
        """
        from kuya.core import KuyaDataFrame
        df_copy = self.df.copy()
        conversions = []
        
        for col in df_copy.columns:
            original_dtype = df_copy[col].dtype
            
            # Try to convert to numeric
            if df_copy[col].dtype == 'object':
                try:
                    df_copy[col] = pd.to_numeric(df_copy[col], errors='raise')
                    conversions.append(f"{col}: {original_dtype} → numeric")
                    continue
                except (ValueError, TypeError):
                    pass
                
                # Try to convert to datetime
                try:
                    df_copy[col] = pd.to_datetime(df_copy[col], errors='raise')
                    conversions.append(f"{col}: {original_dtype} → datetime")
                    continue
                except (ValueError, TypeError):
                    pass
        
        if conversions:
            print("✓ Data types fixed:")
            for conv in conversions:
                print(f"  • {conv}")
        else:
            print("✓ No automatic conversions needed")
        
        return KuyaDataFrame(df_copy)
    
    def handle_outliers(self, method='iqr', columns=None, threshold=1.5):
        """
        Detect and remove outliers using IQR or Z-score.
        
        Parameters:
        -----------
        method : str, default='iqr'
            'iqr' for Interquartile Range method
            'zscore' for Z-score method
        columns : list, optional
            Specific numeric columns to check. If None, applies to all numeric columns
        threshold : float, default=1.5
            For IQR: multiplier for IQR (typically 1.5)
            For zscore: z-score threshold (typically 3)
        
        Returns:
        --------
        pd.DataFrame
            DataFrame with outliers removed
        """
        from kuya.core import KuyaDataFrame
        df_copy = self.df.copy()
        numeric_cols = df_copy.select_dtypes(include=[np.number]).columns.tolist()
        target_cols = columns if columns else numeric_cols
        target_cols = [col for col in target_cols if col in numeric_cols]
        
        if not target_cols:
            print("⚠ No numeric columns to check for outliers")
            return KuyaDataFrame(df_copy)
        
        original_shape = df_copy.shape
        
        if method == 'iqr':
            for col in target_cols:
                Q1 = df_copy[col].quantile(0.25)
                Q3 = df_copy[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - threshold * IQR
                upper_bound = Q3 + threshold * IQR
                df_copy = df_copy[(df_copy[col] >= lower_bound) & (df_copy[col] <= upper_bound)]
        
        elif method == 'zscore':
            from scipy import stats
            for col in target_cols:
                z_scores = np.abs(stats.zscore(df_copy[col].dropna()))
                df_copy = df_copy[z_scores < threshold]
        
        else:
            raise ValueError("method must be 'iqr' or 'zscore'")
        
        rows_removed = original_shape[0] - df_copy.shape[0]
        print(f"✓ Removed {rows_removed} outlier rows using {method.upper()} method")
        print(f"  New shape: {df_copy.shape}")
        
        return KuyaDataFrame(df_copy)
    
    def standardize_columns(self):
        """
        Make all column names lowercase and underscored.
        
        Returns:
        --------
        pd.DataFrame
            DataFrame with standardized column names
        """
        from kuya.core import KuyaDataFrame
        df_copy = self.df.copy()
        old_cols = df_copy.columns.tolist()
        new_cols = []
        
        for col in old_cols:
            # Convert to string, lowercase, replace spaces/special chars with underscore
            new_col = str(col).lower()
            new_col = re.sub(r'[^\w\s]', '', new_col)  # Remove special characters
            new_col = re.sub(r'\s+', '_', new_col)      # Replace spaces with underscore
            new_col = re.sub(r'_+', '_', new_col)       # Replace multiple underscores with single
            new_col = new_col.strip('_')                # Remove leading/trailing underscores
            new_cols.append(new_col)
        
        df_copy.columns = new_cols
        
        print("✓ Column names standardized:")
        for old, new in zip(old_cols, new_cols):
            if old != new:
                print(f"  • {old} → {new}")
        
        return KuyaDataFrame(df_copy)
