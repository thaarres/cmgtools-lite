#!/usr/bin/env python

import ROOT
from array import array
from CMGTools.VVResonances.plotting.TreePlotter import TreePlotter
from CMGTools.VVResonances.plotting.MergedPlotter import MergedPlotter
from CMGTools.VVResonances.plotting.StackPlotter import StackPlotter
from CMGTools.VVResonances.statistics.Fitter import Fitter
from math import log
import os, sys, re, optparse,pickle,shutil,json
# ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
from time import sleep

parser = optparse.OptionParser()
parser.add_option("-s","--sample",dest="sample",default='',help="Type of sample")
parser.add_option("-c","--cut",dest="cut",help="Cut to apply for shape",default='')
parser.add_option("-o","--output",dest="output",help="Output JSON",default='')
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
  histo2D_l1 = mergedPlotter.drawTH2("jj_l1_softDrop_mass:jj_LV_mass",options.cut,"1",40,options.minMVV,options.maxMVV,40,options.mini,options.maxi) #y:x
  histo2D_l2 = mergedPlotter.drawTH2("jj_l2_softDrop_mass:jj_LV_mass",options.cut,"1",40,options.minMVV,options.maxMVV,40,options.mini,options.maxi)  
  histo2D_l1.Add(histo2D_l2)
  histo2D_l1.Scale(float(lumi_))
  return histo2D_l1

def doFit(th1_projY,mjj_mean,mjj_error,N):
  
  fitter=Fitter(['x'])
  fitter.erfexp2Gaus('model','x')
  if N == 0:
    fitter.w.var("mean1").setVal(82.6)
    fitter.w.var("mean1").setMin(75.6)
    fitter.w.var("mean1").setMax(92.6)

    fitter.w.var("mean2").setVal(170.)
    fitter.w.var("mean2").setMin(155.6)
    fitter.w.var("mean2").setMax(190.6)

    fitter.w.var("sigma1").setVal(7.6)
    fitter.w.var("sigma1").setMin(6)
    fitter.w.var("sigma1").setMax(10)
    fitter.w.var("sigma2").setVal(10)
    fitter.w.var("sigma2").setMin(8)
    fitter.w.var("sigma2").setMax(12)

    fitter.w.var("c_0").setVal(-2.7180e-02)
    fitter.w.var("c_1").setVal(86.) #Offset
    fitter.w.var("c_2").setVal(36.) #Width
    fitter.w.var("c_1").setMin(46.)
    fitter.w.var("c_2").setMin(16.)
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
  fitter.projection("model","data","x","debugTT_bin%i.pdf"%N,0,False,"m_{jet}")
  
  
  for var,graph in graphs.iteritems():
      value,error=fitter.fetch(var)
      graph.SetPoint(N,mjj_mean,value)
      graph.SetPointError(N,0.0,error) #No error x
      # graph.SetPointError(N,mjj_error,error) #error x is number of bins in mVV
      
  fitter.delete()    

def doParametrizations(graphs,ff):
  ff.cd()
  parametrizations = {}
  for var,graph in graphs.iteritems():
    func=ROOT.TF1(var+"_func","pol1",0,13000)
    graph.Fit(func,"","",options.minMVV,options.maxMVV)
    graph.Write(var)
    func.Write(var+"_func")
    c = ROOT.TCanvas()
    graph.Draw()
    c.SaveAs("debug_"+options.output+"_"+var+".png")
    
    
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
  
  coarse_bins_low  = [1,3,5,8,8]
  coarse_bins_high = [2,4,7,39,39]
  projX = h2D.ProjectionX()
  for bin in range(0,len(coarse_bins_low)): #h2D_mjet1mjet2.GetNbinsX()):
    print "Projecting bin %i to %i out of total N=%i bins"%(coarse_bins_low[bin],coarse_bins_high[bin],h2D.GetNbinsX())
    binL = float(projX.GetBinCenter(coarse_bins_low[bin]))
    binH = float(projX.GetBinCenter(coarse_bins_high[bin]))
    mjj_mean = (binH+binL)/2.
    if bin == 0:
      mjj_mean = options.minMVV
    mjj_error = (binH-binL)/2
    tmp = h2D.ProjectionY("bin_%i"%(mjj_mean),coarse_bins_low[bin],coarse_bins_high[bin])
    doFit(tmp,mjj_mean,mjj_error,bin)
    if bin == (len(coarse_bins_low)-1):
      mjj_mean = options.maxMVV
      tmp = h2D.ProjectionY("bin_%i"%(mjj_mean),coarse_bins_low[bin],coarse_bins_high[bin])
      doFit(tmp,mjj_mean,mjj_error,bin)
    tmpfile.cd()
    tmp.Write()
  tmpfile.cd()
  h2D.Write()
  for name,graph in graphs.iteritems():
      graph.Write(name)
  tmpfile.Close()
  ff=ROOT.TFile("debug_"+options.output+".root","RECREATE")
  parametrizations = doParametrizations(graphs,ff)
  ff.Close()
  for name,param in parametrizations.iteritems():
    print name
    print param
    print "-------"
  f=open(options.output.replace(".root",""),"w")
  json.dump(parametrizations,f)
  f.close()
  print "Output name is %s" %options.output
  
  
  
