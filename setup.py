#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)


requires = [
]

def get_version():
    init = open(os.path.join(ROOT, 'pyfin', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)