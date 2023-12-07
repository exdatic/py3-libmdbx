#!/usr/bin/env python3
from distutils.command.build import build
import setuptools

setuptools.setup(
    name='libmdbx',
    version="0.10.2",
    description='Bindings for mdbx',
    author='Noel Kuntze',
    author_email='noel.kuntze@thermi.consulting',
    url='https://github.com/Thermi/libmdbx/tree/python-bindings',
    license='SPDX-License-Identifier: OLDAP-2.8',
    keywords=['key-value', 'nosql', 'database', 'mdbx', 'libmdbx', 'lmdb'],
    packages=['libmdbx'],
    cmdclass={
        'build': build,
    },
)
