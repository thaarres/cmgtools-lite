import ROOT
from ROOT import *
import os,copy,sys

def unequalScale(histo,name,alpha,power=1):
    newHistoU =copy.deepcopy(histo) 
    newHistoU.SetName(name+"Up")
    newHistoD =copy.deepcopy(histo) 
    newHistoD.SetName(name+"Down")
    maxFactor = max(pow(histo.GetXaxis().GetXmax(),power),pow(histo.GetXaxis().GetXmin(),power))
    for i in range(1,histo.GetNbinsX()+1):
        x= histo.GetXaxis().GetBinCenter(i)
        for j in range(1,histo.GetNbinsY()+1):
            nominal=histo.GetBinContent(i,j)
            factor = 1+alpha*pow(x,power) 
            newHistoU.SetBinContent(i,j,nominal*factor)
            newHistoD.SetBinContent(i,j,nominal/factor)
    if newHistoU.Integral()>0.0:        
        newHistoU.Scale(1.0/newHistoU.Integral())        
    if newHistoD.Integral()>0.0:        
        newHistoD.Scale(1.0/newHistoD.Integral())        
    return newHistoU,newHistoD 
    
def mirror(histo,histoNominal,name):
    newHisto =copy.deepcopy(histoNominal) 
    newHisto.SetName(name)
    intNominal=histoNominal.Integral()
    intUp = histo.Integral()
    for i in range(1,histo.GetNbinsX()+1):
        for j in range(1,histo.GetNbinsY()+1):
            up=histo.GetBinContent(i,j)/intUp
            nominal=histoNominal.GetBinContent(i,j)/intNominal
            newHisto.SetBinContent(i,j,histoNominal.GetBinContent(i,j)*nominal/up)
    return newHisto       
	
def expandHisto(histo,suffix):
    histogram=ROOT.TH2F(histo.GetName()+suffix,"histo",80,55,215,100,1000,5000)
    for i in range(1,histo.GetNbinsX()+1):
        proje = histo.ProjectionY("q",i,i)
        graph=ROOT.TGraph(proje)
        for j in range(1,histogram.GetNbinsY()+1):
            x=histogram.GetYaxis().GetBinCenter(j)
            bin=histogram.GetBin(i,j)
            histogram.SetBinContent(bin,graph.Eval(x,0,"S"))
    return histogram
        

def conditional(hist):
    for i in range(1,hist.GetNbinsY()+1):
        proj=hist.ProjectionX("q",i,i)
        integral=proj.Integral()
        if integral==0.0:
            print 'SLICE WITH NO EVENTS!!!!!!!!',hist.GetName()
            continue
        for j in range(1,hist.GetNbinsX()+1):
            hist.SetBinContent(j,i,hist.GetBinContent(j,i)/integral)
	    
sampledir = 'samples'
jobdir = 'tmp'
outdir = 'res'

exit_flag = False

jobsPerSample = {}

samples = []
for f in os.listdir(sampledir):
 if f.find('.root') != -1 and f.find('QCD') != -1: samples.append(f.replace('.root',''))

for s in samples:
 filelist = []
 for t in os.listdir(jobdir):
  if t.find(s) == -1: continue
  jobid = t[t.rfind('_')+1:len(t)]
  found = False
  for o in os.listdir(outdir):
   if o.find(s) != -1 and o.find('_'+jobid+'_') != -1:
    found = True
    filelist.append(outdir+"/"+o)
    break
  if not found:
   print "SAMPLE ",s," JOBID ",jobid," NOT FOUND"
   #os.chdir(jobdir+"/"+t)
   #os.system('rm -rf LSFJOB_*')
   #os.system('rm logs')
   #os.system('bsub -q 8nh -o logs job_%s.sh'%(t))
   #os.chdir('../../')
   exit_flag = True
 jobsPerSample[s] = filelist


if exit_flag:
 print "Mergin not done: some files are missing. Exiting!"
 sys.exit()


os.system('rm -r '+outdir+'_out')
os.system('mkdir '+outdir+'_out')

