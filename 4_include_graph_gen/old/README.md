# Two-way-include counter
By Gabriel C. Ullmann, Yann-Gaël Guéhéneuc, Fabio Petrillo, Cristiano Politowski, 2022. This script iterates over a tree of files, checking which files a given file includes, and which files include it.

## How to use it?
We used it for calculating the number of includes in game engine files and subsystems. A step-by-step is described below. You can also see example command calls in the "filepaths" folder. 

- Execute cpp-walker.sh passing the following parameters:
    1. Engine root folder (absolute path)
    2. Search for includes in these folders (can be the same as 1 if there are no external/third party folders to include in the search)
    3. Engine name
    4. Subsystem name
    5. List of subsystem folders separated by comma (path relative to the engine's root)
- The script will output result files (see next section)

# Results
Two folders hold result files: "graphs" and "results".

- Results will be saved to the "graphs" folder for each engine: 
    1. The graphviz include graph (.dot)
    2. Edge count (count of edges in and out for each file)
- Results will be saved to the "results" folder for each engine subsystem: 
    1. Edge count (count of edges in and out for each file, ordered by CBO metric)
    2. Vector map (file names mapped to sequential IDs such A1, B1, etc.). Not used in our paper, created for another experiment.
    3. Vector (file sequential IDs ordered by CBO metric). Not used in our paper, created for another experiment.
- For more information, please read README.md on step 5.