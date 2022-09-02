#!/usr/bin/env python3.8
import pandas as pd


bagname='trial'
robot='robot1'

path= '/home/jazmin/MultiRobots/src/atom/Csv'

register=[]
data= pd.read_csv(f'{path}/{robot}_{bagname}.csv', sep=';')

print((data.position.x[1]))