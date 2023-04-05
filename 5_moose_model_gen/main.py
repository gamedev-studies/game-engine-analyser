import json
import sys
import os
from datetime import datetime
import pandas as pd
  
# utils
def get_current_datestamp():
    return datetime.today().strftime('%Y%m%d')

def load_config(path, project_name="projectname"):
    try:
        f = open(path)
        return json.load(f)
    except:
        print("Missing or malformed config file, please check if there is a " + project_name + "-config.json in the inputs folder")

def extract_name_parent(path):
    # deprecated
    if path and len(path) > 1 and path[0] == "/":
        return path[1:len(path)]
    return path

# main functions
def convert_dot_to_xml(date, config=None, project_name="projectname"):
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
                replaced_line = line.replace('\"', '').replace('\t', '').replace('\\n', '').split(" -> ")
                included_by.append(replaced_line[0].strip())
                include.append(replaced_line[1].strip())

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

        output_file = open('outputs/' + config['project_name'] + '-' + date + '.xml', 'w')
        lines = output_file.writelines(xml_result)
        abs_path = os.path.realpath(output_file.name)
        output_file.close()
        return abs_path
    else:
        print("Missing or malformed config file, please check if there is a " + project_name + "-config.json in the inputs folder")

def generate_tags_from_csv(abs_path, date, config=None, project_name="projectname"):
    if not config == None:
        pharo_code = ""
        abs_path = abs_path.split("outputs")[0]
        templ_lines = open('script_template.txt')
        for line in templ_lines:
            pharo_code += line

        pharo_code = pharo_code.replace('$tagsCSVFilePath$', abs_path + config['tags_csv_file_path'])
        pharo_code = pharo_code.replace('$setProjectName$', config['project_name'])
        pharo_code = pharo_code.replace('$includeXMLPath$', abs_path + 'outputs/' + config['project_name'] + '-' + date + '.xml')
        pharo_code = pharo_code.replace('$projectFullPath$', config['project_full_path'])
        pharo_code = pharo_code.replace('$colorMap$', config['color_map'])

        output_file = open('outputs/' + config['project_name'] + '-model-gen.st', 'w')
        output_file.writelines(pharo_code)
        output_file.close()
    else:
        print("Missing or malformed config file, please check if there is a " + project_name + "-config.json in the inputs folder")

date_obj = get_current_datestamp()
project_name = sys.argv[1]
config_path = 'inputs/' + project_name + '-config.json'
config = load_config(config_path, project_name)
generated_xml = convert_dot_to_xml(date_obj, config, project_name)
generate_tags_from_csv(generated_xml, date_obj, config, project_name)
print("Done!")