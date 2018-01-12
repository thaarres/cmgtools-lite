#!/usr/bin/env python
import ROOT
from array import array
from CMGTools.VVResonances.statistics.Fitter import Fitter
from math import log
import os, sys, re, optparse,pickle,shutil,json
import json
from CMGTools.VVResonances.plotting.tdrstyle import *
setTDRStyle()
from CMGTools.VVResonances.plotting.TreePlotter import TreePlotter
from CMGTools.VVResonances.plotting.MergedPlotter import MergedPlotter

parser = optparse.OptionParser()
parser.add_option("-o","--output",dest="output",help="Output",default='')
parser.add_option("-s","--samples",dest="samples",default='',help="Type of sample")
parser.add_option("-c","--cut",dest="cut",help="Cut to apply for yield in gen sample",default='')
parser.add_option("-v","--vars",dest="vars",help="variable for gen",default='')
parser.add_option("-b","--binsx",dest="binsx",help="bins",default='')
parser.add_option("-g","--genVars",dest="genVars",help="variable for gen",default='')
parser.add_option("-e","--firstEv",dest="firstEv",type=int,help="first event",default=0)
parser.add_option("-E","--lastEv",dest="lastEv",type=int,help="last event",default=-1)



(options,args) = parser.parse_args()


sampleTypes=options.samples.split(',')
dataPlotters=[]

for filename in os.listdir(args[0]):
    for sampleType in sampleTypes:
        if filename.find(sampleType)!=-1:
            fnameParts=filename.split('.')
            fname=fnameParts[0]
            ext=fnameParts[1]
            if ext.find("root") ==-1:
                continue
            dataPlotters.append(TreePlotter(args[0]+'/'+fname+'.root','tree'))
            dataPlotters[-1].setupFromFile(args[0]+'/'+fname+'.pck')
            dataPlotters[-1].addCorrectionFactor('xsec','tree')
            dataPlotters[-1].addCorrectionFactor('genWeight','tree')
            dataPlotters[-1].addCorrectionFactor('puWeight','tree')
data=MergedPlotter(dataPlotters)



binsxStr=options.binsx.split(',')
binsx=[]
for b in binsxStr:
    binsx.append(float(b))

binsz=[]
for b in range(0,51):
    binsz.append(0.7+0.7*b/50.0)

binsDijet = [800, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530,1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019,3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455,5663, 5877, 6099, 6328, 6564, 6808]
varDijet = 'jj_gen_partialMass'

scalexHisto=ROOT.TH1F("scalexHisto","scaleHisto",len(binsx)-1,array('d',binsx))
resxHisto=ROOT.TH1F("resxHisto","resHisto",len(binsx)-1,array('d',binsx))
scaleyHisto=ROOT.TH1F("scaleyHisto","scaleHisto",len(binsx)-1,array('d',binsx))
resyHisto=ROOT.TH1F("resyHisto","resHisto",len(binsx)-1,array('d',binsx))

# scalexHisto=ROOT.TH1F("scalexHisto","scaleHisto",len(binsDijet)-1,array('d',binsDijet))
# resxHisto=ROOT.TH1F("resxHisto","resHisto",len(binsDijet)-1,array('d',binsDijet))
# scaleyHisto=ROOT.TH1F("scaleyHisto","scaleHisto",len(binsDijet)-1,array('d',binsDijet))
# resyHisto=ROOT.TH1F("resyHisto","resHisto",len(binsDijet)-1,array('d',binsDijet))

variables=options.vars.split(',')
genVariables=options.genVars.split(',')


gaussian=ROOT.TF1("gaussian","gaus",0.5,1.5)


f=ROOT.TFile(options.output,"RECREATE")
f.cd()

superHX=data.drawTH2Binned(variables[0]+'/'+genVariables[0]+':'+genVariables[2],options.cut,"1",binsx,binsz) #dijet
superHY=data.drawTH2Binned(variables[1]+'/'+genVariables[1]+':'+genVariables[2],options.cut,"1",binsx,binsz) #mjet
# superHX=data.drawTH2Binned(variables[0]+'/'+genVariables[0]+':'+varDijet,options.cut,"1",binsDijet,binsz) #dijet
# superHY=data.drawTH2Binned(variables[1]+'/'+genVariables[1]+':'+varDijet,options.cut,"1",binsDijet,binsz) #mjet

for bin in range(1,superHX.GetNbinsX()+1):

    tmp=superHX.ProjectionY("q",bin,bin)
    scalexHisto.SetBinContent(bin,tmp.GetMean())
    scalexHisto.SetBinError(bin,tmp.GetMeanError())
    resxHisto.SetBinContent(bin,tmp.GetRMS())
    resxHisto.SetBinError(bin,tmp.GetRMSError())

    tmp=superHY.ProjectionY("q",bin,bin)
    scaleyHisto.SetBinContent(bin,tmp.GetMean())
    scaleyHisto.SetBinError(bin,tmp.GetMeanError())
    resyHisto.SetBinContent(bin,tmp.GetRMS())
    resyHisto.SetBinError(bin,tmp.GetRMSError())

        
scalexHisto.Write()
scaleyHisto.Write()
resxHisto.Write()
resyHisto.Write()
superHX.Write("dataX")
superHY.Write("dataY")
f.Close()    
