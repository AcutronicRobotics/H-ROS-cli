# H-ROS-cli

This is the official repository of the H-ROS CLI. This tool will help you to communicate and configure the
H-ROS SoM. Each H-ROS SoM will integrate an API interface to customize
some critical aspects, such as security or ros_domain_id. Using this tool is optional, the default configuration of an
H-ROS SoM is enough to start working with.

H-ROS is a standardized software and hardware infrastructure to create modular robot hardware. A complete modularity stack for robotics that allows to transform robot parts into devices that speak ROS 2 natively. First class participants of the robot ecosystem that simplify the integration effort.

[![PyPI version](https://badge.fury.io/py/hros.svg)](https://badge.fury.io/py/hros)

## Features
- Get the actual information of the SoM (Version, hostname...)
- Start/Stop the lifecycle that is running
- Get and set the RMW_IMPLEMENTATION running
- Get and set the ROS_DOMAIN_ID running
- Modular Joints specific:
    - Set the actual position as zero
