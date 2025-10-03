from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="bcclassreport",
    version="1.0.0",
    author="Open Source Contributors",
    author_email="mehendalenachiket@gmail.com",  # Update this
    description="Simple, intuitive binary classification metrics and visualizations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nachiket-Mehendale/bcclassreport",  # Update this
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    keywords="binary classification confusion matrix metrics visualization machine-learning",
    project_urls={
        "Bug Reports": "https://github.com/Nachiket-Mehendale/bcclassreport/issues",
        "Source": "https://github.com/Nachiket-Mehendale/bcclassreport",
    },
)
