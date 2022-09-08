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
    path= '/home/jazmin/MultiRobots/src/atom/Csv'
    log.to_csv(f'{path}/{bagname}_pros.csv', sep=',',index=False)






if __name__== "__main__":

    ##CAMBIO
    situation='ideal'
    ruta_prog=True

    ruta=1

    #IGUAL
    robot=f'robot{ruta}'
    bagname=f'{situation}R{ruta}'

    path= '/home/jazmin/MultiRobots/src/atom/Csv'

    import_csv(f'{path}/{bagname}_pros.csv')
