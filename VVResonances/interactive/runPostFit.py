import time,sys
import ROOT
from ROOT import *
ROOT.gSystem.Load("libHiggsAnalysisCombinedLimit")

hmj = ROOT.TH1F('hmj','hmj',h.GetNbinsY(),h.GetYaxis().GetXmin(),h.GetYaxis().GetXmax())
hmvv = ROOT.TH1F('hmvv','hmvv',h.GetNbinsX(),h.GetXaxis().GetXmin(),h.GetXaxis().GetXmax())

fin = TFile.Open('JJ_BulkGWW_HPHP_13TeV_workspace.root','READ')
fin.ls()

workspace = fin.Get("w")
workspace.Print()

print "----------- Parameter Workspace -------------";
parameters_workspace = workspace.allVars();
par = parameters_workspace.createIterator();
par.Reset();
param = par.Next()
newpars = []
while (param):
    param.Print();
    param=par.Next()
print "---------------------------------------------";

print "----------- Pdf in the Workspace -------------";
pdfs_workspace = workspace.allPdfs();
par = pdfs_workspace.createIterator();
par.Reset();
param=par.Next()
newpdfs = []
while (param):
    param.Print();
    param = par.Next()
print "----------------------------------------------";

workspace.var('MH').setVal(2000)
workspace.var('MH').setConstant(1)

workspace.pdf("model_b").Print()
model = workspace.pdf("model_b")
fitResult = model.fitTo(workspace.data("data_obs"),ROOT.RooFit.NumCPU(8),ROOT.RooFit.SumW2Error(False),ROOT.RooFit.Minos(0),ROOT.RooFit.Verbose(0),ROOT.RooFit.Save(1),ROOT.RooFit.Normalization(1.0,ROOT.RooAbsReal.RelativeExpected))
fitResult.Print()

canvas = ROOT.TCanvas("c")
canvas.cd()

varMax=workspace.var('MJ1').getMax()
varMin=workspace.var('MJ1').getMin()
varBins=workspace.var('MJ1').getBins()
workspace.var('MJJ').setRange("lowMJJ",1000,1500)

frame=workspace.var('MJ1').frame()
dataset=workspace.data("data_obs")
dataset.Print()
dataset.plotOn(frame,ROOT.RooFit.Name("datapoints"),ROOT.RooFit.CutRange("lowMJJ"))
names = "shapeBkg_nonRes_JJ_HPHP_13TeV"
model.getPdf('JJ_HPHP_13TeV').plotOn(frame,ROOT.RooFit.Components(names),ROOT.RooFit.NumCPU(8),ROOT.RooFit.Name('nonRes'),ROOT.RooFit.Normalization(1.0,ROOT.RooAbsReal.RelativeExpected),ROOT.RooFit.ProjectionRange("lowMJJ"))

frame.Draw("AH")

canvas2 = ROOT.TCanvas("c2")
canvas2.cd()

frame2=workspace.var('MJJ').frame()
dataset=workspace.data("data_obs")

workspace.var('MJ1').setRange("lowMJ",70,90)
workspace.var('MJ2').setRange("lowMJ",70,90)
dataset=dataset.reduce("{var1}>{mini1}&&{var1}<{maxi1}&&{var2}>{mini2}&&{var2}<{maxi2}".format(var1="MJ1",mini1=70,maxi1=90,var2="MJ2",mini2=70,maxi2=90))
dataset.plotOn(frame2,ROOT.RooFit.Name("datapoints2"),ROOT.RooFit.CutRange("lowMJ"))
names = "shapeBkg_nonRes_JJ_HPHP_13TeV"
model.getPdf('JJ_HPHP_13TeV').plotOn(frame2,ROOT.RooFit.Components(names),ROOT.RooFit.NumCPU(8),ROOT.RooFit.Name('nonRes'),ROOT.RooFit.Normalization(1.0,ROOT.RooAbsReal.RelativeExpected),ROOT.RooFit.ProjectionRange("lowMJ"))

frame2.Draw("AH")

time.sleep(100)
