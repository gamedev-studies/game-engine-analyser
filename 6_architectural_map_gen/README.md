# Generating a Moose model for game engines
By Gabriel C. Ullmann, Yann-Gaël Guéhéneuc, Fabio Petrillo, Cristiano Politowski, 2022-2023.

## Initial setup
- Download Pharo Laucher: https://pharo.org/download.
- Open Pharo Laucher, click "new" and create a new Moose 10 image.
- Launch your Moose 10 image.

**ATTENTION**: the instructions below show how one can manually upload the outputs from step 5 into a Pharo image and visualise it with Moose. Fortunately, over the last few months we have developed an easier way to do that: [Bolée] (https://github.com/gamedev-studies/bolee). Bolée is a package which can be installed in Pharo and provides you a UI for uploading the outputs from step 5 and do model generation and visualisation. 

While Bolée automates most of the operations described below, we will keep the text here because it provides insights on how things used to work before we came up with a UI to accelerate the process. However, we STRONGLY recommend you to install Bolée , read its documentation and use it for executing the entire step 6, since it decreases the possibility of human error when inputing the data (and it looks much cooler!).

## How to use it
- On the top menu, go to Browse > Iceberg, click Add > Clone from Github.com and input the necessary information for the Famix-Cpp repo: https://github.com/moosetechnology/Famix-Cpp.
- After adding it, right click it on the Iceberg list, select Metacello > Install Baseline (Default) for Famix-Cpp. This will install the necessary dependencies.
- Wait for the dependencies to be installed. This may take several minutes. 
- Currently the dependencies for the game engine analyser are not all togheter in 1 package. Therefore, we need to install some dependencies separately. Open Playground by pressing CTRL + O + W or go to Browse > Playground. Copy the following code, paste it in Playground and execute it by clicking "do it" or selecting all and pressing CTRL + D:
```
Metacello new
    baseline: 'GroupTagger';
    repository: 'github://gamedev-studies/group-tagger:main';
    onConflict: [ :ex | ex useIncoming ];
    onUpgrade: [ :ex | ex useIncoming ];
	onDowngrade: [ :ex | ex useLoaded ];
    load.

Metacello new
    baseline: 'Roassal3Exporters';
    repository: 'github://ObjectProfile/Roassal3Exporters';
    load.
```
- Wait for the dependencies to be installed. This may take several minutes. These packages are necessary for us to be able to tag and later export the architectural map to PDF or other format after we generate it.
- Clean the Playground window or open a new one. Now you will execute the code generated in step 5. Copy and paste it into the Playground window.
- Execute the code by clicking "do it" or selecting all and pressing CTRL +D.
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
- Some other non-Moose visualisations we have been experimenting with, such as Chord and Sankey diagrams