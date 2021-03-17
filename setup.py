#!/usr/bin/env python3
"""Setup file for the ICE Portal data scraper."""
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.rst"), encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="iceportal",
    version="1.0.1",
    description="Python client for getting data from the ICE Portal.",
    long_description=long_description,
    url="https://github.com/fabaff/python-iceportal",
    download_url="https://github.com/fabaff/python-iceportal/releases",
    author="Fabian Affolter",
    author_email="fabian@affolter-engineering.ch",
    license="MIT",
    install_requires=[
        "aiohttp>=3.7.4,<4",
        "async_timeout<4",
    ],
    packages=["iceportal"],
    python_requires=">=3.8",
    zip_safe=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
    ],
)
