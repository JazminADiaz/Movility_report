#!/usr/bin/env python3.8
from sqlite3 import Time
import bagpy
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np
import os

bagname='idealR1'
robot='robot1'

b = bagreader(f'/home/jazmin/bagfiles/{bagname}.bag') 

data_twist = b.message_by_topic(f'/{robot}/cmd_vel')
print("File saved: {}".format(data_twist))

path = f'/home/jazmin/bagfiles/{bagname}'

data= pd.read_csv(f'{path}/{robot}-cmd_vel.csv')

data=data.drop_duplicates(subset='Time', keep="first")

path1= '/home/jazmin/MultiRobots/src/atom/Csv/og'

data.to_csv(f'{path1}/{robot}_{bagname}_vel.csv', index=False, sep=';')



'''
data_all=b.message_by_topic('/gazebo/model_states')
print("File saved: {}".format(data_all))



'''

'''
data1 = pd.read_csv(f'{path}/{robot}_Name.csv')
data1=data1.rename(columns = {'data':'Name'})
data1=data1.drop_duplicates(subset='Time', keep="first")
# df = data1.drop_duplicates(subset='Time', keep="first")


data2 = pd.read_csv(f'{path}/{robot}_Pos.csv')
data2=data2.drop_duplicates(subset='Time', keep="first")

'''



'''
'''

  
# using merge function by setting how='inner'
#output1 = pd.merge(data1, data2, on='Time', how='inner')

#path=f'/home/jazmin/bagfiles/{bagname}'  
#pd.concat([df1.set_index('A'),df2.set_index('A')], axis=1, join='inner')


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
