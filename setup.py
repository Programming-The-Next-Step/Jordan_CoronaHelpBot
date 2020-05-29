# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:20:51 2020

@author: User
"""

import setuptools


setuptools.setup(
    name="Jordan.py",
    version="0.0.1",
    py_modules=["jordan"],
    description="Chatbot helping you not get crazy in times of Corona.",
    author="MarlaDre",
    author_email="marla.a.dressel@gmail.com",
    python_requires=">=3.6",
    url="https://github.com/Programming-The-Next-Step/Jordan_CoronaHelpBot",
    packages="setuptools.find_packages()", # speciify dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ]
    )