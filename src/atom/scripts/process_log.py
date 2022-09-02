#!/usr/bin/env python3.8
import pandas as pd


bagname='trial'
robot='robot1'

path= '/home/jazmin/MultiRobots/src/atom/Csv'

register=[]
data= pd.read_csv(f'{path}/{robot}_{bagname}.csv', sep=';')

df = pd.DataFrame(columns=['Time' ,'Robot','Move'])

print(df)
for a in range(len(data['Time'])):
    posx= data.at[a,'position.x']
    posy= data.at[a,'position.y']
    timeA= data.at[a,'Time']
    if posx>-28.3 and posx< -20.66 and posy>23.5 and posy<40:
        place='esquina'
    else:
        place='a_unknown'
    df2=pd.DataFrame({'Time':[str(timeA)], 'Robot':[str(robot)], 'Move':[str(place)] })
    df=pd.concat([df, df2], ignore_index=True, axis=0)

path1= '/home/jazmin/MultiRobots/src/atom/Csv'

df.to_csv(f'{path1}/{robot}_{bagname}_pros.csv', sep=';', index=False)


    # pd.concat
    
    

print(df)
#for a in len(data):
#    if data.position.x
#df.at[1,'Product_Name']

