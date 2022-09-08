#!/usr/bin/env python3.8
import posix
import string
from turtle import position
import rospy
import csv
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Twist, Pose, Quaternion, Point, Vector3
from std_msgs.msg import String
import numpy as np

import math 

##CAMBIO
situation='deviation10'
ruta_prog=True

ruta=10

#IGUAL
robot=f'robot{ruta}'
bagname=f'{situation}R{ruta}'
#deviation1 -> the bus takes deviation from one street has to do a turn 2 blocks awway


def callback_1(event):
  global posx, posy, ruta
  Vel=Twist()
  
  if ruta==1 and ruta_prog==True:

    Vel.linear.x=0.7
    pub.publish(Vel)

    if (((posx - (3.41))**2) + ((posy-(-32.72))**2))<(radio**2):
      Vel.linear.x=0.0
      pub.publish(Vel)
      rospy.sleep(5)
      Vel.linear.x=0.7
      pub.publish(Vel)
      rospy.sleep(3)

    if (((posx - (0.6))**2) + ((posy-(-26.79))**2))<(radio**2):
      Vel.linear.x=0.0
      Vel.angular.z=-0.3
      pub.publish(Vel)
      rospy.sleep(1)
      Vel.linear.x=0.7
      Vel.angular.z=0.0
      pub.publish(Vel)
      rospy.sleep(10)
      Vel.linear.x=0.0
      Vel.angular.z=0.2
      pub.publish(Vel)
      rospy.sleep(1)

    if (((posx - (-4.32))**2) + ((posy-(-13.63))**2))<(radio**2):
      Vel.linear.x=0.0
      pub.publish(Vel)
      rospy.sleep(4)
      Vel.angular.z=0.1
      pub.publish(Vel)
      rospy.sleep(2)
      Vel.angular.z=0.0
      Vel.linear.x=0.7
      pub.publish(Vel)
      rospy.sleep(3)


    if (((posx - (-5.96))**2) + ((posy-(-10.72))**2))<(radio**2):
      

      Vel.linear.x=0.0
      Vel.angular.z=-0.1
      pub.publish(Vel)
      rospy.sleep(2)
      Vel.angular.z=0.0
      Vel.linear.x=0.7
      pub.publish(Vel)
      rospy.sleep(2)
      
    if (((posx - (-12.77))**2) + ((posy-(4.48))**2))<(radio**2):
      

      Vel.linear.x=0.0
      pub.publish(Vel)
      rospy.sleep(2)
      Vel.linear.x=0.7
      pub.publish(Vel)
      rospy.sleep(2)

    if (((posx - (-21.34))**2) + ((posy-(23.13))**2))<(radio**2):
      
      Vel.linear.x=0.0
      pub.publish(Vel)
      rospy.sleep(2)

      Vel.linear.x=0.7
      pub.publish(Vel)
      rospy.sleep(2)
      
    if (((posx - (-23.53))**2) + ((posy-(27.84))**2))<(radio**2):
      Vel.linear.x=0.0
      Vel.angular.z=-0.1
      pub.publish(Vel)
      rospy.sleep(3)
      Vel.angular.z=0.0
      Vel.linear.x=0.7
      pub.publish(Vel)
      rospy.sleep(3)

    if (((posx - (-24.56))**2) + ((posy-(32.31))**2))<(radio**2):
      Vel.linear.x=0.0
      Vel.angular.z=0.1
      pub.publish(Vel)
      rospy.sleep(2)

      Vel.angular.z=0.0
      Vel.linear.x=0.7
      pub.publish(Vel)
      rospy.sleep(2)

    if (((posx - (-27.72))**2) + ((posy-(40.19))**2))<(radio**2):
      Vel.linear.x=0.0
      Vel.angular.z=0.0
      pub.publish(Vel)
      

        

def callback(data):
  global r, posx, posy
  Time=rospy.get_time()

  #Time=rospy.get_rostime()
  r=r+2
  for a in  range(len(data.name)):
    if data.name[a]== f'robot1':
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
path= '/home/jazmin/MultiRobots/src/atom/Csv'
f = open(f'{path}/{bagname}.csv', 'w', encoding='UTF8')
writer = csv.writer(f)
writer.writerow(['Time' ,'Robot','PosX','PosY','Speed'])

### Global variable


r=0 #rate to save the log
radio=0.3
posx=0
posy=0
vel_lx=0
vel_lz=0

speed_s=np.array([])

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
