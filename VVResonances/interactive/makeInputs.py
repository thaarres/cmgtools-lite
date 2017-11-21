import ROOT
import os,sys

cat={}
cat['HP1'] = 'jj_l1_tau2/jj_l1_tau1<0.35'
cat['HP2'] = 'jj_l2_tau2/jj_l2_tau1<0.35'
cat['LP1'] = 'jj_l1_tau2/jj_l1_tau1>0.35&&jj_l1_tau2/jj_l1_tau1<0.75'
cat['LP2'] = 'jj_l2_tau2/jj_l2_tau1>0.35&&jj_l2_tau2/jj_l2_tau1<0.75'
cat['NP1'] = 'jj_l1_tau2/jj_l1_tau1>0.75'
cat['NP2'] = 'jj_l2_tau2/jj_l2_tau1>0.75'

cuts={}

cuts['common'] = '((HLT_JJ)*(run>500) + (run<500))*(njj>0&&Flag_goodVertices&&Flag_CSCTightHaloFilter&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_eeBadScFilter&&jj_LV_mass>700&&abs(jj_l1_eta-jj_l2_eta)<1.3&&jj_l1_softDrop_mass>0.&&jj_l2_softDrop_mass>0.)'

cuts['HPHP'] = '('+cat['HP1']+'&&'+cat['HP2']+')'
cuts['LPLP'] = '('+cat['LP1']+'&&'+cat['LP2']+')'
cuts['HPLP'] = '(('+cat['HP1']+'&&'+cat['LP2']+')||('+cat['LP1']+'&&'+cat['HP2']+'))'
cuts['NP'] = '(('+cat['LP1']+'&&'+cat['NP2']+')||('+cat['NP1']+'&&'+cat['LP2']+'))'

cuts['nonres'] = '1'

purities=['HPHP','HPLP','LPLP','NP']
purities=['HPHP']

BulkGravWWTemplate="BulkGravToWW_narrow"
BulkGravZZTemplate="BulkGravToZZToZhadZhad_narrow"
BRWW=1.
BRZZ=1.

dataTemplate="JetHT"
#nonResTemplate="QCD_Pt_" #high stat
nonResTemplate="QCD_Pt-" #low stat --> use this for tests

minMJ=55.0
maxMJ=215.0

minMVV=1000.0
maxMVV=5000.0

binsMJ=80
binsMVV=100

cuts['acceptance']= "(jj_LV_mass>{minMVV}&&jj_LV_mass<{maxMVV}&&jj_l1_softDrop_mass>{minMJ}&&jj_l1_softDrop_mass<{maxMJ}&&jj_l2_softDrop_mass>{minMJ}&&jj_l2_softDrop_mass<{maxMJ})".format(minMVV=minMVV,maxMVV=maxMVV,minMJ=minMJ,maxMJ=maxMJ)
cuts['acceptanceGEN']='(jj_l1_gen_softDrop_mass>0&&jj_l2_gen_softDrop_mass>0&&jj_gen_partialMass>0)'

cuts['acceptanceMJ']= "(jj_l1_softDrop_mass>{minMJ}&&jj_l1_softDrop_mass<{maxMJ}&&jj_l2_softDrop_mass>{minMJ}&&jj_l2_softDrop_mass<{maxMJ})".format(minMJ=minMJ,maxMJ=maxMJ) 
cuts['acceptanceGENMJ']= '(jj_l1_gen_softDrop_mass>0&&jj_l2_gen_softDrop_mass>0&&jj_gen_partialMass>0)'

cuts['acceptanceMVV'] = "(jj_LV_mass>{minMVV}&&jj_LV_mass<{maxMVV})".format(minMVV=minMVV,maxMVV=maxMVV)

def makeSignalShapesMVV(filename,template):

 cut='*'.join([cuts['common'],cuts['acceptanceMJ']])
 rootFile=filename+"_MVV.root"
 cmd='vvMakeSignalMVVShapes.py -s "{template}" -c "{cut}"  -o "{rootFile}" -V "jj_LV_mass"  samples'.format(template=template,cut=cut,rootFile=rootFile,minMJ=minMJ,maxMJ=maxMJ)
 os.system(cmd)
 jsonFile=filename+"_MVV.json"
 print 'Making JSON'
 cmd='vvMakeJSON.py  -o "{jsonFile}" -g "MEAN:pol1,SIGMA:pol2,ALPHA:pol3,N:pol0,SCALESIGMA:pol3,f:pol3" -m 1000 -M 5000  {rootFile}  '.format(jsonFile=jsonFile,rootFile=rootFile)
 os.system(cmd)

