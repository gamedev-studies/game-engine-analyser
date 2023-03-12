# Two-way-include counter
By Gabriel C. Ullmann, Yann-Gaël Guéhéneuc, Fabio Petrillo, Cristiano Politowski, 2022.

Results will be saved in this folder. For more information, please read the README.md file on the root folder of this repository. 

In the CSV file called "result_manual_path_resolution.csv" you can see the count of include paths that remained unresolved for each selected system after our manual count. These are mostly:
- System libraries (stdio.h, windows.h)
- Code generated on compilation only
- Third party libs that for some reason were not inside the repository

As explained in threats to validity, we are aware we might have missed some include paths in our manual check, but even if that is the case, the percentage of these occurences is low (less than 13%).