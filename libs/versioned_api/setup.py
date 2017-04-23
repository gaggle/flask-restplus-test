from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='versioned_api',
    version='0.0.0',
    description='Versioned API framework',
    long_description=long_description,
    install_requires=['flask-restplus'],
)
