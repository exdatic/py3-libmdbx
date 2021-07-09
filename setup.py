#!/usr/bin/env python3

import distutils.command.build
import setuptools

import os
import subprocess

version="0.10.1"
try:
      with open("VERSION", "r") as fd:
            version=fd.read().decode("utf-8")
            version=version.strip()
except:
      pass


class poke_libpath(setuptools.Command):
    #user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
      # poke lib location into code
      lib_location=os.environ.get("MDBX_LIB_LOCATION", "/usr/lib/libmdbx.so")
      proc=subprocess.run(["sed", "s%@MDBX_SOLIB_LOCATION@%{}%".format(lib_location), "libmdbx/mdbx.py.in"],
            capture_output=True)
      with open("libmdbx/mdbx.py", "w") as fd:
            fd.write(proc.stdout.decode("utf-8"))
class build(distutils.command.build.build):
    _sub_command = (
        'poke_libpath',
        None,
    )
    _sub_commands = distutils.command.build.build.sub_commands
    sub_commands = [_sub_command] + _sub_commands


setuptools.setup(name='libmdbx',
      version=version,
      description='Bindings for mdbx',
      author='Noel Kuntze',
      author_email='noel.kuntze@thermi.consulting',
      url='https://github.com/Thermi/libmdbx/tree/python-bindings',
      license='SPDX-License-Identifier: OLDAP-2.8',
      keywords=['key-value', 'nosql', 'database', 'mdbx', 'libmdbx', 'lmdb'],
      packages=['libmdbx'],
      install_requires=['ctypes'],
      cmdclass={
            'poke_libpath': poke_libpath,
            'build': build,
      },
)
