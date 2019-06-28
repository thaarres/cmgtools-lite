#!/usr/bin/env python

import ROOT
from array import array
from CMGTools.VVResonances.plotting.TreePlotter import TreePlotter
from CMGTools.VVResonances.plotting.MergedPlotter import MergedPlotter
from CMGTools.VVResonances.plotting.StackPlotter import StackPlotter
from CMGTools.VVResonances.statistics.Fitter import Fitter
from math import log
import os, sys, re, optparse,pickle,shutil,json
ROOT.gROOT.SetBatch(True)
testcorr= True

def returnString(func):
    st='0'
    for i in range(0,func.GetNpar()):
        st=st+"+("+str(func.GetParameter(i))+")"+("*MH"*i)
    return st    

def getBinning(binsMVV,minx,maxx,bins):
    l=[]
    if binsMVV=="":
        for i in range(0,bins+1):
            l.append(minx + i* (maxx - minx)/bins)
    else:
        s = binsMVV.split(",")
        for w in s:
            l.append(int(w))
    return l

def truncate(binning,mmin,mmax):
    res=[]
    for b in binning:
        if b >= mmin and b <= mmax:
            res.append(b)
    return res


def getMJPdf(mvv_min,mvv_max,MH,postfix=""):
 
        var = ROOT.RooRealVar("MVV","MVV",mvv_min,mvv_max)
	
        pdfName 	= "signal_%d%s" %(MH,postfix)
        

        mean        = ROOT.RooRealVar("mean_%d%s"%(MH,postfix),"mean_%d%s"%(MH,postfix),MH ,0.8*MH,1.2*MH)
        sigma       = ROOT.RooRealVar("sigma_%d%s"%(MH,postfix),"sigma_%d%s"%(MH,postfix),MH*0.05,MH*0.02,MH*0.10)
        alpha       = ROOT.RooRealVar("alpha_%d%s"%(MH,postfix),"alpha_%d%s"%(MH,postfix),1.2,0.0,18)
        alpha2      = ROOT.RooRealVar("alpha2_%d%s"%(MH,postfix),"alpha2_%d%s"%(MH,postfix),1.2,0.0,10)
        sign        = ROOT.RooRealVar("sign_%d%s"%(MH,postfix),"sign_%d%s"%(MH,postfix),5,0,600)
        sign2        = ROOT.RooRealVar("sign2_%d%s"%(MH,postfix),"sign2_%d%s"%(MH,postfix),5,0,50)  
        
  
        
	function = ROOT.RooDoubleCB(pdfName, pdfName, var, mean, sigma, alpha, sign,  alpha2, sign2)  
	return function,var


parser = optparse.OptionParser()
parser.add_option("-s","--sample",dest="sample",default='',help="Type of sample")
parser.add_option("-c","--cut",dest="cut",help="Cut to apply for shape",default='')
parser.add_option("-o","--output",dest="output",help="Output JSON",default='')
parser.add_option("-V","--MVV",dest="mvv",help="mVV variable",default='')
parser.add_option("--fix",dest="fixPars",help="Fixed parameters",default="")
parser.add_option("-m","--minMVV",dest="min",type=float,help="mVV variable",default=1)
parser.add_option("-M","--maxMVV",dest="max",type=float, help="mVV variable",default=1)
parser.add_option("-r","--minMX",dest="minMX",type=float, help="smallest Mx to fit ",default=1000.0)
parser.add_option("-R","--maxMX",dest="maxMX",type=float, help="largest Mx to fit " ,default=7000.0)
parser.add_option("--binsMVV",dest="binsMVV",help="use special binning",default="")
parser.add_option("-t","--triggerweight",dest="triggerW",action="store_true",help="Use trigger weights",default=False)

(options,args) = parser.parse_args()
#define output dictionary

samples={}
graphs={'MEAN':ROOT.TGraphErrors(),'SIGMA':ROOT.TGraphErrors(),'ALPHA1':ROOT.TGraphErrors(),'N1':ROOT.TGraphErrors(),'ALPHA2':ROOT.TGraphErrors(),'N2':ROOT.TGraphErrors()}

for filename in os.listdir(args[0]):
    if not (filename.find(options.sample)!=-1):
        continue
    if filename.find("VBF")!=-1 and options.sample.find("VBF")==-1:
        continue

