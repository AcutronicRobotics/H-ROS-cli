#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name="hros",
    version="0.0.1",
    author="Asier Bilbao, Lander Usategui",
    author_email="asier@erlerobotics.com, lander@erlerobotics.com",
    description="H-ROS command line utility",
    url="https://github.com/erlerobot/h-ros-cli",
    entry_points = {
      'console_scripts': ['hros=hros.__main__:main'],
    },
    install_requires=[
          'nmap',
          'netifaces'
      ],

    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved ::  License",
        "Operating System :: OS Independent",
    ],
)
