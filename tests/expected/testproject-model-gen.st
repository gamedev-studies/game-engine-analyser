| importer tagger |

"Create model using XML and metamodels".
importer := FamixCPreprocImporter new rootFolder: './home/ullmann/Documents/research/game-engine-analyser/tests/testproject' ; runOn: '/home/ullmann/Documents/research/game-engine-analyser/5_moose_model_gen/outputs/testproject-includes.xml' modelName: 'testproject-20230404'.

"instantiate a new tagger and settings"
tagger := GroupTagger new.

"set index of the Moose model you want to query"
tagger setModel: importer model.

"set tag colors and project name"
tagger setColorMap: (Dictionary newFrom: { 'STU' -> '#34b4eb' . 'BDS' -> '#eb3a34' . 'BET' -> '#34eb61'  }).
tagger setProjectName: 'testproject'.

"set autotagging to false"
tagger setAutotagFolderContents: false.

"search the model for each path_from_root, tag file/folder with respective subsystem"
tagger initialize: '/home/ullmann/Documents/research/game-engine-analyser/5_moose_model_gen/inputs/testproject-tags.csv' recursive: true.