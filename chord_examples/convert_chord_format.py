import pandas as pd
import numpy as np

def replace_subsystem(ds, line):
    result = line
    for sub in ds.values:
        result = result.replace('"' + sub[0] + '"', str(sub[1]))
    result = result.replace(' -> ', ',')
    result = result.replace('\t', '')
    return result

engines = [ "cocos2dx", "godot", "urho3d", "flaxengine", "gameplay", "o3de", "olc", "panda3d", "piccolo", "UnrealEngine"]

ds = pd.read_json('example_nodes.json')
print(ds.values)

for engine in engines:
    converted_dot = ''
    path = '../6_architectural_map_gen/outputs/' + engine + '.dot'
    with open(path) as file:
        for line in file:
           converted_dot += replace_subsystem(ds, line)

    converted_dot = converted_dot.replace('digraph "source tree" {', 'source,target')
    converted_dot = converted_dot.replace('}', '')
    with open('new_' + engine + '.csv', 'w') as file:
        file.write(converted_dot)