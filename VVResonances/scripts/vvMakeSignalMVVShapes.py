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
ROOT.gStyle.SetOptStat(0)

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


def getMJPdf(mvv_min,mvv_max,MH,postfix="",fixPars="1"):
 
        var = ROOT.RooRealVar("MVV","MVV",mvv_min,mvv_max)
	
        pdfName 	= "signal_%d%s" %(MH,postfix)
        

        mean        = ROOT.RooRealVar("mean_%d%s"%(MH,postfix),"mean_%d%s"%(MH,postfix),MH ,0.8*MH,1.2*MH)
        sigma       = ROOT.RooRealVar("sigma_%d%s"%(MH,postfix),"sigma_%d%s"%(MH,postfix),MH*0.05,MH*0.02,MH*0.10)
        alpha       = ROOT.RooRealVar("alpha_%d%s"%(MH,postfix),"alpha_%d%s"%(MH,postfix),1.2,0.0,18)
        alpha2      = ROOT.RooRealVar("alpha2_%d%s"%(MH,postfix),"alpha2_%d%s"%(MH,postfix),1.2,0.0,10)
        sign        = ROOT.RooRealVar("sign_%d%s"%(MH,postfix),"sign_%d%s"%(MH,postfix),5,0,600)
        sign2        = ROOT.RooRealVar("sign2_%d%s"%(MH,postfix),"sign2_%d%s"%(MH,postfix),5,0,50)  
        
        #if fixPars!="1":
            #fixedPars =fixPars.split(',')
            #for par in fixedPars:
                #parVal = par.split(':')
                #if len(parVal) > 1:
                    #if par.find("MEAN")!=-1:
                        #mean.setVal(float(parVal[1]))
                        #mean.setConstant(1)
                    #if par.find("SIGMA")!=-1:
                        #sigma.setVal(float(parVal[1]))
                        #sigma.setConstant(1)
                    #if par.find("ALPHA1")!=-1:
                        #alpha.setVal(float(parVal[1]))
                        #alpha.setConstant(1)
                    #if par.find("ALPHA2")!=-1:
                        #alpha2.setVal(float(parVal[1]))
                        #alpha2.setConstant(1)
                    #if par.find("N1")!=-1:
                        #sign.setVal(float(parVal[1]))
                        #sign.setConstant(1)
                    #if par.find("N2")!=-1:
                        #sign2.setVal(float(parVal[1]))
                        #sign2.setConstant(1)
        print "================================================"
        print fixPars
	function = ROOT.RooDoubleCB(pdfName, pdfName, var, mean, sigma, alpha, sign,  alpha2, sign2)  
	return function,var,[mean,sigma,alpha,alpha2,sign,sign2]

def dodCBFits(h1,mass,prefix,fixpars):
    #h1 = plotter.drawTH1Binned(options.mvv,options.cut+"*(jj_LV_mass>%f&&jj_LV_mass<%f)*(jj_l1_softDrop_mass >65 && jj_l1_softDrop_mass < 85)"%(0.80*mass,1.2*mass),"1",binning)
    
    func,var,params = getMJPdf(1126,5000,mass,options.sample,fixpars)
    data1 = ROOT.RooDataHist("dh","dh", ROOT.RooArgList(var), ROOT.RooFit.Import(h1)) 
    
    print data1
    
    print func
    print var
    func.fitTo(data1,ROOT.RooFit.Range(mass*0.6,mass*1.3),ROOT.RooFit.PrintEvalErrors(-1))
    
    c3 = ROOT.TCanvas("test3","test3",400,400)
    frame = var.frame() 
    data1.plotOn(frame)
    func.plotOn(frame)
    frame.Draw()
   
    c3.SaveAs("test3_M"+str(mass)+"_"+prefix+".pdf")
    del func,var
    return { "MEAN":params[0].getVal(), "SIGMA": params[1].getVal(), "ALPHA1": params[2].getVal(), "ALPHA2": params[3].getVal() , "N1": params[4].getVal(), "N2": params[5].getVal(),"MEANERR":params[0].getError(), "SIGMAERR": params[1].getError(), "ALPHA1ERR": params[2].getError(), "ALPHA2ERR": params[3].getError() , "N1ERR": params[4].getError(), "N2ERR": params[5].getError()}
    

parser = optparse.OptionParser()
parser.add_option("-s","--sample",dest="sample",default='',help="Type of sample")
parser.add_option("-c","--cut",dest="cut",help="Cut to apply for shape",default='')
parser.add_option("--addcut",dest="addcut",help="Cut to apply for shape",default='')
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
print options.addcut

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

#Fhists=ROOT.TFile("massHISTOS_"+options.output,"RECREATE")
allgraphs = {}
for mass in samples.keys():
    h = ROOT.TH2F("corr_mean_M"+str(mass),"corr_mean_M"+str(mass),2,array("f",[85,105,145]),2,array("f",[85,105,145]))
    allgraphs[mass] = h
