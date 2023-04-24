import pandas as pd
import numpy as np
import seaborn as sns

debug_mode = False

def main():
    map_dependencies = {}
    engines = [ "cocos2dx", "godot", "urho3d", "flaxengine", "gameplay", "o3de", "olc", "panda3d", "piccolo" ]
    subsystems = [ "AUD", "COR", "DEB", "EDI", "FES", "GMP", "HID", "LLR", "NIL", "OMP", "PHY", "PLA", "RES", "SDK", "SGC", "SKA", "VFX" ]

    for engine in engines:
        ds = pd.read_csv("inputs/matrix_" + engine + ".csv", sep=",")
        ds = ds.reindex(sorted(ds.columns), axis=1)
        ds = ds.sort_values(by=["asubsystem"])
        map_dependencies[engine] = np.array(ds.values[0:99, 1:18])

    sum = map_dependencies[engines[0]]
    for i in range(1, len(engines)):
        cur_matrix = map_dependencies[engines[i]]
        if debug_mode:
            print("=====")
            print(engines[i])
            print(cur_matrix)
            print(cur_matrix.shape)

        sum = np.add(sum, cur_matrix)

    # do not annotate values 0 and 1
    annot_values = np.array(sum, dtype=str)
    annot_values = np.where(sum < 2, np.array([""], dtype="U1"), annot_values)

    # set figure size
    sns.set(rc={"figure.figsize": (12, 8)})

    # pallette chosen because it is good for colorblind
    colormap = sns.color_palette("bwr")
    hm = sns.heatmap(
        sum.tolist(),
        vmin=0,
        vmax=9,
        annot=annot_values,
        xticklabels=subsystems,
        yticklabels=subsystems,
        cmap=colormap,
        cbar=True,
        fmt="",
    )
    fig = hm.get_figure()
    fig.savefig("outputs/heatmap.pdf")

    # generate csv for column and row counts
    sumRows(sum, subsystems)
    sumCols(sum, subsystems)


# get the sum for each column in the heatmap
# useful to understand how much included a subsystem is
def sumCols(matrix, subsystems):
    vals = []
    sub_count = len(subsystems)
    for i in range(0, sub_count):
        vals.append(matrix[:, i].sum())
    ds_most_inc_by = pd.DataFrame()
    ds_most_inc_by["subsystem"] = subsystems
    ds_most_inc_by["included_by"] = vals
    result = ds_most_inc_by.sort_values(by=["included_by"], ascending=False)
    result.to_csv("outputs/included_by.csv")

# get the sum for each row in the heatmap
# useful to understand how much a subsystem includes
def sumRows(matrix, subsystems):
    count = 0
    vals = []
    for line in matrix:
        vals.append(line.sum())
        count += 1
    ds_most_inc = pd.DataFrame()
    ds_most_inc["subsystem"] = subsystems
    ds_most_inc["include"] = vals
    result = ds_most_inc.sort_values(by=["include"], ascending=False)
    result.to_csv("outputs/include.csv")


main()
