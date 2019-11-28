import ROOT
from CMGTools.VVResonances.plotting.RooPlotter import *
from CMGTools.VVResonances.plotting.TreePlotter import TreePlotter
from CMGTools.VVResonances.plotting.MergedPlotter import MergedPlotter
from CMGTools.VVResonances.plotting.StackPlotter import StackPlotter

import ROOT as rt
import os,copy, random
from array import array
from time import sleep
from datetime import datetime
import argparse
startTime = datetime.now()
import CMS_lumi, tdrstyle
tdrstyle.setTDRStyle()
prelim = 1
if prelim:
   CMS_lumi.extraText = "Preliminary"
else:
   CMS_lumi.extraText = ""
# ROOT.gROOT.SetBatch(True)

HCALbinsMVV= [838,890,944,1000,1058,1118,1181,1246,1313,1383,1455,1530,1607,1687,1770,1856,1945,2037]#,2132,2231,2332,2438,2546,2659,2775,2895,3019,3147,3279,3416,3558,3704,3854,4010,4171,4337,4509,4686,4869,5058,5253,5455,5663,5877,6099,6328,6564,6808]
HCALbinsMVV= [1126,1181,1246,1313,1383,1455,1530,1607,1687,1770,1856,1945,2037,2132,2231,2332,2438,2546,2659,2775,2895,3019,3147,3279,3416,3558,3704,3854,4010,4171,4337,4509,4686,4869,5058,5253,5455,5663,5877,6099,6328,6564,6808]
xbins = array('d',HCALbinsMVV)

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-b','--batch', action='store_true', help="stop at generation step", default = False)
#     args = parser.parse_args()

in_directory='/eos/user/t/thaarres/www/vvana/3D_latest/control_plots_latest/combined_latest/'
out_directory='control_plots_PAPER/'
try: os.stat(out_directory)
except: os.mkdir(out_directory)

lumi=41367.929231882
# lumi=35900.
if  lumi==35900.: lumi_13TeV = "35.9 fb^{-1}"
else: lumi_13TeV = "41.4 fb^{-1}"
lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPeriod=0
cuts={}
iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.30
 
def getMCunc(hist):
   
    x   = []
    y   = []
    exl = []
    eyl = []
    # exh = []
#     eyh = []

    for bin in range(1,hist.GetNbinsX()+1):
        if hist.GetBinContent(bin) != 0:
            if bin == 1:
                x  .append(float(hist.GetBinLowEdge(bin)) )
                y  .append(1. )
                exl.append(hist.GetBinWidth(bin))
                eyl.append(hist.GetBinError(bin)/hist.GetBinContent(bin))
            
            x  .append(float(hist.GetBinCenter(bin)) )
            y  .append(float(1.)                     )
            exl.append(hist.GetBinWidth(bin))
            eyl.append(hist.GetBinError(bin)/hist.GetBinContent(bin))
            
            if bin == hist.GetNbinsX():
                x  .append( hist.GetBinLowEdge(bin)+hist.GetBinWidth(bin) )
                y  .append(1. )
                exl.append(hist.GetBinWidth(bin))
                eyl.append(hist.GetBinError(bin)/hist.GetBinContent(bin))
        elif hist.GetBinContent(bin) == 0:     
            x  .append(float(hist.GetBinCenter(bin)) )
            y  .append(float(1.)                     )
            exl.append(hist.GetBinWidth(bin))
            eyl.append(0)
        
        # exh.append(hist.GetBinWidth(bin)/2)
#         eyh.append(hist.GetBinErrorUp(bin))
        
    
    n   = len(x)    
    vx   = array("f",x   )
    vy   = array("f",y   )
    vexl = array("f",exl )
    veyl = array("f",eyl )
    # vexh = array("f",exh )
 #    veyh = array("f",eyh )
    
    
    mcunc = rt.TGraphErrors(n,vx,vy,vexl,veyl)
    mcunc.SetFillStyle(3013)
    mcunc.SetMarkerColor(rt.kBlack)
    mcunc.SetFillColor(rt.kBlack)
    mcunc.SetLineColor(rt.kBlack)
    return mcunc    
    
def GetRatioPad():
  c1_1 = rt.TPad("c1_1", "newpad1",0.,0.,1,0.2)
  c1_1.Draw()
  c1_1.cd()
  c1_1.SetTopMargin(0)
  c1_1.SetBottomMargin( 3*B/H )
  c1_1.SetLeftMargin( L/W )
  c1_1.SetRightMargin( R/W )
  c1_1.SetFillStyle(0)
  c1_1.SetFrameFillStyle(4000)
  c1_1.SetGrid(1)
  return c1_1
def GetMainPad():
   #change the CMS_lumi variables (see CMS_lumi.py)
   CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
   CMS_lumi.lumi_8TeV = "18.3 fb^{-1}"
   CMS_lumi.lumi_13TeV = "77.3 fb^{-1}"
   CMS_lumi.writeExtraText = 1
   CMS_lumi.extraText = "Preliminary"
   CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

   iPos = 11
   if( iPos==0 ): CMS_lumi.relPosX = 0.14

   H_ref = 600 
   W_ref = 600 
   W = W_ref
   H  = H_ref

   iPeriod = 0
   iPeriod = 4
   # references for T, B, L, R
   T = 0.08*H_ref
   B = 0.12*H_ref 
   L = 0.12*W_ref
   R = 0.04*W_ref

   pad = ROOT.TPad("pad", "pad", 0, 0.3, 1, 1.0)
   pad.SetFillColor(0)
   pad.SetBorderMode(0)
   pad.SetFrameFillStyle(0)
   pad.SetFrameBorderMode(0)
   #pad.SetLeftMargin( L/W )
   #pad.SetRightMargin( R/W )
   pad.SetTopMargin( T/H )
   #pad.SetBottomMargin( B/H )
   pad.SetTickx(0)
   pad.SetTicky(0)
   pad.SetBottomMargin(0.01)    
   pad.SetTopMargin(0.1)
 
   return pad
def getCanvas(cname):
 ROOT.gStyle.SetOptStat(0)
 #change the CMS_lumi variables (see CMS_lumi.py)
 CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
 CMS_lumi.lumi_8TeV = "18.3 fb^{-1}"
 CMS_lumi.lumi_13TeV = "77.3 fb^{-1}"
 CMS_lumi.writeExtraText = 1
 CMS_lumi.extraOverCmsTextSize=0.6
 if prelim:
    CMS_lumi.extraText = "Preliminary"
 else:
    CMS_lumi.extraText = ""
 # CMS_lumi.writeExtraText = 1
 # # CMS_lumi.extraText = " "
 # CMS_lumi.lumi_sqrtS = "13 TeV"# (2016+2017)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
 # iPos = 0
 # if( iPos==0 ): CMS_lumi.relPosX = 0.014
 # #iPos = 11
 # iPos = 11
 # if( iPos==0 ): CMS_lumi.relPosX = 0.30
 H_ref = 600 
 W_ref = 600 
 W = W_ref
 H  = H_ref
 iPeriod = 0
 # references for T, B, L, R
 T = 0.08*H_ref
 B = 0.12*H_ref 
 L = 0.15*W_ref
 R = 0.04*W_ref
 canvas = ROOT.TCanvas(cname,cname,50,50,W,H)
 canvas.SetFillColor(0)
 canvas.SetBorderMode(0)
 canvas.SetFrameFillStyle(0)
 canvas.SetFrameBorderMode(0)
 canvas.SetLeftMargin( L/W )
 canvas.SetRightMargin( R/W )
 canvas.SetTopMargin( T/H )
 canvas.SetBottomMargin( B/H )
 canvas.SetTickx(0)
 canvas.SetTicky(0)
 legend = ROOT.TLegend(0.4865772,0.6381119,0.942953,0.8951049,"","brNDC")
 # legend = ROOT.TLegend(0.52,0.65,0.92,0.9,"","brNDC")
 legend.SetBorderSize(0)
 legend.SetLineColor(1)
 legend.SetLineStyle(1)
 legend.SetLineWidth(1)
 legend.SetFillColor(0)
 legend.SetFillStyle(0)
 legend.SetTextFont(42)
 
 pt = ROOT.TPaveText(0.6224832,0.4256993,0.9731544,0.5743007,"NDC")
 # pt.SetTextFont(72)
 pt.SetTextSize(0.04)
 pt.SetTextAlign(12)
 pt.SetFillColor(0)
 pt.SetBorderSize(0)
 pt.SetFillStyle(0)
 
 
 return canvas, legend, pt  
