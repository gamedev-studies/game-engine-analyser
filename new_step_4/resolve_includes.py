import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path

script_path = Path().absolute()
file_save_path = 'bobo.txt'
engine_path = sys.argv[1]
engine_name = sys.argv[2]

def to_array(path_str):
    path_str = path_str.replace('<', '').replace('>', '').replace('"', '')
    return path_str.split('/')[::-1]

def to_astr(path_arr):
    return "/".join(path_arr)

def resolve_include(possible_files, ref_path):
    ref_pos = 1
    if len(possible_files) == 0:
        return '(unresolved)'
    else:
        # no need to check if there is nothing to check
        if len(ref_path) == 1:
            return possible_files[0]
        else:
            # check if matches
            for file in possible_files:
                if ref_path[ref_pos] + "/" in file:
                    return file
            # if not exact match, return first
            # todo: go back other folders
            return possible_files[0]

def get_unique_file_names(includes):
    arr = []
    for item in includes:
        path = to_array(item)
        arr.append(path[0])
    arr = np.unique(np.array(arr))
    arr = filter(lambda item: ("." in item), arr)
    arr = list(arr)
    return arr

def build_find_commands(unique_filenames):
    # how to get full path?
    unique_filenames = list(map(lambda item: (".*/" + item), unique_filenames))
    str_command = "find . -type f -regex '" + \
        ("\|".join(unique_filenames)) + "'"
    return str_command + " > " + file_save_path

arr_res_2nd = []
arr_unresolved = []

# 1 - load
ds = pd.read_csv('./outputs/errors.txt', names=['file', 'includes'], header=None)[0:10000]
list_unresolved_paths = ds['includes'].values
unique_filenames = get_unique_file_names(list_unresolved_paths)

# 2 - build command string
str_command = build_find_commands(unique_filenames)

# 3 - execute and save
os.chdir(engine_path)
os.system(str_command)
list_unresolved_paths = list(open(file_save_path, 'r'))

# 4 - resolve each unique filename on errors.txt
for filename in unique_filenames:
    filename = filename.replace(".*/", "")
    possible_files = list(filter(lambda path: filename in path, list_unresolved_paths))
    
    # 4.1 - if the file is in the list, try to resolve
    if len(possible_files) > 0:
        ref_path = to_array(possible_files[0])
        resolved_filename = resolve_include(possible_files, ref_path)
        if resolved_filename == "(unresolved)":
            arr_unresolved.append(filename)
        else:
            arr_res_2nd.append([ref_path[0].replace('\n', ''), resolved_filename.replace('\n', '')])
    else:
        arr_unresolved.append(filename)

# 5 - print stats
print("==========")
print(len(arr_res_2nd), "resolved on 2nd pass")
print(len(arr_unresolved), "unresolved", )
print("==========")

# 6 - write report resolved
os.chdir(script_path)
output = 'digraph "source tree" { overlap=scale; size="8,10"; ratio="fill"; fontsize="16"; fontname="Helvetica"; clusterrank="local";'
for path in arr_res_2nd:
    ds_filtered = ds[(ds['includes'].str.contains(path[0]))]
    abs_path = path[1].replace('./', engine_path + '/')
    output += ds_filtered.values[0][0] + ' -> ' + abs_path + '\n'
output += "}"
file = open("outputs/" + engine_name + "_res_2nd.dot", "w")
file.write(output)
file.close()

# 7 - write report unresolved
output = ""
for path in arr_unresolved:
    ds_filtered = ds[(ds['includes'].str.contains(path))]
    output += ds_filtered.values[0][0] + ',' + path + '\n'

file = open("outputs/" + engine_name + "_unresolved.csv", "w")
file.write(output)
file.close()