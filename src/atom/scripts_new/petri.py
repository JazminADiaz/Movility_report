#!/usr/bin/python3
#captcp statistic /tmp/meine_aufgabe-5-2.pcap
from tkinter.tix import Tree
import pandas as pd
import pm4py
from pm4py.visualization.petri_net.visualizer import ALIGNMENTS
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
#conformace checking:

from pm4py.algo.conformance.tokenreplay import algorithm as token_based_replay
from pm4py.algo.conformance.tokenreplay.diagnostics import duration_diagnostics
from pm4py.algo.conformance.tokenreplay.diagnostics import duration_diagnostics

def import_csv():



    #inductive miner
        
        #perfect model
    
    file_path= '/home/jazmin/MultiRobots/src/atom/Csv/New/ideal20.csv'
    perfect_model_d = pd.read_csv(file_path, sep=',')
    perfect_model_d = pm4py.format_dataframe(perfect_model_d, case_id='Robot', activity_key='Move', timestamp_key='Time', timest_format='%H:%M:%S')
    perfect_model = pm4py.convert_to_event_log(perfect_model_d)

    perf_m_net, i_m, f_m =pm4py.discover_petri_net_heuristics(perfect_model)

    pm4py.save_vis_petri_net(perf_m_net, i_m, f_m, '/home/jazmin/MultiRobots/src/atom/Csv/New/ideal.png' )

    file_path2='/home/jazmin/MultiRobots/src/atom/Csv/New/normal_t.csv'
    deviation_d = pd.read_csv(file_path2, sep=',')
    deviation_d = pm4py.format_dataframe(deviation_d, case_id='Robot', activity_key='Move', timestamp_key='Time', timest_format='%H:%M:%S')
    deviation=pm4py.convert_to_event_log(deviation_d)

    dev_m_net, i_m2, f_m2 = pm4py.discover_petri_net_heuristics(deviation) 
    pm4py.save_vis_petri_net(dev_m_net, i_m2, f_m2, '/home/jazmin/MultiRobots/src/atom/Csv/New/normal.png' )
    
    parameters = {pn_visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "png"}
    gviz = pn_visualizer.apply(dev_m_net, i_m2, f_m2, parameters=parameters, variant=pn_visualizer.Variants.FREQUENCY, log=perfect_model)

    pn_visualizer.save(gviz, "/home/jazmin/MultiRobots/src/atom/Csv/New/normal_frec.png")
    #


    #stadistics


    fitness_allig= pm4py.fitness_alignments(perfect_model, dev_m_net, i_m2, f_m2)
    print(f'alig_fit is:{fitness_allig["averageFitness"]}')

    #Aligment

    prec = pm4py.precision_alignments(perfect_model, dev_m_net, i_m2, f_m2)
    print(prec)


if __name__== "__main__":

    ideal='ideal'

    situation='deviation1'


    ruta=1

    #IGUAL

    bagnameI='Ideal'
    bagnameS='notideal'
    path= '/home/jazmin/MultiRobots/src/atom/Csv'

    import_csv()

