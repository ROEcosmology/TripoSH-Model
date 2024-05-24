from setuptools import setup

import numpy
from Cython.Build import cythonize
from Cython.Distutils import build_ext, Extension
from extension_helpers._setup_helpers import pkg_config


# Define project metadata
PKG_NAME = 'hitomipy'
PKG_SRC = ['hitomi.pyx',]

LANGUAGE = 'c++'

# Declare dependencies
LIBS = ['m', 'gsl', 'fftw3',]

pkg_config_options = pkg_config(
    LIBS,
    default_libraries=LIBS
)

cflags = pkg_config_options['extra_compile_args']
include_dirs = pkg_config_options['include_dirs']
libs = pkg_config_options['libraries']
lib_dirs = pkg_config_options['library_dirs']

include_dirs += ['.', numpy.get_include(),]

# Declare Cython extensions
CYTHON_DIRECTIVES = {
   'language_level': '3',
   'c_string_encoding': 'utf-8',
   'embedsignature': True,
}

hitomipy_ext = Extension(
    PKG_NAME,
    sources=PKG_SRC,
    extra_compile_args=cflags,
    include_dirs=include_dirs,
    libraries=libs,
    library_dirs=lib_dirs,
    language=LANGUAGE
)

extmod = cythonize(
    [hitomipy_ext,],
    compiler_directives=CYTHON_DIRECTIVES
)

# Set up
setup(
    name=PKG_NAME,
    cmdclass={'build_ext': build_ext},
    ext_modules=extmod
)