def makeSignalShapesMJ(filename,template,leg):
 for p in purities:
  cut='*'.join([cuts['common'],cuts[p]])
  rootFile=filename+"_MJ"+leg+"_"+p+".root"
  doExp=1
  if p=='HPHP':
      doExp=0
  cmd='vvMakeSignalMJShapes.py -s "{template}" -c "{cut}"  -o "{rootFile}" -V "jj_{leg}_softDrop_mass" -m {minMJ} -M {maxMJ} -e {doExp} -f "alpha:1.347" samples'.format(template=template,cut=cut,rootFile=rootFile,leg=leg,minMJ=minMJ,maxMJ=maxMJ,doExp=doExp)
  os.system(cmd)
  jsonFile=filename+"_MJ"+leg+"_"+p+".json"

  if p=='HPHP':
      cmd='vvMakeJSON.py  -o "{jsonFile}" -g "mean:pol4,sigma:pol4,alpha:pol3,n:pol0,alpha2:pol3,n2:pol0,slope:pol0,f:pol0" -m 1000 -M 5000  {rootFile}  '.format(jsonFile=jsonFile,rootFile=rootFile)
  else:
      cmd='vvMakeJSON.py  -o "{jsonFile}" -g "mean:pol3,sigma:pol1,alpha:pol0,n:pol0,slope:pol1,f:laur4,alpha2:pol0,n2:pol0" -m 1000 -M 5000  {rootFile}  '.format(jsonFile=jsonFile,rootFile=rootFile)

  os.system(cmd)

def makeSignalYields(filename,template,branchingFraction,sfP = {'HPHP':1.0,'HPLP':1.0,'LPLP':1.0}):
 	 
 for p in purities:
  cut = "*".join([cuts[p],cuts['common'],cuts['acceptance'],str(sfP[p])])
  #Signal yields
  yieldFile=filename+"_"+p+"_yield"
  cmd='vvMakeSignalYields.py -s {template} -c "{cut}" -o {output} -V "jj_LV_mass" -m {minMVV} -M {maxMVV} -f "pol5" -b {BR} -x 950 samples'.format(template=template, cut=cut, output=yieldFile,minMVV=minMVV,maxMVV=maxMVV,BR=branchingFraction)
  os.system(cmd)

def makeDetectorResponse(name,filename,template,addCut="1"):
 #first parameterize detector response
 for p in purities:
  print "=========== PURITY: ", p
  cut='*'.join([cuts['common'],cuts[p],'(jj_l1_gen_softDrop_mass>10&&jj_l2_gen_softDrop_mass>10&&jj_gen_partialMass>0)',addCut])
  resFile=filename+"_"+name+"_detectorResponse_"+p+".root"		 
  cmd='vvMake2DDetectorParam.py  -o "{rootFile}" -s "{samples}" -c "{cut}"  -v "jj_LV_mass,jj_l1_softDrop_mass"  -g "jj_gen_partialMass,jj_l1_gen_softDrop_mass,jj_l1_gen_pt"  -b "200,250,300,350,400,450,500,600,700,800,900,1000,1500,2000,5000"   samples'.format(rootFile=resFile,samples=template,cut=cut,binsMVV=binsMVV,minMVV=minMVV,maxMVV=maxMVV,tag=name)
  os.system(cmd)
  
def makeBackgroundShapesMJKernel(name,filename,template,leg,addCut="1"):
 
 #template += ",QCD_Pt-,QCD_HT"
 for p in purities:
  resFile=filename+"_"+name+"_detectorResponse_"+p+".root"	
  print "=========== PURITY: ", p
  cut='*'.join([cuts['common'],cuts[p],addCut,cuts['acceptanceGEN'],cuts['acceptanceMVV']])
  rootFile=filename+"_"+name+"_MJ"+leg+"_"+p+".root"  	      
  cmd='vvMake1DTemplateWithKernels.py -H "y" -o "{rootFile}" -s "{samples}" -c "{cut}"  -v "jj_{leg}_gen_softDrop_mass" -b {binsMJ}  -x {minMJ} -X {maxMJ} -r {res} samples'.format(rootFile=rootFile,samples=template,cut=cut,leg=leg,res=resFile,binsMJ=binsMJ,minMJ=minMJ,maxMJ=maxMJ)
  os.system(cmd)

def makeBackgroundShapesMJSpline(name,filename,template,leg,addCut="1"):

 #template += ",QCD_Pt-,QCD_HT"
 for p in purities:
  print "=========== PURITY: ", p
  cut='*'.join([cuts['common'],cuts[p],addCut,cuts['acceptance']])
  rootFile=filename+"_"+name+"_MJ"+leg+"_"+p+"_spline.root"	      
  cmd='vvMake1DTemplateSpline.py  -o "{rootFile}" -s "{samples}" -c "{cut}"  -v "jj_{leg}_softDrop_mass"  -b {binsMJ}  -x {minMJ} -X {maxMJ} -f 6 samples'.format(rootFile=rootFile,samples=template,cut=cut,leg=leg,binsMJ=binsMJ,minMJ=minMJ,maxMJ=maxMJ)
  os.system(cmd)

