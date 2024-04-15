# Mobile Manipulator Robot with ROS and Gazebo Simulation

![Mobile Manipulator Robot](https://github.com/rajeev-gupta-bashrc/MM_ROBOT/blob/main/images/mm_robot.jpg)

## Overview
This project involves simulating a mobile manipulator robot in Gazebo using ROS Noetic. The robot is a differential drive base mounted with a 5-degree-of-freedom (5-DOF) manipulator. It is capable of navigating its environment autonomously by receiving waypoint commands and controlling its velocity through the `cmd_vel` topic.

## Features
- **Gazebo Simulation:** The robot is simulated in Gazebo, providing a realistic environment for testing and development.
- **ROS Noetic:** Utilizing ROS Noetic, the leading robotics middleware, for communication, control, and simulation.
- **Differential Drive Base:** The robot's base is equipped with differential drive wheels, enabling it to move in any direction without changing its orientation.
- **5-DOF Manipulator:** Mounted on the base is a 5-degree-of-freedom manipulator, providing the robot with the capability to manipulate objects in its environment.
- **Waypoint Navigation:** The robot receives waypoint commands and navigates to specified locations autonomously by reading velocity commands on the `cmd_vel` topic.

## Getting Started
To get started with the mobile manipulator robot simulation, follow these steps:

1. **Install ROS Noetic:** Install ROS Noetic on your system by following the instructions provided on the [ROS wiki](https://wiki.ros.org/noetic/Installation).
   
2. **Set Up ROS Workspace:** Create and set up a ROS workspace for your project:

    ```bash
    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/src
    catkin_init_workspace
    cd ~/catkin_ws
    catkin_make
    source devel/setup.bash
    ```

3. **Clone Repository:** Clone the mobile manipulator robot repository into your ROS workspace:

    ```bash
    cd ~/catkin_ws/src
    git clone git@github.com:rajeev-gupta-bashrc/MM_ROBOT.git
    ```

4. **Install Dependencies:** Install any dependencies required by the project using ROS package manager (rosdep) and/or system package manager:

    ```bash
    cd ~/catkin_ws
    rosdep install --from-paths src --ignore-src -r -y
    ```

5. **Build Packages:** Build the ROS packages in your workspace:

    ```bash
    catkin_make
    ```

6. **Launch Simulation:** Launch the Gazebo simulation of the mobile manipulator robot:

    ```bash
    roslaunch mobile_manipulator mobile_manipulator_gazebo.launch
    ```

7. **Play with various scripts using the command below:** For example:

    ```bash
    rosrun mobile_manipulator path_planner.py
    ```

## Contributing
Contributions to the mobile manipulator robot project are welcome! If you have any ideas, bug fixes, or improvements, feel free to submit a pull request or open an issue on the project repository.

