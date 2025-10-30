"""
Core module for extending Pandas DataFrame with Kuya methods.
"""

import pandas as pd
from kuya.clean import KuyaCleaner
from kuya.eda import KuyaEDA
from kuya.viz import KuyaViz
from kuya.advanced import KuyaDataQuality, KuyaTransform, KuyaInsights


class KuyaDataFrame(pd.DataFrame):
    """
    Extended Pandas DataFrame with Kuya's helper methods.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cleaner = KuyaCleaner(self)
        self._eda = KuyaEDA(self)
        self._viz = KuyaViz(self)
        
        # Lazy load advanced features
        self._quality = None
        self._transform = None
        self._insights = None
        self._quality = KuyaDataQuality(self)
        self._transform = KuyaTransform(self)
        self._insights = KuyaInsights(self)
    
    # Clean methods
    def clean_missing(self, method='drop', value=None, columns=None):
        """Drop or fill missing values automatically."""
        return self._cleaner.clean_missing(method, value, columns)
    
    def fix_dtypes(self):
        """Auto-convert columns to numeric, datetime, etc."""
        return self._cleaner.fix_dtypes()
    
    def handle_outliers(self, method='iqr', columns=None):
        """Detect and remove outliers using IQR or Z-score."""
        return self._cleaner.handle_outliers(method, columns)
    
    def standardize_columns(self):
        """Make all column names lowercase and underscored."""
        return self._cleaner.standardize_columns()
    
    # EDA methods
    def summary(self):
        """Returns full descriptive summary."""
        return self._eda.summary()
    
    def check_missing(self):
        """Shows missing value count and percentage."""
        return self._eda.check_missing()
    
    def unique_summary(self):
        """Shows count of unique values for each column."""
        return self._eda.unique_summary()
    
    def correlation_report(self):
        """Displays correlation table."""
        return self._eda.correlation_report()
    
    # Visualization methods
    def quick_plot(self, kind, x, y=None, **kwargs):
        """Simple wrapper for matplotlib/seaborn."""
        return self._viz.quick_plot(kind, x, y, **kwargs)
    
    def plot_histogram(self, column, **kwargs):
        """Plots histogram for a single column."""
        return self._viz.plot_histogram(column, **kwargs)
    
    def corr_heatmap(self, **kwargs):
        """Plots correlation heatmap."""
        return self._viz.corr_heatmap(**kwargs)
    
    def pairplot(self, columns=None, **kwargs):
        """Visualizes pairwise relations between features."""
        return self._viz.pairplot(columns, **kwargs)
    
    # Advanced methods
    def quality_report(self):
        """Generate comprehensive data quality report."""
        if self._quality is None:
            from kuya.advanced import KuyaDataQuality
            self._quality = KuyaDataQuality(self)
        return self._quality.quality_report()
    
    def smart_encode(self, columns=None, method='auto'):
        """Intelligently encode categorical variables."""
        if self._transform is None:
            from kuya.advanced import KuyaTransform
            self._transform = KuyaTransform(self)
        return self._transform.smart_encode(columns, method)
    
    def normalize(self, columns=None, method='minmax'):
        """Normalize numeric columns."""
        if self._transform is None:
            from kuya.advanced import KuyaTransform
            self._transform = KuyaTransform(self)
        return self._transform.normalize(columns, method)
    
    def smart_analysis(self):
        """Automated intelligent analysis with AI-like insights."""
        from kuya.advanced import smart_analysis
        return smart_analysis(self)
    
    def auto_insights(self):
        """Generate automated insights from data."""
        if self._insights is None:
            from kuya.advanced import KuyaInsights
            self._insights = KuyaInsights(self)
        return self._insights.auto_insights()
    
    # Advanced Quality methods
    def quality_report(self):
        """Generate comprehensive data quality report."""
        return self._quality.quality_report()
    
    def detect_duplicates(self, subset=None):
        """Detect and show duplicate rows."""
        return self._quality.detect_duplicates(subset)
    
    def suggest_dtypes(self):
        """Suggest optimal data types for memory optimization."""
        return self._quality.suggest_dtypes()
    
    # Advanced Transform methods
    def smart_encode(self, columns=None, method='auto'):
        """Intelligently encode categorical variables."""
        return self._transform.smart_encode(columns, method)
    
    def normalize(self, columns=None, method='minmax'):
        """Normalize numeric columns."""
        return self._transform.normalize(columns, method)
    
    def create_features(self):
        """Auto-generate useful features from existing columns."""
        return self._transform.create_features()
    
    # Advanced Insights methods
    def auto_insights(self):
        """Generate automated insights from data."""
        return self._insights.auto_insights()
    
    def compare_groups(self, group_col, value_col):
        """Compare groups and find significant differences."""
        return self._insights.compare_groups(group_col, value_col)
    
    def magic_analyze(self, target_col=None):
        """
        🪄 MAGIC ANALYZE - Complete automated analysis with one command!
        
        This is Kuya's most powerful feature - it performs a comprehensive
        analysis including cleaning, quality assessment, insights, and 
        visualizations automatically.
        
        Parameters:
        -----------
        target_col : str, optional
            Target column for focused analysis
        
        Returns:
        --------
        dict: Complete analysis results
        """
        print("\n" + "🌟" * 35)
        print("✨ KUYA MAGIC ANALYZE - COMPLETE AUTOMATED ANALYSIS ✨")
        print("🌟" * 35 + "\n")
        
        results = {}
        
        # Step 1: Quality Assessment
        print("🔍 Step 1/5: Assessing Data Quality...")
        results['quality'] = self.quality_report()
        
        # Step 2: Basic Statistics
        print("\n📊 Step 2/5: Computing Statistics...")
        self.summary()
        
        # Step 3: Generate Insights
        print("\n💡 Step 3/5: Generating Insights...")
        results['insights'] = self.auto_insights()
        
        # Step 4: Correlations
        print("\n🔗 Step 4/5: Analyzing Relationships...")
        numeric_cols = self.select_dtypes(include=['number']).columns
        if len(numeric_cols) >= 2:
            results['correlations'] = self.correlation_report()
        
        # Step 5: Visualizations
        print("\n📈 Step 5/5: Creating Visualizations...")
        
        # Histogram for target or first numeric column
        if target_col:
            self.plot_histogram(target_col)
        elif len(numeric_cols) > 0:
            self.plot_histogram(numeric_cols[0])
        
        # Correlation heatmap if enough numeric columns
        if len(numeric_cols) >= 2:
            self.corr_heatmap()
        
        print("\n" + "🌟" * 35)
        print("✅ MAGIC ANALYZE COMPLETE!")
        print("🌟" * 35 + "\n")
        
        return results