def makeBackgroundShapesMVVKernel(name,filename,template,addCut="1"):
 
 #template += ",QCD_Pt-,QCD_HT"
 for p in purities:
  resFile=filename+"_"+name+"_detectorResponse_"+p+".root"	
  print "=========== PURITY: ", p
  cut='*'.join([cuts['common'],cuts[p],addCut,cuts['acceptanceGEN'],cuts['acceptanceMJ']])    
  rootFile=filename+"_"+name+"_MVV_"+p+".root"
  cmd='vvMake1DMVVTemplateWithKernels.py -H "x" -o "{rootFile}" -s "{samples}" -c "{cut}"  -v "jj_gen_partialMass" -b {binsMVV}  -x {minMVV} -X {maxMVV} -r {res} samples'.format(rootFile=rootFile,samples=template,cut=cut,res=resFile,binsMVV=binsMVV,minMVV=minMVV,maxMVV=maxMVV)
  os.system(cmd)

def makeBackgroundShapesMVVConditional(name,filename,template,leg,addCut=""):
	
 #template += ",QCD_Pt-,QCD_HT"
 for p in purities:
  resFile=filename+"_"+name+"_detectorResponse_"+p+".root"	
  print "=========== PURITY: ", p
  cut='*'.join([cuts['common'],cuts[p],addCut,cuts['acceptanceGEN']])
  rootFile=filename+"_"+name+"_COND2D_"+p+"_"+leg+".root"		 
  cmd='vvMake2DTemplateWithKernels.py  -o "{rootFile}" -s "{samples}" -c "{cut}"  -v "jj_{leg}_gen_softDrop_mass,jj_gen_partialMass"  -b {binsMJ} -B {binsMVV} -x {minMJ} -X {maxMJ} -y {minMVV} -Y {maxMVV}  -r {res} samples'.format(rootFile=rootFile,samples=template,cut=cut,leg=leg,binsMVV=binsMVV,minMVV=minMVV,maxMVV=maxMVV,res=resFile,binsMJ=binsMJ,minMJ=minMJ,maxMJ=maxMJ)
  os.system(cmd)

def mergeBackgroundShapes(name,filename):

 for p in purities:
  inputx=filename+"_"+name+"_COND2D_"+p+"_l1.root"	
  inputy=filename+"_"+name+"_COND2D_"+p+"_l2.root"	
  inputz=filename+"_"+name+"_MVV_"+p+".root"      
  rootFile=filename+"_"+name+"_2D_"+p+".root"	     
  cmd='vvMergeHistosToPDF3D.py -i "{inputx}" -I "{inputy}" -z "{inputz}" -o "{rootFile}"'.format(rootFile=rootFile,inputx=inputx,inputy=inputy,inputz=inputz)
  os.system(cmd)

def makeNormalizations(name,filename,template,data=0,addCut='1',factor=1):

  for p in purities:
   rootFile=filename+"_"+p+".root"
   cut='*'.join([cuts['common'],cuts[p],addCut,cuts['acceptance']])
   cmd='vvMakeData.py -s "{samples}" -d {data} -c "{cut}"  -o "{rootFile}" -v "jj_l2_softDrop_mass,jj_l1_softDrop_mass,jj_LV_mass" -b "{bins},{bins},{BINS}" -m "{mini},{mini},{MINI}" -M "{maxi},{maxi},{MAXI}" -f {factor} -n "{name}"  samples'.format(samples=template,cut=cut,rootFile=rootFile,BINS=binsMVV,bins=binsMJ,MINI=minMVV,MAXI=maxMVV,mini=minMJ,maxi=maxMJ,factor=factor,name=name,data=data)
   os.system(cmd)
               	  
makeSignalShapesMVV("JJ_BulkGWW",BulkGravWWTemplate)
makeSignalShapesMJ("JJ_BulkGWW",BulkGravWWTemplate,'l1')
makeSignalShapesMJ("JJ_BulkGWW",BulkGravWWTemplate,'l2')
makeSignalYields("JJ_BulkGWW",BulkGravWWTemplate,BRWW,{'HPHP':0.99*0.99,'HPLP':0.99*1.03,'LPLP':1.03*1.03})

makeDetectorResponse("nonRes","JJ",nonResTemplate,cuts['nonres'])
#do not use these
#makeBackgroundShapesMJKernel("nonRes","JJ",nonResTemplate,'l1',cuts['nonres'])
#makeBackgroundShapesMJKernel("nonRes","JJ",nonResTemplate,'l2',cuts['nonres'])
#makeBackgroundShapesMJSpline("nonRes","JJ",nonResTemplate,'l1',cuts['nonres'])
#makeBackgroundShapesMJSpline("nonRes","JJ",nonResTemplate,'l2',cuts['nonres'])
#
makeBackgroundShapesMVVKernel("nonRes","JJ",nonResTemplate,cuts['nonres'])
makeBackgroundShapesMVVConditional("nonRes","JJ",nonResTemplate,'l1',cuts['nonres'])
makeBackgroundShapesMVVConditional("nonRes","JJ",nonResTemplate,'l2',cuts['nonres'])
mergeBackgroundShapes("nonRes","JJ")

makeNormalizations("nonRes","JJ",nonResTemplate,0,cuts['nonres'],1.0)
# makeNormalizations("data","JJ",dataTemplate,1)
