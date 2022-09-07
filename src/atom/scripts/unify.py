import pandas as pd

robot='robot1'
situation='ideal'
muestra='1'
bagname='idealR1'
path= '/home/jazmin/MultiRobots/src/atom/Csv/og'

data= pd.read_csv(f'{path}/{robot}_{bagname}_vel.csv')

data1= pd.read_csv(f'{path}/{robot}_{bagname}_og.csv')
data1= data1.drop_duplicates(subset='Time', keep="first")

df = pd.concat([data1.set_index('Time'), data.set_index('Time')], axis=1, join='inner')
