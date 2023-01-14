#$1 = engine root folder
#$2 = engine includes folder (same as root)
#$3 = engine name
#$4 = subsystem name
#$5 = list of subsystem folders separated by comma
ENGINE_INCLUDE_GRAPH=graphs/$3_subsystem.dot
EDGE_COUNT=graphs/$3_edge_count.csv
CACHE_USED=0

# check if the include graph and count has already been generated
# if so, don't repeat it, it takes too long
if test -f "$ENGINE_INCLUDE_GRAPH" && test -f "$EDGE_COUNT"; then
   CACHE_USED=1
   echo "INFO: include graphs found in cache"
else
   CACHE_USED=0
   echo "INFO: include graphs not found in cache, generating it..."
   perl src/cinclude2dot.pl --src=$1 --include=$2 --paths >> graphs/$3_subsystem.dot
   gvpr -f src/count_edges.gvpr graphs/$3_subsystem.dot >> graphs/$3_edge_count.csv
   python3 src/remove_linebreaks.py $3 $4
fi

echo "INFO: order edges and generate vector"
mkdir results/$3_$4
python3 src/order_edges.py $3 $4 $5

if [ "$CACHE_USED" -eq 1 ] 
then
   echo "INFO: done with cached include graphs"
else
   echo "INFO: done with newly generated include graphs"
fi

echo "INFO: computing metrics for all engines and subsystems"
python3 src/compute_metric.py
echo "INFO: done computing metrics"