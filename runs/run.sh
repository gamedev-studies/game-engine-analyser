echo "Run - any"
echo "===================="

# /media/ullmann/HDDGabriel/research/engines
base_tool=/home/ullmann/Documents/research/game-engine-analyser
base_project=/home/ullmann/Documents/research/game-engines

cd $base_tool/4_include_graph_gen
sh cpp-walker.sh $base_project/$1 $base_project/$1 $1

# copy from 4 to 5
# copy from 3 to 4
cp ./outputs/$1-includes.dot $base_tool/5_moose_model_gen/inputs
cp $base_tool/3_subsystem_detection/$1.csv $base_tool/5_moose_model_gen/inputs/$1-tags.csv

cd $base_tool/5_moose_model_gen
python3 main.py $1
