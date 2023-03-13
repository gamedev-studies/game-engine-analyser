# Game Engine Analyser
By Gabriel C. Ullmann, Yann-Gaël Guéhéneuc, Fabio Petrillo, Cristiano Politowski, 2023.

sh cpp-walker.sh /media/ullmann/HDDGabriel/research/engines/godot /media/ullmann/HDDGabriel/research/engines/godot godot

## How to use it?
Call the script cpp-walker.sh passing the following parameters:
1. Project root folder: absolute path to your project.
2. Project includes folder: other folders where you would like to search for includes. This parameter may be useful if you have your project spread on different repos on different folders. You can have as many paths as you need separated by comma. If your entire project is in the same folder and you have no need to lookup in other folders, please simply pass the absolute path to your project.
3. Project name.

## Results
After execution, the following files will be created in the "outputs" folders:
- Include graph (.dot)
- Unresolved include list (.csv)
- Resolved/unresolved include report (.csv)

## Next steps
- You will use the include graph as input on step 5
- Before proceeding, please check the resolved/unresolved include report. It can help you understand how well the tool resolved your includes. 
- A high percentage of unresolved includes may be a sign that you forgot to tell the tool to look for files in an external include path. In this case, try to determine the paths and pass them as the second parameter of cpp-walker.sh. 