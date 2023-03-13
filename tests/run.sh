base=/home/ullmann/Documents/research/game-engine-analyser
cd $base/4_include_graph_gen
sh cpp-walker.sh $base/tests/testproject $base/tests/testproject testproject

# copy from 4 to 5
# copy from test to 4
cp ./outputs/testproject-includes.dot $base/5_moose_model_gen/inputs
cp $base/tests/testproject-config.json $base/5_moose_model_gen/inputs
cp $base/tests/testproject-tags.csv $base/5_moose_model_gen/inputs

cd $base/5_moose_model_gen
python3 main.py testproject