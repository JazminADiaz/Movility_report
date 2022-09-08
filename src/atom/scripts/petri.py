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
    
    file_path= f'{path}/{bagnameI}.csv'
    perfect_model_d = pd.read_csv(file_path, sep=',')
    perfect_model_d = pm4py.format_dataframe(perfect_model_d, case_id='Robot', activity_key='Move', timestamp_key='Time', timest_format='%H:%M:%S.%f')
    perfect_model = pm4py.convert_to_event_log(perfect_model_d)
    perf_m_net, i_m, f_m = inductive_miner.apply(perfect_model)

    pm4py.save_vis_petri_net(perf_m_net, i_m, f_m, f'{path}/{bagnameI}_petri.png' )
    '''
        parameters = {pn_visualizer.Variants.WO_DECORATION.value.Parameters.FORMAT: "png"}
        gviz = pn_visualizer.apply(perf_m_net, i_m, f_m, parameters=parameters, variant=pn_visualizer.Variants.FREQUENCY, log=perfect_model)
        pn_visualizer.save(gviz, f'{path}/{bagnameI}_petri_frec.png')
    '''


        #deviation model
    file_path2= f'{path}/{bagnameS}.csv'
    deviation_d = pd.read_csv(file_path2, sep=',')
    deviation_d = pm4py.format_dataframe(deviation_d, case_id='Robot', activity_key='Move', timestamp_key='Time', timest_format='%H:%M:%S')
    deviation=pm4py.convert_to_event_log(deviation_d)
    dev_m_net, i_m2, f_m2 = pm4py.discover_petri_net_inductive(deviation) 
    pm4py.save_vis_petri_net(dev_m_net, i_m2, f_m2, f'{path}/{bagnameS}_petri.png' )

          #Conformance checking
    #replayed_traces = pm4py.conformance_diagnostics_token_based_replay(deviation, perf_m_net, i_m, f_m)
    parameters_tbr = {token_based_replay.Variants.TOKEN_REPLAY.value.Parameters.DISABLE_VARIANTS: True, token_based_replay.Variants.TOKEN_REPLAY.value.Parameters.ENABLE_PLTR_FITNESS: True}
    replayed_traces, place_fitness, trans_fitness, unwanted_activities = token_based_replay.apply(perfect_model, dev_m_net,i_m2,f_m2, parameters=parameters_tbr)
    
    trans_diagnostics = duration_diagnostics.diagnose_from_trans_fitness(perfect_model, trans_fitness)
    for trans in trans_diagnostics:
        print(trans, trans_diagnostics[trans])
        #diagnostics
    
    '''
      #Conformance checking
    #replayed_traces = pm4py.conformance_diagnostics_token_based_replay(deviation, perf_m_net, i_m, f_m)
    parameters_tbr = {token_based_replay.Variants.TOKEN_REPLAY.value.Parameters.DISABLE_VARIANTS: True, token_based_replay.Variants.TOKEN_REPLAY.value.Parameters.ENABLE_PLTR_FITNESS: True}
    replayed_traces, place_fitness, trans_fitness, unwanted_activities = token_based_replay.apply(deviation, perf_m_net,i_m,f_m, parameters=parameters_tbr)
    
    trans_diagnostics = duration_diagnostics.diagnose_from_trans_fitness(deviation, trans_fitness)
    for trans in trans_diagnostics:
        print(trans, trans_diagnostics[trans])
        #diagnostics


    
    act_diagnostics = duration_diagnostics.diagnose_from_notexisting_activities(deviation, unwanted_activities)
    for act in act_diagnostics:
        print(act, act_diagnostics[act])
    
    '''
    

                                    

if __name__== "__main__":

    ideal='ideal'

    situation='deviation1'
    ruta_prog=True

    ruta=1

    #IGUAL
    robot=f'robot{ruta}'
    bagnameI=f'{ideal}R{ruta}'
    bagnameS=f'{situation}R{ruta}'
    bagnameI='Ideal'
    bagnameS='notideal'
    path= '/home/jazmin/MultiRobots/src/atom/Csv'

    import_csv()

