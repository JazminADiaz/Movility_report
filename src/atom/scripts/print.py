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

#bagname=f'{robot}_{situation}_{muestra}'
bagname='idealR1'
def callback_1(event):
  global posx, posy, ruta
  Vel=Twist()
  
  if ruta==1:

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
      rospy.sleep(10)

    if (((posx - (-24.65))**2) + ((posy-(32.6))**2))<(radio**2):
      Vel.linear.x=0.0
      Vel.angular.z=0.1
      pub.publish(Vel)
      rospy.sleep(2)
      Vel.angular.z=0.0
      Vel.linear.x=0.7
      pub.publish(Vel)
      rospy.sleep(10)

    if (((posx - (-27.72))**2) + ((posy-(40.19))**2))<(radio**2):
      Vel.linear.x=0.0
      Vel.angular.z=0.0
      pub.publish(Vel)
      

      '''
    #gira un poco a la derecha
          Vel.angular.z=-0.5
          Vel.linear.x=0.5
          pub.publish(Vel)
          rospy.sleep(5)
    #gira un poco a la izq
        
          Vel.angular.z=0.5
          pub.publish(Vel)
          rospy.sleep(5)
          Vel.angular.z=0
          pub.publish(Vel)
          rospy.sleep(1)  

    ##Segunda esquina

        if (((posx - (-4.86))**2) + ((posy-(-14.12))**2))<(radio**2):
          Vel.linear.x=0.0
          pub.publish(Vel)
          rospy.sleep(4)
          Vel.linear.x=0.5
          pub.publish(Vel)
          rospy.sleep(5)

    ##Tercera esquina

        if (((posx - (-13.32))**2) + ((posy-(4.01))**2))<(radio**2):
          Vel.linear.x=0.0
          pub.publish(Vel)
          rospy.sleep(4)



    #gira un poco a la izq
          Vel.linear.x=0.5
          Vel.angular.z=-0.5
          pub.publish(Vel)
          rospy.sleep(5)
          Vel.angular.z=0
          pub.publish(Vel)
          rospy.sleep(1)  
    #gira un poco a la derecha
          Vel.angular.z=0.5
          Vel.linear.x=0.5
          pub.publish(Vel)
          rospy.sleep(5)

    ##Cuarta esquina

        if (((posx - (-21.41))**2) + ((posy-(22))**2))<(radio**2):
          Vel.linear.x=0.0
          pub.publish(Vel)
          rospy.sleep(4)

          
    #gira un poco a la derecha
          Vel.angular.z=-0.5
          Vel.linear.x=0.5
          pub.publish(Vel)
          rospy.sleep(4)
    #gira un poco a la izq
        
          Vel.angular.z=0.5
          pub.publish(Vel)
          rospy.sleep(4)
          Vel.angular.z=0
          pub.publish(Vel)
          rospy.sleep(1)  

    #Mitad de via


    #gira un poco a la der
        
          Vel.angular.z=-0.5
          Vel.linear.x=0.5
          pub.publish(Vel)
          rospy.sleep(4)



    #gira un poco a la derecha
          Vel.angular.z=0.4
          pub.publish(Vel)
          rospy.sleep(2)

          Vel.angular.z=0
          pub.publish(Vel)
          rospy.sleep(4)  

        else:
          Vel.linear.x=0.7
          pub.publish(Vel)
        

      
      '''
        

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
radio=0.3
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
