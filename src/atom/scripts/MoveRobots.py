#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import sys

def move_robot(linear_vel, ang_vel):
    rospy.init_node("MoveRobots", anonymous=True)
    pub = rospy.Publisher('/robot2/cmd_vel', Twist, queue_size=10)
    rate= rospy.Rate(10)

    vel = Twist()

    while not rospy.is_shutdown():
        vel.linear.x= linear_vel
        vel.linear.y=0
        vel.linear.z=0

        vel.angular.x=0
        vel.angular.y=0
        vel.angular.x=ang_vel

        pub.publish(vel)
        rate.sleep()

    while rospy.is_shutdown():
        vel.linear.x= 0   
        vel.linear.y=0
        vel.linear.z=0

        vel.angular.x=0
        vel.angular.y=0 
        vel.angular.x=0

if __name__ == '__main__':
    try:
        move_robot(0.1, 0.1)
    except rospy.ROSInterruptException:
        pass


