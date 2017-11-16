import ROOT
from ROOT import *
import os, copy

def unequalScale(histo,name,alpha,power=1):
    newHistoU =copy.deepcopy(histo) 
    newHistoU.SetName(name+"Up")
    newHistoD =copy.deepcopy(histo) 
    newHistoD.SetName(name+"Down")
    for i in range(1,histo.GetNbinsX()+1):
        x= histo.GetXaxis().GetBinCenter(i)
        nominal=histo.GetBinContent(i)
        factor = 1+alpha*pow(x,power) 
        newHistoU.SetBinContent(i,nominal*factor)
        newHistoD.SetBinContent(i,nominal/factor)
    return newHistoU,newHistoD 
    
def mirror(histo,histoNominal,name):
    newHisto =copy.deepcopy(histoNominal) 
    newHisto.SetName(name)
    intNominal=histoNominal.Integral()
    intUp = histo.Integral()
    for i in range(1,histo.GetNbinsX()+1):
        up=histo.GetBinContent(i)/intUp
        nominal=histoNominal.GetBinContent(i)/intNominal
        newHisto.SetBinContent(i,histoNominal.GetBinContent(i)*nominal/up)
    return newHisto 

# read out files
filelist = os.listdir('./res')

mg_files = []
pythia_files = []
herwig_files = []

for f in filelist:
 if f.find('QCD_HT') != -1: mg_files.append('./res/'+f)
 elif f.find('QCD_Pt_') != -1: pythia_files.append('./res/'+f)
 else: herwig_files.append('./res/'+f)

#now hadd them
cmd = 'hadd -f JJ_nonRes_MVV_HPHP_altshape2.root '
for f in mg_files:
 cmd += f
 cmd += ' '
print cmd
os.system(cmd)

cmd = 'hadd -f JJ_nonRes_MVV_HPHP_altshapeUp.root '
for f in herwig_files:
 cmd += f
 cmd += ' '
print cmd
os.system(cmd)
 
cmd = 'hadd -f JJ_nonRes_MVV_HPHP_nominal.root '
for f in pythia_files:
 cmd += f
 cmd += ' '
print cmd
os.system(cmd)

#now retrieve histos
fhadd_madgraph = ROOT.TFile.Open('JJ_nonRes_MVV_HPHP_altshape2.root','READ')
fhadd_herwig = ROOT.TFile.Open('JJ_nonRes_MVV_HPHP_altshapeUp.root','READ')
fhadd_pythia = ROOT.TFile.Open('JJ_nonRes_MVV_HPHP_nominal.root','READ')

mvv_nominal = fhadd_pythia.Get('mvv_nominal')
histo_nominal = fhadd_pythia.Get('histo_nominal')
#histo_nominal_ScaleUp = fhadd_pythia.Get('histo_nominal_ScaleUp')
#histo_nominal_ScaleDown = fhadd_pythia.Get('histo_nominal_ScaleDown')

mvv_altshapeUp = fhadd_herwig.Get('mvv_nominal')
histo_altshapeUp = fhadd_herwig.Get('histo_nominal')
#histo_altshape_ScaleUp = fhadd_herwig.Get('histo_nominal_ScaleUp')
#histo_altshape_ScaleDown = fhadd_herwig.Get('histo_nominal_ScaleDown')

mvv_altshape2 = fhadd_madgraph.Get('mvv_nominal')
histo_altshape2 = fhadd_madgraph.Get('histo_nominal')


#save everything in the final out file after renaming and do usual operations on histos
outf = ROOT.TFile.Open('JJ_nonRes_MVV_HPHP.root','RECREATE') 

mvv_nominal.Write('mvv_nominal')
histo_nominal.Write('histo_nominal')
#histo_nominal_ScaleUp.Write('histo_nominal_ScaleUp')
#histo_nominal_ScaleDown.Write('histo_nominal_ScaleDown')
mvv_altshapeUp.Write('mvv_altshapeUp')
histo_altshapeUp.Write('histo_altshapeUp')
#histo_altshape_ScaleUp.Write('histo_altshape_ScaleUp')
#histo_altshape_ScaleDown.Write('histo_altshape_ScaleDown')
mvv_altshape2.Write('mvv_altshape2')
histo_altshape2.Write('histo_altshape2')

histogram_altshapeDown=mirror(histo_altshapeUp,histo_nominal,"histo_altshapeDown")
histogram_altshapeDown.Write('histo_altshapeDown')

alpha=1.5/5000
histogram_pt_down,histogram_pt_up=unequalScale(histo_nominal,"histo_nominal_PT",alpha)
histogram_pt_down.Write()
histogram_pt_up.Write()

alpha=1.5*1000
histogram_opt_down,histogram_opt_up=unequalScale(histo_nominal,"histo_nominal_OPT",alpha,-1)
histogram_opt_down.Write()
histogram_opt_up.Write()