def getLegend():
    legend = ROOT.TLegend(0.7084422,0.3798951,0.9174874,0.4795455,"","brNDC")
    legend.SetBorderSize(0)
    legend.SetLineColor(1)
    legend.SetLineStyle(1)
    legend.SetLineWidth(1)
    legend.SetFillColor(0)
    legend.SetFillStyle(0)
    legend.SetTextFont(42)
    return legend
def get_canvas(cname):

 #change the CMS_lumi variables (see CMS_lumi.py)
 CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
 CMS_lumi.lumi_8TeV = "18.3 fb^{-1}"
 CMS_lumi.writeExtraText = 1
 if prelim:
    CMS_lumi.extraText = "Preliminary"
 else:
    CMS_lumi.extraText = ""
 CMS_lumi.lumi_sqrtS = "77.3 fb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

 iPos = 11
 if( iPos==0 ): CMS_lumi.relPosX = 0.30

 H_ref = 600 
 W_ref = 600 
 W = W_ref
 H  = H_ref

 iPeriod = 0

 # references for T, B, L, R
 T = 0.08*H_ref
 B = 0.12*H_ref 
 L = 0.12*W_ref
 R = 0.04*W_ref

 canvas = ROOT.TCanvas(cname,cname,50,50,W,H)
 canvas.SetFillColor(0)
 canvas.SetBorderMode(0)
 canvas.SetFrameFillStyle(0)
 canvas.SetFrameBorderMode(0)
 canvas.SetLeftMargin( L/W )
 canvas.SetRightMargin( R/W )
 canvas.SetTopMargin( T/H )
 canvas.SetBottomMargin( B/H )
 canvas.SetTickx(0)
 canvas.SetTicky(0)
 
 return canvas

def get_pad(name):

 #change the CMS_lumi variables (see CMS_lumi.py)
 CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
 CMS_lumi.lumi_8TeV = "18.3 fb^{-1}"
 CMS_lumi.lumi_13TeV = "77.3 fb^{-1}"
 CMS_lumi.writeExtraText = 1
 if prelim:
    CMS_lumi.extraText = "Preliminary"
 else:
    CMS_lumi.extraText = ""
 CMS_lumi.lumi_sqrtS = "13 TeV (2016+2017)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

 iPos = 0
 if( iPos==0 ): CMS_lumi.relPosX = 0.05

 H_ref = 600 
 W_ref = 600 
 W = W_ref
 H  = H_ref

 iPeriod = 0
 iPeriod = 4
 # references for T, B, L, R
 T = 0.08*H_ref
 B = 0.12*H_ref 
 L = 0.12*W_ref
 R = 0.04*W_ref

 pad = ROOT.TPad(name, name, 0, 0.3, 1, 1.0)
 pad.SetFillColor(0)
 pad.SetBorderMode(0)
 pad.SetFrameFillStyle(0)
 pad.SetFrameBorderMode(0)
 #pad.SetLeftMargin( L/W )
 #pad.SetRightMargin( R/W )
 pad.SetTopMargin( T/H )
 #pad.SetBottomMargin( B/H )
 pad.SetTickx(0)
 pad.SetTicky(0)
 
 return pad    
