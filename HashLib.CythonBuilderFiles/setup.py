from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(
           "HashLib4Python.pyx",                # our Cython source
           sources=["HashLib4CPPWrapper.cpp"],  # additional source file(s)
           language="c++",             # generate C++ code
      ))
