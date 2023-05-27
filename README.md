# Game Engine Analyser: An Exploratory Approach for Game Engine Architecture Recovery
By Gabriel C. Ullmann, Yann-Gaël Guéhéneuc, Fabio Petrillo, Cristiano Politowski, 2022-2023. A series of scripts to perform game engine architecture recovery.

## How to use it
- Each folder in the repository holds data or scripts to perform one of the steps described in the approach section of our paper "An Exploratory Approach for Game Engine Architecture Recovery".
- Until step 3, all work is manual. Therefore, there are no scripts to execute. If you want to reproduce this approach, place your own data in this folders.
- From step 4 and on, please read carefully the README.md file which is in each folder. It holds all instructions for performing each step.

## Setting up
This entire approach was written and run on Ubuntu 20.04.5 LTS. In order to run all scripts, you will need to install the following:
- Python 3.8
- All Python packages from requirements.txt (in this folder)
- Perl 5
- Graphviz
- Pharo Launcher (from pharo.org)

## Tests
Automated tests are in tests/run.sh.

## Naming standard
For inputs and outputs, project name should come first, then an hyphen, then one or more words to describe the file. Folders and scripts follow the snake case standard.

Example inputs:
- project-config.json
- project-includes.dot
- project-tags.csv

Example outputs:
- project-includes.dot
- project-report.csv
- project-includes-unr.csv
- project-includes.xml
- project-tags.st
