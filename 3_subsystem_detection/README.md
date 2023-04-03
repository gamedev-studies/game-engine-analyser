# Subsystem Detection
By Gabriel C. Ullmann, Yann-Gaël Guéhéneuc, Fabio Petrillo, Cristiano Politowski, 2023.

This is a manual step. For each project (e.g. game engine) you want to analyse, you have to build a CSV with the following columns:
- subsystem: subystem acronym (e.g. PLA)
- entity_description: (optional) a brief explanation about the entity's functionality
- path_from_root: path to entity from project root
- related_information: links to documentation or related resources that allow us to better understand the entity

If you are trying to reproduce the work we did in previous papers (e.g. An Exploratory Approach for Game Engine Architecture Recovery, 2023) you will have to clone the game engine repositories and revert the state of the repository to the commit mentioned in the paper. For example, for commit hash feb0d90190:

    git reset --hard feb0d90190