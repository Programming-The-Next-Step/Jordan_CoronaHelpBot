# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:20:51 2020

@author: User
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="jordan.py",
    version="0.0.1",
    py_modules=["jordan"],
    description="Chatbot helping you not get crazy in times of Corona.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="MarlaDre",
    author_email="marla.a.dressel@gmail.com",
    python_requires=">=3.6",
    url="https://github.com/Programming-The-Next-Step/Jordan_CoronaHelpBot",
    packages=setuptools.find_packages(), # specify dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ]
    )