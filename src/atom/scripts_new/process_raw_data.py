#!/usr/bin/env python3.8
import pandas as pd
import numpy as np

import csv

##CAMBIO
situation='robot21'

bagname=f'normal_{situation}'

saving=[]
place=[]
placex=np.array([])
placey=np.array([])
r=2.7


s_place=''
s_place_saved=''
vel_s=''

path= '/home/jazmin/MultiRobots/src/atom/Csv/New'


data= pd.read_csv(f'{path}/{bagname}.csv', sep=',')
print(data)

f = open(f'{path}/{bagname}_pros.csv', 'w', encoding='UTF8')

writer = csv.writer(f)

writer.writerow(['Time' ,'Robot','Move'])
writer.writerow([data.Time[0] ,situation,'start'])

#### PLACES TO CHECK
place.append('C1')
placex=np.append(placex, -41.137)
placey=np.append(placey, 17.35)
'''
place.append('C2')
placex=np.append(placex, -42.31)
placey=np.append(placey, -6.07)

place.append('C3')
placex=np.append(placex, -42.45)
placey=np.append(placey, -28.57)

place.append('C5')
placex=np.append(placex, -24.07)
placey=np.append(placey, -21.05)

place.append('C6')
placex=np.append(placex, -16.22)
placey=np.append(placey, -39.69)


place.append('C7')
placex=np.append(placex, -28.601)
placey=np.append(placey, 40.77)

'''



place.append('C4')
placex=np.append(placex, -32.44)
placey=np.append(placey, -1.379)






place.append('C8')
placex=np.append(placex, -21.768)
placey=np.append(placey, 24.659)

place.append('C9')
placex=np.append(placex, -13.22)
placey=np.append(placey, 5.64)

place.append('C14')
placex=np.append(placex, -2.87)
placey=np.append(placey, 32.8)


place.append('C15')
placex=np.append(placex, 5.07)
placey=np.append(placey, 13.78)

place.append('C16')
placex=np.append(placex, 12.84)
placey=np.append(placey, -4.454)

place.append('C17')
placex=np.append(placex, 21.308)
placey=np.append(placey, -23.597)

place.append('C22')
placex=np.append(placex, 39.98)
placey=np.append(placey, -15.02)

place.append('C21')
placex=np.append(placex, 31.93)
placey=np.append(placey, 4.09)

place.append('C20')
placex=np.append(placex, 23.719)
placey=np.append(placey, 22.325)

place.append('C23')
placex=np.append(placex, 41.28)
placey=np.append(placey, 29.75)




#place.append('End')

#placex=np.append(placex, -27.72)
#placey=np.append(placey, 40.19)



for a in range((len(data['Time']))):
    posx= data.at[a,'PosX']
    posy= data.at[a,'PosY']
    timeA= data.at[a,'Time']
    speed= data.at[a,'Speed']

#TIEMPO
    
    t=timeA
    h=t/3600
    hi= int(t/3600)
    m=(h-hi)*60
    mi=int(m)
    s=(m-mi)*60
    si=int(s)
    z=(s-si)*1000
    timeA=(str(hi)+':'+str(mi)+':'+str(int(round(s))))


#LUGAR
    for i in range(len(place)):

        
        if (((posx - placex[i])**2) + ((posy-placey[i])**2))<(r**2):

            s_place=place[i]
            
        



    if s_place!=s_place_saved:
        writer.writerow([data.Time[a],situation,s_place])
        #writer.writerow([timeA,situation,s_place])
        print(place[i])
        s_place_saved=s_place






#VELOCIDAD
    if a <( (len(data['Speed'])) -1):
        
        speed_a =data.at[a+1,'Speed']
        
        if speed<(0.001):
            vel='stop'



        if (round(speed_a, 1)==round(speed, 1) and speed_a>(0.1)):

            vel= 'mov_cte'


        if vel_s!=vel:
            writer.writerow([data.Time[a],situation,vel])
            vel_s=vel


#INICIO Y FINAL 

    if a== (len(data['Time']))-1:
        writer.writerow([data.Time[a] ,situation,'end'])

        
f.close()
'''
cv=f'normal_robot'




robot1=pd.read_csv(f'{path}/{cv}1_pros.csv', sep=',')
robot2=pd.read_csv(f'{path}/{cv}2_pros.csv', sep=',')
robot3=pd.read_csv(f'{path}/{cv}3_pros.csv', sep=',')
robot4=pd.read_csv(f'{path}/{cv}4_pros.csv', sep=',')
robot5=pd.read_csv(f'{path}/{cv}5_pros.csv', sep=',')


frames=[robot1, robot2, robot3, robot4, robot5]


result = pd.concat(frames)
file_path='/home/jazmin/MultiRobots/src/atom/Csv/New/normal.csv'


result.to_csv(file_path, sep=',', index=False)

log = pd.read_csv(file_path, sep=',')
import pandas as pd


time_log=[]
for i in range(0, len(log.Time)):
    t=log.Time[i]
    #print("t="+str(t))
    h=t/3600
    hi= int(t/3600)
    m=(h-hi)*60
    mi=int(m)
    s=(m-mi)*60
    time_log.append(str(hi)+':'+str(mi)+':'+str(int(round(s))))

log['Time'] = time_log
path= '/home/jazmin/MultiRobots/src/atom/Csv/New/normal_time.csv'
log.to_csv({path}, sep=',',index=False)


'''


