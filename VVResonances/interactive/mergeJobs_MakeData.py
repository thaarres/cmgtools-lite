import ROOT
from ROOT import *
import math
import os

# read out files
filelist = os.listdir('./res/')

mg_files = []
pythia_files = []
herwig_files = []

for f in filelist:
 #if f.find('COND2D') == -1: continue
 if f.find('QCD_HT') != -1: mg_files.append('./res/'+f)
 elif f.find('QCD_Pt_') != -1: pythia_files.append('./res/'+f)
 else: herwig_files.append('./res/'+f)

#now hadd them
cmd = 'hadd -f JJ_nonRes_HPHP_altshape2.root '
for f in mg_files:
 cmd += f
 cmd += ' '
print cmd
os.system(cmd)

cmd = 'hadd -f JJ_nonRes_HPHP_altshapeUp.root '
for f in herwig_files:
 cmd += f
 cmd += ' '
print cmd
os.system(cmd)
 
cmd = 'hadd -f JJ_nonRes_HPHP_nominal.root '
for f in pythia_files:
 cmd += f
 cmd += ' '
print cmd
os.system(cmd)

fin = ROOT.TFile.Open('JJ_nonRes_HPHP_nominal.root','READ')
hmcin = fin.Get('nonRes')

fout = ROOT.TFile.Open('JJ_HPHP.root','RECREATE')
hout = ROOT.TH3F('data','data',hmcin.GetNbinsX(),hmcin.GetXaxis().GetXmin(),hmcin.GetXaxis().GetXmax(),hmcin.GetNbinsY(),hmcin.GetYaxis().GetXmin(),hmcin.GetYaxis().GetXmax(),hmcin.GetNbinsZ(),hmcin.GetZaxis().GetXmin(),hmcin.GetZaxis().GetXmax())
hmcout = ROOT.TH3F('nonRes','nonRes',hmcin.GetNbinsX(),hmcin.GetXaxis().GetXmin(),hmcin.GetXaxis().GetXmax(),hmcin.GetNbinsY(),hmcin.GetYaxis().GetXmin(),hmcin.GetYaxis().GetXmax(),hmcin.GetNbinsZ(),hmcin.GetZaxis().GetXmin(),hmcin.GetZaxis().GetXmax())
hmcout.Add(hmcin)

for k in range(1,hmcin.GetNbinsZ()+1):
 for j in range(1,hmcin.GetNbinsY()+1):
  for i in range(1,hmcin.GetNbinsX()+1):
   evs = hmcin.GetBinContent(i,j,k)*35900.
   #if evs >= 1:
   err = math.sqrt(evs)
   hout.SetBinContent(i,j,k,evs)
   hout.SetBinError(i,j,k,err)

hout.Write()
hmcout.Write()

fin.Close()
fout.Close()