def plot(dir,data,qcd,herwig,madgraph,mcs,sigs,legDat,legqcd,legMCs,legSigs,postfix,luminosity):
  
  histnames = []
  fdata = ROOT.TFile.Open ( dir + data ,'READ')   
  
  for hist in fdata.GetListOfKeys():
    histnames.append(hist.GetName()) 
  fdata.Close()   
  # histnames = ["LPLP_Jet_1_softdrop_mass" ,"LPLP_Jet_2_softdrop_mass" ,"LPLP_Dijet_invariant_mass"]
  
  fmcs = []
  fsigs = []
 
  #Open files
  for f in mcs : 
    fmc   = ROOT.TFile.Open ( dir + f   ,'READ'); 
    fmcs.append(fmc)   
    print "opened file " ,fmc.GetName()
  for f in sigs: 
    fsig  = ROOT.TFile.Open ( dir + f   ,'READ'); 
    fsigs.append(fsig)    
  
  # histnames=["looseSel_Leading_jet_softdrop_mass"]
  for h in histnames:
    # if not h.find("looseSel")!=-1: continue
    hmcs  = []
    hsigs = []
    print "Histogram: ", h
    histname = h.replace("Leading_jet","Jet_1").replace("Second_leading_jet","Jet_2")
    
    for fmc in fmcs: 
      htmp  = fmc.Get(h);
      print htmp.GetName()
      hmc = copy.deepcopy(htmp)
      hmc.Sumw2()
      hmc .SetName(fmc .GetName()+"_"+histname+"_hmc") ; 
      hmc .Scale(luminosity)
      if fmc .GetName().find("WJetsToQQ_HT800toInf")!=-1: 
        print "Sample is WJets!! Scale by " ,float(0.205066345) #clemens 10.2/98.4
        hmc .Scale(float(0.205066345))
      if fmc .GetName().find("ZJetsToQQ_HT800toInf")!=-1: 
        print "Sample is ZJets!! Scale by " ,float(0.09811023622) #clemens:18.54/41.34
        hmc .Scale( float(0.09811023622))
      hmcs.append(hmc)

    for i,fsig in enumerate(fsigs ): 
      htmp = fsig.Get(histname);
      hsig = copy.deepcopy(htmp)
      hsig.Sumw2()
      hsig.SetName(fsig.GetName()+"_"+histname+"_hsig"); 
      hsig.Scale(float(lumi)) ; 
      hsigs.append(hsig);

    fdata = ROOT.TFile.Open ( dir + data ,'READ')
    hdata = copy.deepcopy(fdata.Get(h))
    hdata .SetName(histname+"hdata")
    hdata.SetBinErrorOption(rt.TH1.kPoisson)

    
    fqcd  = ROOT.TFile.Open ( dir + qcd ,'READ')   
    hqcd = copy.deepcopy(fqcd.Get(histname))
    hqcd .SetName(histname+"hqcd")
    hqcd.Sumw2()
    
    fherwig  = ROOT.TFile.Open ( dir + herwig ,'READ')   
    hherwig = copy.deepcopy(fherwig.Get(histname))
    hherwig .SetName(histname+"hherwig")
    hherwig.Sumw2()
    
    fmg  = ROOT.TFile.Open ( dir + madgraph ,'READ')   
    hmg = copy.deepcopy(fmg.Get(histname))
    hmg .SetName(histname+"hmg")
    hmg.Sumw2()
    
   
    hqcd.Scale(luminosity)
    hherwig.Scale(luminosity)
    hmg.Scale(luminosity)
    
    hqcd.SetFillColor(36)
    c = [ROOT.kMagenta+2,ROOT.kOrange+7,ROOT.kGreen+2]
    s = [1,2,4]
    for i,h in enumerate (hsigs):
      h.Scale(0.3*(hdata.Integral()/h.Integral()))
      h.SetLineColor(c[i]);
      h.SetLineStyle(s[i]);
      h.SetFillColor(0)

    c = [629,21,47]
    for i,h in enumerate(hmcs): 
        h.SetFillColor(c[i])
    
    canvas, legend = getCanvas(histname)
    canvas.Range(0,0,1,1)

    # ratio pad
    c1_1 = GetRatioPad()
    canvas.cd()

    #main pad
    c1_2 = GetMainPad()
 
    logY = 0
    if histname.find("_p_T")!=-1: 
        logY=1
        for h in hsigs: 
            h.Scale(0.00001)
    if histname.find("Dijet")!=-1: 
      logY=1
      hqcd.Rebin(100)
      hherwig.Rebin(100)
      hmg.Rebin(100)
      hdata.Rebin(100)
      for h in hmcs: 
          h.Rebin(100)
      for h in hsigs: 
          h.Scale(0.00001)
          h.Rebin(100)
      # if histname.find("Dijet")!=-1:
 #           #hmc =  hmc.Rebin(len(xbins)-1 ,"hmc_rebinned",xbins)
 #           #for h in hsigs: h.Rebin(2).Rebin(len(xbins)-1,"hsig_rebinned",xbins)
 #           #hdata= hdata.Rebin(len(xbins)-1,"hdata_rebinned",xbins)
 #         for h in hsigs: h.Rebin(2)
 #         hdata.GetYaxis().SetTitle("Events / 200 GeV")
    elif histname.find("softdrop")!=-1:
        hqcd.Rebin(2)
        hherwig.Rebin(2)
        hmg.Rebin(2)
        hdata.Rebin(2)
        for h in hsigs: h.Rebin(2)
        for h in hmcs: h.Rebin(2)
    else:
        print "No rebinning needed!"
    minorbkgs = 0.
    for h in hmcs: 
      minorbkgs += h.Integral()
    SF = float(((hdata.Integral()-minorbkgs)/hqcd.Integral()))
    print "QCD scalefactor = ", SF
    hqcd.Scale(SF)
    SF2 = float(((hdata.Integral()-minorbkgs)/hherwig.Integral()))
    print "QCD scalefactor Herwig = ", SF2
    hherwig.Scale(SF2)
    SF3 = float(((hdata.Integral()-minorbkgs)/hmg.Integral()))
    print "QCD scalefactor madGraph= ", SF3
    hmg.Scale(SF3)
    c1_2.cd()
    
    hdata.GetXaxis().SetLabelSize(0.)
    hdata.GetXaxis().SetTitleSize(0.)
   
    hdata.Draw("EP")
    hmcs.reverse()
    htot = copy.deepcopy(hqcd)
    htotherwig = copy.deepcopy(hherwig)
    htotmg = copy.deepcopy(hmg)
    ths1 = ROOT.THStack ("test1","test1")
    for hh in hmcs:
        ths1.Add(hh)
        htot.Add(hh)
        htotherwig.Add(hh)
        htotmg.Add(hh)
    htot.Sumw2()
    htotherwig.Sumw2()
    htotmg.Sumw2()
    htotherwig.SetLineStyle(9)
    htotmg.SetLineStyle(2)
    htotherwig.SetFillColorAlpha(0, 0.00)
    htotmg.SetFillColorAlpha(0, 0.00)
    
    legend.AddEntry(hdata ,legDat,"LEP")
    legend.AddEntry(hqcd        ,"QCD Pythia8","F")   
    legend.AddEntry(htotherwig    ,"         Herwig++","L")
    legend.AddEntry(htotmg        ,"         MadGraph+Pythia8","L")
    
    for h,leg in zip(hmcs,legMCs)  : legend.AddEntry(h,leg,"F")
    for h,leg in zip(hsigs,legSigs): legend.AddEntry(h,leg,"L")
    
    
    ths1.Add(hqcd)
    ths1.Draw("HISTsame")
    for h in hsigs: 
      h.Draw("HISTCSAME")
    htot.SetMarkerSize(0)
    htot.SetFillColor(rt.kBlack)
    htot.SetFillStyle(3013)
    htot.SetLineColor(rt.kBlack)
    htot.Draw("E2same")
    htotherwig.Draw("HIST same")
    htotmg.Draw("HIST same")
    hdata.Draw("EPSAME")
    maxY = hdata.GetMaximum()*2.0
    if histname.find("Deltaeta")!=-1 or  histname.find("phi")!=-1:  maxY = hdata.GetMaximum()*3.0
    hdata.GetYaxis().SetRangeUser(0.0,maxY)
    hdata.GetYaxis().SetTitleSize(0.04)
    xtitle = hdata.GetXaxis().GetTitle().replace("Leading jet","Jet 1").replace("Second leading jet","Jet 2")
    hdata.GetXaxis().SetTitle(xtitle)
    if logY:
      c1_2.SetLogy()
      maxY = maxY*100
      hdata.GetYaxis().SetRangeUser(0.1,maxY)

    
    legend.Draw()
    if luminosity==35900.: cmslabel_prelim(c1_2,'2016',11)
    else : cmslabel_prelim(c1_2,'2017',11)
    canvas.Update()
    
    c1_1.cd()
    hsum = hqcd.Clone("qcdhist%i" %random.randint(0,10000))
    hsumH  = htotherwig.Clone("herwigtot%i" %random.randint(0,10000))
    hsumMG = htotmg.Clone("mgtot%i" %random.randint(0,10000))
    for h in hmcs: 
      hsum.Add(h)
    ratiohist = hdata.Clone("ratiohist%i" %random.randint(0,10000))
    ratiohistMG = hdata.Clone("MG_ratiohist%i" %random.randint(0,10000))
    ratiohistHW = hdata.Clone("H_ratiohist%i" %random.randint(0,10000))
    ratiohist.Divide(hsum)
    ratiohistMG.Divide(hsumMG)
    ratiohistHW.Divide(hsumH)
    ratiohistHW.SetLineStyle(9)
    ratiohistMG.SetLineStyle(2)
    ratiohistHW.SetFillColorAlpha(0, 0.00)
    ratiohistMG.SetFillColorAlpha(0, 0.00)
    ratiohist.SetMarkerColor(1)
    # ratiohist.SetLineColor(1)
    ratiohist.SetMarkerSize(1)
    ratiohist.GetXaxis().SetLabelSize(0.14)
    ratiohist.GetXaxis().SetTitleSize(0.17)
    ratiohist.GetXaxis().SetTitleOffset(0.)
    ratiohist.GetYaxis().SetLabelSize(0.14)
    ratiohist.GetYaxis().SetTitleSize(0.16)
    ratiohist.GetYaxis().SetTitleOffset(0.2)
    ratiohist.GetYaxis().CenterTitle()
    ratiohist.GetYaxis().SetTitle("Data/MC")
    ratiohist.GetXaxis().SetTitle(xtitle)
    ratiohist.GetYaxis().SetRangeUser(0.2,1.8)
    ratiohist.SetNdivisions(505,"x")
    ratiohist.SetNdivisions(105,"y")
    ratiohist.Draw("")
    ratiohist.GetXaxis().SetTitleOffset(0.98)
    canvas.Update()
    MCunc = getMCunc(hsum)
    MCunc.Draw("3same")
    ratiohistHW.Draw("HISTsame")
    ratiohistMG.Draw("HISTsame")
    ratiohist.Draw("same")
    canvas.Update()
    c1_2.RedrawAxis()
    oname = directory+"/"+canvas.GetName()+postfix
    canvas.SaveAs(oname+".pdf")
    canvas.SaveAs(oname+".png")
    canvas.SaveAs(oname+".C")
    f = ROOT.TFile(oname+".root","RECREATE")
    f.cd()
    for h in hsigs:
      h.Write(h.GetName().split("/")[1].split("_")[2])
    for h in hmcs:
      h.Write(h.GetName().split("/")[1].split("_")[2])
    hqcd.Write("hqcd")
    hdata.Write("hdata")
    htotherwig.Write("hherwig")
    htotmg.Write("hmg")
    
    f.Write()
    f.Close()
    
    
    
    # sleep(100)
    
    

