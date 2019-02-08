# H-ROS-cli

This is the official repository of the H-ROS CLI. This tool will help you to communicate and configure the 
[H-ROS SoM](https://acutronicrobotics.com/technology/som/). Each H-ros SoM will integrate an API interface to customize
some critical aspects, such as security or ros_domain_id. Using this tool is optional, the default configuration of an
H-ROS SoM is enough to start working with.

The actual version of this CLI is `0.04`.

## Features
- Get the actual information of the SoM (Version, hostname...)
- Start/Stop the lifecycle that is running
- Get and set the RMW_IMPLEMENTATION running
- Get and set the ROS_DOMAIN_ID running
- Modular Joints specific:
    - Set the actual position as zero
    
## Learn more

The documentation of this CLI is available in the official [Acutronic Robotics documentation](https://acutronicrobotics.com/docs/technology/h-ros/api).