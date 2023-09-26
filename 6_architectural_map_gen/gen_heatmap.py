import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.colors as colors

debug_mode = False

def main():
    map_dependencies = {}
    subsystems = [ "AUD", "COR", "DEB", "EDI", "FES", "GMP", "HID", "LLR", "OMP", "PHY", "PLA", "RES", "SDK", "SGC", "SKA", "VFX" ]
    ds = pd.read_csv("inputs/matrix_all.csv", sep=",")
    ds = ds.drop(columns=['asubsystem'])
    print(ds)
    sum = np.array(ds.values)

    # do not annotate values 0 and 1
    annot_values = np.array(sum, dtype=str)
    annot_values = np.where(sum < 3, np.array([""], dtype="U1"), annot_values)

    # set figure size
    sns.set(rc={"figure.figsize": (12, 8)})

    # pallette chosen because it is good for colorblind
    colormap = sns.color_palette("bwr")
    
    cmap_colors = ['#ffeceb', '#fcdad7', '#fa6557', '#9c0f02' ]
    colormap = colors.ListedColormap(cmap_colors)

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