def plotMC(dir,qcd,mcs,sigs,legqcd,legMCs,legSigs,postfix):
  
  histnames = []
  fdata = ROOT.TFile.Open ( dir + qcd ,'READ')   
  
  for hist in fdata.GetListOfKeys():
    histnames.append(hist.GetName()) 
  fdata.Close()   
  # histnames = ["LPLP_Jet_1_softdrop_mass" ,"LPLP_Jet_2_softdrop_mass" ,"LPLP_Dijet_invariant_mass"]
  # histnames = ["looseSel_Jet_1_p_T"]
  
  fmcs = []
  fsigs = []
 
  #Open files
  for f in mcs : 
    fmc   = ROOT.TFile.Open ( dir + f   ,'READ'); 
    fmcs.append(fmc)   
    print "opened file " ,fmc.GetName()
  for f in sigs: 
    fsig  = ROOT.TFile.Open ( dir + f   ,'READ'); 
    fsigs.append(fsig)    
  
  # histnames=["looseSel_Leading_jet_softdrop_mass"]
  for h in histnames:
    # if not h.find("looseSel")!=-1: continue
    hmcs  = []
    hsigs = []
    print "Histogram: ", h
    histname = h.replace("Leading_jet","Jet_1").replace("Second_leading_jet","Jet_2")
    for fmc in fmcs: 
      htmp  = fmc.Get(histname);
      print htmp.GetName()
      hmc = copy.deepcopy(htmp)
      hmc.Sumw2()
      hmc .SetName(fmc .GetName()+"_"+histname+"_hmc") ; 
      hmc .Scale(lumi)
      if fmc .GetName().find("WJetsToQQ_HT800toInf")!=-1: 
        print "Sample is WJets!! Scale by " ,float(0.205066345) #clemens 10.2/98.4
        hmc .Scale(float(0.205066345))
      if fmc .GetName().find("ZJetsToQQ_HT800toInf")!=-1: 
        print "Sample is ZJets!! Scale by " ,float(0.09811023622) #clemens:18.54/41.34
        hmc .Scale( float(0.09811023622))
      hmcs.append(hmc)
      
    for i,fsig in enumerate(fsigs ): 
      htmp = fsig.Get(histname);
      hsig = copy.deepcopy(htmp)
      hsig.Sumw2()
      hsig.SetName(fsig.GetName()+"_"+histname+"_hsig"); 
      hsig.Scale(float(lumi)) ; 
      hsigs.append(hsig);
      
    fqcd  = ROOT.TFile.Open ( dir + qcd ,'READ')   
    hqcd = copy.deepcopy(fqcd.Get(histname))
    hqcd .SetName(histname+"hqcd")
    hqcd.Sumw2()
   
    hqcd.Scale(lumi)
    # if fqcd .GetName().find("Flat")!=-1:
 #      print "Sample is pt-flat!! Scale by " ,float(309800000.0)
 #      hqcd .Scale( float(309800000.0))
      
    minorbkgs = 0.
    for h in hmcs: 
      minorbkgs += h.Integral()
    SF = 1
    print "QCD scalefactor = ", SF
    hqcd.Scale(SF)
    hqcd.SetFillColor(36)
    c = [ROOT.kMagenta+2,ROOT.kOrange+7,ROOT.kGreen+2]
    s = [1,2,9]*3
    for i,h in enumerate (hsigs):
      h.Scale(0.3*(hqcd.Integral()/h.Integral()))
      h.SetLineColor(c[i]);
      h.SetLineStyle(s[i]);
      h.SetFillColor(0)

    c = [629,21,47]*3
    for i,h in enumerate(hmcs): h.SetFillColor(c[i])
    
    canvas, legend = getCanvas(histname)
    canvas.Range(0,0,1,1)

    # ratio pad
    c1_1 = GetRatioPad()
    canvas.cd()

    #main pad
    c1_2 = GetMainPad()
 
    logY = 0
    if histname.find("Dijet")!=-1 or histname.find("_p_T")!=-1: 
      logY=1
      for h in hsigs: h.Scale(0.0002)
    legend.AddEntry(hqcd  ,legqcd,"F")
    for h,leg in zip(hmcs,legMCs)  : legend.AddEntry(h,leg,"F")
    for h,leg in zip(hsigs,legSigs): legend.AddEntry(h,leg,"L")
    c1_2.cd()
    
    hqcd.GetXaxis().SetLabelSize(0.)
    hqcd.GetXaxis().SetTitleSize(0.)
    hsum = hqcd.Clone("qcdhist%i" %random.randint(0,10000))
    hsum.Sumw2()
    for h in hmcs: 
      hsum.Add(h)
      
    hqcd.Draw("HIST")
   
    hmcs.reverse()
    ths1 = ROOT.THStack ("test1","test1")
    for hh in hmcs:
        ths1.Add(hh)
    ths1.Add(hqcd)
    ths1.Draw("HISTsame")
    hsum.SetMarkerSize(0)
    hsum.SetFillColor(rt.kBlack)
    hsum.SetFillStyle(3013)
    hsum.SetLineColor(rt.kBlack)
    hsum.Draw("E2same")
    for h in hsigs: 
      h.Draw("HISTCSAME")
    maxY = hqcd.GetMaximum()*1.6
    hqcd.GetYaxis().SetRangeUser(0.0,maxY)
    hqcd.GetYaxis().SetTitleSize(0.04)
    xtitle = hqcd.GetXaxis().GetTitle().replace("Leading jet","Jet 1").replace("Second leading jet","Jet 2")
    hqcd.GetXaxis().SetTitle(xtitle)
    if logY:
      c1_2.SetLogy()
      maxY = maxY*100
      hqcd.GetYaxis().SetRangeUser(0.1,maxY)

    
    legend.Draw()

    cmslabel_prelim(c1_2,'2017',11)
    canvas.Update()
    
    c1_1.cd()
   
    ratiohist  = getMCunc(hsum)

    hdraw = hsum.Clone("sumclone")
    hdraw.Divide(hdraw)
    hdraw.SetMarkerColor(0)
    hdraw.SetLineColor(0)
    hdraw.SetMarkerSize(0)
    hdraw.GetXaxis().SetLabelSize(0.14)
    hdraw.GetXaxis().SetTitleSize(0.17)
    hdraw.GetXaxis().SetTitleOffset(0.)
    hdraw.GetYaxis().SetLabelSize(0.14)
    hdraw.GetYaxis().SetTitleSize(0.16)
    hdraw.GetYaxis().SetTitleOffset(0.2)
    hdraw.GetYaxis().CenterTitle()
    hdraw.GetYaxis().SetTitle("MC unc.")
    hdraw.GetXaxis().SetTitle(xtitle)
    hdraw.GetYaxis().SetRangeUser(0.7,1.3)
    # hdraw.GetXaxis().SetRangeUser(hqcd.GetXaxis().GetXmin(),hqcd.GetXaxis().GetXmax())
    hdraw.SetNdivisions(505,"x")
    hdraw.SetNdivisions(105,"y")
    hdraw.Draw("")
    
    ratiohist.Draw("3same")
    hdraw.GetXaxis().SetTitleOffset(0.98)
    canvas.Update()
    canvas.Update()
    c1_2.RedrawAxis()
    oname = directory+"/"+canvas.GetName()+postfix
    canvas.SaveAs(oname+"_MC.pdf")
    canvas.SaveAs(oname+"_MC.png")
    canvas.SaveAs(oname+"_MC.C")
    del ratiohist,hsum,hqcd,hsigs