allgraphs_sigma = {}
for mass in samples.keys():
    h = ROOT.TH2F("corr_sigma_M"+str(mass),"corr_sigma_M"+str(mass),2,array("f",[55,105,215]),2,array("f",[55,105,215]))
    #h = ROOT.TH2F("corr_sigma_M"+str(mass),"corr_sigma_M"+str(mass),2,array("f",[70,102,150]),2,array("f",[70,102,150]))
    #h = ROOT.TH2F("corr_sigma_M"+str(mass),"corr_sigma_M"+str(mass),2,array("f",[70,105,145]),2,array("f",[70,105,145]))
    allgraphs_sigma[mass] = h

graphs_all=[]

graph_sum_sigma = ROOT.TH2F("corr_sigma","corr_sigma",2,array("f",[55,105,215]),2,array("f",[55,105,215]))
graph_sum_mean  = ROOT.TH2F("corr_mean","corr_mean",2,array("f",[85,105,145]),2,array("f",[85,105,145]))

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


    #extra_extra_cut = "&& (jj_LV_mass>%f&&jj_LV_mass<%f)"%(0.84*mass,1.08*mass)
    extra_extra_cut = "&& (jj_LV_mass>%f&&jj_LV_mass<%f)"%(0.8*mass,1.1*mass)
    binning= truncate(getBinning(options.binsMVV,options.min,options.max,100),0.80*mass,1.2*mass)    
    histo = plotter.drawTH1Binned(options.mvv,options.cut+extra_extra_cut,"1",binning)
    fitter.importBinnedData(histo,['MVV'],'data')
    ps = []
   
    #htmp = ROOT.TH2F("corr_mean_M"+str(mass),"corr_mean_M"+str(mass),2,array("f",[55,105,215]),2,array("f",[55,105,215]))
    #allgraphs.append( htmp)
    if testcorr==True:
        
       #histo = plotter.drawTH1(options.mvv,options.cut.replace(options.addcut,"")+"*(jj_l1_softDrop_mass>65&&jj_l1_softDrop_mass<105)"%(0.80*mass,1.2*mass),"1",binning)
  
       
        print "do 2D histos"
        print 
        
        histos2D = plotter.drawTH2("jj_LV_mass:jj_l2_softDrop_mass",options.cut.replace(options.addcut,"1"),"1",80,55,215,50,1126,5000)
        ctest = ROOT.TCanvas("test","test",400,400)
        histos2D.Draw("colz")
        ctest.SaveAs(samples[mass]+"_M"+str(mass)+"_2D.pdf")
        ctest.SaveAs(samples[mass]+"_M"+str(mass)+"_2D.png")
        proj = histos2D.ProjectionX("p")
        
        graph_mean = ROOT.TGraphErrors()
        graph_sigma = ROOT.TGraphErrors()
        graph_alpha = ROOT.TGraphErrors()
        graph_alpha2 = ROOT.TGraphErrors()
        graph_n = ROOT.TGraphErrors()
        graph_n2 = ROOT.TGraphErrors()
        n=0
        #bins_all = [[0,80],[0,10],[10,20],[20,40],[40,80]]
        #if samples[mass].find("hbb")==-1:
            #bins_all = [[0,80],[0,11],[11,16],[16,22],[22,80]]
        bins_all = [[5,25],[25,50]]
        histos3D = plotter.drawTH3("jj_LV_mass:jj_l2_softDrop_mass:jj_l1_softDrop_mass",options.cut.replace(options.addcut,"1")+extra_extra_cut,"1",80,55,215,80,55,215,50,1126,5000)
       
        
        #hall = histos3D.ProjectionZ("all",0,80,0,80)#,proj.GetBin(55),proj.GetBin(85))
        hall = histos3D.ProjectionZ("all",0,25,25,80)#,proj.GetBin(55),proj.GetBin(85))
        #hall = histos3D.ProjectionZ("all",0,80,0,80)#,proj.GetBin(55),proj.GetBin(85))
        par = dodCBFits(hall,mass,"all",options.fixPars)
        mean = par["MEAN"] #fit.GetParameter(1)
        sigma = par["SIGMA"] #fit.GetParameter(2)
        alpha = par["ALPHA1"]
        alpha2 = par["ALPHA2"]
        n1 = par["N1"]
        n2 = par["N2"]
        
        for bins in bins_all:
          for bins2 in bins_all:
            ps .append( histos3D.ProjectionZ("p2"+str(n+1),bins[0],bins[1],bins2[0],bins2[1]))#,proj.GetBin(55),proj.GetBin(85))
            
            #ps .append( histos2D.ProjectionY("p2"+str(n+1),bins[0],bins[1]))#,proj.GetBin(55),proj.GetBin(85))
            
            par = dodCBFits(ps[-1],mass,str(n+1),options.fixPars)
            b1 = proj.GetBinCenter(bins[0])+ (proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2. 
            b2 = proj.GetBinCenter(bins2[0])+ (proj.GetBinCenter(bins2[1])-proj.GetBinCenter(bins2[0]))/2.
            if b1 <105: b1 = 90
            if b2 < 105: b2 = 90
            if b1 > 105: b1 = 120
            if b2 > 105: b2 = 120
            
            allgraphs[mass].Fill(b1 ,b2 , par['MEAN']/mean)
            allgraphs_sigma[mass].Fill(b1 ,b2 , par['SIGMA']/sigma)
            #graph_sum_mean.Fill(b1 ,b2 , par['MEAN']/mean)
            #graph_sum_sigma.Fill(b1 ,b2 , par['SIGMA']/sigma)
            
            #print "fill this mofo "
            #print  par['MEAN']/mean
            #print graph_sum_mean.Integral()
            #break
            
        for bins in bins_all: 
            ps .append( histos3D.ProjectionZ("p2"+str(n+1),bins[0],bins[1],bins[0],bins[1]))
            par = dodCBFits(ps[-1],mass,str(n+1),options.fixPars)
            graph_mean.SetPoint(n,proj.GetBinCenter(bins[0])+ (proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2. ,par["MEAN"]/mean)
            graph_mean.SetPointError(n,(proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2., par["MEANERR"]/mean)
            graph_sigma.SetPoint(n,proj.GetBinCenter(bins[0])+ (proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2. ,par["SIGMA"]/sigma)
            graph_sigma.SetPointError(n,1., par["SIGMAERR"]/sigma)
            # graph_sigma.SetPointError(n,(proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2., par["SIGMAERR"]/sigma)
            graph_alpha.SetPoint(n,proj.GetBinCenter(bins[0])+ (proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2. ,par["ALPHA1"]/alpha)
            graph_alpha.SetPointError(n,(proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2., par["ALPHA1ERR"]/alpha)
            graph_alpha2.SetPoint(n,proj.GetBinCenter(bins[0])+ (proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2. ,par["ALPHA2"]/alpha2)
            graph_alpha2.SetPointError(n,(proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2., par["ALPHA2ERR"]/alpha2)
            graph_n.SetPoint(n,proj.GetBinCenter(bins[0])+ (proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2. ,par["N1"]/n1)
            graph_n.SetPointError(n,(proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2., par["N1ERR"]/n1)
            graph_n2.SetPoint(n,proj.GetBinCenter(bins[0])+ (proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2. ,par["N2"]/n2)
            graph_n2.SetPointError(n,(proj.GetBinCenter(bins[1])-proj.GetBinCenter(bins[0]))/2., par["N2ERR"]/n2)
                
            n+=1
       
        graph_mean.SetName("gorr_mean_M"+str(mass))
        graph_sigma.SetName("gorr_sigma_M"+str(mass))
        graph_alpha.SetName("gorr_alpha_M"+str(mass))
        graph_alpha2.SetName("gorr_alpha2_M"+str(mass))
        graph_n.SetName("gorr_n_M"+str(mass))
        graph_n2.SetName("gorr_n2_M"+str(mass))
        graphs_all.append(graph_mean)
        graphs_all.append(graph_sigma)
        graphs_all.append(graph_alpha)
        graphs_all.append(graph_alpha2)
        graphs_all.append(graph_n)
        graphs_all.append(graph_n2)
        
        #graph_sum_sigma.Add(allgraphs_sigma[mass])
        #graph_sum_mean.Add(allgraphs[mass]) 
        
        print "======================================" 
        print allgraphs
        print "+++++++++++++++++++++++++++++++"
        ctest = ROOT.TCanvas("test","test",400,400)
        allgraphs[mass].Draw("colz")
        ctest.SaveAs(samples[mass]+"_M"+str(mass)+"_2D.pdf")
    #Fhists.cd()
    #histo.Write("%i"%mass)
    roobins = ROOT.RooBinning(len(binning)-1,array("d",binning))
   
   
    
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
    
#Fhists.Write()
#Fhists.Close()  

print allgraphs

F =ROOT.TFile(options.output,"RECREATE")
for name,graph in graphs.iteritems():
    graph.Write(name)
 
if testcorr==True:
    for mass in allgraphs.keys():
        graph_sum_sigma.Add(allgraphs_sigma[mass])
        graph_sum_mean.Add(allgraphs[mass])
    print graph_sum_mean.Integral()
    graph_sum_sigma.Scale(1/float(N))
    graph_sum_mean .Scale(1/float(N))
    print allgraphs
    graph_sum_sigma.Write()
    graph_sum_mean .Write()
    print graph_sum_mean.Integral()
    
    for g in allgraphs.keys():
        print g
        allgraphs[g].Write()
        allgraphs_sigma[g].Write()
        #htest.Write()
        print "write "+allgraphs[g].GetName()
    for g in graphs_all:
        g.Write()

F.Close()

print 'wrote file '+options.output

            
