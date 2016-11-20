import sys
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

import smartproxy

PACKAGE = "smartproxy"
NAME = "smartproxy"
DESCRIPTION = "yet another auto proxy provider"
AUTHOR = "taoyang"
AUTHOR_EMAIL = "ty@puton.info"
URL = "http://puton.info"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache License, Version 2.0",
    url=URL,
    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'smartproxy=smartproxy.run:main'
        ]
    },

)