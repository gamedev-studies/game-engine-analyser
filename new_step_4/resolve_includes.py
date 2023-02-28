import os
import sys
import numpy as np
import pandas as pd

file_save_path = 'bobo.txt'
engine_path = sys.argv[1]

def to_array(path_str):
    path_str = path_str.replace('<', '').replace('>', '').replace('"', '')
    return path_str.split('/')[::-1]


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
    unique_filenames = list(map(lambda item: (".*/" + item), unique_filenames))
    str_command = "find . -type f -regex '" + \
        ("\|".join(unique_filenames)) + "'"
    return str_command + " > " + file_save_path


arr_res_2nd = []
arr_unresolved = []

# 1 - load
ds = pd.read_csv('errors.txt', names=['file', 'includes'], header=None)[0:1000]
unique_filenames = get_unique_file_names(ds['includes'].values)

# 2 - build command string
str_command = build_find_commands(unique_filenames)

# 3 - execute and save
os.chdir(engine_path)
os.system(str_command)
result = list(open(file_save_path, 'r'))

# 4 - resolve one by one
for filename in unique_filenames:
    defg = filename.replace(".*/", "")
    abc = list(filter(lambda item: defg in item, result))
    print(abc, defg)
    if len(abc) > 0:
        ref_path = to_array(abc[0])
        possible_files = list(filter(lambda item: defg in item, result))
        risolvido = resolve_include(possible_files, ref_path)
        arr_res_2nd.append(risolvido)
    else:
        arr_unresolved.append(filename)