for s in jobsPerSample.keys():

 factor = 1./float(len(jobsPerSample[s]))
 print "sample: ", s,"number of files:",len(jobsPerSample[s]),"adding histo with scale factor:",factor

 outf = ROOT.TFile.Open(outdir+'_out/JJ_nonRes_COND2D_HPHP_l1_%s.root'%(s),'RECREATE')
  
 finalHistos = {}
 finalHistos['histo_nominal_coarse'] = ROOT.TH2F("histo_nominal_coarse_out","histo_nominal_coarse_out",80,55,215,40,1000,5000)
 finalHistos['mjet_mvv_nominal'] = ROOT.TH2F("mjet_mvv_nominal_out","mjet_mvv_nominal_out",80,55,215,100,1000,5000)
 finalHistos['mjet_mvv_nominal_3D'] = ROOT.TH3F("mjet_mvv_nominal_3D_out","mjet_mvv_nominal_3D_out",80,55,215,80,55,215,100,1000,5000)
    
 for f in jobsPerSample[s]:

  inf = ROOT.TFile.Open(f,'READ')
    
  for h in inf.GetListOfKeys():
  
   for k in finalHistos.keys():
    if h.GetName() == k:

     histo = ROOT.TH1F()
     histo = inf.Get(h.GetName())

     finalHistos[h.GetName()].Add(histo,factor)
   
 print "Write file: ",outdir+'_out/JJ_nonRes_COND2D_HPHP_l1_%s.root'%(s)
   
 outf.cd()  
 
 for k in finalHistos.keys():
  finalHistos[k].SetTitle(k)
  finalHistos[k].Write(k)
   
 outf.Close()
 outf.Delete()



  
# read out files
filelist = os.listdir('./'+outdir+'_out/')

mg_files = []
pythia_files = []
herwig_files = []

for f in filelist:
 if f.find('COND2D') == -1: continue
 if f.find('QCD_HT') != -1: mg_files.append('./'+outdir+'_out/'+f)
 elif f.find('QCD_Pt_') != -1: pythia_files.append('./'+outdir+'_out/'+f)
 else: herwig_files.append('./'+outdir+'_out/'+f)

#now hadd them
cmd = 'hadd -f JJ_nonRes_COND2D_HPHP_l1_altshape2.root '
for f in mg_files:
 cmd += f
 cmd += ' '
print cmd
os.system(cmd)

cmd = 'hadd -f JJ_nonRes_COND2D_HPHP_l1_altshapeUp.root '
for f in herwig_files:
 cmd += f
 cmd += ' '
print cmd
os.system(cmd)
 
cmd = 'hadd -f JJ_nonRes_COND2D_HPHP_l1_nominal.root '
for f in pythia_files:
 cmd += f
 cmd += ' '
print cmd
os.system(cmd)


#now retrieve histos
fhadd_madgraph = ROOT.TFile.Open('JJ_nonRes_COND2D_HPHP_l1_altshape2.root','READ')
fhadd_herwig = ROOT.TFile.Open('JJ_nonRes_COND2D_HPHP_l1_altshapeUp.root','READ')
fhadd_pythia = ROOT.TFile.Open('JJ_nonRes_COND2D_HPHP_l1_nominal.root','READ')

mjet_mvv_nominal_3D = fhadd_pythia.Get('mjet_mvv_nominal_3D') 
mjet_mvv_nominal_3D.SetName('mjet_mvv_nominal_3D')
mjet_mvv_nominal_3D.SetTitle('mjet_mvv_nominal_3D')
mjet_mvv_nominal = fhadd_pythia.Get('mjet_mvv_nominal')
mjet_mvv_nominal.SetName('mjet_mvv_nominal')
mjet_mvv_nominal.SetTitle('mjet_mvv_nominal')
histo_nominal = fhadd_pythia.Get('histo_nominal_coarse')
histo_nominal.SetName('histo_nominal_coarse')
histo_nominal.SetTitle('histo_nominal_coarse')

mjet_mvv_altshapeUp_3D = fhadd_herwig.Get('mjet_mvv_nominal_3D') 
mjet_mvv_altshapeUp_3D.SetName('mjet_mvv_altshapeUp_3D')
mjet_mvv_altshapeUp_3D.SetTitle('mjet_mvv_altshapeUp_3D')
mjet_mvv_altshapeUp = fhadd_herwig.Get('mjet_mvv_nominal')
mjet_mvv_altshapeUp.SetName('mjet_mvv_altshapeUp')
mjet_mvv_altshapeUp.SetTitle('mjet_mvv_altshapeUp')
histo_altshapeUp = fhadd_herwig.Get('histo_nominal_coarse')
histo_altshapeUp.SetName('histo_altshapeUp_coarse')
histo_altshapeUp.SetTitle('histo_altshapeUp_coarse')

