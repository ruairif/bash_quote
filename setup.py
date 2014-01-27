#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = ''
with open('README.rst') as f:
    readme = f.read()

history = ''
with open('HISTORY.rst') as f:
    history = f.read()

reqs = []
with open('requirements.txt') as f:
    reqs = f.read().splitlines()



setup(
    name='bash_quote',
    version='1.0.0',
    description='Browse quotes on bash.org from the comfort of your shell.',
    long_description=readme + '\n\n' + history,
    author='Ruairi Fahy',
    author_email='ruairifahy91@gmail.com',
    url='https://github.com/ruairif/bash_quote',
    packages=[
        'bash_quote',
    ],
    package_dir={'bash_quote': 'bash_quote'},
    include_package_data=True,
    install_requires=reqs,
    license='BSD',
    zip_safe=False,
    keywords='bash_quote',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'bashquote = bash_quote.bash_quote:main',
        ]
    }
)
