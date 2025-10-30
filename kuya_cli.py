#!/usr/bin/env python3
"""
Kuya CLI - Command Line Interface for quick data analysis
Usage: kuya analyze <file> [--target COLUMN]
"""

import argparse
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import kuya as ky
from kuya.core import KuyaDataFrame


def print_banner():
    """Print Kuya CLI banner."""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║      ██╗  ██╗██╗   ██╗██╗   ██╗ █████╗                  ║
    ║      ██║ ██╔╝██║   ██║╚██╗ ██╔╝██╔══██╗                 ║
    ║      █████╔╝ ██║   ██║ ╚████╔╝ ███████║                 ║
    ║      ██╔═██╗ ██║   ██║  ╚██╔╝  ██╔══██║                 ║
    ║      ██║  ██╗╚██████╔╝   ██║   ██║  ██║                 ║
    ║      ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝                 ║
    ║                                                           ║
    ║        Your Friendly Data Analysis Assistant              ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)


def analyze_file(filepath, target=None, output=None):
    """Perform magic analysis on a file."""
    print_banner()
    
    # Check if file exists
    if not os.path.exists(filepath):
        print(f"❌ Error: File not found: {filepath}")
        return 1
    
    print(f"📂 Loading: {filepath}\n")
    
    try:
        # Load data
        df = ky.load(filepath)
        df = KuyaDataFrame(df)
        
        # Perform magic analysis
        results = df.magic_analyze(target_col=target)
        
        # Save results if requested
        if output:
            print(f"\n💾 Saving cleaned data to: {output}")
            df_clean = df.clean_missing(method='fill')
            df_clean = df_clean.handle_outliers(method='iqr')
            ky.save(df_clean, output)
            print("✅ Saved successfully!")
        
        print("\n🎉 Analysis complete! Kuya has finished analyzing your data.")
        return 0
        
    except Exception as e:
        print(f"\n❌ Error during analysis: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


def quick_clean(filepath, output):
    """Quick clean and save."""
    print_banner()
    print(f"🧹 Quick Clean: {filepath}\n")
    
    try:
        df = ky.load(filepath)
        df = KuyaDataFrame(df)
        
        print("Cleaning steps:")
        df = df.standardize_columns()
        df = df.fix_dtypes()
        df = df.clean_missing(method='fill')
        df = df.handle_outliers(method='iqr')
        
        ky.save(df, output)
        print(f"\n✅ Cleaned data saved to: {output}")
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return 1


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Kuya - Your Friendly Data Analysis Assistant',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  kuya analyze data.csv                    # Full analysis
  kuya analyze data.csv --target sales     # Focus on 'sales' column
  kuya analyze data.csv --output clean.csv # Save cleaned data
  kuya clean data.csv --output clean.csv   # Quick clean only
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Perform complete analysis')
    analyze_parser.add_argument('file', help='Data file to analyze')
    analyze_parser.add_argument('--target', '-t', help='Target column for focused analysis')
    analyze_parser.add_argument('--output', '-o', help='Save cleaned data to file')
    
    # Clean command
    clean_parser = subparsers.add_parser('clean', help='Quick clean data')
    clean_parser.add_argument('file', help='Data file to clean')
    clean_parser.add_argument('--output', '-o', required=True, help='Output file')
    
    # Version command
    version_parser = subparsers.add_parser('version', help='Show version')
    
    args = parser.parse_args()
    
    if args.command == 'analyze':
        return analyze_file(args.file, args.target, args.output)
    elif args.command == 'clean':
        return quick_clean(args.file, args.output)
    elif args.command == 'version':
        print_banner()
        print("Kuya version 0.1.0")
        print("Your Friendly Data Analysis Assistant\n")
        return 0
    else:
        parser.print_help()
        return 0


if __name__ == '__main__':
    sys.exit(main())
