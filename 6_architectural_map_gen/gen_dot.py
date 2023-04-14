import pandas as pd
import numpy as np

engines = [ "cocos2dx", "godot", "urho3d", "flaxengine", "gameplay", "o3de", "olc", "panda3d", "piccolo" ]
subsystems = [ "AUD", "COR", "DEB", "EDI", "FES", "GMP", "HID", "LLR", "NIL", "OMP", "PHY", "PLA", "RES", "SDK", "SGC", "SKA", "VFX" ]

# for each engine
for engine in engines:
    dot_file = ""

    # load include matrix
    ds = pd.read_csv("inputs/matrix_" + engine + ".csv", sep=",")
    ds = ds.reindex(sorted(ds.columns), axis=1)
    ds = ds.sort_values(by=["asubsystem"])
    matrix = np.array(ds.values[0:99, 1:18])

    # when 1, create line for include
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 1:
                dot_file += "\t\"" + subsystems[j] + "\" -> \"" + subsystems[i] + "\"\n"

    # add header, save
    with open("outputs/" + engine + ".dot", "w") as file:
        file.write("digraph \"source tree\" {\n")
        file.write(dot_file)
        file.write("}")