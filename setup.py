"""Setuptools for building the extension package"""
from setuptools import setup, Extension
import numpy as np

PACKAGE_NAME = 'ar'

setup(
    name=PACKAGE_NAME,
    author_email='rhys.ulerich@gmail.com',
    author='Rhys Ulerich',
    classifiers=['Development Status :: 3 - Alpha'],
    install_requires=['numpy'],
    license='MPL2',
    #setup_requires=['setuptools_scm'],
    url='http://github.com/RhysU/ar',
    use_scm_version=True,
    ext_modules=[
        Extension(
            PACKAGE_NAME,
            depends=['ar.hpp'],
            sources=['ar-python.cpp'],
            include_dirs=[np.get_include()],
        )
    ],
)
