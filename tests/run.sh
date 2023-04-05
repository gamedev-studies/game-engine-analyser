echo "Run game engine analyser tests"
echo "===================="
echo "1/2 - Run tool and get outputs"
echo "===================="

current_date=$(date '+%Y%m%d')
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

echo "===================="
echo "2/2 - Compare generated and expected outputs"
echo "===================="

# account for date change on generated .st
sed "s/#current_date#/$current_date/g" $base/tests/expected/testproject-model-gen.st > $base/tests/expected/testproject-model-gen-today.st

# file descriptions
description=("List of unresolved includes" "Model generation code")

# generated files
generated=("$base/4_include_graph_gen/outputs/testproject-includes-unr.csv" "$base/5_moose_model_gen/outputs/testproject-model-gen.st")

# expected files
expected=("$base/tests/expected/testproject-includes-unr.csv"  "$base/tests/expected/testproject-model-gen-today.st")

# Iterate through the arrays
for i in "${!generated[@]}"; do
  # Compute the MD5 hashes
  hash1=$(md5sum "${generated[i]}" | cut -d ' ' -f 1)
  hash2=$(md5sum "${expected[i]}" | cut -d ' ' -f 1)

  # Compare the hashes
  if [ "$hash1" == "$hash2" ]; then
    echo "PASSED: ${description[i]}"
  else
    echo "FAILED: ${description[i]}"
  fi
done

# check include resolution report
if diff $base/4_include_graph_gen/outputs/testproject-report.csv $base/tests/expected/testproject-report.csv -I '^analysis\|^report' >/dev/null ; then
    echo "PASSED: include resolution report"
else
    echo "FAILED: include resolution report"
fi

# file descriptions
description=("Include count (.dot)" "Include count (.xml)")

# generated files
generated=("$base/4_include_graph_gen/outputs/testproject-includes.dot" "$base/5_moose_model_gen/outputs/testproject-$current_date.xml")

# expected files
expected=("$base/tests/expected/testproject-includes.dot" "$base/tests/expected/testproject-includes.xml")

# Iterate through the arrays
for i in "${!generated[@]}"; do
  # Count the number of lines
  lines1=$(wc -l "${generated[i]}" | cut -d ' ' -f 1)
  lines2=$(wc -l "${expected[i]}" | cut -d ' ' -f 1)

  # Compare the number of lines
  if [ "$lines1" -eq "$lines2" ]; then
    echo "PASSED: ${description[i]}"
  else
    echo "FAILED: ${description[i]}"
  fi
done