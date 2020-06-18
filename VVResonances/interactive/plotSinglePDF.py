import ROOT
from ROOT import *
import time
from array import array
def getListOfBinsLowEdge(hist,dim):
    axis =0
    N = 0
    if dim =="x":
        axis= hist.GetXaxis()
        N = hist.GetNbinsX()
    if dim =="y":
        axis = hist.GetYaxis()
        N = hist.GetNbinsY()
    if dim =="z":
        axis = hist.GetZaxis()
        N = hist.GetNbinsZ()
    if axis==0:
        return {}
    
    mmin = axis.GetXmin()
    mmax = axis.GetXmax()
    r =[]
    for i in range(1,N+2):
        #v = mmin + i * (mmax-mmin)/float(N)
        r.append(axis.GetBinLowEdge(i))
    return r
    
f = ROOT.TFile.Open('workspace_JJ_ZprimeZH_VV_HPHP_13TeV_2016ZprimeZH.root','READ')
ws = f.w

modelTTjets = ws.pdf('shapeBkg_TTJets_JJ_VV_HPHP_13TeV_2016')

MJ1= ws.var("MJ1");
MJ2= ws.var("MJ2");
MJJ= ws.var("MJJ");
args = ROOT.RooArgSet(MJ1,MJ2,MJJ)

print "n_exp_binJJ_VV_HPHP_13TeV_2016_proc_TTJets"
o_norm_ttjets = ws.obj("n_exp_binJJ_VV_HPHP_13TeV_2016_proc_TTJets")

nEventsTT = o_norm_ttjets.getVal()
print "Expected tt+jets events: ",nEventsTT
modelTTjets.Print('v')

ttjets = modelTTjets.generate(args,int(nEventsTT*10))

finmc = ROOT.TFile.Open("results_2016_tt/JJ_2016_nonRes_VV_HPHP.root",'READ')
hmcin = finmc.Get('nonRes')
xbins = array("f",getListOfBinsLowEdge(hmcin,"x"))
zbins = array("f",getListOfBinsLowEdge(hmcin,"z"))
  
hout_ttjets = ROOT.TH3F('ttjets','ttjets',len(xbins)-1,xbins,len(xbins)-1,xbins,len(zbins)-1,zbins)
if ttjets!=None:
 #print signal.sumEntries()
 for i in range(0,int(ttjets.sumEntries())):
  a = ttjets.get(i)
  it = a.createIterator()
  var = it.Next()
  x=[]
  while var:
      x.append(var.getVal())
      var = it.Next()
  #print x
  hout_ttjets.Fill(x[0],x[1],x[2])  

print "Integral",hout_ttjets.Integral()
x_proj = hout_ttjets.ProjectionX()
x_proj.Draw("PE")
time.sleep(1000)  