# Game Engine Analyser
By Gabriel C. Ullmann, Yann-Gaël Guéhéneuc, Fabio Petrillo, Cristiano Politowski, 2022.

## How to use it?
- Copy to the "inputs" the include graph (.dot) and tags file for your game engine project. If you performed steps 3 and 4 of the approach, you will have this date. If you did not perform these steps, please go back and complete them first for your game engine of choice.
- For the following steps, you will need the name of your project. Let's pretend its called "your_engine".
- On the "inputs" folder, add a file called "config_your_engine.json". You can copy the same contents from "config_example.json".
- Inside your config file, you will need to inform:
    - project_name: your project's name, all lowercase and without spaces.
    - project_full_path: the absolute path to your project as mentioned in the .dot files.
    - project_shortened_path: the part of your "project_full_path" that represents the root folder of the engine. From this folder below, there should be game engine files only.
    - includes_dot_file_path: your .dot file relative path.
    - tags_csv_file_path: your tags file relative path.
- Execute main.py passing the project name as a parameter (it must be written in the same way as your config file name).
- The script will output result files (see next section).

# Results
Result files are placed in the "outputs" folder. After script execution, you should see there:
- A .xml file: it contains all includes, which can be used in the next step, the Moose importer.
- A .st file: it contains Pharo code to tag entities in the model you will create in the next step.
- For more information, please read README.md on step 6.
