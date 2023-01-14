import json
import sys
import pandas as pd
  
# utils
def load_config(path):
    try:
        f = open(path)
        return json.load(f)
    except:
        print("Missing or malformed config file, please check if there is a config.json in the inputs folder")

def extract_name_parent(path):
    # deprecated
    if path and len(path) > 1 and path[0] == "/":
        return path[1:len(path)]
    return path

# main functions
def convert_dot_to_xml(config=None):
    if not config == None:
        # Aux vars
        included_by = []
        include = []

        # Using readlines()
        input_file = open(config['includes_dot_file_path'], 'r')
        lines = input_file.readlines()
        
        count = 0
        # Strips the newline character
        for line in lines:
            count += 1
            strp_line = line.strip()
            if len(strp_line) > 1 and strp_line[1] == "/":
                abc = line.replace('\"', '').replace('\t', '').replace('\n', '').split(" -> ")
                included_by.append(abc[0])
                include.append(abc[1])

        ds = pd.DataFrame()
        ds['includedBy'] = included_by
        ds['include'] = include

        xml_result = ""
        xml_result += "<project>\n"
        for item in included_by:
            filtered = ds[(ds['includedBy'] == item)]
            first = True
            for filtered_item in filtered.values:
                if first:
                    xml_result += "<file name=\"" + item + "\">\n"
                    xml_result += "<include type=\"local\" name=\"" + filtered_item[1] + "\" />\n"
                    first = False
                else:
                    xml_result += "<include type=\"local\" name=\"" + filtered_item[1] + "\" />\n"
            xml_result += "</file>\n"
        xml_result += "</project>\n"

        xml_result = xml_result.replace(config['project_full_path'], config['project_shortened_path'])

        output_file = open('outputs/' + config['project_name'] + '-includes.xml', 'w')
        lines = output_file.writelines(xml_result)
        output_file.close()
    else:
        print("Missing or malformed config file, please check if there is a config.json in the inputs folder")

def generate_tags_from_csv(config=None):
    pharo_code = "|model foldersTags tagsColors files modelFolders projName|\nprojName := '" + config['project_name'] + "'.\nmodel := MooseModel root at: x.\nfoldersTags := Dictionary newFrom: {\n"
    if not config == None:
        ds = pd.read_csv(config['tags_csv_file_path'], sep=',')
        for item in ds.values:
            path_parts = extract_name_parent(item[1])
            if not "'" + path_parts + "'" in pharo_code:
                pharo_code += "'" + path_parts + "' -> '" + item[0] + "' ."
        pharo_code += "}.\ntagsColors := Dictionary newFrom: { 'AUD' -> '#f0e442'. 'OMP' -> '#ff0000'. 'HID' -> '#ea9999'. 'DEB' -> '#cccccc'. 'SGC' -> '#009e73'. 'LLR' -> '#00b816'. 'VFX' -> '#b8f100'. 'FES' -> '#6de900'. 'PLA' -> '#8288f1'. 'GMP' -> '#af93f8'. 'SDK' -> '#f8beff'. 'SKA' -> '#fce5cd'. 'PHY' -> '#fbbc04'. 'RES' -> '#efefef'. 'COR' -> '#4fc8e5'. 'EDI' -> '#56b4e9' }.\nmodelFolders := model allWithType: FamixCPreprocFolder.\ntagsColors keys do: [ :key | (model tagNamed: projName , '-' , key) color: (Color fromHexString: (tagsColors at: key))].\nfoldersTags keys do: [ :key | (modelFolders select: [:file | file name = key]) do: [ :file | file tagWith: (model tagNamed: projName , '-' ,(foldersTags at: key))] ]."
        output_file = open('outputs/' + config['project_name'] + '-tags.st', 'w')
        output_file.writelines(pharo_code)
        output_file.close()
    else:
        print("Missing or malformed config file, please check if there is a config.json in the inputs folder")

project_name = sys.argv[1]
config_path = 'inputs/config_' + project_name + '.json'
config = load_config(config_path)
convert_dot_to_xml(config)
generate_tags_from_csv(config)
print("Done!")