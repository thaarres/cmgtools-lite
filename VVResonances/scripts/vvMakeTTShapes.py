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
ROOT.gStyle.SetOptStat(0)
from time import sleep

parser = optparse.OptionParser()
parser.add_option("-s","--sample",dest="sample",default='',help="Type of sample")
parser.add_option("-c","--cut",dest="cut",help="Cut to apply for shape",default='')
parser.add_option("-o","--output",dest="output",help="outname",default='')
parser.add_option("-m","--min",dest="mini",type=float,help="min MJJ",default=40)
parser.add_option("-M","--max",dest="maxi",type=float,help="max MJJ",default=160)
parser.add_option("--store",dest="store",type=str,help="store fitted parameters in this file",default="")
parser.add_option("--corrFactor",dest="corrFactor",type=float,help="add correction factor xsec",default=1.)
parser.add_option("-f","--fix",dest="fixPars",help="Fixed parameters",default="1")
parser.add_option("--minMVV","--minMVV",dest="minMVV",type=float,help="mVV variable",default=1)
parser.add_option("--maxMVV","--maxMVV",dest="maxMVV",type=float, help="mVV variable",default=1)
parser.add_option("--binsMVV",dest="binsMVV",help="use special binning",default="")
parser.add_option("-t","--triggerweight",dest="triggerW",action="store_true",help="Use trigger weights",default=False)
(options,args) = parser.parse_args()


debug_out = "debug_TT/"
if not os.path.exists(debug_out): os.system('mkdir '+debug_out)
  
def getMean(h2,binL,binH):
  nbins = h2.GetYaxis().GetNbins()
  h1 = h2.ProjectionX("",0,nbins)
  h1.GetXaxis().SetRange(binL,binH)
  return h1.GetMean() 
  
def getFileList():
  samples={}
  samplenames = options.sample.split(",")
  for filename in os.listdir(args[0]):
    if filename.find("root") ==-1:
      continue
    for samplename in samplenames:
      if not (filename.find(samplename)!=-1):
        continue
      fnameParts=filename.split('.')
      try:
        fname=filename.split('.')[0]
        samples[fname] = fname
        print 'Fitting ttbar using file(s) ',filename
      except AssertionError as error:
          print(error)
          print('Root files does not have proper . separator')
  if len(samples) == 0:
    raise Exception('No input files found for samplename(s) {}'.format(options.sample))
  return samples

def getPlotters(samples_in):
  plotters_ = []
  for name in samples_in.keys():
    plotters_.append(TreePlotter(args[0]+'/'+samples[name]+'.root','AnalysisTree'))
    plotters_[-1].setupFromFile(args[0]+'/'+samples[name]+'.pck')
    plotters_[-1].addCorrectionFactor('xsec','tree')
    plotters_[-1].addCorrectionFactor('genWeight','tree')
    plotters_[-1].addCorrectionFactor('puWeight','tree')
    if options.triggerW: 
      plotters_[-1].addCorrectionFactor('triggerWeight','tree')	
    plotters_[-1].addCorrectionFactor(options.corrFactor,'flat')
  return plotters_
  
def get2DHist(plts, lumi_):
  mergedPlotter = MergedPlotter(plts)
  histo2D_l1 = mergedPlotter.drawTH2("jj_l1_softDrop_mass:jj_LV_mass",options.cut,"1",80,options.minMVV,options.maxMVV,80,options.mini,options.maxi) #y:x
  histo2D_l2 = mergedPlotter.drawTH2("jj_l2_softDrop_mass:jj_LV_mass",options.cut,"1",80,options.minMVV,options.maxMVV,80,options.mini,options.maxi)  
  histo2D_l1.Add(histo2D_l2)
  histo2D_l1.Scale(float(lumi_))
  c = ROOT.TCanvas()
  histo2D_l1.Draw("COLZ")
  histo2D_l1.GetXaxis().SetTitle("m_{jj}")
  histo2D_l1.GetYaxis().SetTitle("m_{j}")
  c.SaveAs(debug_out+"/%s_2D.pdf"%options.output)
  return histo2D_l1

