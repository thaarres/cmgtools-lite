#!/usr/bin/env python
import os, re
import commands
import math, time
import sys
#vvMakeData.py -s "QCD_Pt_" -d 0 -c "((HLT_JJ)*(run>500) + (run<500))*(njj>0&&Flag_goodVertices&&Flag_CSCTightHaloFilter&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_eeBadScFilter&&jj_LV_mass>700&&abs(jj_l1_eta-jj_l2_eta)<1.3&&jj_l1_softDrop_mass>0.&&jj_l2_softDrop_mass>0.)*(jj_l1_tau2/jj_l1_tau1<0.35&&jj_l2_tau2/jj_l2_tau1<0.35)*1*(jj_LV_mass>1000.0&&jj_LV_mass<7000.0&&jj_l1_softDrop_mass>55.0&&jj_l1_softDrop_mass<610.0&&jj_l2_softDrop_mass>55.0&&jj_l2_softDrop_mass<610.0)"  -o "JJ_HPHP.root" -v "jj_l1_softDrop_mass,jj_l2_softDrop_mass,jj_LV_mass" -b "277,277,160" -m "55.0,55.0,1000.0" -M "610.0,610.0,7000.0" -f 1.0 -n "nonres"  samples

print 
print 'START'
print 
########   YOU ONLY NEED TO FILL THE AREA BELOW   #########
########   customization  area #########
files = []
for f in os.listdir('./samples'):
 if f.find('.root') != -1 and f.find('QCD') != -1: files.append(f)
 
NumberOfJobs= len(files) # number of jobs to be submitted
interval = 1 # number files to be processed in a single job, take care to split your file so that you run on all files. The last job might be with smaller number of files (the ones that remain).
OutputFileNames = "JJ_HPHP" # base of the output file name, they will be saved in res directory
ScriptName = "vvMakeData.py"
options = ' -d 0'
options+= ' -c "((HLT_JJ)*(run>500) + (run<500))*(njj>0&&Flag_goodVertices&&Flag_CSCTightHaloFilter&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_eeBadScFilter&&jj_LV_mass>700&&abs(jj_l1_eta-jj_l2_eta)<1.3&&jj_l1_softDrop_mass>0.&&jj_l2_softDrop_mass>0.)*(jj_l1_tau2/jj_l1_tau1<0.35&&jj_l2_tau2/jj_l2_tau1<0.35)*1*(jj_LV_mass>1000.0&&jj_LV_mass<5000.0&&jj_l1_softDrop_mass>55.0&&jj_l1_softDrop_mass<215.0&&jj_l2_softDrop_mass>55.0&&jj_l2_softDrop_mass<215.0)"'
options+= ' -v "jj_l2_softDrop_mass,jj_l1_softDrop_mass,jj_LV_mass" -b "80,80,100" -m "55.0,55.0,1000.0" -M "215.0,215.0,5000.0" -f 1.0 -n "nonRes"'
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
for x in range(1, int(NumberOfJobs)+1):
   ##### creates directory and file list for job #######
   os.system("mkdir tmp/"+str(files[x-1]).replace(".root",""))
   os.chdir("tmp/"+str(files[x-1]).replace(".root",""))
   #os.system("sed '"+str(1+interval*(x-1))+","+str(interval*x)+"!d' ../../"+FileList+" > list.txt ")
   
   ##### creates jobs #######
   with open('job_%s.sh'%files[x-1].replace(".root",""), 'w') as fout:
      fout.write("#!/bin/sh\n")
      fout.write("echo\n")
      fout.write("echo\n")
      fout.write("echo 'START---------------'\n")
      fout.write("echo 'WORKDIR ' ${PWD}\n")
      fout.write("source /afs/cern.ch/cms/cmsset_default.sh\n")
      fout.write("cd "+str(path)+"\n")
      fout.write("cmsenv\n")
      fout.write(ScriptName+options+" -o res/"+OutputFileNames+"_"+files[x-1]+" -s "+files[x-1]+"\n")
      #fout.write("cmsRun "+ScriptName+" outputFile='res/"+OutputFileNames+"_"+str(x)+".root' inputFiles_clear inputFiles_load='tmp/"+str(x)+"/list.txt'\n")
      fout.write("echo 'STOP---------------'\n")
      fout.write("echo\n")
      fout.write("echo\n")
   os.system("chmod 755 job_%s.sh"%(files[x-1].replace(".root","")) )
   
   ###### sends bjobs ######
   os.system("bsub -q "+queue+" -o logs job_%s.sh"%(files[x-1].replace(".root","")))
   print "job nr " + str(x) + " submitted"
   
   os.chdir("../..")
   
print
print "your jobs:"
os.system("bjobs")
print
print 'END'
print
