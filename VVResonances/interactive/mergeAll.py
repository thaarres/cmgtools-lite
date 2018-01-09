from modules.submitJobs import merge2DTemplate,merge1DMVVTemplate

# Description: If program fails mid job, before merging. Merge manually here!

purities=['HPHP','HPLP']

nonResTemplate="QCD_Pt_" #high stat
# nonResTemplate="QCD_Pt-" #low stat --> use this for tests
#nonResTemplate="Dijet" #to compare shapes

minMJ=55.0
maxMJ=215.0

minMVV=1000.0
maxMVV=5000.0

minMX=1200.0
maxMX=7000.0

binsMJ=80
binsMVV=100

jobList= ['QCD_Pt_2400to3200_1', 'QCD_Pt_470to600_1', 'QCD_Pt_470to600_2', 'QCD_Pt_470to600_3', 'QCD_Pt_470to600_4', 'QCD_Pt_470to600_5', 'QCD_Pt_470to600_6', 'QCD_Pt_470to600_7', 'QCD_Pt_470to600_8', 'QCD_Pt_470to600_9', 'QCD_Pt_470to600_10', 'QCD_Pt_470to600_11', 'QCD_Pt_470to600_12', 'QCD_Pt_470to600_13', 'QCD_Pt_470to600_14', 'QCD_Pt_470to600_15', 'QCD_Pt_470to600_16', 'QCD_Pt_470to600_17', 'QCD_Pt_470to600_18', 'QCD_Pt_470to600_19', 'QCD_Pt_470to600_20', 'QCD_Pt_470to600_21', 'QCD_Pt_170to300_1', 'QCD_Pt_1400to1800_1', 'QCD_Pt_1400to1800_2', 'QCD_Pt_1400to1800_3', 'QCD_Pt_1400to1800_4', 'QCD_Pt_1800to2400_1', 'QCD_Pt_1800to2400_2', 'QCD_Pt_1800to2400_3', 'QCD_Pt_300to470_1', 'QCD_Pt_300to470_2', 'QCD_Pt_300to470_3', 'QCD_Pt_300to470_4', 'QCD_Pt_300to470_5', 'QCD_Pt_300to470_6', 'QCD_Pt_300to470_7', 'QCD_Pt_300to470_8', 'QCD_Pt_300to470_9', 'QCD_Pt_300to470_10', 'QCD_Pt_300to470_11', 'QCD_Pt_300to470_12', 'QCD_Pt_300to470_13', 'QCD_Pt_300to470_14', 'QCD_Pt_3200toInf_1', 'QCD_Pt_1000to1400_1', 'QCD_Pt_1000to1400_2', 'QCD_Pt_1000to1400_3', 'QCD_Pt_1000to1400_4', 'QCD_Pt_1000to1400_5', 'QCD_Pt_1000to1400_6', 'QCD_Pt_1000to1400_7', 'QCD_Pt_1000to1400_8', 'QCD_Pt_1000to1400_9', 'QCD_Pt_1000to1400_10', 'QCD_Pt_1000to1400_11', 'QCD_Pt_1000to1400_12', 'QCD_Pt_1000to1400_13', 'QCD_Pt_600to800_1', 'QCD_Pt_600to800_2', 'QCD_Pt_600to800_3', 'QCD_Pt_600to800_4', 'QCD_Pt_600to800_5', 'QCD_Pt_600to800_6', 'QCD_Pt_600to800_7', 'QCD_Pt_600to800_8', 'QCD_Pt_600to800_9', 'QCD_Pt_600to800_10', 'QCD_Pt_600to800_11', 'QCD_Pt_600to800_12', 'QCD_Pt_600to800_13', 'QCD_Pt_600to800_14', 'QCD_Pt_600to800_15', 'QCD_Pt_600to800_16', 'QCD_Pt_600to800_17', 'QCD_Pt_600to800_18', 'QCD_Pt_600to800_19', 'QCD_Pt_600to800_20', 'QCD_Pt_600to800_21', 'QCD_Pt_600to800_22', 'QCD_Pt_600to800_23', 'QCD_Pt_600to800_24', 'QCD_Pt_600to800_25', 'QCD_Pt_600to800_26', 'QCD_Pt_600to800_27', 'QCD_Pt_600to800_28', 'QCD_Pt_600to800_29', 'QCD_Pt_600to800_30', 'QCD_Pt_600to800_31', 'QCD_Pt_600to800_32', 'QCD_Pt_600to800_33', 'QCD_Pt_600to800_34', 'QCD_Pt_600to800_35', 'QCD_Pt_600to800_36', 'QCD_Pt_600to800_37', 'QCD_Pt_600to800_38', 'QCD_Pt_600to800_39', 'QCD_Pt_800to1000_1', 'QCD_Pt_800to1000_2', 'QCD_Pt_800to1000_3', 'QCD_Pt_800to1000_4', 'QCD_Pt_800to1000_5', 'QCD_Pt_800to1000_6', 'QCD_Pt_800to1000_7', 'QCD_Pt_800to1000_8', 'QCD_Pt_800to1000_9', 'QCD_Pt_800to1000_10', 'QCD_Pt_800to1000_11', 'QCD_Pt_800to1000_12', 'QCD_Pt_800to1000_13', 'QCD_Pt_800to1000_14', 'QCD_Pt_800to1000_15', 'QCD_Pt_800to1000_16', 'QCD_Pt_800to1000_17', 'QCD_Pt_800to1000_18', 'QCD_Pt_800to1000_19', 'QCD_Pt_800to1000_20', 'QCD_Pt_800to1000_21', 'QCD_Pt_800to1000_22', 'QCD_Pt_800to1000_23', 'QCD_Pt_800to1000_24', 'QCD_Pt_800to1000_25']
files= ['QCD_Pt_1000to1400.root', 'QCD_Pt_1400to1800.root', 'QCD_Pt_170to300.root', 'QCD_Pt_1800to2400.root', 'QCD_Pt_2400to3200.root', 'QCD_Pt_300to470.root', 'QCD_Pt_3200toInf.root', 'QCD_Pt_470to600.root', 'QCD_Pt_600to800.root', 'QCD_Pt_800to1000.root']


for p in purities:
	merge1DMVVTemplate(jobList,files,"1D_"  +p,p,binsMVV,binsMJ,minMVV,maxMVV,minMJ,maxMJ)
	merge2DTemplate   (jobList,files,"2Dl1_" +p, p,"l1",binsMVV,binsMJ,minMVV,maxMVV,minMJ,maxMJ)
	merge2DTemplate   (jobList,files,"2Dl2_" +p, p,"l2",binsMVV,binsMJ,minMVV,maxMVV,minMJ,maxMJ)
 