def doFit(th1_projY,mjj_mean,mjj_error,N):
  
  fitter=Fitter(['x'])
  fitter.erfexp2Gaus('model','x')
  if N == 0:
    fitter.w.var("c_0").setVal(-5.8573e-02)
    fitter.w.var("c_1").setVal(4.4386e+02) #offset
    fitter.w.var("c_2").setVal(1.0707e+02) #width
    fitter.w.var("f_g1").setVal(7.8678e-02)
    fitter.w.var("f_res").setVal(5.9669e-01)
    fitter.w.var("mean1").setVal(8.1225e+01)
    fitter.w.var("mean2").setVal(1.7409e+02)
    fitter.w.var("sigma1").setVal(6.7507e+00)
    fitter.w.var("sigma2").setVal(1.3369e+01)
    
    # fitter.w.var("c_0")   .setMax(0.5*-5.8573e-02)
    # fitter.w.var("c_1")   .setMin(0.5*4.4386e+02) #offset
    # fitter.w.var("c_2")   .setMin(0.5*1.0707e+02) #width
    # fitter.w.var("f_g1")  .setMin(0.5*7.8678e-02)
    # fitter.w.var("f_res") .setMin(0.5*5.9669e-01)
    # fitter.w.var("mean1") .setMin(0.5*8.1225e+01)
    # fitter.w.var("mean2") .setMin(0.5*1.7409e+02)
    # fitter.w.var("sigma1").setMin(0.5*6.7507e+00)
    # fitter.w.var("sigma2").setMin(0.5*1.3369e+01)
    #
    # fitter.w.var("c_0")   .setMin(1.5*-5.8573e-02)
    # fitter.w.var("c_1")   .setMax(1.5*4.4386e+02) #offset
    # fitter.w.var("c_2")   .setMax(1.5*1.0707e+02) #width
    # fitter.w.var("f_g1")  .setMax(1.5*7.8678e-02)
    # fitter.w.var("f_res") .setMax(1.5*5.9669e-01)
    # fitter.w.var("mean1") .setMax(1.5*8.1225e+01)
    # fitter.w.var("mean2") .setMax(1.5*1.7409e+02)
    # fitter.w.var("sigma1").setMax(1.5*6.7507e+00)
    # fitter.w.var("sigma2").setMax(1.5*1.3369e+01)
 
  else:
    for var,graph in graphs.iteritems():
      yvalues = graphs[var].GetY()
      yvalues = [yvalues[index] for index in xrange(graphs[var].GetN())]
      print"For %s: Setting starting values of fit to values from previous bin:%f"%(var,yvalues[-1])
      fitter.w.var(var).setVal(yvalues[-1])
      
  if options.fixPars!="1":
    fixedPars =options.fixPars.split(',')
    if len(fixedPars) > 0:
      print "   - Fix parameters: ", fixedPars
    for par in fixedPars:
      parVal = par.split(':')
      fitter.w.var(parVal[0]).setVal(float(parVal[1]))
      fitter.w.var(parVal[0]).setConstant(1)
  fitter.importBinnedData(th1_projY,['x'],'data')
  fitter.fit('model','data',[ROOT.RooFit.SumW2Error(1),ROOT.RooFit.Save(1),ROOT.RooFit.Range(options.mini,options.maxi)]) #55,140 works well with fitting only the resonant part
  #ROOT.RooFit.Minos(ROOT.kTRUE)
  fitter.projection("model","data","x","%s/%s_%s.pdf"%(debug_out,options.output,th1_projY.GetName()),0,False,"m_{jet} (GeV)")
  
  
  for var,graph in graphs.iteritems():
      value,error=fitter.fetch(var)
      graph.SetPoint(N,mjj_mean,value)
      graph.SetPointError(N,0.0,error) #No error x
      # graph.SetPointError(N,mjj_error,error) #error x is number of bins in mVV
      
  fitter.delete()    

