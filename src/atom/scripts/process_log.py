#!/usr/bin/env python3.8
import pandas as pd


bagname='subset5'
robot='robot1'

path= '/home/jazmin/MultiRobots/src/atom/Csv'



data= pd.read_csv(f'{path}/{robot}_{bagname}.csv', sep=';')


print(data['position.x'])

#for a in len(data):
#    if data.position.x

