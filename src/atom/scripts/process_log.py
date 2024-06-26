#!/usr/bin/env python3.8
import pandas as pd
import numpy as np

import csv

##CAMBIO
situation='deviation10'
ruta=10

#IGUAL
robot=f'robot{ruta}'
bagname=f'{situation}R{ruta}'
print(bagname)


place=[]
placex=np.array([])
placey=np.array([])
r=2.7


s_place='not_yet'
s_place_saved=''
vel_s=''

path= '/home/jazmin/MultiRobots/src/atom/Csv'


data= pd.read_csv(f'{path}/{bagname}.csv', sep=',')
print(data)

f = open(f'{path}/{bagname}_pros.csv', 'w', encoding='UTF8')

writer = csv.writer(f)

writer.writerow(['Time' ,'Robot','Move'])

#### PLACES TO CHECK
place.append('Mario_Cell')
placex=np.append(placex, 6.97)
placey=np.append(placey, -40.47)


place.append('Cafe_Palantino')
placex=np.append(placex, 2.58)
placey=np.append(placey, -31.726)

place.append('LiliPink')
placex=np.append(placex, -5.407)
placey=np.append(placey, -12.86)

place.append('Confam_drog')
placex=np.append(placex, -13.167)
placey=np.append(placey, 5.625)


place.append('Exito')
placex=np.append(placex, -21.52)
placey=np.append(placey, 24.45)

place.append('Sweet')
placex=np.append(placex, -28.72)
placey=np.append(placey, 41.14)


place.append('Notaria4')
placex=np.append(placex, 21.66)
placey=np.append(placey, -23.708)

place.append('mettler')
placex=np.append(placex, 32.11)
placey=np.append(placey, 4.05)

place.append('CristoRey_I')
placex=np.append(placex, 40.16)
placey=np.append(placey, -14.89)

place.append('GobernacioNarino')
placex=np.append(placex, 13.15)
placey=np.append(placey, -4.61)

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
        writer.writerow([timeA,robot,s_place])
        print(place[i])
        s_place_saved=s_place






#VELOCIDAD
    if a <( (len(data['Speed'])) -1):
        
        speed_a =data.at[a+1,'Speed']
        
        if speed<(0.001):
            vel='stop'

        if (round(speed_a, 1)-0.1>=round(speed, 1)):
            print(f'aceleración:s_a={speed_a}, s={speed}')
            vel= 'aceleración'

        if (round(speed_a, 1)+0.3<=round(speed, 1)):
            vel= 'desacelaración'
            print(f'desaceleración:s_a={speed_a}, s={speed}')
        #if (vel_s!=vel):


        if (round(speed_a, 1)==round(speed, 1) and speed_a>(0.1)):

            vel= 'mov_cte'


        if vel_s!=vel:
            writer.writerow([timeA,robot,vel])
            vel_s=vel


#INICIO Y FINAL 
f.close()

