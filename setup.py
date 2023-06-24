from setuptools import setup, find_packages
from os.path import abspath, dirname, join

setup(
    name="pypi_test_sb",

    version="1.0.0",
    packages=find_packages(),
    description="Testing pypi upload",
    long_description_content_type="text/markdown",
    url="https://github.com/shayda-banihashemi/pypi_test_sb.git",
    author_name="shayda",
    author_email="shayda.banihashemi@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only"
    ]
)##