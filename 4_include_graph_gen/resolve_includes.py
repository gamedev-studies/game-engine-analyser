import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime

script_path = Path().absolute()
file_save_path = 'unresolved.txt'
engine_path = sys.argv[1]
engine_name = sys.argv[2]

# ignore 8 lines which are graphviz boilerplate
count_1st = int(sys.argv[3].split(" ")[0]) - 8

starting_time = sys.argv[6] + ' ' + sys.argv[7] + ' ' + sys.argv[8] + ' ' + sys.argv[9]

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

def append_to_old_file(old_filename, new_text):
    with open(old_filename, "r") as file:
        lines = file.readlines()
    count = len(lines)
    print("count", count)
    print("new_text", new_text[0:15])

    with open(old_filename, "w") as file:
        for i, line in enumerate(lines):
            clear_line = line.replace('/\\n', '/')
            if i < (count - 1):  
                file.write(clear_line)
            else:  
                file.write(new_text)  
    
def save_report(stpass, ndpass, unresolved, count_unresolved, count_total):
    perc_unr = (count_unresolved/count_total)*100
    file = open('./outputs/' + engine_name + '_report.csv', 'w')
    file.write("attribute,value\n")
    file.write("engine name," + engine_name + '\n')
    file.write("analysis started at," + starting_time + '\n')
    file.write("report generated at," + datetime.today().strftime('%d %b %Y %I:%M:%S') + '\n')
    file.write("resolved on 1st pass," + str(stpass) + '\n')
    file.write("resolved on 2nd pass," + str(ndpass) + '\n')
    file.write("unresolved," + str(unresolved) + '\n')
    file.write("total includes," + str(count_total) + '\n')
    file.write("percentage of unresolved," + str(round(perc_unr, 2)) + '\n')
    file.close()

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

# 5 - print include count report
os.chdir(script_path)
count_2nd = len(arr_res_2nd)
count_unresolved = len(arr_unresolved)
count_total = count_1st + count_2nd + count_unresolved
save_report(count_1st, count_2nd, count_unresolved, count_unresolved, count_total)

# 6 - write report resolved
output = ''
for path in arr_res_2nd:
    ds_filtered = ds[(ds['includes'].str.contains(path[0]))]
    abs_path = path[1].replace('./', engine_path + '/')
    output += '	"' + ds_filtered.values[0][0] + '" -> "' + abs_path + '"\n'

output += "}"

append_to_old_file("./outputs/" + engine_name + "_includes.dot", output)

# 7 - write report unresolved
output = ""
for path in arr_unresolved:
    path = path.replace("++", "\+\+")
    ds_filtered = ds[(ds['includes'].str.contains(path))]
    if len(ds_filtered) > 0:
        output += ds_filtered.values[0][0] + ',' + path + '\n'
    else:
        output += 'NA,' + path + '\n'

file = open("outputs/" + engine_name + "_unresolved.csv", "w")
file.write(output)
file.close()