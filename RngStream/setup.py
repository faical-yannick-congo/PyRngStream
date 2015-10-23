#!/usr/bin/env python

"""
setup.py file for SWIG rngstream
"""

from distutils.core import setup, Extension


RngStream_module = Extension('_RngStream',
                           sources=['RngStream_wrap.c', 'RngStream.c'],
                           )

setup (name = 'RngStream',
       version = '0.1',
       author      = "David Hill & Yannick Congo",
       description = """L'Ecuyer Python Module RngStream of the Mrg32k3a Package""",
       ext_modules = [RngStream_module],
       py_modules = ["RngStream"],
       )