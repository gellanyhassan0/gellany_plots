
from setuptools import setup, find_packages


setup(
    name='gellany_plots',
    version='0.0.1',
    packages=find_packages(include=['gellany_plots', 'gellany_plots.*']),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
    ]
)
