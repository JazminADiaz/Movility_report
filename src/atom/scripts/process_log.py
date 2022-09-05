#!/usr/bin/env python3.8
import pandas as pd
import numpy as np

bagname='trial_2'
robot='robot1'
place=[]
placex=np.array([])
placey=np.array([])
r=1.3
import csv
flag=False

path= '/home/jazmin/MultiRobots/src/atom/Csv'


data= pd.read_csv(f'{path}/{robot}_{bagname}.csv', sep=';')


path1= '/home/jazmin/MultiRobots/src/atom/Csv'

f = open(f'{path1}/{robot}_{bagname}_pros.csv', 'w', encoding='UTF8')
writer = csv.writer(f)

writer.writerow(['Time' ,'Robot','Move'])

#### PLACES TO CHECK
place.append('Exito')
placex=np.append(placex, -21.5)
placey=np.append(placey, 24.5)



place.append('Amorel')
placex=np.append(placex, -13.3)
placey=np.append(placey, 5.7)



place.append('Sebas')
placex=np.append(placex, -5.3)
placey=np.append(placey, -13)

for a in range(len(data['Time'])):
    posx= data.at[a,'position.x']
    posy= data.at[a,'position.y']
    timeA= data.at[a,'Time']

    for i in range(len(place)):
        if (((posx - placex[i])**2) + ((posy-placey[i])**2))<(r**2):
            s_place=place[i]
            flag=True
        if flag ==False:
            s_place='moving'
            flag=False
    writer.writerow([timeA,robot,s_place])
f.close()




'''
df = pd.DataFrame(columns=['Time' ,'Robot','Move'])


#### PLACES TO CHECK
place.append('Exito')
placex=np.append(placex, -21.5)
placey=np.append(placey, 24.5)



place.append('Amorel')
placex=np.append(placex, -13.3)
placey=np.append(placey, 5.7)



place.append('Sebas')
placex=np.append(placex, -5.3)
placey=np.append(placey, -13)




#####with open('document.csv','a') as fd:
   # fd.write(myCsvRow)

for a in range(len(data['Time'])):
    posx= data.at[a,'position.x']
    posy= data.at[a,'position.y']
    timeA= data.at[a,'Time']
    
    for i in range(len(place)):
        if (((posx - placex[i])**2) + ((posy-placey[i])**2))<(r**2):
            s_place=place[i]
            flag=True
    if flag ==False:
        s_place='moving'
        flag=False

    #df2=pd.DataFrame({'Time':[str(timeA)], 'Robot':[str(robot)], 'Move':[str(s_place)] })
    #df=pd.concat([df, df2], ignore_index=True, axis=0)

path1= '/home/jazmin/MultiRobots/src/atom/Csv'



#df.to_csv(f'{path1}/{robot}_{bagname}_pros.csv', sep=';', index=False)
'''
