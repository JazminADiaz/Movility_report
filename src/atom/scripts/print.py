#!/usr/bin/env python3.8
import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Twist

def callback(data):
    for a in  range(len(data.name)):
      if data.name[a]== 'Robot2':
        vel.linear.x= 0.1
        vel.angular.z=0.0

        pub.publish(vel)
        rate.sleep()
        #rospy.loginfo(data.pose[a])
        rospy.loginfo(data.name[a])  




  #  print(data.pose.pose)
          
  #  rospy.loginfo(data.pose)            


    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

rospy.init_node('MoveRobots', anonymous=True)

rospy.Subscriber('/gazebo/model_states', ModelStates, callback)
pub = rospy.Publisher('/robot2/cmd_vel', Twist, queue_size=10)
#pub1= rospy.Publisher('/gazebo/set_model_state', ModelStates, queue_size=10)
# spin() simply keeps python from exiting until this node is stopped

rate= rospy.Rate(10)
vel = Twist()

rospy.spin()

