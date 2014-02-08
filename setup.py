# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = open('requirements.txt').read().splitlines()
long_description = open('README.rst').read()

setup(
    name='requests-expects',
    version='0.1.0',
    description='Expects plugin for HTTP request and response assertions',
    long_description=long_description,
    url='https://github.com/jaimegildesagredo/requests-expects',
    author='Jaime Gil de Sagredo Luna',
    author_email='jaimegildesagredo@gmail.com',
    license='Apache 2.0',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=requirements,
    entry_points={
        'expects.plugins': [
            'response = requests_expects:Response'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License'
    ]
)
