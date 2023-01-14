import os
import sys
import numpy as np
import pandas as pd

debug = False

def get_vector_format(line):
    result = line.strip().replace('"', "").split("->")
    return list(map(lambda item: item.strip(), result))

def generate_unique_node_ids(node_list, id_type):
    name_map = {}
    all_node_names = np.array([])

    if id_type == "for_yann" or id_type == "for_consensus":
        ascii_begin = 65
        ascii_end = 91
        ascii_limit = ascii_end - ascii_begin
        alphabet = np.arange(ascii_begin, ascii_end)
    elif id_type == "number":
        starting_number = 1

    # get unique names
    for node in node_list:
        all_node_names = np.append(all_node_names, str(node).strip())
    unique_names = np.unique(all_node_names)

    counter = 0
    if id_type == "for_yann" or id_type == "for_consensus":
        cycle = 1
        for name in unique_names:
            name_map[name] = chr(alphabet[counter]) + str(cycle)
            counter += 1
            if counter == ascii_limit:
                counter = 0
                cycle += 1
    elif id_type == "number":
        counter = starting_number
        for name in unique_names:
            name_map[name] = str(counter)
            counter += 1
    else:
        print("Error: unknown ID type. Types allowed: string, number.")

    return name_map

def to_set(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def concat_vector_items(id_type, ordered_dot_ids):
    first_item = True
    if id_type == "for_consensus":
        result_vector = np.array([])
        for file_id in ordered_dot_ids:
            result_vector = np.append(result_vector, file_id[0])
        result_vector = to_set(result_vector)
        result_vector = ",".join(result_vector)
    elif id_type == "for_yann":
        result_vector = ""
        for file_id in ordered_dot_ids:
            if first_item:
                result_vector += "inc".join(file_id)
                first_item = False
            else:
                result_vector += "," + ("inc".join(file_id))
    elif id_type == "number":
        result_vector = ""
        for file_id in ordered_dot_ids:
            pair = ",".join(file_id)
            if first_item:
                result_vector += "(" + pair + ",1)"
                first_item = False
            else:
                result_vector += ",(" + pair + ",1)"
    return result_vector

def gen_vector(id_type="number", save_to_file=True, engine="engine", subsystem="subsystem", subsystem_folder_string=""):
    # prepare to check subsystem folders
    subsystem_folders = subsystem_folder_string.split(",")
    
    # order edges by sum of includes and save
    engine = sys.argv[1]
    path = os.getcwd() + "/graphs/" + engine + "_"
    ds = []
    try:
        ds = pd.read_csv(path + "edge_count.csv")
    except Exception as e:
        print("Error when reading edge count file:", e)

    if (len(ds) == 0):
        print("ATTENTION! Edge count file is empty or malformed, cannot proceed")
        exit()

    ds = ds[(ds.includes != "includes")]
    query = ""
    first_query_item = True
    for subsystem_folder in subsystem_folders:
        if first_query_item:
            # check if path contains file/folder we passed as CLI param
            query += "edge.str.contains('" + subsystem_folder + "')"
            first_query_item = False
        else:
            query += " | edge.str.contains('" + subsystem_folder + "/')"
    ds = ds.sort_values(by="sum", ascending=False)
    ds = ds.query(query)
    ds.to_csv("./results/" + engine + "_" + subsystem + "/" + engine + "_" + subsystem + "_edges_ordered.csv")

    # read the dot file and save lines to array
    dot_file = open(path + "subsystem.dot", "r")
    dot_file_lines = []
    for line in dot_file:
        dot_file_lines.append(line)

    # generate unique ids for files
    ordered_dot = []
    ordered_dot_ids = []
    ordered_file_names = ds["edge"].values 
    name_map = generate_unique_node_ids(ordered_file_names, id_type)

    if id_type == "number" or id_type == "for_yann":
        for file_name in ordered_file_names:
            for line in dot_file_lines:
                if file_name + '" ->' in line:
                    ordered_dot.append(get_vector_format(line))
        for line in ordered_dot:
            node = ""
            include = ""
            # match names in the .dot with the ids
            try:
                node = name_map[line[0]]
                include = name_map[line[1]]
            except KeyError:
                keys = list(name_map.values())
                if id_type == "number":
                    include = str(int(keys[len(keys) - 1]) + 1)
                elif id_type == "for_yann":
                    include = "null"
                print("child/parent of parent file not in the subsystem folder: ", line[1])
            ordered_dot_ids.append([node, include])
    elif id_type == "for_consensus":
        for line in ordered_file_names:
            try:
                if debug:
                    print(line)
                node = name_map[line]
            except KeyError:
                node = "null"
                print("warning! parent file not in the subsystem folder: ", line[0])
            ordered_dot_ids.append([node, "null"])
    result_vector = concat_vector_items(id_type, ordered_dot_ids)

    if not save_to_file:
        if debug:
            print(result_vector)
            print(name_map)
    else:
        vector_file = open("./results/" + engine + "_" + subsystem + "/" + engine + "_" + subsystem + "_vector.csv", "w")
        if id_type == "for_consensus":
            result_vector = "[[" + result_vector.replace(",", "],[") + "]]"
        vector_file.write(result_vector)
        vector_file.close()

        map_file = open("./results/" + engine + "_" + subsystem + "/" + engine + "_" + subsystem + "_vector_map.json", "w")
        map_file.write(str(name_map).replace("'", '"'))
        map_file.close()

print("start")
if sys.argv[1] and sys.argv[2]:
    print(sys.argv[1], sys.argv[2])
    gen_vector("for_consensus", True, sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print("No engine/subsystem name informed")
