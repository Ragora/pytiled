#!/usr/bin/env python

from distutils.core import setup

setup(name="tiled",
    version="1.0",
    description="Tiled map editor python support.",
    author="Robert MacGregor",
    author_email="ragoradev@gmail.com",
    install_requires = [
        "requirements.txt"
    ],
    packages=["tiled"],
 )
