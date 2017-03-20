#!/usr/bin/env python

# from distutils.core import setup
from setuptools import setup, find_packages

VERSION = open('VERSION').read().strip()
REQUIREMENTS = [line.strip() for line in open('requirements.txt')]

setup(
    name='Common-Utils',
    version=VERSION,
    description='Python Common Utils Library',
    author='lishiwei',
    author_email='shiwei.lee@163.com',
    install_requires=REQUIREMENTS,
    url='https://github.com/ColorCloud/common-utils/',
    # packages=[],
    packages=find_packages()
)