#found sample. get the mass
    fnameParts=filename.split('.')
    fname=fnameParts[0]
    ext=fnameParts[1]
    if ext.find("root") ==-1:
        continue
        
    
    mass = float(fname.split('_')[-1])
    if mass < options.minMX or mass > options.maxMX: continue
        

    samples[mass] = fname

    print 'found',filename,'mass',str(mass) 


#Now we have the samples: Sort the masses and run the fits
N=0

Fhists=ROOT.TFile("massHISTOS_"+options.output,"RECREATE")


for mass in sorted(samples.keys()):

    print 'fitting',str(mass) 
    plotter=TreePlotter(args[0]+'/'+samples[mass]+'.root','AnalysisTree')
    plotter.addCorrectionFactor('genWeight','tree')
    plotter.addCorrectionFactor('puWeight','tree')
    if options.triggerW:
        plotter.addCorrectionFactor('jj_triggerWeight','tree')	
        print "Using triggerweight"
       
    fitter=Fitter(['MVV'])
    fitter.signalResonance('model',"MVV",mass,False)
   
    fitter.w.var("MH").setVal(mass)

    binning= truncate(getBinning(options.binsMVV,options.min,options.max,100),0.80*mass,1.2*mass)    
    histo = plotter.drawTH1Binned(options.mvv,options.cut+"*(jj_LV_mass>%f&&jj_LV_mass<%f)"%(0.80*mass,1.2*mass),"1",binning)
    fitter.importBinnedData(histo,['MVV'],'data')
    ps = []
    if testcorr==True:
        print "do 2D histos"
        histos2D = plotter.drawTH2("jj_LV_mass:jj_l2_softDrop_mass",options.cut,"1",80,55,215,50,1126,5000)
        ctest = ROOT.TCanvas("test","test",400,400)
        histos2D.Draw("colz")
        ctest.SaveAs(samples[mass]+"_M"+str(mass)+"_2D.pdf")
        ctest.SaveAs(samples[mass]+"_M"+str(mass)+"_2D.png")
        proj = histos2D.ProjectionX("p")
        
        graph_mean = ROOT.TGraphErrors()
        graph_sigma = ROOT.TGraphErrors()
        n=-1
        bins_all = [[0,80],[0,10],[10,20],[20,40],[40,80]]
        if samples[mass].find("hbb")==-1:
            bins_all = [[0,80],[0,11],[11,16],[16,22],[22,80]]
        for bins in bins_all:
            ps .append( histos2D.ProjectionY("p2"+str(n+1),bins[0],bins[1]))#,proj.GetBin(55),proj.GetBin(85))
            c3 = ROOT.TCanvas("test3","test3",400,400)
            fit = ROOT.TF1("gauss","gaus",0.9*mass,1.1*mass)
            ps[-1].Fit(fit,"","",0.9*mass,1.1*mass)
            ps[-1].Draw("same")
            #proj.Draw()
            c3.SaveAs("test3_M"+str(mass)+".pdf")
            if n==-1:
                mean = fit.GetParameter(1)
                sigma = fit.GetParameter(2)
                n+=1
            else:
                graph_mean.SetPoint(n,proj.GetBinCenter(bins[0])+ (proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2. ,fit.GetParameter(1)/mean)
                graph_mean.SetPointError(n,(proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2., fit.GetParError(1)/mean)
                #graph_mean.SetPointError(n,0, fit.GetParError(1)/mean)
                graph_sigma.SetPoint(n,proj.GetBinCenter(bins[0])+ (proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2. ,fit.GetParameter(2)/sigma)
                graph_sigma.SetPointError(n,(proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2., fit.GetParError(2)/sigma)
                print fit.GetParameter(2)
                n+=1
        pol3=ROOT.TF1("pol","pol3",55,215)
        f1 = ROOT.TF1("f1","[0]+[1]*log(x)",1,13000)
        f2 = ROOT.TF1("f2","[0]+[1]*sqrt(x)",1,13000)
        f3 = ROOT.TF1("f3","[0]+[1]*TMath::DiLog(x)",1,13000)
        f4 = ROOT.TF1("f4","[0]+[1]*log(x)-[2]*x",1,13000)
        f4.SetParLimits(2,0,1)
        f5 = ROOT.TF1("f5","[0]+[1]*log(sqrt(x))",1,13000)
        f6 = ROOT.TF1("f6","[0]+[1]*log(x*x)",1,13000)
        f7 = ROOT.TF1("f7","1-[0]*exp(-(x-55))",1,13000)
        
        
        f10 = ROOT.TF1("f10","[0]+[1]/sqrt(x)",1,13000)
        
        c = ROOT.TCanvas("test2","test2",400,400)
        graph_mean.SetMinimum(0.8)
        graph_mean.SetMaximum(1.2)
        graph_mean.SetLineColor(ROOT.kBlue)
        graph_mean.SetMarkerStyle(8)
        graph_mean.SetMarkerColor(ROOT.kBlue)
        graph_mean.Fit(f2,"","",55,215)
        graph_mean.Draw("lap")
        graph_sigma.SetLineColor(ROOT.kRed)
        graph_sigma.SetMarkerStyle(5)
        graph_sigma.SetMarkerColor(ROOT.kRed)
        graph_sigma.Fit(f10,"","",55,215)
        graph_sigma.Draw("plsame")        
        c.SaveAs(samples[mass]+"_M"+str(mass)+".pdf")
        c.SaveAs(samples[mass]+"_M"+str(mass)+".png")
         
        f=open("testcorr_"+samples[mass]+".json","w") 
        f.write("{'sigma_corr' : '("+str(f10.GetParameter(0))+"+"+str(f10.GetParameter(1))+"/sqrt(MJ1) + "+str(f10.GetParameter(0))+"+"+str(f10.GetParameter(1))+"/sqrt(MJ2))/2.'" )
        f.write(", 'mean_corr' : '("+str(f2.GetParameter(0))+"+"+str(f2.GetParameter(1))+"*sqrt(MJ1) + "+str(f2.GetParameter(0))+"+"+str(f2.GetParameter(1))+"*sqrt(MJ2))/2.' }" )
        f.close()
        

    Fhists.cd()
    histo.Write("%i"%mass)
    roobins = ROOT.RooBinning(len(binning)-1,array("d",binning))
   
    #if samples[mass].find("hbb")==-1:
    #fitter.signalResonance('model1',"MVV",mass,False)
    #bins_all = [[0,80],[0,11],[11,16],[16,22],[22,80]]
    h1 = plotter.drawTH1Binned(options.mvv,options.cut+"*(jj_LV_mass>%f&&jj_LV_mass<%f)*(jj_l1_softDrop_mass >65 && jj_l1_softDrop_mass < 85)"%(0.80*mass,1.2*mass),"1",binning)
    
    func,var = getMJPdf(1126,5000,mass,options.sample)
    data1 = ROOT.RooDataHist("dh","dh", ROOT.RooArgList(var), ROOT.RooFit.Import(h1)) 
    
    print data1
    
    print func
    print var
    func.fitTo(data1,ROOT.RooFit.Range(mass*0.8,mass*1.2),ROOT.RooFit.SumW2Error(kTRUE),ROOT.RooFit.PrintEvalErrors(-1),ROOT.RooFit.Save(kTRUE))
    #fitter.importBinnedData(h1,['MVV'],'data1')
    c3 = ROOT.TCanvas("test3","test3",400,400)
    frame = var.frame() 
    func.PlotOn(frame)
    frame.Draw()
    #fitter.fit('model1','data1')
    #h1.Draw("same")
            ##proj.Draw()
    c3.SaveAs("test3_M"+str(mass)+".pdf")
    
    #fitter.projection("model1","data1","MVV","1debugVV_"+options.output+"_"+str(mass)+".png",roobins)
    
    
    if options.fixPars!="1":
        fixedPars =options.fixPars.split(',')
        print fixedPars
        for par in fixedPars:
            parVal = par.split(':')
	    if len(parVal) > 1:
             fitter.w.var(parVal[0]).setVal(float(parVal[1]))
             fitter.w.var(parVal[0]).setConstant(1)
    
    
  
    fitter.fit('model','data',[ROOT.RooFit.SumW2Error(0)])
    fitter.fit('model','data',[ROOT.RooFit.SumW2Error(0),ROOT.RooFit.Minos(1)])
    
    
    fitter.projection("model","data","MVV","debugVV_"+options.output+"_"+str(mass)+".png",roobins)

    for var,graph in graphs.iteritems():
        value,error=fitter.fetch(var)
        graph.SetPoint(N,mass,value)
        graph.SetPointError(N,0.0,error)
                
    N=N+1
    fitter.delete()
    
Fhists.Write()
Fhists.Close()        
F=ROOT.TFile(options.output,"RECREATE")
F.cd()
for name,graph in graphs.iteritems():
    graph.Write(name)
F.Close()
            
