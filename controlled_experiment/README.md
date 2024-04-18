# A User Study to Evaluate Game Engine Architecture Visualisation
By Gabriel C. Ullmann, Yann-Gaël Guéhéneuc, Fabio Petrillo, Cristiano Politowski and Nicolas Anquetil, 2023. 

This package contains information that can be used to replicate the user study described in our paper "A User Study to Evaluate Game Engine Architecture Visualisation". Participants demographics, task statements, collected data and statistical methods used are shown here in detail. 

## Summary
1. Participant Demographics
2. Parts of the Questionnaire 
    - A. Task Statements
    - B. Debriefing Questionnaire
    - C. Changes to Original Task Statements
3. Dependent Variables, Description and Analysis
    - A. Description
    - B. Two-sample T-test Inputs
    - C. Two-sample T-test Results
    - D. Normality Test Results
    - E. Statistical Significance Test Results
    - F. Descriptive Statistics of the Measurements
    - G. Measured effect size
4. Collected Data for Dependent Variables
    - A. Consent (Both Groups)
    - B. Blue Group Results (Control Group)
    - C. Green Group Results (Treatment Group)
    - D. Debriefing Results (Both Groups)
    - E. Measurements of the Dependent Variables
5. Data for Godot model generation
6. Screenshots from our Study Setup on Moose

## How to use?
All files in this package are either CSV, TSV or MD and can be visualised either on a code editor (e.g. VS Code) or spreadsheet editor (e.g. MS Excel, Google Sheets). We recommend you to read the paper first and then refer to the files as needed, so you have the general context and also the specific data related to it. The boxplots which are shown on the paper are not included here for brevity but can be re-generated based on the data in folder number 4. 

## FAQ
Here are answers to some questions you might have with regard to reproducing this user study.

### How do I generate a Godot model on Moose?
Please use our tool, called Bolée, which runs on Moose 10 (https://github.com/gamedev-studies/bolee). By inputting the CSV and XML we provide, along with the absolute path to Godot's repository (on your local environment), you should be able to generate a FamixCPP model (https://github.com/moosetechnology/Famix-Cpp) which is usable in Moose and which can be used to replicate this user study. 

### What tools you used on Moose exactly?
You can see how we setup our Moose image in the screenshots provided on folder 6. We used the Tag browser, Architectural Map and Source Code Browser. P.S: Unfortunately you will not be able to reproduce our study exactly as it was because currently propagating to the Source Code Browser is not possible. We did in our study by placing workarounds in the code that work for our image only. We are working to turn these workarounds into features which are integrated into Moose and that can be used for everyone in any Moose image. In the meantime, you can ask participants to look at the model in Moose, and inspect the code on VS Code. Thank you for your understanding.

### Which Moose version did you use?
Moose 10. It is also doable in Moose 11, but some of our tools, such as Bolée, are not yet fully compatible with version 11. 

### How do I install Moose?
Install Pharo Launcher first (https://pharo.org/). From there you can click "New" to create a new image, then choose Moose 10 (development).

### What if I wanna generate my own model from my own software repository?
In this case, please use our Game Engine Analyser (https://github.com/gamedev-studies/game-engine-analyser). Despite the name, it can be used to create the CSV and XML files necessary to generate Moose models with Bolée for any C++ repository. Current limitation: our analyser supports C++ only. If you want to analyse non-C software you will have to write your own parser and perhaps a Moose metamodel as well.

## Contact
In case you have questions or suggestions, please contact us by email: g_cavalh@live.concordia.ca or gabriel.cavalheiroullmann@concordia.ca. We will do our best to help.