def doParametrizations(graphs,ff):
  ranges = {}
  ranges["c_0"   ]= [-0.1,0.1]
  ranges["c_1"   ]= [300,600]
  ranges["c_2"   ]= [40,200]
  ranges["f_g1"  ]= [0,0.5]
  ranges["f_res" ]= [0.4,0.8]
  ranges["mean1" ]= [70,90]
  ranges["mean2" ]= [160,190]
  ranges["sigma1"]= [0,12]
  ranges["sigma2"]= [6,20]
  pols = {}
  pols["c_0"   ]= "pol3"
  pols["c_1"   ]= "pol3"
  pols["c_2"   ]= "pol3"
  pols["f_g1"  ]= "pol2"
  pols["f_res" ]= "pol2"
  pols["mean1" ]= "pol2"
  pols["mean2" ]= "pol3"
  pols["sigma1"]= "pol3"
  pols["sigma2"]= "pol3"
  
  
  ff.cd()
  parametrizations = {}
  for var,graph in graphs.iteritems():
    func=ROOT.TF1(var+"_func",pols[var],0,13000)
    for i in range(5):
      r = graph.Fit(func,"","",options.minMVV,options.maxMVV)
    graph.Write(var)
    func.Write(var+"_func")
    c = ROOT.TCanvas()
    colors = ["#4292c6","#41ab5d","#ef3b2c","#ffd300","#D02090","#fdae61","#abd9e9","#2c7bb6"]
    mstyle = [8,4]
    graph.SetLineWidth(3)
    graph.SetLineStyle(1)
    graph.SetMarkerStyle(8)
    graph.Draw("APE")
    # graph.GetYaxis().SetRangeUser(graph.GetMinimum()/2,graph.GetMaximum()*2);
    graph.GetXaxis().SetRangeUser(options.minMVV,options.maxMVV)
    graph.GetYaxis().SetRangeUser(ranges[var][0],ranges[var][1])
    graph.GetXaxis().SetTitle("M_{jj}")
    graph.GetYaxis().SetTitle(var)
    leg = ROOT.TLegend(0.75, 0.75, 0.85, 0.85)
    ROOT.SetOwnership(leg, False)
    leg.SetBorderSize(0)
    leg.AddEntry(graph, var, "")
    leg.SetTextSize(0.04)
    leg.Draw()
    c.SaveAs(debug_out+options.output+"_"+var+".pdf")
    
    
    st='(0'
    for i in range(0,func.GetNpar()):
      st=st+"+("+str(func.GetParameter(i))+")"+("*MJJ"*i)
      st+=")"
    parametrizations[var] = st
  return parametrizations
              
  
if __name__ == "__main__":
  
  
  
  graphs={'mean1':ROOT.TGraphErrors(),'sigma1':ROOT.TGraphErrors(),'mean2':ROOT.TGraphErrors(),'sigma2':ROOT.TGraphErrors(),'f_g1':ROOT.TGraphErrors(),'f_res':ROOT.TGraphErrors(),
            'c_0':ROOT.TGraphErrors(),'c_1':ROOT.TGraphErrors(),'c_2':ROOT.TGraphErrors()}
  
  lumi = args[1]
  samples = getFileList()
  plotters = getPlotters(samples)
  h2D = get2DHist(plotters,lumi)
  tmpfile = ROOT.TFile("testTT.root","RECREATE")
  
  coarse_bins_low  = [1,3,5,7,7,7]
  coarse_bins_high = [2,4,6,79,79,79]
  projX = h2D.ProjectionX()
  for bin in range(0,len(coarse_bins_low)): #h2D_mjet1mjet2.GetNbinsX()):
    binL = float(projX.GetBinLowEdge(coarse_bins_low[bin]))
    binH = float(projX.GetBinLowEdge(coarse_bins_high[bin])+projX.GetBinWidth(coarse_bins_high[bin]))
    mjj_mean = getMean(h2D,coarse_bins_low[bin],coarse_bins_high[bin])
    mjj_error = (binH-binL)/2
    if bin == (len(coarse_bins_low)-2):
      mjj_mean = options.maxMVV-mjj_mean
    # if bin == 0:
    #   mjj_mean = options.minMVV
    if bin == (len(coarse_bins_low)-1):
      mjj_mean = options.maxMVV
    tmp = h2D.ProjectionY("mjjmean%i_binL%i_binH%i"%(mjj_mean,binL,binH),coarse_bins_low[bin],coarse_bins_high[bin])
    doFit(tmp,mjj_mean,mjj_error,bin)
    tmpfile.cd()
    tmp.Write()
  tmpfile.cd()
  h2D.Write()
  for name,graph in graphs.iteritems():
      graph.Write(name)
  tmpfile.Close()
  ff=ROOT.TFile(debug_out+options.output+".root","RECREATE")
  parametrizations = doParametrizations(graphs,ff)
  ff.Close()
  for name,param in parametrizations.iteritems():
    print name
    print param
    print "-------"
  f=open(options.output+".json","w")
  json.dump(parametrizations,f)
  f.close()
  print "Output name is %s" %options.output+".json"
  
  
  
