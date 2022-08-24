#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import sys
import os
import argparse

def move_robot(linear_vel, ang_vel):
    rospy.init_node("MoveRobots", anonymous=True)
    robot= sys.argv[1]
    #pub = rospy.Publisher(rf'{robot}/cmd_vel', Twist, queue_size=10)
    pub = rospy.Publisher(rf'{robot}/cmd_vel', Twist, queue_size=10)
    rate= rospy.Rate(10)

    vel = Twist()

    for r in range(2):
        
        if str(robot)=='robot1':

            while not rospy.is_shutdown():
                vel.linear.x= linear_vel
                vel.linear.y=0
                vel.linear.z=0

                vel.angular.x=0
                vel.angular.y=0
                vel.angular.x=ang_vel

                pub.publish(vel)
                rate.sleep()

if __name__ == '__main__':
    try:
        move_robot(0.1, 0.1)
    except rospy.ROSInterruptException:
        pass