mjet_mvv_altshape2_3D = fhadd_madgraph.Get('mjet_mvv_nominal_3D') 
mjet_mvv_altshape2_3D.SetName('mjet_mvv_altshape2_3D')
mjet_mvv_altshape2_3D.SetTitle('mjet_mvv_altshape2_3D')
mjet_mvv_altshape2 = fhadd_madgraph.Get('mjet_mvv_nominal')
mjet_mvv_altshape2.SetName('mjet_mvv_altshape2')
mjet_mvv_altshape2.SetTitle('mjet_mvv_altshape2')
histo_altshape2 = fhadd_madgraph.Get('histo_nominal_coarse')
histo_altshape2.SetName('histo_altshape2_coarse')
histo_altshape2.SetTitle('histo_altshape2_coarse')

#save everything in the final out file after renaming and do usual operations on histos
outf = ROOT.TFile.Open('JJ_nonRes_COND2D_HPHP_l1.root','RECREATE') 

mjet_mvv_nominal.Write('mjet_mvv_nominal')
mjet_mvv_altshapeUp.Write('mjet_mvv_altshapeUp')
mjet_mvv_altshape2.Write('mjet_mvv_altshape2')
mjet_mvv_nominal_3D.Write('mjet_mvv_nominal_3D')
mjet_mvv_altshapeUp_3D.Write('mjet_mvv_altshapeUp_3D')
mjet_mvv_altshape2_3D.Write('mjet_mvv_altshape2_3D')

finalHistograms = {}

histo_nominal.Write('histo_nominal_coarse')
conditional(histo_nominal)
expanded=expandHisto(histo_nominal,"")
conditional(expanded)
expanded.SetName('histo_nominal')
expanded.SetTitle('histo_nominal')
expanded.Write('histo_nominal')
finalHistograms['histo_nominal'] = expanded

histo_altshapeUp.Write('histo_altshapeUp_coarse')
conditional(histo_altshapeUp)
expanded=expandHisto(histo_altshapeUp,"herwig")
conditional(expanded)
expanded.SetName('histo_altshapeUp')
expanded.SetTitle('histo_altshapeUp')
expanded.Write('histo_altshapeUp')
finalHistograms['histo_altshapeUp'] = expanded

histo_altshape2.Write('histo_altshape2_coarse')
conditional(histo_altshape2)
expanded=expandHisto(histo_altshape2,"madgraph")
conditional(expanded)
expanded.SetName('histo_altshape2')
expanded.SetTitle('histo_altshape2')
expanded.Write('histo_altshape2')

histogram_altshapeDown=mirror(finalHistograms['histo_altshapeUp'],finalHistograms['histo_nominal'],"histo_altshapeDown")
conditional(histogram_altshapeDown)
histogram_altshapeDown.SetName('histo_altshapeDown')
histogram_altshapeDown.SetTitle('histo_altshapeDown')
histogram_altshapeDown.Write()

alpha=1.5/215.
histogram_pt_down,histogram_pt_up=unequalScale(finalHistograms['histo_nominal'],"histo_nominal_PT",alpha)
conditional(histogram_pt_down)
histogram_pt_down.SetName('histo_nominal_PTDown')
histogram_pt_down.SetTitle('histo_nominal_PTDown')
histogram_pt_down.Write('histo_nominal_PTDown')
conditional(histogram_pt_up)
histogram_pt_up.SetName('histo_nominal_PTUp')
histogram_pt_up.SetTitle('histo_nominal_PTUp')
histogram_pt_up.Write('histo_nominal_PTUp')

alpha=1.5*55.
h1,h2=unequalScale(finalHistograms['histo_nominal'],"histo_nominal_OPT",alpha,-1)
conditional(h1)
h1.SetName('histo_nominal_OPTDown')
h1.SetTitle('histo_nominal_OPTDown')
h1.Write('histo_nominal_OPTDown')
conditional(h2)
h2.SetName('histo_nominal_OPTUp')
h2.SetTitle('histo_nominal_OPTUp')
h2.Write('histo_nominal_OPTUp')

outf.Close()
