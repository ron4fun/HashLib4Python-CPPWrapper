from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(
           "HashFactory.pyx",               # our Cython source
           sources=["HashLibWrapper.cpp"],  # additional source file(s)
           language="c++",             # generate C++ code
      ))
