import os
import sys
import pandas as pd

engines = ['cocos2d-x','FlaxEngine','gameplay','godot','o3de','olcPixelGameEngine','panda3d','Piccolo','UnrealEngine','Urho3D']
#engines = ['Piccolo']
subsystems = ['AUD','COR','EDI','GMP','HID','LLR','OMP','PHY','PLA','RES','DEB','FES','SDK','SGC','SKA','VFX']
all_eng_subs = pd.DataFrame()
all_eng_subs['header'] = subsystems

def compute_metric():
    for engine in engines:
        aux = []
        for subsystem in subsystems:
            path = os.getcwd() + "/results"
            eng_sub_name = engine + '_' + subsystem
            #print("=====")
            #print(subsystem)
            if os.path.exists(path + '/' + eng_sub_name + '/' + eng_sub_name + '_edges_ordered.csv'):
                ds = pd.read_csv(path + '/' + eng_sub_name + '/' + eng_sub_name + '_edges_ordered.csv', sep=",")
                aux.append(ds['sum'].sum())
                #print(ds['sum'].sum())
                #print("=====")
            else:
                aux.append(0)
        all_eng_subs[engine] = aux

    result = ""
    for engine in engines:
        all_eng_subs_sorted = all_eng_subs.sort_values(by=engine, ascending=False)
        result += engine + ","
        first = True
        for item in all_eng_subs_sorted['header'].values:
            if first:
                first = False
                result += "[[" + item + "]"
            else:
                result += ",[" + item + "]"
        result += "]\n"
    print(result)

compute_metric()