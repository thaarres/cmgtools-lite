3#!/bin/env python
import ROOT
import json
import math
ROOT.gSystem.Load("libHiggsAnalysisCombinedLimit")
from time import sleep
import optparse, sys

def getMVVPdf(j,MH):

        var = w.var(options.var)
	
        pdfName 	= "signal_%d" % MH
        Jmean 		= eval(j['MEAN'])
        Jsigma		= eval(j['SIGMA'])
        Jscalesigma	= eval(j['SCALESIGMA'])
        Jalpha 		= eval(j['ALPHA'])
        Jn 		= eval(j['N'])
        Jf 		= eval(j['f'])

        mean        = ROOT.RooRealVar("mean_%d"%MH,"mean_%d"%MH,Jmean)
        sigma       = ROOT.RooRealVar("sigma","sigma_%d"%MH,Jsigma)
        scalesigma  = ROOT.RooRealVar("scalesigma_%d"%MH,"scalesigma_%d"%MH,Jscalesigma)
        alpha       = ROOT.RooRealVar("alpha_%d"%MH,"alpha_%d"%MH,Jalpha)
        sign        = ROOT.RooRealVar("sign_%d"%MH,"sign_%d"%MH,Jn)
        gsigma      = ROOT.RooFormulaVar("gsigma_%d"%MH,"@0*@1",ROOT.RooArgList(sigma,scalesigma))
        sigfrac     = ROOT.RooRealVar("sigfrac_%d"%MH,"sigfrac_%d"%MH,Jf)
        

        scalesigma.setConstant(ROOT.kTRUE)
        sigfrac.setConstant(ROOT.kTRUE)
        alpha.setConstant(ROOT.kTRUE)
        sign.setConstant(ROOT.kTRUE)
        mean.setConstant(ROOT.kTRUE)
        sigma.setConstant(ROOT.kTRUE)
        
        
        gauss 	= ROOT.RooGaussian("gauss_%d"%MH, "gauss_%d"%MH, var, mean, gsigma)
        cb    	= ROOT.RooCBShape("cb_%d"%MH, "cb_%d"%MH,var, mean, sigma, alpha, sign)
        function = ROOT.RooAddPdf(pdfName, pdfName,gauss, cb, sigfrac) 
        getattr(w,'import')(function,ROOT.RooFit.Rename(pdfName))

def getMJPdf(j,MH):
 
        var = w.var(options.var)
	
        pdfName 	= "signal_%d" % MH
        Jmean 		= eval(j['mean'])
        Jsigma		= eval(j['sigma'])
        Jalpha 		= eval(j['alpha'])
        Jalpha2 	= eval(j['alpha2'])
        Jn 		= eval(j['n'])
        Jn2 		= eval(j['n2'])

        mean        = ROOT.RooRealVar("mean_%d"%MH,"mean_%d"%MH,Jmean)
        sigma       = ROOT.RooRealVar("sigma_%d"%MH,"sigma_%d"%MH,Jsigma)
        alpha       = ROOT.RooRealVar("alpha_%d"%MH,"alpha_%d"%MH,Jalpha)
        alpha2      = ROOT.RooRealVar("alpha2_%d"%MH,"alpha2_%d"%MH,Jalpha2)
        sign        = ROOT.RooRealVar("sign_%d"%MH,"sign_%d"%MH,Jn)
        sign2        = ROOT.RooRealVar("sign2_%d"%MH,"sign2_%d"%MH,Jn2)        

        alpha.setConstant(ROOT.kTRUE)
        sign.setConstant(ROOT.kTRUE)
        alpha2.setConstant(ROOT.kTRUE)
        sign2.setConstant(ROOT.kTRUE)
        mean.setConstant(ROOT.kTRUE)
        sigma.setConstant(ROOT.kTRUE)
        
	function = ROOT.RooDoubleCB(pdfName, pdfName, var, mean, sigma, alpha, sign,  alpha2, sign2)  
	getattr(w,'import')(function,ROOT.RooFit.Rename(pdfName))
		
parser = optparse.OptionParser()
parser.add_option("-f","--file",dest="file",default='',help="input file")
parser.add_option("-v","--var",dest="var",help="mVV or mJ",default='mVV')

(options,args) = parser.parse_args()

inFileName = options.file
massPoints = [1000,1200,1400,1600,1800,2000,2500,3000,3500,4000,4500]
varName = {'mVV':'Dijet invariant mass (GeV)','mJ':'m_{jet} softdrop (GeV)'}
varBins = {'mVV':'[3000,700,6000]','mJ':'[77,55,210]'}
w=ROOT.RooWorkspace("w","w")
w.factory(options.var+varBins[options.var])
w.var(options.var).SetTitle(varName[options.var])
        
def main():
    with open(inFileName) as jsonFile:
        j = json.load(jsonFile)
    
    c1 = ROOT.TCanvas("c1", "c1", 800, 600)
    c1.Draw()
    graphs = []
    leg = ROOT.TLegend(0.8, 0.2, 0.95, 0.8)
    frame = w.var(options.var).frame()   
    
    for i, MH in enumerate(massPoints):  # mind that MH is evaluated below
    
        if options.var == 'mVV': getMVVPdf(j,MH)
	else: getMJPdf(j,MH)
       
        w.pdf('signal_%d'%MH).plotOn(frame, ROOT.RooFit.LineColor(i+840),ROOT.RooFit.Name(str(MH)))#,ROOT.RooFit.Range(MH*0.8,1.2*MH))#ROOT.RooFit.Normalization(1, ROOT.RooAbsReal.RelativeExpected),

        leg.AddEntry(frame.findObject(str(MH)), "%d GeV" % MH, "L")

    frame.Draw()
    leg.Draw("same")
    c1.SaveAs("signalShapes%s_%s.png" %(options.var, inFileName.rsplit(".", 1)[0]))
    sleep(5)


if __name__ == '__main__':
    main()
