#!/usr/bin/env python3.8
import string
import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Twist, Quaternion, Point, Vector3, Pose
from std_msgs.msg import String
import string


rospy.init_node('MoveRobots', anonymous=True)
robot='robot1'
rate= rospy.Rate(10)

pos= Point()
orie=Quaternion()
vel_l=Vector3()
vel_a=Vector3()

def callback(data):
    for a in  range(len(data.name)):
      if data.name[a]== 'robot1':

        
        position=data.pose[a]
        name=data.name[a]
        pub1.publish(name)
        pub5.publish(position)
        rate.sleep()


        #rospy.loginfo(data.pose[a])
##        rospy.loginfo(data.name[a])  




  #  print(data.pose.pose) f"Hello, {first_name}!"
          
  #  rospy.loginfo(data.pose)            

rospy.Subscriber('/gazebo/model_states', ModelStates, callback)
pub = rospy.Publisher('/gazebo/model_states', ModelStates, queue_size=10)
pub1 = rospy.Publisher(f'{robot}/name', String, quxeue_size=10)
pub2 = rospy.Publisher(f'{robot}/Orientation', Quaternion, queue_size=10)
pub3 = rospy.Publisher(f'{robot}/LinearVel', Vector3, queue_size=10)
pub4 = rospy.Publisher(f'{robot}/AngularVel', Vector3, queue_size=10)
pub5 = rospy.Publisher(f'{robot}/Pose', Pose, queue_size=10)
#pub1= rospy.Publisher('/gazebo/set_model_state', ModelStates, queue_size=10)
# spin() simply keeps python from exiting until this node is stopped

rospy.spin()

