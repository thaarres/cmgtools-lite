import ROOT
from ROOT import *
import os, copy

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
    histogram=ROOT.TH2F(histo.GetName()+suffix,"histo",277,55,610,160,1000,7000)
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
  
# read out files
filelist = os.listdir('./res/')

mg_files = []
pythia_files = []
herwig_files = []

for f in filelist:
 if f.find('COND2D') == -1: continue
 if f.find('QCD_HT') != -1: mg_files.append('./res/'+f)
 elif f.find('QCD_Pt_') != -1: pythia_files.append('./res/'+f)
 else: herwig_files.append('./res/'+f)

#now hadd them
cmd = 'hadd -f JJ_nonRes_COND2D_HPHP_l2_altshape2.root '
for f in mg_files:
 cmd += f
 cmd += ' '
print cmd
os.system(cmd)

cmd = 'hadd -f JJ_nonRes_COND2D_HPHP_l2_altshapeUp.root '
for f in herwig_files:
 cmd += f
 cmd += ' '
print cmd
os.system(cmd)
 
cmd = 'hadd -f JJ_nonRes_COND2D_HPHP_l2_nominal.root '
for f in pythia_files:
 cmd += f
 cmd += ' '
print cmd
os.system(cmd)

#now retrieve histos
fhadd_madgraph = ROOT.TFile.Open('JJ_nonRes_COND2D_HPHP_l2_altshape2.root','READ')
fhadd_herwig = ROOT.TFile.Open('JJ_nonRes_COND2D_HPHP_l2_altshapeUp.root','READ')
fhadd_pythia = ROOT.TFile.Open('JJ_nonRes_COND2D_HPHP_l2_nominal.root','READ')

mjet_mvv_nominal_3D = fhadd_pythia.Get('mjet_mvv_nominal_3D') 
mjet_mvv_nominal = fhadd_pythia.Get('mjet_mvv_nominal')
histo_nominal = fhadd_pythia.Get('histo_nominal_coarse')
#histo_nominal_ScaleUp = fhadd_pythia.Get('histo_nominal_ScaleUp_coarse')
#histo_nominal_ScaleDown = fhadd_pythia.Get('histo_nominal_ScaleDown_coarse')

#mjet_mvv_nominal = fhadd_madgraph.Get('mjet_mvv_nominal')
#histo_nominal = fhadd_madgraph.Get('histo_nominal_coarse')
#histo_nominal_ScaleUp = fhadd_madgraph.Get('histo_nominal_ScaleUp_coarse')
#histo_nominal_ScaleDown = fhadd_madgraph.Get('histo_nominal_ScaleDown_coarse')

mjet_mvv_altshapeUp_3D = fhadd_herwig.Get('mjet_mvv_nominal_3D') 
mjet_mvv_altshapeUp = fhadd_herwig.Get('mjet_mvv_nominal')
histo_altshapeUp = fhadd_herwig.Get('histo_nominal_coarse')
#histo_altshape_ScaleUp = fhadd_herwig.Get('histo_nominal_ScaleUp_coarse')
#histo_altshape_ScaleDown = fhadd_herwig.Get('histo_nominal_ScaleDown_coarse')

mjet_mvv_altshape2_3D = fhadd_madgraph.Get('mjet_mvv_nominal_3D') 
mjet_mvv_altshape2 = fhadd_madgraph.Get('mjet_mvv_nominal')
histo_altshape2 = fhadd_madgraph.Get('histo_nominal_coarse')

#mjet_mvv_altshape2 = fhadd_pythia.Get('mjet_mvv_nominal')
#histo_altshape2 = fhadd_pythia.Get('histo_nominal_coarse')

#save everything in the final out file after renaming and do usual operations on histos
outf = ROOT.TFile.Open('JJ_nonRes_COND2D_HPHP_l2.root','RECREATE') 

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
expanded.Write('histo_nominal')
finalHistograms['histo_nominal'] = expanded

#histo_nominal_ScaleUp.Write('histo_nominal_ScaleUp_coarse')
#conditional(histo_nominal_ScaleUp)
#expanded=expandHisto(histo_nominal_ScaleUp)
#conditional(expanded)
#expanded.Write('histo_nominal_ScaleUp')

#histo_nominal_ScaleDown.Write('histo_nominal_ScaleDown_coarse')
#conditional(histo_nominal_ScaleDown)
#expanded=expandHisto(histo_nominal_ScaleDown)
#conditional(expanded)
#expanded.Write('histo_nominal_ScaleDown')

histo_altshapeUp.Write('histo_altshapeUp_coarse')
conditional(histo_altshapeUp)
expanded=expandHisto(histo_altshapeUp,"herwig")
conditional(expanded)
expanded.Write('histo_altshapeUp')
finalHistograms['histo_altshapeUp'] = expanded

#histo_altshape_ScaleUp.Write('histo_altshape_ScaleUp_coarse')
#conditional(histo_altshape_ScaleUp)
#expanded=expandHisto(histo_altshape_ScaleUp)
#conditional(expanded)
#expanded.Write('histo_altshape_ScaleUp')

#histo_altshape_ScaleDown.Write('histo_altshape_ScaleDown_coarse')
#conditional(histo_altshape_ScaleDown)
#expanded=expandHisto(histo_altshape_ScaleDown)
#conditional(expanded)
#expanded.Write('histo_altshape_ScaleDown')

histo_altshape2.Write('histo_altshape2_coarse')
conditional(histo_altshape2)
expanded=expandHisto(histo_altshape2,"madgraph")
conditional(expanded)
expanded.Write('histo_altshape2')

histogram_altshapeDown=mirror(finalHistograms['histo_altshapeUp'],finalHistograms['histo_nominal'],"histo_altshapeDown")
conditional(histogram_altshapeDown)
histogram_altshapeDown.Write()

alpha=1.5/610.
histogram_pt_down,histogram_pt_up=unequalScale(finalHistograms['histo_nominal'],"histo_nominal_PT",alpha)
conditional(histogram_pt_down)
histogram_pt_down.Write()
conditional(histogram_pt_up)
histogram_pt_up.Write()

alpha=1.5*55.
h1,h2=unequalScale(finalHistograms['histo_nominal'],"histo_nominal_OPT",alpha,-1)
conditional(h1)
h1.Write()
conditional(h2)
h2.Write()

outf.Close()