def plotTrigWeight(dir,datafile,qcdfiles,signalfiles, qcdleg,signallegs):
     rb =2
     allHists = []
     histnames = []
     fdata = ROOT.TFile.Open ( dir + datafile ,'READ')   
  
     for hist in fdata.GetListOfKeys():
       histnames.append(hist.GetName()) 
     fdata.Close()   
     histnames =["looseSel_Dijet_invariant_mass"] 
     histnames =['looseSel_Jet_1_softdrop_mass']
     fmcs = []
     fsigs = []
 
     #Open files
     for f in qcdfiles : 
       fmc   = ROOT.TFile.Open ( dir + f   ,'READ'); 
       fmc.SetName(f)
       fmcs.append(fmc)   
       print "opened file " ,fmc.GetName()
     for f in signalfiles: 
       fsig  = ROOT.TFile.Open ( dir + f   ,'READ'); 
       fsigs.append(fsig)    
  
     for h in histnames:
       hmcs  = []
       hsigs = []
       print "Histogram: ", h
       for fmc in fmcs: 
         histname = h
         htmp  = fmc.Get(histname);
         print htmp.GetName()
         hmc = copy.deepcopy(htmp)
         hmc.Sumw2()
         hmc .SetName(fmc .GetName()+"_"+histname+"_hmc") ; 
         hmc .Scale(lumi)
         hmcs.append(hmc)
      
       for i,fsig in enumerate(fsigs ): 
         htmp = fsig.Get(histname);
         hsig = copy.deepcopy(htmp)
         hsig.Sumw2()
         hsig.SetName(fsig.GetName()+"_"+histname+"_hsig"); 
         hsig.Scale(float(lumi)) ; 
         hsigs.append(hsig);
      
       
       fdata = ROOT.TFile.Open ( dir + datafile ,'READ')
       hdata = copy.deepcopy(fdata.Get(h))
       hdata .SetName(histname+"hdata")
       hdata.SetBinErrorOption(rt.TH1.kPoisson)
       hdata.SetFillColorAlpha(0, 0.00);
       allHists.append(hdata)

       l = [2,1]
       minorbkgs = 0.
       for h in hmcs: 
           print "For " ,h.GetName()
           SF = hdata.Integral()/h.Integral()
           
           print "Using SF = " ,SF
           SF=1.
           h.Scale(SF)
           h.SetLineColor(1)
           h.SetFillColorAlpha(0, 0.00);
           h.SetLineStyle(l[i])
           allHists.append(h)

       for i,h in enumerate (hsigs):
         h.Scale(0.3*(hmcs[0].Integral()/h.Integral()))
         h.SetLineColor(rt.kRed);
         h.SetFillColorAlpha(0, 0.00);
         h.SetFillColor(0)
         h.SetLineStyle(l[i])
         allHists.append(h)

    
       canvas, legend = getCanvas(histname)
       legend2 = getLegend()
       canvas.Range(0,0,1,1)

       # ratio pad
       c1_1 = GetRatioPad()
       canvas.cd()

       #main pad
       c1_2 = GetMainPad()
 
       
       logY = 0
       # if histname.find("Dijet")!=-1 or histname.find("_p_T")!=-1:
 #         logY=1
 #
 #         for h in hsigs:
 #             h.Scale(0.0002)
 #         for h in hmcs:
 #             h = h.Rebin(len(xbins)-1 ,"hmc_rebinned",xbins)
 #         hdata = hdata.Rebin(len(xbins)-1,"hdata_rebinned",xbins)
       # else:
       # for h in allHists:
       #     h.Rebin(2)
          
       legend.AddEntry(hdata     ,"Data","LEP")
       legend.AddEntry(hmcs[1]   ,qcdleg,"L")
       legend.AddEntry(hsigs[1]  ,signallegs[0],"L")
       
       
       
       c1_2.cd()
    
       hdata.GetXaxis().SetLabelSize(0.)
       hdata.GetXaxis().SetTitleSize(0.)
       
       if histname.find("Dijet")!=-1 : hdataDR = hdata.Rebin(len(xbins)-1 ,"hdata_rebinned",xbins)
       else: hdataDR = hdata.Rebin(rb)
       hdataDR.Draw("EC")
       hmcsRebinned = []
       hsigsRebinned = []
       for i,h in enumerate(hmcs):
           if histname.find("Dijet")!=-1 : hDR = h.Rebin(len(xbins)-1 ,"hmc_rebinned_%s"%h.GetName(),xbins)
           else: hDR = h.Rebin(rb)
           hDR.SetLineStyle(l[i])
           hDR.Draw("hist same")
           hmcsRebinned.append(hDR)
           # h.Rebin(rb)
           # h.Draw("E2same")
       for i,h in enumerate(hsigs): 
         if histname.find("Dijet")!=-1 : hSDR = h.Rebin(len(xbins)-1 ,"hms_rebinned_%s"%h.GetName(),xbins)
         else: hSDR = h.Rebin(rb)
         hSDR.Draw("HISTSAME")
         hDR.SetLineStyle(l[i])
         hsigsRebinned.append(hDR)
         # h.Rebin(rb)
       maxY = hdataDR.GetMaximum()*2.2
       hdataDR.GetYaxis().SetRangeUser(0.0,maxY)
       hdataDR.GetYaxis().SetTitleSize(0.04)
       hdataDR.GetYaxis().SetTitle("Events")
       xtitle = hdataDR.GetXaxis().GetTitle().replace("Leading jet","Jet 1").replace("Second leading jet","Jet 2")
       if histname.find("softdrop")!=-1 : xtitle= "m_{jet1}"
       hdataDR.GetXaxis().SetTitle(xtitle)
       if logY:
         c1_2.SetLogy()
         maxY = maxY*10000
         hdataDR.GetYaxis().SetRangeUser(0.1,maxY)

    
       legend.Draw()
       legend2.AddEntry(hmcsRebinned[1]   ,"With weight","L")
       legend2.AddEntry(hmcsRebinned[0]   ,"No weight","L")
       legend2.Draw("same")

       cmslabel_prelim(c1_2,'2017',11)
       canvas.Update()
    
       c1_1.cd()
       ratios = []
       for i,hsum in enumerate(hmcsRebinned): 
        c1_1.cd()  
        ratiohist = hdataDR.Clone("ratiohist%i"%i)     
        ratiohist.Divide(hsum)
        ratiohist.SetLineStyle(l[i])
        ratiohist.SetMarkerSize(1)
        ratiohist.SetFillColorAlpha(0, 0.0);
        ratios.append(ratiohist)

       ratios[0].GetXaxis().SetLabelSize(0.14)
       ratios[0].GetXaxis().SetTitleSize(0.17)
       ratios[0].GetXaxis().SetTitleOffset(0.)
       ratios[0].GetYaxis().SetLabelSize(0.14)
       ratios[0].GetYaxis().SetTitleSize(0.16)
       ratios[0].GetYaxis().SetTitleOffset(0.2)
       ratios[0].GetYaxis().CenterTitle()
       ratios[0].GetYaxis().SetTitle("Data/MC")
       ratios[0].GetXaxis().SetTitle(xtitle)
       ratios[0].GetYaxis().SetRangeUser(0.2,1.8)
       ratios[0].SetNdivisions(505,"x")
       ratios[0].SetNdivisions(105,"y")
       ratios[0].Draw("HIST")
       ratios[0].GetXaxis().SetTitleOffset(0.98)
       ratios[1].Draw("HISTsame")
       canvas.Update()
       
       oname = dir+"trigWeightCompare_"+histname
       canvas.SaveAs(oname+".pdf")
       canvas.SaveAs(oname+".png")
       canvas.SaveAs(oname+".C")
       canvas.SaveAs(oname+".root")
       del ratiohist,hmcs,hsigs
       
