#!/usr/bin/env python3

# TODO: like https://github.com/jnwatson/py-lmdb/blob/master/setup.py

from distutils.core import setup

setup(name='libmdbx',
      version='0.10.1',
      description='Bindings for mdbx',
      author='Noel Kuntze',
      author_email='noel.kuntze@thermi.consulting',
      url='https://github.com/Thermi/libmdbx/tree/python-bindings',
      license='SPDX-License-Identifier: OLDAP-2.8',
      keywords=['key-value', 'nosql', 'database', 'mdbx', 'libmdbx', 'lmdb'],
      packages=['libmdbx'],
     )
