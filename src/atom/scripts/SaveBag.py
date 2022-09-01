#!/usr/bin/env python3.8
import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Twist


robot='robot1'
pub1 = rospy.Publisher('/robot1/cmd_vel', Twist, queue_size=10)
pub2 = rospy.Publisher('/gazebo/model_states', ModelStates, queue_size=10)
rospy.init_node('MoveRobots', anonymous=True)
rate= rospy.Rate(10)
vel = Twist()
States=ModelStates


def callback(data):
    for a in  range(len(data.name)):
        if data.name[a]== 'robot1':

            pub1.publish(vel)
            pub2.publish(ModelStates)
            rate.sleep()



#rospy.Subscriber('/gazebo/model_states', ModelStates, callback)


rospy.spin()
