#!/usr/bin/env python3.8
from sqlite3 import Time
import bagpy
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np
import os

bagname='subset4'
robot='robot1'

b = bagreader(f'/home/jazmin/bagfiles/{bagname}.bag') 
print(b.topic_table)


data_name=b.message_by_topic(f'/{robot}_name')
print("File saved: {}".format(data_name))

data_pose = b.message_by_topic(f'/{robot}_Pos')
print("File saved: {}".format(data_pose))

data_twist = b.message_by_topic(f'/{robot}_Vel')
print("File saved: {}".format(data_twist))

path = f'/home/jazmin/bagfiles/{bagname}'

data1 = pd.read_csv(f'{path}/{robot}_name.csv')
data1=data1.rename(columns = {'data':'Name'})

data2 = pd.read_csv(f'{path}/{robot}_Pos.csv')

data3= pd.read_csv(f'{path}/{robot}_Vel.csv')
  
# using merge function by setting how='inner'
#output1 = pd.merge(data1, data2, on='Time', how='inner')

#path=f'/home/jazmin/bagfiles/{bagname}'


df_list = []
df = pd.concat([data1.set_index('Time'), data2.set_index('Time'), data3.set_index('Time')], axis=1, join='inner')
    
print(df)

df.to_csv('holi', sep=';')
#concatted = pd.concat(df_list)

#pd.concat([df1.set_index('A'),df2.set_index('A')], axis=1, join='inner')

'''



'''




#df = pd.DataFrame(list())
#df.to_csv('/home/jazmin/MultiRobots/src/atom/scripts/info/set1.csv')

#info=pd.read_csv(df)
#print(info)




'''
path='/home/jazmin/MultiRobots/src/atom/scripts/info/info.csv'
info=pd.read_csv(path)

for a in range(len(df_imu.Time -1 )):
    model=df_imu.name[a]
    pose=df_imu.pose[a]

    info['new_column'] = model
    info.to_csv(path)



'''
