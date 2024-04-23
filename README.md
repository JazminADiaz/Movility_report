# Movility_report
Using process mining tool PM4PY to detect deviations in bus routes in Pasto, Colombia. Using Gazebo as simulator and ros noetic as controller.

# Specifications:

Developed in Ubuntu 20.04
Scaled map of the center of Pasto - Colombia in Gazebo.
Routes controlled using ROS NOETIC
Logs created, replicable and available
Process discovery (process mining)
Process discovery (process mining)
Conformance Checking (process mining)
Detection of deviation in bus routes

# Instalation:
ROS-Noetic:
Enable ROS repositories
'''
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

'''
Install
'''

sudo apt update
sudo apt install ros-noetic-desktop-full
'''

Set up enviroment variables.
'''
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
'''

PM4PY

First make sure you have python install, then run this command:

'''
pip install pm4py
'''

# Use

You will need to open different terminals so you can run:
'''
roscore
'''
Then you can launch the world in Gazebo
'''
roslaunch atom main.launch
'''
Last you can move robot1 or robot2 (up to you): 
'''
rosrun teleop_twist_keyboard teleop_twist_keyboard.py /cmd_vel:=/robot1/cmd_vel
'''
You can save the information using:

'''
rosbag record -O subset4  /robot1_Vel /robot1_Pos /robot1_Name
'''

Then you can use the scripts available in the Scripts folder to analize all the files.
