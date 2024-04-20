# Game Engine Analyser: An Exploratory Approach for Game Engine Architecture Recovery
By Gabriel C. Ullmann, Yann-Gaël Guéhéneuc, Fabio Petrillo, Cristiano Politowski, Nicolas Anquetil, 2022-2023. 

Game engines are tools to facilitate video game development. They provide graphics, sound, and physics simulation features, which would have to be otherwise implemented by developers. Even though essential for modern commercial video game development, game engines are complex and developers often struggle to understand their architecture, leading to maintainability and evolution issues that negatively affect video game productions. To address these problems, we present the Subsystem-Dependency Recovery Approach (SyDRA), which helps game engine developers understand game engine architecture and therefore make informed game engine development choices. By applying this approach to 10 open-source game engines, we obtain architectural models that can be used to compare game engine architectures and identify and solve issues of excessive coupling and folder nesting.

In this repository, you will find a series of scripts to perform game engine architecture recovery following the Subsystem Dependency Recovery Approach (SyDRA).

## How To Use It
- Each numbered folder inside this repository holds data or scripts to perform one of the steps described in the approach section of our paper "An Exploratory Approach for Game Engine Architecture Recovery".
- In steps 1 to 3, all work is manual. Therefore, there are no scripts to execute. If you want to reproduce this approach, place your own data in these folders. You can use the files we provide in these folders as references to create your own.
- From step 4 and on, please read carefully the README.md file which is in each folder. It holds all the instructions for performing each step.

## Contents Summary
Inside this repository, you will find the following:
- 1_system_selection: selected game engines for analysis.
- 2_subsystem_selection: selected game engine subsystems for analysis.
- 3_subsystem_detection: results of the subsystem detection performed manually by us.
- 4_include_graph_gen: scripts for include graph generation and their outputs.
- 5_moose_model_gen: scripts for Moose model generation and their outputs.
- 6_architectural_map_gen: instructions on how to use Pharo and Moose to generate architectural maps and other visualisations.
- tests: automated tests for the game engine analyser.
- runs: bash scripts and examples which you can use to run the analyser in any C++ game engine (or other software).
- controlled_experiment: demographic data and results of our controlled experiment made to evaluate SyDRA.

## Setting Up
This entire approach was written and run on Ubuntu 20.04.5 LTS. To run all scripts, you will need to install the following:
- Python 3.8
- All Python packages from requirements.txt (in this folder)
- Perl 5
- Graphviz
- Pharo Launcher (from pharo.org)

## Naming Standards
For inputs and outputs, the project name should come first, then a hyphen, and then one or more words to describe the file (kebab-case). Folders and scripts follow the snake_case standard.

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

# Other Sources and Contact Info
- You can also find this project on Ptidej: https://www.ptidej.net/downloads/replications/icec24.
- In case you have questions or suggestions, please contact us by email: g_cavalh at live.concordia.ca or gabriel.cavalheiroullmann at concordia.ca. We will do our best to help.
