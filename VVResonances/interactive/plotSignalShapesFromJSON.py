3#!/bin/env python
import ROOT
import json
import math
ROOT.gSystem.Load("libHiggsAnalysisCombinedLimit")
from time import sleep
import optparse, sys
from  CMGTools.VVResonances.plotting.CMS_lumi import *

# ROOT.gROOT.SetBatch(True)

path = "/eos/user/t/thaarres/www/vvana/3D_latest/signalFits/"

def getLegend(x1=0.70010112,y1=0.693362,x2=0.90202143,y2=0.829833):
  legend = ROOT.TLegend(x1,y1,x2,y2)
  legend.SetTextSize(0.032)
  legend.SetLineColor(0)
  legend.SetShadowColor(0)
  legend.SetLineStyle(1)
  legend.SetLineWidth(1)
  legend.SetFillColor(0)
  legend.SetFillStyle(0)
  legend.SetMargin(0.35)
  return legend
  
def getCanvas(name="c1"):
	
	H_ref = 600
	W_ref = 800
	W = W_ref
	H  = H_ref
	
	T = 0.08*H_ref
	B = 0.12*H_ref 
	L = 0.12*W_ref
	R = 0.04*W_ref
	canvas = ROOT.TCanvas(name,name,50,50,W,H)
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
	
	ROOT.gStyle.SetOptStat(0)
	ROOT.gStyle.SetOptTitle(0)
	canvas.cd()
	
	return canvas
	
def getMVVPdf(j,MH,postfix=""):

        var = w.var(options.var)
        
        pdfName 	= "signal_%d%s" %(MH,postfix)
        Jmean 		= eval(j['MEAN'])
        Jsigma		= eval(j['SIGMA'])
        Jalpha1     = eval(j['ALPHA1'])
        Jalpha2     = eval(j['ALPHA2'])
        Jn1 		= eval(j['N1'])
        Jn2 		= eval(j['N2'])
        
        mean        = ROOT.RooRealVar("mean_%d%s"%(MH,postfix),"mean_%d%s"%(MH,postfix),Jmean)
        sigma       = ROOT.RooRealVar("sigma","sigma_%d%s"%(MH,postfix),Jsigma)        
        alpha1      = ROOT.RooRealVar("alpha1_%d%s"%(MH,postfix),"alpha1_%d%s"%(MH,postfix),Jalpha1)
        alpha2      = ROOT.RooRealVar("alpha2_%d%s"%(MH,postfix),"alpha2_%d%s"%(MH,postfix),Jalpha2)
        n1          = ROOT.RooRealVar("n1_%d%s"%(MH,postfix),"n1_%d%s"%(MH,postfix),Jn1)
        n2          = ROOT.RooRealVar("n2_%d%s"%(MH,postfix),"n2_%d%s"%(MH,postfix),Jn2)
        

        alpha1.setConstant(ROOT.kTRUE)
        alpha2.setConstant(ROOT.kTRUE)
        n2.setConstant(ROOT.kTRUE)
        n1.setConstant(ROOT.kTRUE)
        mean.setConstant(ROOT.kTRUE)
        sigma.setConstant(ROOT.kTRUE)
        
        
        # gauss     = ROOT.RooGaussian("gauss_%d%s"%(MH,postfix), "gauss_%d%s"%(MH,postfix), var, mean, gsigma)
        # cb        = ROOT.RooCBShape("cb_%d%s"%(MH,postfix), "cb_%d%s"%(MH,postfix),var, mean, sigma, alpha, sign)
        # function = ROOT.RooAddPdf(pdfName, pdfName,gauss, cb, sigfrac)
        function = ROOT.RooDoubleCB(pdfName, pdfName,var, mean,sigma,alpha1,n1,alpha2,n2)
        getattr(w,'import')(function,ROOT.RooFit.Rename(pdfName))

