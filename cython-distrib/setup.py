from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

setup(
  cmdclass = {'build_ext': build_ext},
  ext_modules = [
    Extension("integrate_f5", ["integrate_f5.pyx"],
              include_dirs=[np.get_include()],
              extra_compile_args=[],
              extra_link_args=[]),
  ]
)
