#$1 = engine root folder
#$2 = engine includes folder (same as root)
#$3 = engine name

now=$(date)
echo "BEGIN"
echo $now

rm outputs/$3_includes.dot
perl cinclude2dot.pl --src=$1 --include=$2 --paths >> outputs/$3_includes.dot
first_pass=$(wc -l outputs/$3_includes.dot)
python3 resolve_includes.py $1 $3 $first_pass

now=$(date)
echo "END"
echo $now