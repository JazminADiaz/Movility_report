#!/usr/bin/env python3.8
import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import csv
from datetime import datetime


pos=[]
with open('/home/dolos/JADM/MultiRobots/src/atom/csv/Position.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    header= 'Robot;PosX;PosY;PosZ'
    
    # write the header
    writer.writerow(header)
    f.close()
class save_info:

    def __init__(self):
        rospy.init_node('Save_moves', anonymous=True)
        rospy.Subscriber('/gazebo/model_states', ModelStates, self.callback)



    def callback(self,data):
   
        for a in  range(len(data.name)):
            
            if data.name[a]== 'Robot1':
                
                self.posX= data.pose[a].position.x
                self.posY= data.pose[a].position.y
                self.posZ= data.pose[a].position.z
                info="Robot1;"+str(self.posX)+ ";"+str(self.posY)+ ";"+str(self.posZ)
        pos.append(info)
        
        with open('/home/dolos/JADM/MultiRobots/src/atom/csv/Position.csv', 'w', newline='') as f:
            writer = csv.writer(f)
        
            # write multiple rows
            writer.writerow(info)

if __name__ == '__main__':
    
   
    save_info()
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    

