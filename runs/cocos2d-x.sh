echo "Run - cocos2d-x"
echo "===================="

# /media/ullmann/HDDGabriel/research/engines
base_tool=/home/ullmann/Documents/research/game-engine-analyser
base_project=/home/ullmann/Documents/research/game-engines

cd $base_tool/4_include_graph_gen
sh cpp-walker.sh $base_project/cocos2d-x $base_project/cocos2d-x cocos2d-x

# copy from 4 to 5
# copy from 3 to 4
cp ./outputs/cocos2d-x-includes.dot $base_tool/5_moose_model_gen/inputs
cp $base_tool/3_subsystem_detection/cocos2d-x.csv $base_tool/5_moose_model_gen/inputs/cocos2d-x-tags.csv

cd $base_tool/5_moose_model_gen
python3 main.py cocos2d-x
