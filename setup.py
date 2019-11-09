# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='vicuna',
    version='0.1.0',
    description='Vicuna package for Python-Guide.org',
    long_description=readme,
    author='Chengsi ZHOU',
    author_email='zhouchengsi@hotmail.com',
    url='https://github.com/kennethreitz/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
