#!/usr/bin/env python3.8
import string
import rospy
import csv
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Twist, Pose, Quaternion, Point, Vector3
from std_msgs.msg import String

rospy.init_node('MoveRobots', anonymous=True)
robot='robot1'
situation='ideal'
muestra='1'

bagname=f'{robot}_{situation}_{muestra}'


rate= rospy.Rate(1000)

pub1 = rospy.Publisher(f'/{robot}_Name', String, queue_size=500)
pub2 = rospy.Publisher(f'/{robot}_Pos', Pose, queue_size=500)
pub3 = rospy.Publisher(f'/{robot}_Vel', Twist, queue_size=500)




def callback(data):
  global r
  Time=rospy.get_time()
  #Time=rospy.get_rostime()
  r=r+1
  for a in  range(len(data.name)):
    if data.name[a]== 'robot1':

      name=data.name[a]
#      pub1.publish(name)
      position=data.pose[a]
#      pub2.publish(position)
      velocity=data.twist[a]
#      pub3.publish(velocity)
  if r%100==0:    
    row=[Time, name,position.position.x, position.position.y, velocity.linear.x, velocity.angular.z]
  
  

    writer.writerow(row)

        #rospy.loginfo(data.pose[a])

path1= '/home/jazmin/MultiRobots/src/atom/Csv/og'
f = open(f'{path1}/{bagname}_og.csv', 'w', encoding='UTF8')
writer = csv.writer(f)
writer.writerow(['Time' ,'Robot','PosX','PosY','LinX', 'AngZ'])


r=0
rospy.Subscriber('/gazebo/model_states', ModelStates, callback)



rate.sleep()


name_s=[]
#rospy.Subscriber('/gazebo/model_states', ModelStates, callback)
rospy.spin()


