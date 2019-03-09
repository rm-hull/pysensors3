#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='PySensors3',
    version="0.1.0",
    author="Richard Hull",
    author_email="richard.hull@destructuring-bind.org",
    packages=['sensors'],
    url='https://github.com/rm-hull/pysensors3',
    license='LGPL v2.1',
    description='Python3 bindings to libsensors (via ctypes)',
    long_description=open('README.rst').read(),
    keywords=['sensors', 'hardware', 'monitoring'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved ::'
        ' GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: System',
        'Topic :: System :: Hardware',
        'Topic :: System :: Monitoring',
    ]
)
