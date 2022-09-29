from importlib.resources import path
import os
import pm4py
import pandas as pd

path ='/home/jazmin/MultiRobots/src/atom/Csv/only_ideal.csv'

#path ='/home/jazmin/MultiRobots/src/atom/Csv/SaE/notideal.csv'


perfect_model_d = pd.read_csv(path, sep=',')
perfect_model_d = pm4py.format_dataframe(perfect_model_d, case_id='Robot', activity_key='Move', timestamp_key='Time', timest_format='%H:%M:%S')
perfect_model = pm4py.convert_to_event_log(perfect_model_d)
log=perfect_model

#filtered_log = pm4py.filter_variants_top_k(log, 3)
#print(filtered_log)

notideal = pd.read_csv('/home/jazmin/MultiRobots/src/atom/Csv/SaE/notideal.csv', sep=',')
notideal = pm4py.format_dataframe(notideal, case_id='Robot', activity_key='Move', timestamp_key='Time', timest_format='%H:%M:%S')
noideal = pm4py.convert_to_event_log(notideal)
filtered_log=noideal




net, initial_marking, final_marking = pm4py.discover_petri_net_heuristics(filtered_log)
print(pm4py.convert_to_dataframe(filtered_log))


from pm4py.algo.conformance.tokenreplay import algorithm as token_based_replay
parameters_tbr = {token_based_replay.Variants.TOKEN_REPLAY.value.Parameters.DISABLE_VARIANTS: True, token_based_replay.Variants.TOKEN_REPLAY.value.Parameters.ENABLE_PLTR_FITNESS: True}
replayed_traces, place_fitness, trans_fitness, unwanted_activities = token_based_replay.apply(log, net,
                                                                                              initial_marking,
                                                                                              final_marking,
                                                                                              parameters=parameters_tbr)
from pm4py.algo.conformance.tokenreplay.diagnostics import duration_diagnostics
trans_diagnostics = duration_diagnostics.diagnose_from_trans_fitness(log, trans_fitness)
for trans in trans_diagnostics:
    print(trans, trans_diagnostics[trans])

    '''
    from pm4py.algo.conformance.tokenreplay.diagnostics import duration_diagnostics
act_diagnostics = duration_diagnostics.diagnose_from_notexisting_activities(log, unwanted_activities)
for act in act_diagnostics:
    print(act, act_diagnostics[act])

# build decision trees
string_attributes = ["org:group"]
numeric_attributes = []
parameters = {"string_attributes": string_attributes, "numeric_attributes": numeric_attributes}

from pm4py.algo.conformance.tokenreplay.diagnostics import root_cause_analysis
trans_root_cause = root_cause_analysis.diagnose_from_trans_fitness(log, trans_fitness, parameters=parameters)

from pm4py.visualization.decisiontree import visualizer as dt_vis
for trans in trans_root_cause:
    clf = trans_root_cause[trans]["clf"]
    feature_names = trans_root_cause[trans]["feature_names"]
    classes = trans_root_cause[trans]["classes"]
    # visualization could be called
    gviz = dt_vis.apply(clf, feature_names, classes)
    dt_vis.view(gviz)
                        
from pm4py.algo.conformance.tokenreplay.diagnostics import root_cause_analysis
act_root_cause = root_cause_analysis.diagnose_from_notexisting_activities(log, unwanted_activities,
                                                                          parameters=parameters)
for act in act_root_cause:
    clf = act_root_cause[act]["clf"]
    feature_names = act_root_cause[act]["feature_names"]
    classes = act_root_cause[act]["classes"]
    # visualization could be called
    gviz = dt_vis.apply(clf, feature_names, classes)
    dt_vis.view(gviz)
    
    '''