def plotCombo(file,postfix="TOTAL"):
    # f = ROOT.TFile.Open (out_directory+file ,'READ')
    f = ROOT.TFile.Open ("resCP17_MG/"+file ,'READ')
    hZJets        = f.Get("ZJetsToQQ")                                         ;hZJets        .SetName("hZJets" ); hZJets.SetFillColor(ROOT.kRed-6)
    hWJets        = f.Get("WJetsToQQ")                                         ;hWJets        .SetName("hWJets" ); hWJets.SetFillColor(ROOT.kCyan+2)
    hTT           = f.Get("TTHad")                                             ;hTT           .SetName("hTT" ); hTT.SetFillColor(414)
    hqcd          = f.Get("hqcd")                                              ;hqcd           .SetName("hqcd" )
    hherwig       = f.Get("hherwig")                                           ;hherwig      .SetName("hherwig" )
    hmg           = f.Get("hmg")                                               ;hmg          .SetName("hmg" )
    hdata         = f.Get("hdata")                                             ;hdata        .SetName("hdata" )
    hWprime       = f.Get("WprimeToWZToWhadZhad")  ; hWprime       .Scale(0.1*hdata.Integral()/hWprime       .Integral());hWprime       .SetName("hWprime" )      ;hWprime      .SetLineStyle(1);
    hBulkGravToWW = f.Get("BulkGravToWW")          ; hBulkGravToWW .Scale(0.1*hdata.Integral()/hBulkGravToWW .Integral());hBulkGravToWW .SetName("hBulkGravToWW" );hBulkGravToWW.SetLineStyle(1);
    hBulkGravToZZ = f.Get("BulkGravToZZ")          ; hBulkGravToZZ .Scale(0.1*hdata.Integral()/hBulkGravToZZ .Integral());hBulkGravToZZ .SetName("hBulkGravToZZ" );hBulkGravToZZ.SetLineStyle(1);hBulkGravToZZ.SetLineColor(ROOT.kTeal)
    hmg    .SetLineStyle(2)
    hherwig.SetLineStyle(3)
    
    legend = ROOT.TLegend(0.3865772,0.5781119,0.972953,0.8951049,"","brNDC")
    # legend = ROOT.TLegend(0.52,0.65,0.92,0.9,"","brNDC")
    legend.SetBorderSize(0)
    legend.SetLineColor(1)
    legend.SetLineStyle(1)
    legend.SetLineWidth(1)
    legend.SetFillColor(0)
    legend.SetFillStyle(0)
    legend.SetTextFont(42)
 
    pt = ROOT.TPaveText(0.7224832,0.3256993,0.9731544,0.4743007,"NDC")
    # pt.SetTextFont(72)
    pt.SetTextSize(0.04)
    pt.SetTextAlign(12)
    pt.SetFillColor(0)
    pt.SetBorderSize(0)
    pt.SetFillStyle(0)
    c = ROOT.TCanvas('c')
    pad1 = get_pad("pad1") #ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0.01)    
    pad1.SetTopMargin(0.1) 
    pad1.Draw()
    pad1.cd()	 

    logY = 0
    ytitleex = "5 GeV"
    if f.GetName().find("Dijet")!=-1 or f.GetName().find("_p_T")!=-1:
        logY=1
        ytitleex = "100 GeV"
    
    
       
    hdata.GetXaxis().SetLabelSize(0.)
    hdata.GetXaxis().SetTitleSize(0.)
    if file.find("DDT")!=-1:
        ytitleex = "0.05"
        hdata.GetXaxis().SetRangeUser(0.20,1.4)
        hWprime       .Scale(2)
        hBulkGravToWW .Scale(2)
        hBulkGravToZZ .Scale(2)
    hdata.SetLineWidth(2)
    hdata.GetYaxis().SetTitleOffset(1.3)
    
    hdata.GetYaxis().SetTitle("Events / %s"%ytitleex)
    hdata.GetYaxis().SetTitleSize(0.06)
    hdata.GetYaxis().SetLabelSize(0.06)
    hdata.GetYaxis().SetNdivisions(509);
    if f.GetName().find("Dijet")!=-1 or f.GetName().find("_p_T")!=-1:hdata.GetYaxis().SetNdivisions(505);
    hdata.Draw("EP")
    htot = copy.deepcopy(hqcd)
    ths1 = ROOT.THStack ("stack","ctack")

    ths1.Add(hTT   ) ; htot.Add(hTT   );
    ths1.Add(hZJets) ; htot.Add(hZJets);
    ths1.Add(hWJets) ; htot.Add(hWJets);
    ths1.Add(hqcd)
    ths1.Draw("HISTsame")
    
    hBulkGravToZZ.Draw("HIST SAME")
    hBulkGravToWW.Draw("HIST SAME")
    hWprime      .Draw("HIST SAME")
    hherwig.SetFillColorAlpha(0, 0.00)
    hmg.SetFillColorAlpha(0, 0.00)
    hherwig.Draw("HIST same")
    hmg.Draw("HIST same")

    htot.SetMarkerSize(0)
    htot.SetFillColor(rt.kBlack)
    htot.SetFillStyle(3013)
    htot.SetLineColor(rt.kBlack)
    htot.Draw("E2same")
    hdata.Draw("EPSAME")
    maxY = hdata.GetMaximum()*2.0
    if f.GetName().find("Deltaeta")!=-1 or  f.GetName().find("phi")!=-1:  maxY = hqcd.GetMaximum()*3.0
    # hdata.GetYaxis().SetRangeUser(0.0,maxY)
    # hdata.GetYaxis().SetTitleSize(0.04)
    # hdata.GetYaxis().SetTitle("Events")
    xtitle = hdata.GetXaxis().GetTitle().replace("Leading jet","Jet 1").replace("Second leading jet","Jet 2")
    if f.GetName().find("softdrop")!=-1 : xtitle= "m_{jet1} [GeV]"
    hdata.GetXaxis().SetTitle(xtitle)
    if logY:
      pad1.SetLogy()
      maxY = maxY*20
      hdata.GetYaxis().SetRangeUser(0.2,maxY)
      hWprime       .Scale(0.00005)
      hBulkGravToWW .Scale(0.00005)
      hBulkGravToZZ .Scale(0.00005)
    hdata.GetYaxis().SetRangeUser(0.02,maxY)
    
    legend.Draw()
    pt.AddText("m_{jj} > 1126 GeV")
    pt.AddText("|#Delta#eta_{jj}| < 1.3")
    pt.AddText("55 < m_{jet} < 215 GeV")
    pt.Draw()
    CMS_lumi.CMS_lumi(pad1, 4, 11)
        
    pad1.Modified()
    pad1.Update()
    
    c.Update()
    c.cd()
    pad2 = ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
    pad2.SetTopMargin(0.01)
    pad2.SetBottomMargin(0.4)
    pad2.SetGridy()
    pad2.Draw()
    pad2.cd()
    
    # ratio pad
    hsum = htot.Clone("tot%i" %random.randint(0,10000))
    hsumH  = hherwig.Clone("herwigtot%i" %random.randint(0,10000))
    hsumMG = hmg.Clone("mgtot%i" %random.randint(0,10000))
    ratiohist = hdata.Clone("ratiohist%i" %random.randint(0,10000))
    ratiohist.Divide(hsum)
    
    ratiohistMG = hdata.Clone("MG_ratiohist%i" %random.randint(0,10000))
    ratiohistHW = hdata.Clone("H_ratiohist%i" %random.randint(0,10000))
    ratiohistMG.Divide(hsumMG)
    ratiohistHW.Divide(hsumH)
    ratiohistHW.SetLineStyle(3)
    ratiohistMG.SetLineStyle(2)
    ratiohistHW.SetFillColorAlpha(0, 0.00)
    ratiohistMG.SetFillColorAlpha(0, 0.00)
    ratiohist.SetDirectory(0);
    ratiohist.SetStats(0);
    ratiohist.GetXaxis().SetLabelFont(42);
    ratiohist.GetXaxis().SetLabelOffset(0.02);
    ratiohist.GetXaxis().SetLabelSize(0.15);
    ratiohist.GetXaxis().SetTitleSize(0.15);
    ratiohist.GetXaxis().SetTitleOffset(1);
    ratiohist.GetXaxis().SetTitleFont(42);
    ratiohist.GetYaxis().SetTitle("#frac{Data}{Simulation}");
    ratiohist.GetYaxis().CenterTitle(True);
    ratiohist.GetYaxis().SetNdivisions(205);
    ratiohist.GetYaxis().SetLabelFont(42);
    ratiohist.GetYaxis().SetLabelOffset(0.007);
    ratiohist.GetYaxis().SetLabelSize(0.15);
    ratiohist.GetYaxis().SetTitleSize(0.14);
    ratiohist.GetYaxis().SetTitleOffset(0.5);
    ratiohist.GetYaxis().SetTitleFont(42);
    ratiohist.GetXaxis().SetNdivisions(505)   
    if file.find("DDT")!=-1: ratiohist.GetXaxis().SetNdivisions(908)  
    ratiohist.SetMarkerColor(1)
    # # ratiohist.SetLineColor(1)
    # ratiohist.SetMarkerSize(1)
    # ratiohist.GetXaxis().SetLabelSize(0.14)
    # ratiohist.GetXaxis().SetTitleSize(0.17)
    # ratiohist.GetXaxis().SetTitleOffset(0.)
    # ratiohist.GetYaxis().SetLabelSize(0.14)
    # ratiohist.GetYaxis().SetTitleSize(0.16)
    # ratiohist.GetYaxis().SetTitleOffset(0.2)
    # ratiohist.GetYaxis().CenterTitle()
    # ratiohist.GetYaxis().SetTitle("Data/MC")
    ratiohist.GetXaxis().SetTitle(xtitle)
    ratiohist.GetYaxis().SetRangeUser(0.2,1.8)
    # ratiohist.SetNdivisions(505,"x")
 #    ratiohist.SetNdivisions(105,"y")
    ratiohist.Draw("")
    ratiohist.GetXaxis().SetTitleOffset(0.98)
    c.Update()
    MCunc = getMCunc(hsum)
    MCunc.SetLineColor(0)
    MCunc.Draw("3same")
    ratiohistHW.Draw("HISTsame")
    ratiohistMG.Draw("HISTsame")
    ratiohist.Draw("same")
    c.Update()
    pad1.RedrawAxis()
    
    
    pad1.cd()	
    legend.SetNColumns(2)
    legend.AddEntry(hqcd        ,"QCD Pythia8","F")   
    legend.AddEntry(hWJets        ,"W+jets","F")
    legend.AddEntry(hherwig     ,"QCD Herwig++","L")
    legend.AddEntry(hZJets        ,"Z+jets","F")
    legend.AddEntry(hmg         ,"QCD MG+Pythia8","L")
  
    legend.AddEntry(hTT           ,"t#bar{t}","F")
    legend.AddEntry(MCunc       ,"Stat. uncertainty","F")
    legend.AddEntry(hBulkGravToWW ,"G_{bulk} (2 TeV)#rightarrowWW","L")
    legend.AddEntry(hdata       ,"Data","LEP")
    legend.AddEntry(hBulkGravToZZ ,"G_{bulk} (2 TeV)#rightarrowZZ","L")
    legend.AddEntry(0       ,"","")
    legend.AddEntry(hWprime       ,"W' (2 TeV)#rightarrowWZ","L")
   
    
    oname = out_directory+"/"+postfix
    if prelim: oname = out_directory+"/"+postfix+"_prelim"
    c.SaveAs(oname+".pdf")
    c.SaveAs(oname+".png")
    c.SaveAs(oname+".C")
    c.SaveAs(oname+".root")
    # sleep(1000000)
        
       
