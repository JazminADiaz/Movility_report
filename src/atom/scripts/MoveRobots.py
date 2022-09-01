#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import sys




def move_robot(linear_vel, ang_vel):
    rospy.init_node("MoveRobots", anonymous=True)
    
    pub = rospy.Publisher('/robot1/cmd_vel', Twist, queue_size=10)
    #pub = rospy.Publisher(rf'{robot}/cmd_vel', Twist, queue_size=10)
    rate= rospy.Rate(10)

    vel = Twist()

    while True:
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
        linear_vel=0.1
        ang_vel=0.1
        move_robot(linear_vel, ang_vel)
    except rospy.ROSInterruptException:
        pass


