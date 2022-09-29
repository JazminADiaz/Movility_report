import os
import glob
import pandas as pd
import pm4py
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.algo.conformance.tokenreplay.diagnostics import duration_diagnostics

fitnesA=[]
fitnesN=[]

file_path= '/home/jazmin/MultiRobots/src/atom/Csv/New/ideal20_t.csv'
perfect_model_d = pd.read_csv(file_path, sep=',')
perfect_model_d = pm4py.format_dataframe(perfect_model_d, case_id='Robot', activity_key='Move', timestamp_key='Time', timest_format='%H:%M:%S')
perfect_model = pm4py.convert_to_event_log(perfect_model_d)

perf_m_net, i_m, f_m =pm4py.discover_petri_net_heuristics(perfect_model)
parameters = {pn_visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "png"}
gviz = pn_visualizer.apply(perf_m_net, i_m, f_m, parameters=parameters, variant=pn_visualizer.Variants.FREQUENCY, log=perfect_model)

pn_visualizer.save(gviz, "/home/jazmin/MultiRobots/src/atom/Csv/New/Idela20_frec.png")

file_path2= '/home/jazmin/MultiRobots/src/atom/Csv/New/normal_t.csv'
deviation_d = pd.read_csv(file_path2, sep=',')
deviation_d = pm4py.format_dataframe(deviation_d, case_id='Robot', activity_key='Move', timestamp_key='Time', timest_format='%H:%M:%S')
deviation_model = pm4py.convert_to_event_log(deviation_d)

dev_1, i_m1, f_m1 =pm4py.discover_petri_net_heuristics(deviation_model)
parameters = {pn_visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "png"}
gviz = pn_visualizer.apply(dev_1, i_m1, f_m1, parameters=parameters, variant=pn_visualizer.Variants.FREQUENCY, log=perfect_model)

pn_visualizer.save(gviz, "/home/jazmin/MultiRobots/src/atom/Csv/New/normal_frec.png")











os.chdir("/home/jazmin/MultiRobots/src/atom/Csv/New/normales")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

for f in all_filenames:
    

    file_path2=f'/home/jazmin/MultiRobots/src/atom/Csv/New/normales/{f}'
    deviation_d = pd.read_csv(file_path2, sep=',')
    deviation_d = pm4py.format_dataframe(deviation_d, case_id='Robot', activity_key='Move', timestamp_key='Time', timest_format='%H:%M:%S')
    deviation=pm4py.convert_to_event_log(deviation_d)

    dev_m_net, i_m2, f_m2 = pm4py.discover_petri_net_heuristics(deviation) 
    pm4py.save_vis_petri_net(dev_m_net, i_m2, f_m2, f'/home/jazmin/MultiRobots/src/atom/Csv/New/petri_{f}.png' )

    fitness_allig= pm4py.fitness_alignments(perfect_model, dev_m_net, i_m2, f_m2)

    fitnesN.append(f'FitA{f}')
    fitnesA.append({fitness_allig["averageFitness"]})



col1 = "Robot"
col2 = "AverageFitnes"
data = pd.DataFrame({col1:fitnesN,col2:fitnesA})
data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)
    
