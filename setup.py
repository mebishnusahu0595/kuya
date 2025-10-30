from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kuya-data",  # Note: 'kuya' might be taken, using 'kuya-data' as backup
    version="0.1.1",
    author="Bishnu PS",
    author_email="bishnups@example.com",
    description="🎉 Your friendly AI-powered data analysis assistant - 10x faster than traditional Pandas workflows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mebishnusahu0595/kuya",
    project_urls={
        "Bug Reports": "https://github.com/mebishnusahu0595/kuya/issues",
        "Source": "https://github.com/mebishnusahu0595/kuya",
        "Documentation": "https://github.com/mebishnusahu0595/kuya#readme",
    },
    packages=find_packages(exclude=["tests*", "examples*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.20.0",
        "matplotlib>=3.3.0",
        "seaborn>=0.11.0",
        "scipy>=1.7.0",
        "openpyxl>=3.0.0",  # For Excel support
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.9",
        ],
    },
    keywords=[
        "data-analysis",
        "pandas",
        "data-science",
        "eda",
        "machine-learning",
        "data-cleaning",
        "visualization",
        "ai-powered",
        "automation",
        "analytics",
        "data-quality",
        "preprocessing",
    ],
    include_package_data=True,
    zip_safe=False,
)
