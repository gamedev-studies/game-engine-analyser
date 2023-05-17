import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.colors as colors

def main():
    engine = sys.argv[1]
    subsystems = [ "AUD", "COR", "DEB", "EDI", "FES", "GMP", "HID", "LLR", "OMP", "PHY", "PLA", "RES", "SDK", "SGC", "SKA", "VFX" ]

    ds = pd.read_csv("inputs/matrix_" + engine + ".csv", sep=",")
    ds = ds.reindex(sorted(ds.columns), axis=1)
    ds = ds.sort_values(by=["asubsystem"])
    ds = ds[~ds["asubsystem"].str.contains("NIL")]
    ds = ds.drop(["asubsystem", engine + "-NIL"], axis=1)
    sum = ds.values

    # generate csv for column and row counts
    sumRows(engine, sum, subsystems)
    sumCols(engine, sum, subsystems)

# get the sum for each column in the heatmap
# useful to understand how much included a subsystem is
def sumCols(engine, matrix, subsystems):
    vals = []
    sub_count = len(subsystems)
    for i in range(0, sub_count):
        vals.append(matrix[:, i].sum())
    ds_most_inc_by = pd.DataFrame()
    ds_most_inc_by["subsystem"] = subsystems
    ds_most_inc_by["included_by"] = vals
    result = ds_most_inc_by.sort_values(by=["included_by"], ascending=False)
    result.to_csv("outputs/" + engine + "_included_by.csv")

# get the sum for each row in the heatmap
# useful to understand how much a subsystem includes
def sumRows(engine,matrix, subsystems):
    count = 0
    vals = []
    for line in matrix:
        vals.append(line.sum())
        count += 1
    ds_most_inc = pd.DataFrame()
    ds_most_inc["subsystem"] = subsystems
    ds_most_inc["include"] = vals
    result = ds_most_inc.sort_values(by=["include"], ascending=False)
    result.to_csv("outputs/" + engine + "_include.csv")

main()
