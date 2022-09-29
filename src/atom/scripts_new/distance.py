#23.72, 22.325
#41.28, 29.75

from cmath import sqrt

###Total 
Tx1=23.72
Ty1=22.325

#x2=-28.72 
#y2= 41.14

Tx2= 41.28
Ty2= 29.75

Td=sqrt((Tx2-Tx1)**2+(Ty2-Ty1)**2)
Tt=Td/0.5
print(f'Total:{Td}, {Tt}')

print(4*12)
print(19/0.5)
print(((11*19)/0.5)+48)


import pm4py
import pandas as pd

file_path2=f'/home/jazmin/MultiRobots/src/atom/Csv/New/comb_time.csv'
deviation_d = pd.read_csv(file_path2, sep=',')
log = pm4py.format_dataframe(deviation_d, case_id='Robot', activity_key='Move', timestamp_key='Time', timest_format='%H:%M:%S')
all_case_durations = pm4py.get_all_case_durations(log)
print(all_case_durations)



