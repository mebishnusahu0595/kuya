"""
Kuya - Your Friendly Data Analysis Assistant
Built on top of Pandas to make data cleaning, exploration, and visualization effortless.

Author: Bishnu PS
Version: 0.1.0
"""

__version__ = "0.1.0"
__author__ = "Bishnu PS"

# Import main modules
from kuya.clean import KuyaCleaner
from kuya.eda import KuyaEDA
from kuya.viz import KuyaViz
from kuya.io import load, save

# Import core DataFrame extension
from kuya.core import KuyaDataFrame

# Import advanced features
from kuya.advanced import (
    quick_clean,
    smart_analysis,
    auto_report,
    KuyaDataQuality,
    KuyaTransform,
    KuyaInsights
)

# Convenience imports
__all__ = [
    'KuyaDataFrame',
    'KuyaCleaner',
    'KuyaEDA', 
    'KuyaViz',
    'load',
    'save',
    'quick_clean',
    'smart_analysis',
    'auto_report',
    'KuyaDataQuality',
    'KuyaTransform',
    'KuyaInsights',
]

# Quick access message
print("🎉 Kuya loaded successfully! Your data assistant is ready.")
