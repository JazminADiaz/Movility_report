#!/usr/bin/env python3.8
import string
import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Twist, Pose, Quaternion, Point, Vector3
from std_msgs.msg import String


rospy.init_node('MoveRobots', anonymous=True)
robot='robot1'

rate= rospy.Rate(50)

pub = rospy.Publisher('/gazebo/model_states', ModelStates, queue_size=5)
pub1 = rospy.Publisher(f'/{robot}_Name', String, queue_size=55)
pub2 = rospy.Publisher(f'/{robot}_Pos', Pose, queue_size=55)
pub3 = rospy.Publisher(f'/{robot}_Vel', Twist, queue_size=55)


def callback(data):
    for a in  range(len(data.name)):
      if data.name[a]== 'robot1':

        name=data.name[a]
        pub1.publish(name)
        position=data.pose[a]
        pub2.publish(position)
        velocity=data.twist[a]
        pub3.publish(velocity)
        rate.sleep()


        #rospy.loginfo(data.pose[a])


rospy.Subscriber('/gazebo/model_states', ModelStates, callback)
rospy.spin()


