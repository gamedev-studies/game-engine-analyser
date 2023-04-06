echo "Run - any"
echo "===================="

# project name, project path, tool path

cd $3/4_include_graph_gen
sh cpp-walker.sh $2/$1 $2/$1 $1

# copy from 4 to 5
# copy from 3 to 4
cp ./outputs/$1-includes.dot $3/5_moose_model_gen/inputs
cp $3/3_subsystem_detection/$1.csv $3/5_moose_model_gen/inputs/$1-tags.csv

cd $3/5_moose_model_gen
python3 main.py $1