def getMJPdf(j,MH,postfix=""):
 
        var = w.var(options.var)
	
        pdfName 	= "signal_%d%s" %(MH,postfix)
        Jmean 		= eval(j['mean'])
        Jsigma		= eval(j['sigma'])
        Jalpha 		= eval(j['alpha'])
        Jalpha2 	= eval(j['alpha2'])
        Jn 		= eval(j['n'])
        Jn2 		= eval(j['n2'])

        mean        = ROOT.RooRealVar("mean_%d%s"%(MH,postfix),"mean_%d%s"%(MH,postfix),Jmean)
        sigma       = ROOT.RooRealVar("sigma_%d%s"%(MH,postfix),"sigma_%d%s"%(MH,postfix),Jsigma)
        alpha       = ROOT.RooRealVar("alpha_%d%s"%(MH,postfix),"alpha_%d%s"%(MH,postfix),Jalpha)
        alpha2      = ROOT.RooRealVar("alpha2_%d%s"%(MH,postfix),"alpha2_%d%s"%(MH,postfix),Jalpha2)
        sign        = ROOT.RooRealVar("sign_%d%s"%(MH,postfix),"sign_%d%s"%(MH,postfix),Jn)
        sign2        = ROOT.RooRealVar("sign2_%d%s"%(MH,postfix),"sign2_%d%s"%(MH,postfix),Jn2)        

        alpha.setConstant(ROOT.kTRUE)
        sign.setConstant(ROOT.kTRUE)
        alpha2.setConstant(ROOT.kTRUE)
        sign2.setConstant(ROOT.kTRUE)
        mean.setConstant(ROOT.kTRUE)
        sigma.setConstant(ROOT.kTRUE)
        
	function = ROOT.RooDoubleCB(pdfName, pdfName, var, mean, sigma, alpha, sign,  alpha2, sign2)  
	getattr(w,'import')(function,ROOT.RooFit.Rename(pdfName))
		
parser = optparse.OptionParser()
parser.add_option("-f","--file",dest="file",default='JJ_BulkGWW_MVV.json',help="input file")
parser.add_option("-v","--var",dest="var",help="mVV or mJ",default='mVV')
parser.add_option("-l","--leg",dest="leg",help="mVV or mJ",default='l1')
postfix = "Jet 1 "
(options,args) = parser.parse_args()
if options.leg == "l2" !=-1: postfix = "Jet 2 "

inFileName = options.file
massPoints = [1000,1200,1400,1600,1800,2000,2500,3000,3500,4000,4500]
massPoints = [1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,3200,3400,3600,3800,4000,4200,4400,4600,4800,5000,5200]
varName = {'mVV':'M_{VV} (GeV)','mJ':'%ssoftdrop mass (GeV)'%postfix}
varBins = {'mVV':'[37,1000,5500]','mJ':'[80,55,215]'}
w=ROOT.RooWorkspace("w","w")
w.factory(options.var+varBins[options.var])
w.var(options.var).SetTitle(varName[options.var])
colors= []
colors.append(["#deebf7","#c6dbef","#9ecae1","#6baed6","#4292c6","#2171b5","#08519c","#08306b"]*3)   
colors.append(["#e5f5e0","#c7e9c0","#a1d99b","#74c476","#41ab5d","#238b45","#006d2c","#00441b"]*3)       
colors.append(["#fee0d2","#fcbba1","#fc9272","#fb6a4a","#ef3b2c","#cb181d","#a50f15","#67000d"]*3) 
def doSingle():
    with open(inFileName) as jsonFile:
      j = json.load(jsonFile)
    
      c1 = getCanvas()
      c1.Draw()
      leg = ROOT.TLegend(0.8, 0.2, 0.95, 0.8)
      frame = w.var(options.var).frame()   
      
      for i, MH in enumerate(massPoints):  # mind that MH is evaluated below
        if options.var == 'mVV': getMVVPdf(j,MH)
        else: getMJPdf(j,MH)
        w.pdf('signal_%d'%MH).plotOn(frame, ROOT.RooFit.LineColor(ROOT.TColor.GetColor(colors[i])),ROOT.RooFit.Name(str(MH)))#,ROOT.RooFit.Range(MH*0.8,1.2*MH))#ROOT.RooFit.Normalization(1, ROOT.RooAbsReal.RelativeExpected),
        leg.AddEntry(frame.findObject(str(MH)), "%d GeV" % MH, "L")
      frame.GetYaxis().SetTitle("A.U")
      frame.GetYaxis().SetNdivisions(4,5,0)
      frame.SetMaximum(0.1)
      if options.var == 'mVV':frame.SetMaximum(0.5)
      frame.Draw()
      # leg.Draw("same")
      model = "G_{B} #rightarrow WW"
      if options.file.find("ZZ")!=-1:
          model = "G_{B} #rightarrow ZZ"
      if options.file.find("WZ")!=-1:
          model = "W' #rightarrow WZ"
      if options.file.find("Zprime")!=-1:
          model = "Z' #rightarrow WW"
      if   options.file.find("HPHP")!=-1: purity = "HPHP"
      elif options.file.find("HPLP")!=-1: purity = "HPLP"
      else:purity = "HPLP+HPHP"
      c1.cd()
      pt =ROOT.TPaveText(0.81,0.82,0.84,0.89,"brNDC")
      pt.SetBorderSize(0)
      pt.SetTextAlign(12)
      pt.SetFillStyle(0)
      pt.SetTextFont(42)
      pt.SetTextSize(0.04)
      pt.AddText(model)
      # pt.AddText(purity)

      pt.Draw()
      cmslabel_final(c1,'2016',11)
      c1.Update()
      
      c1.SaveAs(path+"signalShapes%s_%s.png" %(options.var, inFileName.rsplit(".", 1)[0]))
      c1.SaveAs(path+"signalShapes%s_%s.pdf" %(options.var, inFileName.rsplit(".", 1)[0]))
      c1.SaveAs(path+"signalShapes%s_%s.C" %(options.var, inFileName.rsplit(".", 1)[0]))
      c1.SaveAs(path+"signalShapes%s_%s.root" %(options.var, inFileName.rsplit(".", 1)[0]))
  
