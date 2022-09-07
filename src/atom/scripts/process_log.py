#!/usr/bin/env python3.8
import pandas as pd
import numpy as np

bagname='trial2'
robot='robot1'
place=[]
placex=np.array([])
placey=np.array([])
r=2.7
import csv
flag=False
s_place='not_yet'

path= '/home/jazmin/MultiRobots/src/atom/Csv/og'



#data= pd.read_csv(f'{path}/{robot}_{bagname}.csv', sep=';')
data= pd.read_csv(f'{path}/{robot}_{bagname}_og.csv', sep=',')


path1= '/home/jazmin/MultiRobots/src/atom/Csv'

f = open(f'{path1}/{robot}_{bagname}_pros.csv', 'w', encoding='UTF8')
writer = csv.writer(f)

writer.writerow(['Time' ,'Robot','Move'])

#### PLACES TO CHECK
place.append('Mario_Cell')
placex=np.append(placex, 6.97)
placey=np.append(placey, -40.47)


place.append('Cafe_Palantino')
placex=np.append(placex, 3.55)
placey=np.append(placey, -32.63)

place.append('LiliPink')
placex=np.append(placex, -5.407)
placey=np.append(placey, -12.86)

place.append('Confamiliar')
placex=np.append(placex, -12.20)
placey=np.append(placey, 4.67)


place.append('Exito')
placex=np.append(placex, -21.15)
placey=np.append(placey, 23.59)

place.append('Sweet')
placex=np.append(placex, -28.44)
placey=np.append(placey, 40.55)


for a in range(len(data['Time'])):
    posx= data.at[a,'PosX']
    posy= data.at[a,'PosY']
    timeA= data.at[a,'Time']
    s_place_saved=s_place


    for i in range(len(place)):

        
        if (((posx - placex[i])**2) + ((posy-placey[i])**2))<(r**2):
            
            
            s_place=place[i]
            

    if s_place!=s_place_saved:
        writer.writerow([timeA,robot,s_place])
        


f.close()

'''
for a in range(len(data['Time'])):
    posx= data.at[a,'PosX']
    posy= data.at[a,'PosY']
    timeA= data.at[a,'Time']
    s_place_saved=s_place
    for i in range(len(place)):
        
        if (((posx - placex[i])**2) + ((posy-placey[i])**2))<(r**2):
            
            s_place=place[i]
            
            flag=True
        if flag ==False:
            s_place='moving'
            flag=False
       
    
    if s_place!=s_place_saved:
        writer.writerow([timeA,robot,s_place])
f.close()


'''



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
