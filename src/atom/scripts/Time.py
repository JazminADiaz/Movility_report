#!/usr/bin/python3
from cmath import log
import pandas as pd
import pm4py


def import_csv(file_path):
    
    log = pd.read_csv(file_path, sep=',')
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
    log.to_csv('/home/jazmin/MultiRobots/src/atom/Csv/New/normal_t.csv', sep=',',index=False)






if __name__== "__main__":


    import_csv('/home/jazmin/MultiRobots/src/atom/Csv/New/combined_csv.csv')
