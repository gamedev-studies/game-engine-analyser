import os
import sys
import math
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime

script_path = Path().absolute()
print("Current script path:" + script_path)
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
    return str_command + " >> " + file_save_path

def append_to_old_file(old_filename, new_text):
    with open(old_filename, "r") as file:
        lines = file.readlines()
    count = len(lines)

    with open(old_filename, "w") as file:
        for i, line in enumerate(lines):
            clear_line = line.replace('/\\n', '/')
            if i < (count - 1):  
                file.write(clear_line)
            else:  
                file.write(new_text)  

    print("Appended to existing DOT file")
    
def save_report(stpass, ndpass, unresolved, count_unresolved, count_total):
    perc_unr = (count_unresolved/count_total)*100
    file = open(str(script_path) + '/outputs/' + engine_name + '-report.csv', 'w')
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

def resolve_includes(ds, start_line, line_range): 
    # 1 - get paths
    initial_len=len(arr_res_2nd)
    ds = ds[start_line:line_range]

    # for unreal: ignore ThirdParty subfolders, there are too many, it takes too long to analyse
    # other SDK folders are already identified, no need for all
    if 'unreal' in engine_name.lower():
        ds = ds[(~ds['file'].str.contains('ThirdParty'))]

    list_unresolved_paths = ds['includes'].values
    unique_filenames = get_unique_file_names(list_unresolved_paths)
    print('Reading lines:', start_line, 'to', line_range)

    # 2 - build command string
    str_command = build_find_commands(unique_filenames)

    # 3 - execute and save
    os.chdir(engine_path)

    try:
        exit_status = os.system(str_command)
        if exit_status != 0:
            raise Exception("Command failed with exit status " + str(exit_status))
    except Exception as e:
        print("An error occurred: " + str(e))

    unr_paths_file = open(file_save_path, 'r')
    list_unresolved_paths = list(unr_paths_file)
    unr_paths_file.close()

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

    if count_total == 0:
        print("Error: no includes to process in " + file_save_path)
        exit()

    save_report(count_1st, count_2nd, count_unresolved, count_unresolved, count_total)

    # 6 - write report resolved
    output = ''
    for path in arr_res_2nd[initial_len:]:
        ds_filtered = ds[(ds['includes'].str.contains(path[0]))]
        abs_path = path[1].replace('./', engine_path + '/')
        if len(ds_filtered) > 0:
            output += '	"' + ds_filtered.values[0][0] + '" -> "' + abs_path + '"\n'

    output += "}"

    append_to_old_file(str(script_path) + "/outputs/" + engine_name + "-includes.dot", output)

    # 7 - write report unresolved
    output = ""
    import re
    try:
        for path in arr_unresolved:
            path = path.replace("++", "\+\+")
            ds_filtered = ds[(ds['includes'].str.contains(path))]
            if len(ds_filtered) > 0:
                output += ds_filtered.values[0][0] + ',' + path + '\n'
            else:
                output += 'NA,' + path + '\n'
    except re.error as e:
        print("Regex error:", path)

    file = open(str(script_path) + "/outputs/" + engine_name + "-includes-unr.csv", "w")
    file.write(output)
    file.close()

# read every 2000 paths, it works better with long file names
start_line = 0
line_range = 2000
end_line = line_range
arr_res_2nd = []
arr_unresolved = []

print('Resolving includes, pass 2')
ds = pd.read_csv(str(script_path) + '/outputs/errors.txt', names=['file', 'includes'], header=None)
line_count = len(ds)
print('Lines to check:', line_count)
iter_count = math.ceil(line_count/line_range)

if line_count <= line_range:
    resolve_includes(ds, start_line, end_line)
else:
    for i in range(0, iter_count):
        resolve_includes(ds, start_line, end_line)
        start_line += line_range
        end_line += line_range