if __name__ == '__main__':
  #2017 names
  BulkGravWWTemplate ="BulkGravToWW_narrow_M_2000."
  BulkGravZZTemplate ="BulkGravToZZ_narrow_M_2000."
  WprimeTemplate     ="WprimeToWZToWhadZhad_narrow_M_2000."
  
  # #2016 names
  # BulkGravWWTemplate ="BulkGravToWW_narrow_2000"
  # BulkGravZZTemplate ="BulkGravToZZToZhadZhad_narrow_2000"
  # WprimeTemplate     ="WprimeToWZToWhadZhad_narrow_2000"
  
  dataTemplate      ="JetHT"
  nonResTemplate    ="QCD"
  WJetsTemplate     ="WJetsToQQ"
  ZJetsTemplate     ="ZJetsToQQ"
  ttTemplate        ="TT"

  wait = True
  from modules.submitJobs import submitCPs
  template=','.join([dataTemplate])
  template=','.join([nonResTemplate,WJetsTemplate,ZJetsTemplate,ttTemplate,BulkGravWWTemplate,BulkGravZZTemplate,WprimeTemplate,dataTemplate])
  # template=','.join([nonResTemplate,BulkGravWWTemplate,BulkGravZZTemplate,WprimeTemplate,dataTemplate])
  # template=','.join([nonResTemplate,dataTemplate])
  template=','.join([dataTemplate])
  template=','.join(["QCD_HT1000to1500","QCD_HT1500to2000","QCD_HT2000toInf","QCD_HT700to1000"])
  pwd = os.getcwd()
  # samples = pwd +"/samples16/" #For 2016 CPs
  samples = pwd +"/samples/" #For 2017 CPs
  # samples = '/eos/cms/store/cmst3/group/exovv/VVtuple/VV3Dproduction/2017_JEC_V4/' #For 2017 CPs
  # samples = '/eos/cms/store/cmst3/group/exovv/VVtuple/VV3Dproduction/2017_JEC_V6/'
  # samples = '/eos/user/t/thaarres/2017_JECV6_PURew/'
  # samples = '/eos/cms/store/cmst3/group/exovv/VVtuple/VV3Dproduction/2017_JECV6_PURew_June2018'
  # samples = '/eos/cms/store/cmst3/group/exovv/VVtuple/VV3Dproduction/2017_JECV6_PURew_JER/'
  jobname = "CP17_MG"
  # submitCPs(samples,template,wait,jobname)
  # mergeCPs(template,jobname)
  dir = "res"+jobname+"/"
  # dir = "resHPmc/"
  # plot("resCP16_latest/","data.root" , "qcdpt.root","controlplots_2017_QCD_Pt-15to7000.root","qcdht.root",["controlplots_2017_TTHad_pow.root",'controlplots_2017_WJetsToQQ_HT800toInf_new.root','controlplots_2017_ZJetsToQQ_HT800toInf_new.root'] , ["controlplots_2017_WprimeToWZToWhadZhad_narrow_M_2000.root"  , "controlplots_2017_BulkGravToWW_narrow_M_2000.root" , "controlplots_2017_BulkGravToZZ_narrow_M_2000.root"],"Data (2016)" , "QCD Pythia8",["t#bar{t}","W+jets","Z+jets"] , ["W'(2 TeV)#rightarrowWZ" , "G_{Bulk}(2 TeV)#rightarrowWW" , "G_{Bulk}(2 TeV)#rightarrowZZ"],"_2016",35900.)
  # plot("resCP17_latest/","data.root" , "qcdpt.root","qcdherwig.root","qcdht.root",["controlplots_2017_TTHad_pow.root",'controlplots_2017_WJetsToQQ_HT800toInf_new.root','controlplots_2017_ZJetsToQQ_HT800toInf_new.root'] , ["controlplots_2017_WprimeToWZToWhadZhad_narrow_M_2000.root"  , "controlplots_2017_BulkGravToWW_narrow_M_2000.root" , "controlplots_2017_BulkGravToZZ_narrow_M_2000.root"],"Data (2017)" , "QCD Pythia8",["t#bar{t}","W+jets","Z+jets"] , ["W'(2 TeV)#rightarrowWZ" , "G_{Bulk}(2 TeV)#rightarrowWW" , "G_{Bulk}(2 TeV)#rightarrowZZ"],"_2017",41367.929231882)
  # plot(dir,"data.root" , "qcdpt.root",["controlplots_2017_TTHad_pow.root",'controlplots_2017_WJetsToQQ_HT800toInf.root','controlplots_2017_ZJetsToQQ_HT800toInf.root'] , ["controlplots_2017_WprimeToWZToWhadZhad_narrow_M_2000.root"  , "controlplots_2017_BulkGravToWW_narrow_M_2000.root" , "controlplots_2017_BulkGravToZZ_narrow_M_2000.root"],"Data (2017)" , "QCD Pythia8",["t#bar{t}","W+jets","Z+jets"] , ["W'(2 TeV)#rightarrowWZ" , "G_{Bulk}(2 TeV)#rightarrowWW" , "G_{Bulk}(2 TeV)#rightarrowZZ"],"_ptbinned")
  # plotMC(dir, "qcdht.root",["controlplots_2017_TTHad_pow.root",'controlplots_2017_WJetsToQQ_HT800toInf.root','controlplots_2017_ZJetsToQQ_HT800toInf.root'] , ["controlplots_2017_WprimeToWZToWhadZhad_narrow_M_2000.root"  , "controlplots_2017_BulkGravToWW_narrow_M_2000.root" , "controlplots_2017_BulkGravToZZ_narrow_M_2000.root"], "QCD MadGraph",["t#bar{t}","W+jets","Z+jets"] , ["W'(2 TeV)#rightarrowWZ" , "G_{Bulk}(2 TeV)#rightarrowWW" , "G_{Bulk}(2 TeV)#rightarrowZZ"],postfix="MadGraph")
  # plotMC(dir, "qcdpt.root",["controlplots_2017_TTHad_pow.root",'controlplots_2017_WJetsToQQ_HT800toInf.root','controlplots_2017_ZJetsToQQ_HT800toInf.root'] , ["controlplots_2017_WprimeToWZToWhadZhad_narrow_M_2000.root"  , "controlplots_2017_BulkGravToWW_narrow_M_2000.root" , "controlplots_2017_BulkGravToZZ_narrow_M_2000.root"], "QCD Pythia8",["t#bar{t}","W+jets","Z+jets"] , ["W'(2 TeV)#rightarrowWZ" , "G_{Bulk}(2 TeV)#rightarrowWW" , "G_{Bulk}(2 TeV)#rightarrowZZ"],postfix="Pythia8")
  # plotMC(dir, "controlplots_2017_QCD_Pt-15to7000_TuneCUETHS1_Flat.root",["controlplots_2017_TTHad_pow.root",'controlplots_2017_WJetsToQQ_HT800toInf.root','controlplots_2017_ZJetsToQQ_HT800toInf.root'] , ["controlplots_2017_WprimeToWZToWhadZhad_narrow_M_2000.root"  , "controlplots_2017_BulkGravToWW_narrow_M_2000.root" , "controlplots_2017_BulkGravToZZ_narrow_M_2000.root"], "QCD Herwig++",["t#bar{t}","W+jets","Z+jets"] , ["W'(2 TeV)#rightarrowWZ" , "G_{Bulk}(2 TeV)#rightarrowWW" , "G_{Bulk}(2 TeV)#rightarrowZZ"],postfix="Herwig")
  # plotTrigWeight("trigCompareSamples/","data.root",["qcdpt_noTW.root","qcdpt_tw.root"],["Wprime_noTW.root","Wprime_tw.root"], "QCD Pythia8",["W'(1 TeV)#rightarrowWZ"])
  # plotCombo("Dijet_invariant_mass.root","DijetInvMass")
  # plotCombo("Jet_1_softdrop_mass.root","SoftDropMass")
  #
  # os.system("hadd -f %slooseSel_Deltaeta.root              %slooseSel_Deltaeta_*.root            "%(directory,directory))
  # os.system("hadd -f %slooseSel_Dijet_invariant_mass.root  %slooseSel_Dijet_invariant_mass_*.root"%(directory,directory))
  # os.system("hadd -f %slooseSel_Jet_1_DDT.root             %slooseSel_Jet_1_DDT_*.root           "%(directory,directory))
  # os.system("hadd -f %slooseSel_Jet_1_softdrop_mass.root   %slooseSel_Jet_1_softdrop_mass_*.root "%(directory,directory))
 #  os.system("hadd -f %slooseSel_Jet_1_eta.root             %slooseSel_Jet_1_eta_*.root           "%(directory,directory))
 #  os.system("hadd -f %slooseSel_Jet_1_p_T.root             %slooseSel_Jet_1_p_T_*.root           "%(directory,directory))
 #  os.system("hadd -f %slooseSel_Jet_1_phi.root             %slooseSel_Jet_1_phi_*.root           "%(directory,directory))
  
 #  os.system("hadd -f %slooseSel_Jet_1_tau21.root           %slooseSel_Jet_1_tau21_*.root         "%(directory,directory))
 #  os.system("hadd -f %slooseSel_Jet_1_tau_1.root           %slooseSel_Jet_1_tau_1_*.root         "%(directory,directory))
 #  os.system("hadd -f %slooseSel_Jet_1_tau_2.root           %slooseSel_Jet_1_tau_2_*.root         "%(directory,directory))
 #  os.system("hadd -f %slooseSel_Jet_2_DDT.root             %slooseSel_Jet_2_DDT_*.root           "%(directory,directory))
 #  os.system("hadd -f %slooseSel_Jet_2_eta.root             %slooseSel_Jet_2_eta_*.root           "%(directory,directory))
 #  os.system("hadd -f %slooseSel_Jet_2_p_T.root             %slooseSel_Jet_2_p_T_*.root           "%(directory,directory))
 #  os.system("hadd -f %slooseSel_Jet_2_phi.root             %slooseSel_Jet_2_phi_*.root           "%(directory,directory))
 #  os.system("hadd -f %slooseSel_Jet_2_softdrop_mass.root   %slooseSel_Jet_2_softdrop_mass_*.root "%(directory,directory))
 #  os.system("hadd -f %slooseSel_Jet_2_tau21.root           %slooseSel_Jet_2_tau21_*.root         "%(directory,directory))
 #  os.system("hadd -f %slooseSel_Jet_2_tau_1.root           %slooseSel_Jet_2_tau_1_*.root         "%(directory,directory))
 #  os.system("hadd -f %slooseSel_Jet_2_tau_2.root           %slooseSel_Jet_2_tau_2_*.root         "%(directory,directory))
  # plotCombo("looseSel_Deltaeta.root"              , "looseSel_Deltaeta"               )
  plotCombo("looseSel_Dijet_invariant_mass.root"  , "looseSel_Dijet_invariant_mass"   )
  plotCombo("looseSel_Jet_1_DDT.root"             , "looseSel_Jet_1_DDT"              )
  plotCombo("looseSel_Jet_1_softdrop_mass.root"   , "looseSel_Jet_1_softdrop_mass"    )
  
  # plotCombo("looseSel_Jet_1_eta.root"             , "looseSel_Jet_1_eta"              )
  # plotCombo("looseSel_Jet_1_p_T.root"             , "looseSel_Jet_1_p_T"              )
  # plotCombo("looseSel_Jet_1_phi.root"             , "looseSel_Jet_1_phi"              )
  
  # plotCombo("looseSel_Jet_1_tau21.root"           , "looseSel_Jet_1_tau21"            )
  # plotCombo("looseSel_Jet_1_tau_1.root"           , "looseSel_Jet_1_tau_1"            )
  # plotCombo("looseSel_Jet_1_tau_2.root"           , "looseSel_Jet_1_tau_2"            )
  # plotCombo("looseSel_Jet_2_DDT.root"             , "looseSel_Jet_2_DDT"              )
  # plotCombo("looseSel_Jet_2_eta.root"             , "looseSel_Jet_2_eta"              )
  # plotCombo("looseSel_Jet_2_p_T.root"             , "looseSel_Jet_2_p_T"              )
  # plotCombo("looseSel_Jet_2_phi.root"             , "looseSel_Jet_2_phi"              )
  # plotCombo("looseSel_Jet_2_softdrop_mass.root"   , "looseSel_Jet_2_softdrop_mass"    )
  # plotCombo("looseSel_Jet_2_tau21.root"           , "looseSel_Jet_2_tau21"            )
  # plotCombo("looseSel_Jet_2_tau_1.root"           , "looseSel_Jet_2_tau_1"            )
  # plotCombo("looseSel_Jet_2_tau_2.root"           , "looseSel_Jet_2_tau_2"            )
    
    
    
    
         
  # plotCombo("COMB_looseSel_Dijet_invariant_mass.root","Dijet_invariant_mass")
#   plotCombo("COMB_looseSel_Jet_1_DDT.root"           ,"Jet_1_DDT")
#   plotCombo("COMB_looseSel_Jet_1_softdrop_mass.root" ,"Jet_1_softdrop_mass")
#   plotCombo("COMB_looseSel_Jet_2_DDT.root"           ,"Jet_2_DDT")
#   plotCombo("COMB_looseSel_Jet_2_softdrop_mass.root" ,"Jet_2_softdrop_mass")
#