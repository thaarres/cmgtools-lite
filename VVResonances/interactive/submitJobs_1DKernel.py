#!/usr/bin/env python
import os, re
import commands
import math, time
import sys
import ROOT
from ROOT import *

print 
print 'START'
print 
########   YOU ONLY NEED TO FILL THE AREA BELOW   #########
########   customization  area #########
files = []
for f in os.listdir('./samples'):
 if f.find('.root') != -1 and f.find('QCD') != -1: files.append(f)

minEv = {}
maxEv = {}

for f in files:
 inf = ROOT.TFile('./samples/'+f,'READ')
 minEv[f] = []
 maxEv[f] = []
 intree = inf.Get('tree')
 nentries = intree.GetEntries()
 print f,nentries,nentries/500000
 if nentries/500000 == 0:
  minEv[f].append(0)
  maxEv[f].append(500000)
 else:
  for i in range(nentries/500000):
   minEv[f].append(i*500000)
   maxEv[f].append(499999)
#print minEv
#print
#print maxEv

NumberOfJobs = 0
for k in maxEv.keys():
 NumberOfJobs += len(maxEv[k])

print NumberOfJobs
 
#NumberOfJobs= len(files) # number of jobs to be submitted
interval = 1 # number files to be processed in a single job, take care to split your file so that you run on all files. The last job might be with smaller number of files (the ones that remain).
OutputFileNames = "JJ_nonRes_MVV_HPHP" # base of the output file name, they will be saved in res directory
ScriptName = "vvMake1DMVVTemplateWithKernels.py"
options = ' -H "x"'
options+= ' -c "((HLT_JJ)*(run>500) + (run<500))*(njj>0&&Flag_goodVertices&&Flag_CSCTightHaloFilter&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_eeBadScFilter&&jj_LV_mass>700&&abs(jj_l1_eta-jj_l2_eta)<1.3&&jj_l1_softDrop_mass>0.&&jj_l2_softDrop_mass>0.)*(jj_l1_tau2/jj_l1_tau1<0.35&&jj_l2_tau2/jj_l2_tau1<0.35)*1*(jj_l1_gen_softDrop_mass>0&&jj_l2_gen_softDrop_mass>0&&jj_gen_partialMass>0)*(jj_l1_softDrop_mass>55.0&&jj_l1_softDrop_mass<215.0&&jj_l2_softDrop_mass>55.0&&jj_l2_softDrop_mass<215.0)"'
options+= ' -v "jj_gen_partialMass" -b 100  -x 1000.0 -X 5000.0'
options+= ' -r /afs/cern.ch/user/j/jngadiub/workdir/VVAnalysisWith2DFit/CMGToolsForStat74X/CMSSW_7_4_7/src/CMGTools/VVResonances/interactive/JJ_nonRes_detectorResponse_HPHP.root'
options+= ' /afs/cern.ch/user/j/jngadiub/workdir/VVAnalysisWith2DFit/CMGToolsForStat74X/CMSSW_7_4_7/src/CMGTools/VVResonances/interactive/samples'
#FileList = "List.txt" # list with all the file directories
queue = "8nh" # give bsub queue -- 8nm (8 minutes), 1nh (1 hour), 8nh, 1nd (1day), 2nd, 1nw (1 week), 2nw 
########   customization end   #########

path = os.getcwd()
print
print 'do not worry about folder creation:'
os.system("rm -r tmp")
os.system("mkdir tmp")
os.system("mkdir res")
print

##### loop for creating and sending jobs #####
#for x in range(1, int(NumberOfJobs)+1):
for k,v in minEv.iteritems():
  ##### creates directory and file list for job #######
  for j in range(len(v)):
   os.system("mkdir tmp/"+str(k).replace(".root","")+"_"+str(j+1))
   os.chdir("tmp/"+str(k).replace(".root","")+"_"+str(j+1))
   #os.system("sed '"+str(1+interval*(x-1))+","+str(interval*x)+"!d' ../../"+FileList+" > list.txt ")
   
   ##### creates jobs #######
   with open('job_%s_%i.sh'%(k.replace(".root",""),j+1), 'w') as fout:
      fout.write("#!/bin/sh\n")
      fout.write("echo\n")
      fout.write("echo\n")
      fout.write("echo 'START---------------'\n")
      fout.write("echo 'WORKDIR ' ${PWD}\n")
      fout.write("source /afs/cern.ch/cms/cmsset_default.sh\n")
      fout.write("cd "+str(path)+"\n")
      fout.write("cmsenv\n")
      fout.write(ScriptName+options+" -o res/"+OutputFileNames+"_"+str(j+1)+"_"+k+" -s "+k+" -e "+str(minEv[k][j])+" -E "+str(maxEv[k][j])+"\n")
      #fout.write("cmsRun "+ScriptName+" outputFile='res/"+OutputFileNames+"_"+str(x)+".root' inputFiles_clear inputFiles_load='tmp/"+str(x)+"/list.txt'\n")
      fout.write("echo 'STOP---------------'\n")
      fout.write("echo\n")
      fout.write("echo\n")
   os.system("chmod 755 job_%s_%i.sh"%(k.replace(".root",""),j+1) )
   
   ###### sends bjobs ######
   os.system("bsub -q "+queue+" -o logs job_%s_%i.sh"%(k.replace(".root",""),j+1))
   print "job nr " + str(j+1) + " file " + k + " submitted"
   
   os.chdir("../..")
   
print
print "your jobs:"
os.system("bjobs")
print
print 'END'
print
