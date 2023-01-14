# remove weird line breaks from .dot file
# this allows to look for filenames more easily
# remove first
import os
import sys

engine = sys.argv[1]
path = os.getcwd() + "/graphs/" + engine + "_"

# clean graph file
dot_file = open(path + "subsystem.dot", "r")
new_file = ""
for line in dot_file:
    new_file += line.replace("\\n", "")
dot_file.close()

dot_file = open(path + "subsystem.dot", "w")
dot_file.write(new_file)
dot_file.close()

# clean count file
dot_file = open(path + "edge_count.csv", "r")
new_file = ""
for line in dot_file:
    new_file += line.replace("\\n", "")
dot_file.close()

dot_file = open(path +  "edge_count.csv", "w")
dot_file.write(new_file)
dot_file.close()
