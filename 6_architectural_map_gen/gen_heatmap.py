import pandas as pd
import numpy as np
import seaborn as sns

def main():
    map_dependencies = {}
    engines = ['cocos2d-x', 'godot', 'urho3d']
    subsystems = ['AUD','COR','DEB','EDI','FES','GMP','HID','LLR','OMP','PHY','PLA','RES','SDK','SGC','SKA','VFX']

    for engine in engines:
        ds = pd.read_csv('matrix_' + engine + '.csv', sep=',')
        ds2 = ds.reindex(sorted(ds.columns), axis=1)
        ds2 = ds2.sort_values(by=['asubsystem'])
        map_dependencies[engine] = np.array(ds2.values[0:99, 1:17])

    sum2 = map_dependencies['cocos2d-x'] + map_dependencies['godot'] + map_dependencies['urho3d']
    sns.set(rc={'figure.figsize':(12,8)})

    # pallette chosen because it is good for colorblind
    colormap = sns.color_palette("bwr")
    hm = sns.heatmap(sum2.tolist(), vmin=0, vmax=3, annot=True, 
                    xticklabels=subsystems, yticklabels=subsystems, cmap=colormap, cbar=True)
    fig = hm.get_figure()
    fig.savefig("heatmap.pdf") 

# get the sum for each column in the heatmap
# useful to understand how much included a subsystem is
def sumCols(matrix, subsystems):
    vals = []
    for i in range(0,16):
        vals.append(matrix[:,i].sum())
    ds_most_inc_by = pd.DataFrame()
    ds_most_inc_by['sub'] = subsystems
    ds_most_inc_by['values'] = vals
    result = ds_most_inc_by.sort_values(by=['values'], ascending=False)
    print(result)

# get the sum for each row in the heatmap
# useful to understand how much a subsystem includes
def sumRows(matrix, subsystems):
    count = 0
    vals = []
    for line in matrix:
        vals.append(line.sum())
        count += 1
    ds_most_inc = pd.DataFrame()
    ds_most_inc['sub'] = subsystems
    ds_most_inc['values'] = vals
    result = ds_most_inc.sort_values(by=['values'], ascending=False)
    print(result)

main()