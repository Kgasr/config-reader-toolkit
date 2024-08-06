# setup.py

from setuptools import setup, find_packages

setup(
    name='yaml_config_reader',
    version='0.0.1',
    description='A toolkit for reading various file formats like YAML and JSON.',
    url='https://github.com/Kgasr/config-reader-toolkit',
    author='Karan Gupta',
    author_email='karangupta125@gmail.com',
    packages=find_packages(),
    install_requires=['PyYAML'],
)
