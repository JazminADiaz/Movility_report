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
situation='robot21'

bagname=f'normal_{situation}'
#deviation1 -> the bus takes deviation from one street has to do a turn 2 blocks awway

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
path= '/home/jazmin/MultiRobots/src/atom/Csv/New'
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
      rospy.spin()
    except rospy.ROSInterruptException:

      pass

