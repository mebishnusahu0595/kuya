"""
Visualization Module
Make visualizations quick and clean with one-line commands.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class KuyaViz:
    """Visualization utilities for Kuya."""
    
    def __init__(self, df):
        """
        Initialize visualizer with a DataFrame.
        
        Parameters:
        -----------
        df : pd.DataFrame
            The DataFrame to visualize
        """
        self.df = df
        # Set default style
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (10, 6)
    
    def quick_plot(self, kind, x, y=None, title=None, **kwargs):
        """
        Simple wrapper for matplotlib/seaborn plots.
        
        Parameters:
        -----------
        kind : str
            Type of plot: 'bar', 'line', 'scatter', 'box', 'violin', 'pie'
        x : str
            Column name for x-axis
        y : str, optional
            Column name for y-axis (not needed for pie charts)
        title : str, optional
            Plot title
        **kwargs : additional arguments passed to plotting function
        
        Returns:
        --------
        matplotlib figure
        """
        plt.figure(figsize=kwargs.pop('figsize', (10, 6)))
        
        if kind == 'bar':
            if y:
                sns.barplot(data=self.df, x=x, y=y, **kwargs)
            else:
                self.df[x].value_counts().plot(kind='bar', **kwargs)
            plt.xlabel(x)
            plt.ylabel(y if y else 'Count')
        
        elif kind == 'line':
            if y:
                plt.plot(self.df[x], self.df[y], **kwargs)
                plt.ylabel(y)
            else:
                plt.plot(self.df[x], **kwargs)
            plt.xlabel(x)
        
        elif kind == 'scatter':
            if not y:
                raise ValueError("scatter plot requires both x and y")
            sns.scatterplot(data=self.df, x=x, y=y, **kwargs)
            plt.xlabel(x)
            plt.ylabel(y)
        
        elif kind == 'box':
            if y:
                sns.boxplot(data=self.df, x=x, y=y, **kwargs)
            else:
                sns.boxplot(data=self.df[x], **kwargs)
        
        elif kind == 'violin':
            if y:
                sns.violinplot(data=self.df, x=x, y=y, **kwargs)
            else:
                sns.violinplot(data=self.df[x], **kwargs)
        
        elif kind == 'pie':
            if y:
                # Aggregate data
                data = self.df.groupby(x)[y].sum()
            else:
                data = self.df[x].value_counts()
            plt.pie(data.values, labels=data.index, autopct='%1.1f%%', **kwargs)
            plt.axis('equal')
        
        else:
            raise ValueError(f"Unsupported plot kind: {kind}")
        
        if title:
            plt.title(title, fontsize=14, fontweight='bold')
        else:
            plt.title(f"{kind.capitalize()} Plot: {x}" + (f" vs {y}" if y else ""), 
                     fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.show()
        
        return plt.gcf()
    
    def plot_histogram(self, column, bins=30, title=None, **kwargs):
        """
        Plots histogram for a single column.
        
        Parameters:
        -----------
        column : str
            Column name to plot
        bins : int, default=30
            Number of histogram bins
        title : str, optional
            Plot title
        **kwargs : additional arguments passed to plt.hist
        
        Returns:
        --------
        matplotlib figure
        """
        plt.figure(figsize=kwargs.pop('figsize', (10, 6)))
        
        data = self.df[column].dropna()
        
        plt.hist(data, bins=bins, edgecolor='black', alpha=0.7, **kwargs)
        plt.xlabel(column, fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        
        if title:
            plt.title(title, fontsize=14, fontweight='bold')
        else:
            plt.title(f"Distribution of {column}", fontsize=14, fontweight='bold')
        
        # Add statistics
        mean_val = data.mean()
        median_val = data.median()
        plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
        plt.axvline(median_val, color='green', linestyle='--', linewidth=2, label=f'Median: {median_val:.2f}')
        plt.legend()
        
        plt.tight_layout()
        plt.show()
        
        return plt.gcf()
    
    def corr_heatmap(self, method='pearson', annot=True, cmap='coolwarm', **kwargs):
        """
        Plots correlation heatmap.
        
        Parameters:
        -----------
        method : str, default='pearson'
            Correlation method: 'pearson', 'spearman', or 'kendall'
        annot : bool, default=True
            Whether to annotate cells with values
        cmap : str, default='coolwarm'
            Color map
        **kwargs : additional arguments passed to sns.heatmap
        
        Returns:
        --------
        matplotlib figure
        """
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) < 2:
            print("⚠️  Need at least 2 numeric columns for correlation heatmap")
            return None
        
        corr_matrix = self.df[numeric_cols].corr(method=method)
        
        plt.figure(figsize=kwargs.pop('figsize', (12, 8)))
        
        sns.heatmap(
            corr_matrix, 
            annot=annot, 
            cmap=cmap, 
            center=0,
            square=True,
            linewidths=1,
            cbar_kws={"shrink": 0.8},
            fmt='.2f',
            **kwargs
        )
        
        plt.title(f"Correlation Heatmap ({method.capitalize()})", 
                 fontsize=14, fontweight='bold', pad=20)
        plt.tight_layout()
        plt.show()
        
        return plt.gcf()
    
    def pairplot(self, columns=None, hue=None, **kwargs):
        """
        Visualizes pairwise relations between features.
        
        Parameters:
        -----------
        columns : list, optional
            Specific columns to include. If None, uses all numeric columns
        hue : str, optional
            Column name for color coding
        **kwargs : additional arguments passed to sns.pairplot
        
        Returns:
        --------
        seaborn PairGrid
        """
        if columns:
            data = self.df[columns]
        else:
            # Use numeric columns
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
            if len(numeric_cols) > 10:
                print(f"⚠️  Too many numeric columns ({len(numeric_cols)}). Using first 10.")
                numeric_cols = numeric_cols[:10]
            data = self.df[numeric_cols]
        
        if len(data.columns) < 2:
            print("⚠️  Need at least 2 columns for pairplot")
            return None
        
        print("📊 Generating pairplot... This may take a moment.")
        
        if hue and hue in self.df.columns:
            data[hue] = self.df[hue]
            pair_grid = sns.pairplot(data, hue=hue, **kwargs)
        else:
            pair_grid = sns.pairplot(data, **kwargs)
        
        plt.suptitle("Pairwise Relationships", y=1.01, fontsize=14, fontweight='bold')
        plt.show()
        
        return pair_grid
