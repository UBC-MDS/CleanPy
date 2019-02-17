#!/usr/bin/env python

from distutils.core import setup

setup(
    name='CleanPy',
    version='1.0dev',
    url='https://github.com/UBC-MDS/CleanPy',
    author='Patrick Tung, Heather Van Tassel, Phuntsok Tseten',
    author_email='na',
    packages=['cleanpy'],
    install_requires=['numpy', 'pandas'],
    license='MIT',
    description='A package for cleaning messy data on Python'
)