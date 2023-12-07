py3-libmdbx
===========

Python 3 bindings for libmdbx

Installation
============

There are two options:
1) Install it from a package provided by your distro
   (Currently available for Arch Linux and Alpine Linux)

2) Install it via the setup.py script (uses python setuptils)
   Run `python3 setup.py install -h` and add the arguments you require for correct installation

Requirements
============

libmdbx for the functionality.

```bash
git clone https://github.com/erthink/libmdbx.git || cd libmdbx && make && cp libmdbx.so /usr/lib/ 
```
