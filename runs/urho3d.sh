echo "Run - urho3d"
echo "===================="

base_tool=/home/ullmann/Documents/research/game-engine-analyser
base_project=/media/ullmann/HDDGabriel/research/engines

cd $base_tool/4_include_graph_gen
sh cpp-walker.sh $base_project/urho3d $base_project/urho3d urho3d

# copy from 4 to 5
# copy from 3 to 4
cp ./outputs/urho3d-includes.dot $base_tool/5_moose_model_gen/inputs
cp $base_tool/3_subsystem_detection/urho3d.csv $base_tool/5_moose_model_gen/inputs/urho3d-tags.csv

cd $base_tool/5_moose_model_gen
python3 main.py urho3d
