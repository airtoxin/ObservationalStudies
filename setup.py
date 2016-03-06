#!/usr/bin/env python
# -*- conding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='observational_studies',
    version='0.0.1',
    description='observational study helper module',
    long_description=long_description,
    author='Ryoji Ishii',
    author_email='airtoxin@icloud.com',
    license='MIT',
    url='https://github.com/airtoxin/ObservationalStudies',
    packages=find_packages(exclude=['build', 'doc', 'template']),
    include_package_data=False,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Framework :: IPython'
    ],
    keywords='observational_study observational study statistics',
    install_requires=[
    ],
    tests_require=['pytest', 'tox']
)
