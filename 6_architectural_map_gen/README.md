# Generating a Moose model for game engines
By Gabriel C. Ullmann, Yann-Gaël Guéhéneuc, Fabio Petrillo, Cristiano Politowski, 2022. This script 

## How to do it
- Download Pharo Laucher: https://pharo.org/download.
- Open Pharo Laucher, click "new" and create a new Moose 10 image.
- Launch your Moose 10 image.
- On the top menu, go to Browse > Iceberg, click Add > Clone from Github.com and input the necessary information for the Famix-Cpp repo: https://github.com/moosetechnology/Famix-Cpp.
- After adding it, right click it on the Iceberg list, select Metacello > Install Baseline for Famix-Cpp. This will install all repository dependencies.
- Wait for the dependencies to be installed. This may take several minutes.
- Open Playground by pressing CTRL + O + W or go to Browse > Playground.
- Copy the following code, paste it in Playground and execute it by clicking "do it" or selecting all and pressing CTRL +D:
```
Metacello new
    baseline: 'Roassal3Exporters';
    repository: 'github://ObjectProfile/Roassal3Exporters';
    load.
```
- Wait for the dependencies to be installed. This may take several minutes. This package is necessary for us to be able to export the architectural map to PDF or other format after we generate it.
- Clean the Playground window or open a new one. Now you will execute the importer with 3 parameters: rootFolder, runOn and modelName
```
FamixCPreprocImporter new 
    rootFolder: '/path/to/your/engine'; 
    runOn: '/path/to/your/engine.xml';
    modelName: 'yourengine-20230101'.
```
- In the command above you can see some example values for the parameters. Naturally, you will have to replace them by your own. The parameters are described as follows:
    - rootFolder: your game engine's full path, the same you have in your .dot file and .xml file
    - runOn: your game engine include .xml file
    - modelName: a name for your model, to be displayed inside Moose
- After you got your parameters right, execute the code by clicking "do it" or selecting all and pressing CTRL +D.
- If you encountered no errors, clean the Playground window or open a new one. You will now execute code to create tags. Copy and paste the code you have in outputs/yourengine-tags.st to the Playground.
- On the third line, replace "x" by the position of your model on the MooseModel collection. You can find it out by clicking the "models" button on the top right side of the Playground window
- After the replacement is done, execute the code by clicking "do it" or selecting all and pressing CTRL +D.
- On the top menu, go to Moose > Tag Browser. You should see all subsystems from step 3 and their respective files as tags on the list.
- Close the Tag Browser.
- Also on the top menu, go to Moose > Models browser.
- Right click on your game engine model and then in "inspect". A new window will open.
- In the bottom of this window, click "script". A text box will appear. Copy and paste the following code:
```
MiInspectorBrowser inspect: (((self allWithType: FamixCPreprocFolder) select: [ :f | f name ~= '.']) select: [ :f | f parentFolder name = '.']) asMooseGroup.
```
- Execute by selecting all and pressing CTRL + D.
- A new window will open. In this window, click on "Propagate" on the top right corner.
- Back to the top menu, go again to Moose > Tag Browser.
- Back to the top menu, go to Moose > Architectural Map. This is a slow operation so the window may take several minutes to open.
- After the window opens, on the top right corner, click on Settings > Tags to Add > Plus and then select all your tags.
- Back to Settings > Links to Show, select FamixCPreprocInclude.
- Click OK. This is a slow operation so the window may take several minutes to update.
- If no error happened, you will get an architectural map. You can move the nodes around and inspect them if you want. You can also inspect associations.
- To save the map as an image, press CTRL + ALT + SHIFT and click on the window by pressing the mouse wheel down. A context menu will open.
- Click on "explore". A window will open.
- In the bottom of this window, click "script". A text box will appear. Copy and paste the following code:
```
self roassalCanvas pdfExporter noFixedShapes; export.
```
- Execute by selecting all and pressing CTRL + D.
- The architectural map PDF will be saved to your Pharo image's root folder. In Linux, the path to the image should be something like: /home/your_username/Pharo/images/your_image.
- P.S: other formats are available for exporting, such as PNG and SVG. You can see more info at https://github.com/ObjectProfile/Roassal3Exporters.

# Extra
You will also find in this folder:
- The Python code to generate a include heatmap (gen_heatmap.py).
- JavaScript code you can use to count edges from an SVG architectural map (count_edges.js).