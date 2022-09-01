#!/usr/bin/env python

import rospy
from gazebo_msgs.msg import ModelState
from std_msgs.msg import String


def talker():
    #pub = rospy.Publisher('chatter', ModelState)
    pub = rospy.Publisher('chatter', String)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(30) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

    rospy.spin()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



