#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name="hros",
    version="0.04",
    author="Acutronic Robotics",
    author_email="contact@acutronicrobitcs.com",
    description="H-ROS command line utility",
    long_description='''
    This tool will help you to communicate and configure the H-ROS SoM. Each H-ROS SoM will integrate an API interface to customize some critical aspects, such as security or ros_domain_id.
    ''',
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
