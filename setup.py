#!/usr/bin/env python

from setuptools import setup

version = '1.2.0'

setup(
    name='lightning-python',
    version=version,
    description='large-scale image and time series analysis',
    author='alexandonian',
    author_email='alexandonian@gmail.com',
    url='https://github.com/alexandonian/lightning.git',
    packages=[
        'lightning',
        'lightning.blocks',
        'lightning.series',
        'lightning.image',
        'lightning_flash',
        'lightning_flash.image',
        'lightning_classification',
        'lightning_classification.classification',
        'lightning_stats'
    ],
    install_requires=open('requirements.txt').read().split('\n'),
    long_description='See https://github.com/alexandonian/lightning.git'
)

