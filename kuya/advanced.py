"""
Advanced utilities for Kuya - making data analysis extraordinary!
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Any, Optional
import warnings


class KuyaDataQuality:
    """Advanced data quality assessment tools."""
    
    def __init__(self, df):
        self.df = df
    
    def quality_report(self):
        """
        Generate comprehensive data quality report.
        
        Returns:
        --------
        dict: Quality metrics and issues
        """
        print("=" * 70)
        print("🔍 DATA QUALITY REPORT")
        print("=" * 70)
        
        issues = []
        score = 100.0
        
        # Check missing values
        missing_pct = (self.df.isnull().sum().sum() / (len(self.df) * len(self.df.columns))) * 100
        if missing_pct > 0:
            issues.append(f"Missing values: {missing_pct:.2f}% of data")
            score -= min(missing_pct * 2, 20)
        
        # Check duplicates
        dup_count = self.df.duplicated().sum()
        if dup_count > 0:
            dup_pct = (dup_count / len(self.df)) * 100
            issues.append(f"Duplicate rows: {dup_count} ({dup_pct:.2f}%)")
            score -= min(dup_pct, 15)
        
        # Check constant columns
        constant_cols = [col for col in self.df.columns if self.df[col].nunique() == 1]
        if constant_cols:
            issues.append(f"Constant columns: {len(constant_cols)} columns")
            score -= len(constant_cols) * 5
        
        # Check high cardinality
        high_card_cols = [col for col in self.df.select_dtypes(include=['object']).columns 
                         if self.df[col].nunique() > len(self.df) * 0.9]
        if high_card_cols:
            issues.append(f"High cardinality: {len(high_card_cols)} columns")
            score -= len(high_card_cols) * 3
        
        # Check numeric outliers
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        outlier_cols = []
        for col in numeric_cols:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = ((self.df[col] < (Q1 - 1.5 * IQR)) | (self.df[col] > (Q3 + 1.5 * IQR))).sum()
            if outliers > len(self.df) * 0.05:
                outlier_cols.append(col)
        if outlier_cols:
            issues.append(f"Columns with outliers: {len(outlier_cols)}")
            score -= len(outlier_cols) * 2
        
        score = max(score, 0)
        
        # Print report
        print(f"\n📊 Quality Score: {score:.1f}/100")
        
        if score >= 90:
            print("   🌟 Excellent - Data is high quality!")
        elif score >= 75:
            print("   ✅ Good - Minor issues detected")
        elif score >= 50:
            print("   ⚠️  Fair - Several issues need attention")
        else:
            print("   ❌ Poor - Significant quality issues")
        
        if issues:
            print("\n⚠️  Issues Detected:")
            for issue in issues:
                print(f"   • {issue}")
        else:
            print("\n✅ No issues detected!")
        
        # Recommendations
        print("\n💡 Recommendations:")
        if missing_pct > 5:
            print("   • Handle missing values with clean_missing()")
        if dup_count > 0:
            print("   • Remove duplicates with drop_duplicates()")
        if constant_cols:
            print(f"   • Consider removing constant columns: {constant_cols}")
        if outlier_cols:
            print("   • Check outliers with handle_outliers()")
        
        print("=" * 70)
        
        return {
            'score': score,
            'issues': issues,
            'missing_pct': missing_pct,
            'duplicates': dup_count,
            'constant_cols': constant_cols,
            'high_cardinality_cols': high_card_cols,
            'outlier_cols': outlier_cols
        }
    
    def detect_duplicates(self, subset=None):
        """
        Detect and show duplicate rows.
        
        Parameters:
        -----------
        subset : list, optional
            Columns to consider for duplicates
        
        Returns:
        --------
        pd.DataFrame: Duplicate rows
        """
        duplicates = self.df[self.df.duplicated(subset=subset, keep=False)]
        
        if len(duplicates) == 0:
            print("✅ No duplicate rows found!")
            return pd.DataFrame()
        
        dup_count = self.df.duplicated(subset=subset).sum()
        print(f"⚠️  Found {dup_count} duplicate rows:")
        print(duplicates.head(10))
        
        return duplicates
    
    def suggest_dtypes(self):
        """
        Suggest optimal data types for memory optimization.
        
        Returns:
        --------
        dict: Suggested dtype conversions
        """
        suggestions = {}
        
        for col in self.df.columns:
            current_dtype = self.df[col].dtype
            
            if current_dtype == 'int64':
                max_val = self.df[col].max()
                min_val = self.df[col].min()
                
                if min_val >= 0 and max_val <= 255:
                    suggestions[col] = ('int64', 'uint8', '87.5% memory savings')
                elif min_val >= 0 and max_val <= 65535:
                    suggestions[col] = ('int64', 'uint16', '75% memory savings')
                elif min_val >= -128 and max_val <= 127:
                    suggestions[col] = ('int64', 'int8', '87.5% memory savings')
                elif min_val >= -32768 and max_val <= 32767:
                    suggestions[col] = ('int64', 'int16', '75% memory savings')
            
            elif current_dtype == 'float64':
                if self.df[col].apply(lambda x: x == int(x) if pd.notnull(x) else True).all():
                    suggestions[col] = ('float64', 'int32', 'Convert to integer')
                else:
                    suggestions[col] = ('float64', 'float32', '50% memory savings')
            
            elif current_dtype == 'object':
                nunique = self.df[col].nunique()
                if nunique / len(self.df) < 0.5:
                    suggestions[col] = ('object', 'category', f'{(1 - nunique/len(self.df))*100:.0f}% memory savings')
        
        if suggestions:
            print("💡 Memory Optimization Suggestions:")
            print(f"{'Column':<20} {'Current':<15} {'Suggested':<15} {'Benefit'}")
            print("-" * 70)
            for col, (curr, sugg, benefit) in suggestions.items():
                print(f"{col:<20} {curr:<15} {sugg:<15} {benefit}")
        else:
            print("✅ Data types are already optimized!")
        
        return suggestions


class KuyaTransform:
    """Advanced data transformation utilities."""
    
    def __init__(self, df):
        self.df = df
    
    def smart_encode(self, columns=None, method='auto'):
        """
        Intelligently encode categorical variables.
        
        Parameters:
        -----------
        columns : list, optional
            Columns to encode
        method : str
            'auto', 'label', 'onehot'
        
        Returns:
        --------
        pd.DataFrame: Encoded DataFrame
        """
        from kuya.core import KuyaDataFrame
        df_copy = self.df.copy()
        
        if columns is None:
            columns = df_copy.select_dtypes(include=['object', 'category']).columns.tolist()
        
        encoded_cols = []
        
        for col in columns:
            nunique = df_copy[col].nunique()
            
            if method == 'auto':
                if nunique == 2:
                    # Binary encoding
                    df_copy[col] = df_copy[col].astype('category').cat.codes
                    encoded_cols.append(f"{col} → Binary encoding")
                elif nunique <= 5:
                    # One-hot encoding
                    dummies = pd.get_dummies(df_copy[col], prefix=col)
                    df_copy = pd.concat([df_copy, dummies], axis=1)
                    df_copy.drop(col, axis=1, inplace=True)
                    encoded_cols.append(f"{col} → One-hot encoding ({nunique} categories)")
                else:
                    # Label encoding
                    df_copy[col] = df_copy[col].astype('category').cat.codes
                    encoded_cols.append(f"{col} → Label encoding")
            
            elif method == 'label':
                df_copy[col] = df_copy[col].astype('category').cat.codes
                encoded_cols.append(f"{col} → Label encoding")
            
            elif method == 'onehot':
                dummies = pd.get_dummies(df_copy[col], prefix=col)
                df_copy = pd.concat([df_copy, dummies], axis=1)
                df_copy.drop(col, axis=1, inplace=True)
                encoded_cols.append(f"{col} → One-hot encoding")
        
        if encoded_cols:
            print("✓ Encoded categorical variables:")
            for enc in encoded_cols:
                print(f"  • {enc}")
        
        return KuyaDataFrame(df_copy)
    
    def normalize(self, columns=None, method='minmax'):
        """
        Normalize numeric columns.
        
        Parameters:
        -----------
        columns : list, optional
            Columns to normalize
        method : str
            'minmax', 'zscore', 'robust'
        
        Returns:
        --------
        pd.DataFrame: Normalized DataFrame
        """
        from kuya.core import KuyaDataFrame
        df_copy = self.df.copy()
        
        if columns is None:
            columns = df_copy.select_dtypes(include=[np.number]).columns.tolist()
        
        for col in columns:
            if method == 'minmax':
                min_val = df_copy[col].min()
                max_val = df_copy[col].max()
                df_copy[col] = (df_copy[col] - min_val) / (max_val - min_val)
            
            elif method == 'zscore':
                mean_val = df_copy[col].mean()
                std_val = df_copy[col].std()
                df_copy[col] = (df_copy[col] - mean_val) / std_val
            
            elif method == 'robust':
                median_val = df_copy[col].median()
                q75 = df_copy[col].quantile(0.75)
                q25 = df_copy[col].quantile(0.25)
                iqr = q75 - q25
                df_copy[col] = (df_copy[col] - median_val) / iqr
        
        print(f"✓ Normalized {len(columns)} columns using {method} method")
        
        return KuyaDataFrame(df_copy)
    
    def create_features(self):
        """
        Auto-generate useful features from existing columns.
        
        Returns:
        --------
        pd.DataFrame: DataFrame with new features
        """
        from kuya.core import KuyaDataFrame
        df_copy = self.df.copy()
        new_features = []
        
        # Date features
        date_cols = df_copy.select_dtypes(include=['datetime64']).columns
        for col in date_cols:
            df_copy[f'{col}_year'] = df_copy[col].dt.year
            df_copy[f'{col}_month'] = df_copy[col].dt.month
            df_copy[f'{col}_day'] = df_copy[col].dt.day
            df_copy[f'{col}_dayofweek'] = df_copy[col].dt.dayofweek
            df_copy[f'{col}_quarter'] = df_copy[col].dt.quarter
            new_features.extend([f'{col}_year', f'{col}_month', f'{col}_day', 
                               f'{col}_dayofweek', f'{col}_quarter'])
        
        # Numeric interactions (top correlations)
        numeric_cols = df_copy.select_dtypes(include=[np.number]).columns.tolist()
        if len(numeric_cols) >= 2:
            # Create ratio features for highly correlated columns
            corr_matrix = df_copy[numeric_cols].corr()
            for i in range(len(numeric_cols)):
                for j in range(i+1, len(numeric_cols)):
                    col1, col2 = numeric_cols[i], numeric_cols[j]
                    if abs(corr_matrix.iloc[i, j]) > 0.7:
                        # Avoid division by zero
                        if (df_copy[col2] != 0).all():
                            df_copy[f'{col1}_div_{col2}'] = df_copy[col1] / df_copy[col2]
                            new_features.append(f'{col1}_div_{col2}')
        
        if new_features:
            print(f"✓ Created {len(new_features)} new features:")
            for feat in new_features[:10]:
                print(f"  • {feat}")
            if len(new_features) > 10:
                print(f"  ... and {len(new_features) - 10} more")
        
        return KuyaDataFrame(df_copy)


class KuyaInsights:
    """Advanced automated insights generation."""
    
    def __init__(self, df):
        self.df = df
    
    def auto_insights(self):
        """
        Generate automated insights from data.
        
        Returns:
        --------
        list: List of insights
        """
        insights = []
        
        print("=" * 70)
        print("💡 AUTOMATED INSIGHTS")
        print("=" * 70)
        
        # Insight 1: Data size
        rows, cols = self.df.shape
        insights.append(f"Dataset contains {rows:,} rows and {cols} columns")
        
        # Insight 2: Missing data patterns
        missing_cols = self.df.columns[self.df.isnull().any()].tolist()
        if missing_cols:
            insights.append(f"{len(missing_cols)} columns have missing values")
        
        # Insight 3: Numeric distributions
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            skew = self.df[col].skew()
            if abs(skew) > 1:
                direction = "right" if skew > 0 else "left"
                insights.append(f"'{col}' is highly skewed {direction} (skew={skew:.2f})")
        
        # Insight 4: Categorical insights
        cat_cols = self.df.select_dtypes(include=['object', 'category']).columns
        for col in cat_cols:
            nunique = self.df[col].nunique()
            if nunique == 1:
                insights.append(f"'{col}' has only one unique value - consider removing")
            elif nunique == len(self.df):
                insights.append(f"'{col}' appears to be a unique identifier")
            elif nunique < 10:
                top_val = self.df[col].mode()[0]
                top_pct = (self.df[col] == top_val).sum() / len(self.df) * 100
                if top_pct > 50:
                    insights.append(f"'{col}': '{top_val}' dominates ({top_pct:.1f}% of data)")
        
        # Insight 5: Correlations
        if len(numeric_cols) >= 2:
            corr_matrix = self.df[numeric_cols].corr()
            for i in range(len(numeric_cols)):
                for j in range(i+1, len(numeric_cols)):
                    corr_val = corr_matrix.iloc[i, j]
                    if abs(corr_val) > 0.8:
                        col1, col2 = numeric_cols[i], numeric_cols[j]
                        insights.append(f"Strong correlation between '{col1}' and '{col2}' ({corr_val:.2f})")
        
        # Print insights
        print(f"\n🔍 Found {len(insights)} insights:\n")
        for i, insight in enumerate(insights, 1):
            print(f"{i}. {insight}")
        
        print("\n" + "=" * 70)
        
        return insights
    
    def compare_groups(self, group_col, value_col):
        """
        Compare groups and find significant differences.
        
        Parameters:
        -----------
        group_col : str
            Column to group by
        value_col : str
            Column to analyze
        
        Returns:
        --------
        pd.DataFrame: Group statistics
        """
        stats = self.df.groupby(group_col)[value_col].agg([
            ('count', 'count'),
            ('mean', 'mean'),
            ('median', 'median'),
            ('std', 'std'),
            ('min', 'min'),
            ('max', 'max')
        ]).round(2)
        
        print(f"📊 Group Analysis: {value_col} by {group_col}")
        print(stats)
        
        # Find significant differences
        overall_mean = self.df[value_col].mean()
        print(f"\n💡 Insights:")
        for group in stats.index:
            group_mean = stats.loc[group, 'mean']
            diff_pct = ((group_mean - overall_mean) / overall_mean) * 100
            if abs(diff_pct) > 20:
                direction = "above" if diff_pct > 0 else "below"
                print(f"  • {group}: {abs(diff_pct):.1f}% {direction} average")
        
        return stats


# Convenience Functions

def quick_clean(df, handle_missing='auto', handle_outliers=True, 
                standardize_cols=True, fix_types=True):
    """
    One-command data cleaning with smart defaults.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to clean
    handle_missing : str, default='auto'
        'auto' = smart detection, 'drop' = remove rows, 'fill' = fill with mean/mode
    handle_outliers : bool, default=True
        Whether to remove outliers using IQR method
    standardize_cols : bool, default=True
        Whether to standardize column names
    fix_types : bool, default=True
        Whether to auto-convert data types
    
    Returns:
    --------
    KuyaDataFrame
        Cleaned DataFrame
    """
    from kuya.core import KuyaDataFrame
    
    print("🧹 Quick Clean Starting...")
    print("=" * 50)
    
    df_clean = KuyaDataFrame(df.copy())
    
    # Step 1: Standardize columns
    if standardize_cols:
        print("\n📝 Step 1/4: Standardizing column names...")
        df_clean = df_clean.standardize_columns()
    
    # Step 2: Fix data types
    if fix_types:
        print("\n🔧 Step 2/4: Fixing data types...")
        df_clean = df_clean.fix_dtypes()
    
    # Step 3: Handle missing values
    print("\n🔍 Step 3/4: Handling missing values...")
    missing_before = df_clean.isnull().sum().sum()
    
    if handle_missing == 'auto':
        # Smart detection: if < 5% missing, fill; otherwise drop
        missing_pct = (missing_before / (df_clean.shape[0] * df_clean.shape[1])) * 100
        if missing_pct < 5:
            # Fill numeric with median, categorical with mode
            numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
            for col in numeric_cols:
                if df_clean[col].isnull().any():
                    df_clean[col] = df_clean[col].fillna(df_clean[col].median())
            
            categorical_cols = df_clean.select_dtypes(include=['object']).columns
            for col in categorical_cols:
                if df_clean[col].isnull().any():
                    mode_val = df_clean[col].mode()
                    if len(mode_val) > 0:
                        df_clean[col] = df_clean[col].fillna(mode_val[0])
            print(f"  ✓ Filled {missing_before} missing values intelligently")
        else:
            df_clean = df_clean.dropna()
            print(f"  ✓ Dropped rows with missing values ({missing_pct:.1f}% missing)")
    elif handle_missing == 'drop':
        df_clean = df_clean.dropna()
        print(f"  ✓ Dropped rows with missing values")
    elif handle_missing == 'fill':
        df_clean = df_clean.clean_missing(method='fill')
    
    # Convert back to KuyaDataFrame after fillna
    df_clean = KuyaDataFrame(df_clean)
    
    # Step 4: Handle outliers
    if handle_outliers:
        print("\n📊 Step 4/4: Handling outliers...")
        df_clean = df_clean.handle_outliers(method='iqr')
    
    print("\n" + "=" * 50)
    print(f"✨ Quick Clean Complete!")
    print(f"   Original shape: {df.shape}")
    print(f"   Cleaned shape: {df_clean.shape}")
    print("=" * 50)
    
    return df_clean


def smart_analysis(df):
    """
    Automated intelligent analysis with AI-like insights.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to analyze
    
    Returns:
    --------
    dict
        Dictionary containing insights and recommendations
    """
    from kuya.core import KuyaDataFrame
    
    print("🤖 Smart Analysis Starting...")
    print("=" * 50)
    
    if not isinstance(df, KuyaDataFrame):
        df = KuyaDataFrame(df)
    
    insights = {
        'warnings': [],
        'recommendations': [],
        'highlights': [],
        'summary': {}
    }
    
    # Analyze missing values
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    high_missing = missing_pct[missing_pct > 20]
    
    if len(high_missing) > 0:
        insights['warnings'].append(
            f"⚠️  High missing values detected in {len(high_missing)} columns"
        )
        insights['recommendations'].append(
            "Consider dropping columns with >20% missing data or investigating why data is missing"
        )
    
    # Analyze data types
    object_cols = df.select_dtypes(include=['object']).columns
    if len(object_cols) > 0:
        insights['recommendations'].append(
            f"💡 {len(object_cols)} text columns detected - consider encoding for machine learning"
        )
    
    # Analyze correlations
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) >= 2:
        corr_matrix = df[numeric_cols].corr()
        high_corr = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                if abs(corr_matrix.iloc[i, j]) > 0.8:
                    high_corr.append((corr_matrix.columns[i], 
                                     corr_matrix.columns[j], 
                                     corr_matrix.iloc[i, j]))
        
        if high_corr:
            insights['highlights'].append(
                f"🔥 Found {len(high_corr)} strong correlations (|r| > 0.8)"
            )
            for col1, col2, corr in high_corr:
                insights['highlights'].append(f"   • {col1} ↔ {col2}: {corr:.3f}")
    
    # Analyze unique values
    for col in df.columns:
        unique_pct = (df[col].nunique() / len(df)) * 100
        if unique_pct > 95:
            insights['warnings'].append(
                f"🔑 '{col}' might be an ID column ({unique_pct:.0f}% unique)"
            )
        elif unique_pct < 5 and df[col].nunique() > 1:
            insights['highlights'].append(
                f"📊 '{col}' has low cardinality ({df[col].nunique()} unique values) - good for grouping"
            )
    
    # Summary statistics
    insights['summary'] = {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'numeric_columns': len(numeric_cols),
        'categorical_columns': len(object_cols),
        'missing_cells': int(missing.sum()),
        'memory_mb': df.memory_usage(deep=True).sum() / 1024**2
    }
    
    # Print insights
    print("\n🎯 INSIGHTS:")
    print("-" * 50)
    
    if insights['warnings']:
        print("\n⚠️  Warnings:")
        for warning in insights['warnings']:
            print(f"  {warning}")
    
    if insights['recommendations']:
        print("\n💡 Recommendations:")
        for rec in insights['recommendations']:
            print(f"  {rec}")
    
    if insights['highlights']:
        print("\n🔥 Highlights:")
        for highlight in insights['highlights']:
            print(f"  {highlight}")
    
    print("\n📊 Summary:")
    for key, value in insights['summary'].items():
        print(f"  • {key.replace('_', ' ').title()}: {value}")
    
    print("\n" + "=" * 50)
    print("✨ Smart Analysis Complete!")
    print("=" * 50)
    
    return insights


def auto_report(df, output_path='kuya_report', format='txt'):
    """
    Generate an automated analysis report.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to analyze
    output_path : str
        Path for the output report
    format : str
        Report format: 'txt' or 'html'
    
    Returns:
    --------
    str
        Path to the generated report
    """
    from kuya.core import KuyaDataFrame
    from datetime import datetime
    
    print(f"📝 Generating {format.upper()} report...")
    
    if not isinstance(df, KuyaDataFrame):
        df = KuyaDataFrame(df)
    
    # Add extension if not present
    if not output_path.endswith(f'.{format}'):
        output_path = f"{output_path}.{format}"
    
    if format == 'txt':
        _generate_txt_report(df, output_path)
    elif format == 'html':
        _generate_html_report(df, output_path)
    else:
        raise ValueError("Format must be 'txt' or 'html'")
    
    print(f"✓ Report saved to: {output_path}")
    return output_path


def _generate_txt_report(df, output_path):
    """Generate a text report."""
    from datetime import datetime
    
    with open(output_path, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write("KUYA AUTOMATED DATA ANALYSIS REPORT\n")
        f.write("=" * 70 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 70 + "\n\n")
        
        # Basic info
        f.write("1. DATASET OVERVIEW\n")
        f.write("-" * 70 + "\n")
        f.write(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")
        f.write(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB\n\n")
        
        # Column info
        f.write("2. COLUMN INFORMATION\n")
        f.write("-" * 70 + "\n")
        for col in df.columns:
            f.write(f"\n{col}:\n")
            f.write(f"  Type: {df[col].dtype}\n")
            f.write(f"  Missing: {df[col].isnull().sum()} ({df[col].isnull().sum()/len(df)*100:.1f}%)\n")
            f.write(f"  Unique: {df[col].nunique()}\n")
        
        # Numeric summary
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            f.write("\n\n3. NUMERIC COLUMNS SUMMARY\n")
            f.write("-" * 70 + "\n")
            f.write(df[numeric_cols].describe().to_string())
        
        # Correlations
        if len(numeric_cols) >= 2:
            f.write("\n\n4. CORRELATIONS\n")
            f.write("-" * 70 + "\n")
            corr = df[numeric_cols].corr()
            f.write(corr.to_string())
        
        f.write("\n\n" + "=" * 70 + "\n")
        f.write("END OF REPORT\n")
        f.write("=" * 70 + "\n")


def _generate_html_report(df, output_path):
    """Generate an HTML report."""
    from datetime import datetime
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kuya Data Analysis Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
            .container {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
            h2 {{ color: #34495e; margin-top: 30px; }}
            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
            th, td {{ padding: 12px; text-align: left; border: 1px solid #ddd; }}
            th {{ background: #3498db; color: white; }}
            tr:nth-child(even) {{ background: #f9f9f9; }}
            .metric {{ display: inline-block; margin: 10px 20px 10px 0; padding: 15px; 
                      background: #ecf0f1; border-radius: 5px; }}
            .metric-value {{ font-size: 24px; font-weight: bold; color: #2c3e50; }}
            .metric-label {{ font-size: 12px; color: #7f8c8d; text-transform: uppercase; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Kuya Data Analysis Report</h1>
            <p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            
            <h2>Dataset Overview</h2>
            <div class="metric">
                <div class="metric-value">{df.shape[0]:,}</div>
                <div class="metric-label">Rows</div>
            </div>
            <div class="metric">
                <div class="metric-value">{df.shape[1]}</div>
                <div class="metric-label">Columns</div>
            </div>
            <div class="metric">
                <div class="metric-value">{df.memory_usage(deep=True).sum() / 1024**2:.1f} MB</div>
                <div class="metric-label">Memory</div>
            </div>
            
            <h2>Column Information</h2>
            <table>
                <tr>
                    <th>Column</th>
                    <th>Type</th>
                    <th>Missing</th>
                    <th>Unique</th>
                </tr>
    """
    
    for col in df.columns:
        missing_pct = df[col].isnull().sum() / len(df) * 100
        html += f"""
                <tr>
                    <td>{col}</td>
                    <td>{df[col].dtype}</td>
                    <td>{df[col].isnull().sum()} ({missing_pct:.1f}%)</td>
                    <td>{df[col].nunique()}</td>
                </tr>
        """
    
    html += """
            </table>
            
            <h2>Numeric Summary</h2>
    """
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        html += df[numeric_cols].describe().to_html()
    else:
        html += "<p>No numeric columns found.</p>"
    
    html += """
        </div>
    </body>
    </html>
    """
    
    with open(output_path, 'w') as f:
        f.write(html)
