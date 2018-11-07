# -*coding: UTF-8 -*-
__author__ = 'gmaze@ifremer.fr'

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyxpcm",
    version="0.1.1",
    description='pyxpcm: Python Profile Classification Modelling for Xarray',
    url='http://github.com/obidam/pyxpcm',
    author='Guillaume Maze',
    author_email='gmaze@ifremer.fr',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={'pyxpcm': ['data/*.nc']},
    license='GPLv3',
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)