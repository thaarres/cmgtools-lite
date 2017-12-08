#!/bin/bash

echo "run some plots to make post/prefit figure"
#w="workspace_pythia_nominal_dataherwig.root"
#l="dataherwig"
#o="/home/dschaefer/DiBoson3D/GoodnessOfFitTests/dataherwig/"

w="/home/dschaefer/DiBoson3D/test_kernelSmoothing_pythia/workspace_pythia_nominal.root"
l="datapythia"
o="/home/dschaefer/DiBoson3D/GoodnessOfFitTests/datapythia/"

#w="workspace_datamadgraph.root"
#l="datamadgraph"
#o="/home/dschaefer/DiBoson3D/GoodnessOfFitTests/datamadgraph/"
echo "use workspace ${w}"

# python runFitPlots.py -p z -f -n ${w} -l ${l} -o ${o} --log ${l}.log
 python runFitPlots.py -p y -f -n ${w} -l ${l} -o ${o}
#  python runFitPlots.py -p x -f -n ${w} -l ${l} -o ${o}
#  python runFitPlots.py -p z -f -n ${w} -l ${l} -x 150,215 -y 150,215 -o ${o}
#  python runFitPlots.py -p z -f -n ${w} -l ${l} -x 150,215 -y 55,150 -o ${o}
#  
#      python runFitPlots.py -p x -f -n ${w} -l ${l} -z 1000,1300 -o ${o}
#      python runFitPlots.py -p x -f -n ${w} -l ${l} -z 1300,2000 -o ${o}
#      python runFitPlots.py -p x -f -n ${w} -l ${l} -z 2000,5000 -o ${o}
#      
#      python runFitPlots.py -p y -f -n ${w} -l ${l} -z 1000,1300 -o ${o}
#      python runFitPlots.py -p y -f -n ${w} -l ${l} -z 1300,2000 -o ${o}
#      python runFitPlots.py -p y -f -n ${w} -l ${l} -z 2000,5000 -o ${o}
# 
# python runFitPlots.py -p x -f -n ${w} -l ${l} -y 150,215 -o ${o}
# python runFitPlots.py -p x -f -n ${w} -l ${l} -y 55,150 -o ${o}
# 
# python runFitPlots.py -p y -f -n ${w} -l ${l} -x 150,215 -o ${o}
# python runFitPlots.py -p y -f -n ${w} -l ${l} -x 55,150 -o ${o}
# 
echo "############ end of script #################"
