#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name="hros",
    version="0.0.1",
    author="Acutronic Robotics",
    author_email="contact@acutronicrobitcs.com",
    description="H-ROS command line utility",
    url="https://github.com/acutronicrobitcs/h-ros-cli",
    entry_points = {
      'console_scripts': ['hros=hros.__main__:main'],
    },
    install_requires=[
          'nmap',
          'netifaces'
      ],
    license='GPLv3',
    keywords=['H-ROS', 'modular', 'ros2', 'robot operating system'],
    packages=setuptools.find_packages(),
)