def doAll():
    if options.var == 'mJ':  jsons = ["JJ_BulkGWW_MJl1_HPHP.json","JJ_WprimeWZ_MJl1_HPHP.json","JJ_BulkGZZ_MJl1_HPHP.json"]
    if options.var == 'mVV': jsons = ["JJ_BulkGWW_MVV.json","JJ_WprimeWZ_MVV.json","JJ_BulkGZZ_MVV.json"]
    legs = ["G_{B} #rightarrow WW","W' #rightarrow WZ","G_{B} #rightarrow ZZ"]
    c1 = getCanvas()
    c1.Draw()
    leg = getLegend()
    frame = w.var(options.var).frame()   
    for ii,f in enumerate(jsons):
        print f
        name = f.split("_")[1]
        with open(f) as jsonFile:
          j = json.load(jsonFile)
          for i, MH in enumerate(massPoints):  # mind that MH is evaluated below
            if options.var == 'mVV': getMVVPdf(j,MH,name)
            else: getMJPdf(j,MH,name)
            w.pdf('signal_%d%s'%(MH,name)).plotOn(frame, ROOT.RooFit.LineColor(ROOT.TColor.GetColor(colors[ii][i])),ROOT.RooFit.Name(str(MH)+name))#,ROOT.RooFit.Range(MH*0.8,1.2*MH))#ROOT.RooFit.Normalization(1, ROOT.RooAbsReal.RelativeExpected),
        leg.AddEntry(frame.findObject(str(1800)+name), legs[ii], "L")
    frame.GetYaxis().SetTitle("A.U")
    frame.GetYaxis().SetTitleOffset(1.15)
    frame.GetYaxis().SetNdivisions(4,5,0)
    frame.SetMaximum(0.15)
    if options.var == 'mVV':frame.SetMaximum(0.5)
    frame.Draw()
    leg.Draw("same")
    pt =ROOT.TPaveText(0.81,0.60,0.84,0.66,"brNDC")
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(42)
    pt.SetTextSize(0.035)
    pt.AddText("1.2-5.2 TeV")
    pt.Draw()
    cmslabel_final(c1,'sim',11)
    c1.Update()
      
    c1.SaveAs(path+"signalShapes_%s_All.png"  %(options.var))
    c1.SaveAs(path+"signalShapes_%s_All.pdf"  %(options.var))
    c1.SaveAs(path+"signalShapes_%s_All.C"    %(options.var))
    c1.SaveAs(path+"signalShapes_%s_All.root" %(options.var))
    # sleep(1000)
      
if __name__ == '__main__':
    # doSingle()
    doAll()
