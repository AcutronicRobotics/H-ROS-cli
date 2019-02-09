# H-ROS-cli

<a href="http://www.acutronicrobotics.com"><img src="https://acutronicrobotics.com/assets/images/AcutronicRobotics_logo.jpg" align="left" hspace="8" vspace="2" width="200"></a>

This is the official repository of the H-ROS CLI. This tool will help you to communicate and configure the
[H-ROS SoM](https://acutronicrobotics.com/technology/som/). Each H-ROS SoM will integrate an API interface to customize
some critical aspects, such as security or ros_domain_id. Using this tool is optional, the default configuration of an
H-ROS SoM is enough to start working with.

<a href="https://acutronicrobotics.com/technology/H-ROS/"><img src="https://acutronicrobotics.com/technology/H-ROS/imgs/xH-ROS_intro_logo.png.pagespeed.ic.OiG4835AAz.webp" align="right" hspace="8" vspace="2" width="200"></a>

H-ROS is a standardized software and hardware infrastructure to create modular robot hardware. A complete modularity stack for robotics that allows to transform robot parts into devices that speak ROS 2 natively. First class participants of the robot ecosystem that simplify the integration effort.

The actual version of this CLI is `0.04`.

## Features
- Get the actual information of the SoM (Version, hostname...)
- Start/Stop the lifecycle that is running
- Get and set the RMW_IMPLEMENTATION running
- Get and set the ROS_DOMAIN_ID running
- Modular Joints specific:
    - Set the actual position as zero

## Installation
The installation procedure is available in the [documentation](https://acutronicrobotics.com/docs/technology/h-ros/api#installation)

## Learn more

The documentation of this CLI is available in the official [Acutronic Robotics documentation](https://acutronicrobotics.com/docs/technology/h-ros/api).
