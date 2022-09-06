#!/usr/bin/env python3.8
import posix
import string
from turtle import position
import rospy
import csv
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Twist, Pose, Quaternion, Point, Vector3
from std_msgs.msg import String
import time
import math 

robot='robot1'
situation='ideal'
muestra='1'

bagname=f'{robot}_{situation}_{muestra}'

def callback_1(event):
  global posx, posy, ruta
  Vel=Twist()
  
  if ruta==1:
    
    if (((posx - (-22.44))**2) + ((posy-(25.69))**2))<(radio**2):

      Vel.linear.x=0.0
      pub.publish(Vel)
      rospy.sleep(4)

      Vel.angular.z=-0.5
      Vel.linear.x=0.5
      pub.publish(Vel)
      rospy.sleep(4)

      Vel.angular.z=0.5
      pub.publish(Vel)
      rospy.sleep(4)  
      Vel.angular.z=0
    
    if (((posx - (-14.245))**2) + ((posy-(6.33))**2))<(radio**2):
      Vel.linear.x=0.0
      pub.publish(Vel)
      rospy.sleep(4)

      Vel.angular.z=-0.5
      Vel.linear.x=0.5
      pub.publish(Vel)
      rospy.sleep(4)


      Vel.angular.z=0.5
      pub.publish(Vel)
      rospy.sleep(4)  
      Vel.angular.z=0
      
    if (((posx - (-6.22))**2) + ((posy-(-12.135))**2))<(radio**2):
      Vel.linear.x=0.0
      pub.publish(Vel)
      rospy.sleep(4)

      Vel.angular.z=-0.7
      Vel.linear.x=0.5
      pub.publish(Vel)
      rospy.sleep(4)

      
      Vel.angular.z=0.7
      pub.publish(Vel)
      rospy.sleep(4)  
      Vel.angular.z=0

    if (((posx - (1.666))**2) + ((posy-(-30.96))**2))<(radio**2):
      Vel.linear.x=0.0
      pub.publish(Vel)
      rospy.sleep(4)


      Vel.linear.x=0.5
      pub.publish(Vel)
      rospy.sleep(4)

      


    else:
      Vel.linear.x=0.5
      pub.publish(Vel)
    

    

def callback(data):
  global r, posx, posy
  Time=rospy.get_time()

  #Time=rospy.get_rostime()
  r=r+1
  for a in  range(len(data.name)):
    if data.name[a]== 'robot1':
      name=data.name[a]
      position=data.pose[a]
      velocity=data.twist[a]
      posx=position.position.x
      posy=position.position.y
      velx= velocity.linear.x
      vely= velocity.linear.y

  if r%100==0:
    speed=math.sqrt((velx**2)+(vely**2))    
    row=[Time, name, posx, posy, speed ]

    writer.writerow(row)
  
### CREATING THE CSV
path1= '/home/jazmin/MultiRobots/src/atom/Csv/og'
f = open(f'{path1}/{bagname}_og.csv', 'w', encoding='UTF8')
writer = csv.writer(f)
writer.writerow(['Time' ,'Robot','PosX','PosY','Speed'])

### Global variable


r=0 #rate to save the log
ruta=1
radio=0.5
posx=0
posy=0
vel_lx=0
vel_lz=0


if __name__ == '__main__':
    try:
      rospy.init_node('MoveRobots', anonymous=True)
      rospy.Subscriber('/gazebo/model_states', ModelStates, callback)
      #rospy.Subscriber('/gazebo/model_states', ModelStates, callback)
      
      pub= rospy.Publisher('/robot1/cmd_vel', Twist, queue_size=10)
      rospy.Timer(rospy.Duration(1/1000), callback_1)
      rospy.spin()
    except rospy.ROSInterruptException:

      pass



'''
def read_subs():
    Model = message_filters.Subscriber("/gazebo/model_states", ModelStates)
    Vel = message_filters.Subscriber("/robot1/cmd_vel", Twist)

    # Synchronize images
    ts = message_filters.ApproximateTimeSynchronizer([ModelStates, Twist], queue_size=10, slop=0.5)
    ts.registerCallback(image_callback)
    rospy.spin()
    
'''
