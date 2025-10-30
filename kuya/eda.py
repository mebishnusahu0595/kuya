"""
Exploratory Data Analysis Module
Get instant insights and summaries from your dataset.
"""

import pandas as pd
import numpy as np


class KuyaEDA:
    """Exploratory Data Analysis utilities for Kuya."""
    
    def __init__(self, df):
        """
        Initialize EDA with a DataFrame.
        
        Parameters:
        -----------
        df : pd.DataFrame
            The DataFrame to analyze
        """
        self.df = df
    
    def summary(self):
        """
        Returns full descriptive summary (like pandas_profiling lite).
        
        Returns:
        --------
        dict
            Dictionary containing various summaries
        """
        print("=" * 60)
        print("📊 KUYA DATA SUMMARY")
        print("=" * 60)
        
        # Basic info
        print(f"\n📁 Dataset Shape: {self.df.shape[0]} rows × {self.df.shape[1]} columns")
        print(f"💾 Memory Usage: {self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        # Data types
        print("\n📋 Column Types:")
        dtype_counts = self.df.dtypes.value_counts()
        for dtype, count in dtype_counts.items():
            print(f"  • {dtype}: {count} columns")
        
        # Missing values summary
        missing = self.df.isnull().sum()
        if missing.sum() > 0:
            print("\n⚠️  Missing Values:")
            missing_pct = (missing / len(self.df)) * 100
            missing_df = pd.DataFrame({
                'Missing Count': missing[missing > 0],
                'Percentage': missing_pct[missing > 0]
            })
            print(missing_df.to_string())
        else:
            print("\n✓ No missing values detected")
        
        # Numeric summary
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            print(f"\n🔢 Numeric Columns Summary ({len(numeric_cols)} columns):")
            print(self.df[numeric_cols].describe().round(2).to_string())
        
        # Categorical summary
        categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns
        if len(categorical_cols) > 0:
            print(f"\n📝 Categorical Columns Summary ({len(categorical_cols)} columns):")
            for col in categorical_cols[:5]:  # Show first 5
                unique_count = self.df[col].nunique()
                most_common = self.df[col].mode()[0] if len(self.df[col].mode()) > 0 else 'N/A'
                print(f"  • {col}: {unique_count} unique values, most common: '{most_common}'")
            if len(categorical_cols) > 5:
                print(f"  ... and {len(categorical_cols) - 5} more categorical columns")
        
        print("\n" + "=" * 60)
        
        return {
            'shape': self.df.shape,
            'dtypes': self.df.dtypes,
            'missing': missing,
            'numeric_summary': self.df[numeric_cols].describe() if len(numeric_cols) > 0 else None,
            'categorical_cols': categorical_cols.tolist()
        }
    
    def check_missing(self):
        """
        Shows missing value count and percentage.
        
        Returns:
        --------
        pd.DataFrame
            DataFrame with missing value statistics
        """
        missing_count = self.df.isnull().sum()
        missing_pct = (missing_count / len(self.df)) * 100
        
        missing_df = pd.DataFrame({
            'Column': self.df.columns,
            'Missing Count': missing_count.values,
            'Missing %': missing_pct.values
        })
        
        missing_df = missing_df[missing_df['Missing Count'] > 0].sort_values(
            'Missing Count', ascending=False
        )
        
        if len(missing_df) == 0:
            print("✓ No missing values found!")
            return pd.DataFrame()
        
        print(f"⚠️  Found missing values in {len(missing_df)} columns:")
        print(missing_df.to_string(index=False))
        
        return missing_df
    
    def unique_summary(self):
        """
        Shows count of unique values for each column.
        
        Returns:
        --------
        pd.DataFrame
            DataFrame with unique value counts
        """
        unique_counts = []
        
        for col in self.df.columns:
            nunique = self.df[col].nunique()
            nunique_pct = (nunique / len(self.df)) * 100
            unique_counts.append({
                'Column': col,
                'Unique Values': nunique,
                'Unique %': round(nunique_pct, 2),
                'Data Type': str(self.df[col].dtype)
            })
        
        unique_df = pd.DataFrame(unique_counts)
        
        print("🔍 Unique Values Summary:")
        print(unique_df.to_string(index=False))
        
        # Highlight potential ID columns or constants
        potential_ids = unique_df[unique_df['Unique %'] > 95]['Column'].tolist()
        constants = unique_df[unique_df['Unique Values'] == 1]['Column'].tolist()
        
        if potential_ids:
            print(f"\n💡 Potential ID columns (>95% unique): {', '.join(potential_ids)}")
        if constants:
            print(f"⚠️  Constant columns (only 1 value): {', '.join(constants)}")
        
        return unique_df
    
    def correlation_report(self, method='pearson'):
        """
        Displays correlation table with heatmap.
        
        Parameters:
        -----------
        method : str, default='pearson'
            Correlation method: 'pearson', 'spearman', or 'kendall'
        
        Returns:
        --------
        pd.DataFrame
            Correlation matrix
        """
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) < 2:
            print("⚠️  Need at least 2 numeric columns for correlation analysis")
            return pd.DataFrame()
        
        corr_matrix = self.df[numeric_cols].corr(method=method)
        
        print(f"🔗 Correlation Matrix ({method.capitalize()} method):")
        print(corr_matrix.round(3).to_string())
        
        # Find strong correlations (excluding diagonal)
        print("\n🔥 Strong Correlations (|r| > 0.7):")
        strong_corrs = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                col1 = corr_matrix.columns[i]
                col2 = corr_matrix.columns[j]
                corr_val = corr_matrix.iloc[i, j]
                if abs(corr_val) > 0.7:
                    strong_corrs.append(f"  • {col1} ↔ {col2}: {corr_val:.3f}")
        
        if strong_corrs:
            for corr in strong_corrs:
                print(corr)
        else:
            print("  No strong correlations found")
        
        return corr_matrix
