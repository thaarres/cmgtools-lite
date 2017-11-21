#!/usr/bin/env python
import os, re, copy
import commands
import math, time
import sys
import ROOT
from ROOT import *
import subprocess, thread

def waitForBatchJobs( jobname, remainingjobs, listOfJobs, userName, timeCheck):
	if listOfJobs-remainingjobs < listOfJobs:
	    time.sleep(float(timeCheck))
	    nprocess = "bjobs -u %s | awk {'print $8'} | grep %s | wc -l" %(userName,jobname)
	    result = subprocess.Popen(nprocess, stdout=subprocess.PIPE, shell=True)
	    runningJobs =  int(result.stdout.read())
	    print "waiting for %d job(s) in the queue (out of total %d)" %(runningJobs,listOfJobs)
	    waitForBatchJobs( jobname, runningJobs, listOfJobs, userName, timeCheck)  
	else:
		print "Jobs finished! Return to main script"
		return
        
def submitJobs(minEv,maxEv,cmd,OutputFileNames,queue,jobname):
	path = os.getcwd()
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
	      fout.write(cmd+" -o "+path+"/res/"+OutputFileNames+"_"+str(j+1)+"_"+k+" -s "+k+" -e "+str(minEv[k][j])+" -E "+str(maxEv[k][j])+"\n")
	      fout.write("echo 'STOP---------------'\n")
	      fout.write("echo\n")
	      fout.write("echo\n")
	   os.system("chmod 755 job_%s_%i.sh"%(k.replace(".root",""),j+1) )
	   os.system("bsub -q "+queue+" -o logs job_%s_%i.sh -J %s"%(k.replace(".root",""),j+1,jobname))
	   print "job nr " + str(j+1) + " file " + k + " being submitted"
	   os.chdir("../..")
		 
def getEvents():
	files = []
	for f in os.listdir('./samples'):
	 if f.find('.root') != -1 and f.find('QCD_Pt_300to470') != -1: files.append(f)

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


	NumberOfJobs = 0
	for k in maxEv.keys():
	 NumberOfJobs += len(maxEv[k])

	return minEv, maxEv, NumberOfJobs
	
def Make1DMVVTemplateWithKernels(rootFile,template,cut,resFile,binsMVV,minMVV,maxMVV,samples):
	
	print 
	print 'START: Make1DMVVTemplateWithKernels'
	print 

	minEv, maxEv, NumberOfJobs = getEvents() 
	print  NumberOfJobs

	#NumberOfJobs= len(files) # number of jobs to be submitted
	interval = 1 # number files to be processed in a single job, take care to split your file so that you run on all files. The last job might be with smaller number of files (the ones that remain).
	cmd='vvMake1DMVVTemplateWithKernels.py -H "x" -c "{cut}"  -v "jj_gen_partialMass" -b {binsMVV}  -x {minMVV} -X {maxMVV} -r {res} {infolder} '.format(rootFile=rootFile,cut=cut,res=resFile,binsMVV=binsMVV,minMVV=minMVV,maxMVV=maxMVV,infolder=samples)
	OutputFileNames = rootFile.replace(".root","") # base of the output file name, they will be saved in res directory
	queue = "8nh" # give bsub queue -- 8nm (8 minutes), 1nh (1 hour), 8nh, 1nd (1day), 2nd, 1nw (1 week), 2nw 
	########   customization end   #########
	print
	print 'do not worry about folder creation:'
	try: os.system("rm -r tmp")
	except: print "No tmp/ directory"
	os.system("mkdir tmp")
	try: os.stat("res") 
	except: os.mkdir("res")
	print

	#### Creating and sending jobs #####
	 
	jobname = "1DMVV"
	submitJobs(minEv,maxEv,cmd,OutputFileNames,queue,jobname)
	
	print
	print "your jobs:"
	os.system("bjobs")
	runningJobs =[]
	userName=os.environ['USER']
	waitForBatchJobs(jobname,NumberOfJobs,NumberOfJobs, userName, "10")
	
	  
	print
	print 'END: Make1DMVVTemplateWithKernels'
	print

def Make2DTemplateWithKernels(rootFile,template,cut,leg,binsMVV,minMVV,maxMVV,resFile,binsMJ,minMJ,maxMJ):
	
	print 
	print 'START: Make2DTemplateWithKernels'
	print 

	minEv, maxEv, NumberOfJobs = getEvents() 
	print  NumberOfJobs

	#NumberOfJobs= len(files) # number of jobs to be submitted
	interval = 1 # number files to be processed in a single job, take care to split your file so that you run on all files. The last job might be with smaller number of files (the ones that remain).
	cmd='vvMake2DTemplateWithKernels.py -c "{cut}"  -v "jj_{leg}_gen_softDrop_mass,jj_gen_partialMass"  -b {binsMJ} -B {binsMVV} -x {minMJ} -X {maxMJ} -y {minMVV} -Y {maxMVV}  -r {res} samples'.format(rootFile=rootFile,samples=template,cut=cut,leg=leg,binsMVV=binsMVV,minMVV=minMVV,maxMVV=maxMVV,res=resFile,binsMJ=binsMJ,minMJ=minMJ,maxMJ=maxMJ)
	OutputFileNames = rootFile # base of the output file name, they will be saved in res directory
	queue = "8nh" # give bsub queue -- 8nm (8 minutes), 1nh (1 hour), 8nh, 1nd (1day), 2nd, 1nw (1 week), 2nw 
	########   customization end   #########
	print
	print 'do not worry about folder creation:'
	try: os.system("rm -r tmp")
	except: print "No tmp/ directory"
	os.system("mkdir tmp")
	try: os.stat("res") 
	except: os.mkdir("res")
	print

	#### Creating and sending jobs #####
	 
	jobname = "2DMVV"
	submitJobs(minEv,maxEv,cmd,OutputFileNames,queue,jobname)
	
	print
	print "your jobs:"
	os.system("bjobs")
	runningJobs =[]
	userName=os.environ['USER']
	waitForBatchJobs(jobname,NumberOfJobs,NumberOfJobs, userName, "10")
	
	  
	print
	print 'END: Make2DTemplateWithKernels'
	print
		
def unequalScale(histo,name,alpha,power=1,dim=1):
    newHistoU =copy.deepcopy(histo) 
    newHistoU.SetName(name+"Up")
    newHistoD =copy.deepcopy(histo) 
    newHistoD.SetName(name+"Down")
    if dim == 2:
	    maxFactor = max(pow(histo.GetXaxis().GetXmax(),power),pow(histo.GetXaxis().GetXmin(),power))
	    for i in range(1,histo.GetNbinsX()+1):
	        x= histo.GetXaxis().GetBinCenter(i)
	        for j in range(1,histo.GetNbinsY()+1):
	            nominal=histo.GetBinContent(i,j)
	            factor = 1+alpha*pow(x,power) 
	            newHistoU.SetBinContent(i,j,nominal*factor)
	            newHistoD.SetBinContent(i,j,nominal/factor)
	    if newHistoU.Integral()>0.0:        
	        newHistoU.Scale(1.0/newHistoU.Integral())        
	    if newHistoD.Integral()>0.0:        
	        newHistoD.Scale(1.0/newHistoD.Integral())        
    else:
	    for i in range(1,histo.GetNbinsX()+1):
	        x= histo.GetXaxis().GetBinCenter(i)
	        nominal=histo.GetBinContent(i)
	        factor = 1+alpha*pow(x,power) 
	        newHistoU.SetBinContent(i,nominal*factor)
	        newHistoD.SetBinContent(i,nominal/factor)	
    return newHistoU,newHistoD 
    
def mirror(histo,histoNominal,name,dim=1):
    newHisto =copy.deepcopy(histoNominal) 
    newHisto.SetName(name)
    intNominal=histoNominal.Integral()
    intUp = histo.Integral()
    if dim == 2:
		for i in range(1,histo.GetNbinsX()+1):
			for j in range(1,histo.GetNbinsY()+1):
				up=histo.GetBinContent(i,j)/intUp
				nominal=histoNominal.GetBinContent(i,j)/intNominal
				newHisto.SetBinContent(i,j,histoNominal.GetBinContent(i,j)*nominal/up)
    else:
		for i in range(1,histo.GetNbinsX()+1):
			up=histo.GetBinContent(i)/intUp
			nominal=histoNominal.GetBinContent(i)/intNominal
			newHisto.SetBinContent(i,histoNominal.GetBinContent(i)*nominal/up)	
    return newHisto       

def expandHisto(histo,suffix):
    histogram=ROOT.TH2F(histo.GetName()+suffix,"histo",277,55,610,160,1000,7000)
    for i in range(1,histo.GetNbinsX()+1):
        proje = histo.ProjectionY("q",i,i)
        graph=ROOT.TGraph(proje)
        for j in range(1,histogram.GetNbinsY()+1):
            x=histogram.GetYaxis().GetBinCenter(j)
            bin=histogram.GetBin(i,j)
            histogram.SetBinContent(bin,graph.Eval(x,0,"S"))
    return histogram
        
def conditional(hist):
    for i in range(1,hist.GetNbinsY()+1):
        proj=hist.ProjectionX("q",i,i)
        integral=proj.Integral()
        if integral==0.0:
            print 'SLICE WITH NO EVENTS!!!!!!!!',hist.GetName()
            continue
        for j in range(1,hist.GetNbinsX()+1):
            hist.SetBinContent(j,i,hist.GetBinContent(j,i)/integral)

def merge1DMVVTemplate():
	# read out files
	filelist = os.listdir('./res')

	mg_files = []
	pythia_files = []
	herwig_files = []

	for f in filelist:
	 if f.find('QCD_HT') != -1: mg_files.append('./res/'+f)
	 elif f.find('QCD_Pt_') != -1: pythia_files.append('./res/'+f)
	 else: herwig_files.append('./res/'+f)

	#now hadd them
	cmd = 'hadd -f JJ_nonRes_MVV_HPHP_altshape2.root '
	for f in mg_files:
	 cmd += f
	 cmd += ' '
	print cmd
	os.system(cmd)

	cmd = 'hadd -f JJ_nonRes_MVV_HPHP_altshapeUp.root '
	for f in herwig_files:
	 cmd += f
	 cmd += ' '
	print cmd
	os.system(cmd)
 
	cmd = 'hadd -f JJ_nonRes_MVV_HPHP_nominal.root '
	for f in pythia_files:
	 cmd += f
	 cmd += ' '
	print cmd
	os.system(cmd)

	#now retrieve histos
	fhadd_madgraph = ROOT.TFile.Open('JJ_nonRes_MVV_HPHP_altshape2.root','READ')
	fhadd_herwig = ROOT.TFile.Open('JJ_nonRes_MVV_HPHP_altshapeUp.root','READ')
	fhadd_pythia = ROOT.TFile.Open('JJ_nonRes_MVV_HPHP_nominal.root','READ')

	mvv_nominal = fhadd_pythia.Get('mvv_nominal')
	histo_nominal = fhadd_pythia.Get('histo_nominal')
	#histo_nominal_ScaleUp = fhadd_pythia.Get('histo_nominal_ScaleUp')
	#histo_nominal_ScaleDown = fhadd_pythia.Get('histo_nominal_ScaleDown')

	mvv_altshapeUp = fhadd_herwig.Get('mvv_nominal')
	histo_altshapeUp = fhadd_herwig.Get('histo_nominal')
	#histo_altshape_ScaleUp = fhadd_herwig.Get('histo_nominal_ScaleUp')
	#histo_altshape_ScaleDown = fhadd_herwig.Get('histo_nominal_ScaleDown')

	mvv_altshape2 = fhadd_madgraph.Get('mvv_nominal')
	histo_altshape2 = fhadd_madgraph.Get('histo_nominal')


	#save everything in the final out file after renaming and do usual operations on histos
	outf = ROOT.TFile.Open('JJ_nonRes_MVV_HPHP.root','RECREATE') 

	mvv_nominal.Write('mvv_nominal')
	histo_nominal.Write('histo_nominal')
	#histo_nominal_ScaleUp.Write('histo_nominal_ScaleUp')
	#histo_nominal_ScaleDown.Write('histo_nominal_ScaleDown')
	mvv_altshapeUp.Write('mvv_altshapeUp')
	histo_altshapeUp.Write('histo_altshapeUp')
	#histo_altshape_ScaleUp.Write('histo_altshape_ScaleUp')
	#histo_altshape_ScaleDown.Write('histo_altshape_ScaleDown')
	mvv_altshape2.Write('mvv_altshape2')
	histo_altshape2.Write('histo_altshape2')

	histogram_altshapeDown=mirror(histo_altshapeUp,histo_nominal,"histo_altshapeDown",1)
	histogram_altshapeDown.Write('histo_altshapeDown')

	alpha=1.5/5000
	histogram_pt_down,histogram_pt_up=unequalScale(histo_nominal,"histo_nominal_PT",alpha,1,1)
	histogram_pt_down.Write()
	histogram_pt_up.Write()

	alpha=1.5*1000
	histogram_opt_down,histogram_opt_up=unequalScale(histo_nominal,"histo_nominal_OPT",alpha,-1,1)
	histogram_opt_down.Write()
	histogram_opt_up.Write()	

def merge2DTemplate():  
	# read out files
	filelist = os.listdir('./res/')

	mg_files = []
	pythia_files = []
	herwig_files = []

	for f in filelist:
	 if f.find('COND2D') == -1: continue
	 if f.find('QCD_HT') != -1: mg_files.append('./res/'+f)
	 elif f.find('QCD_Pt_') != -1: pythia_files.append('./res/'+f)
	 else: herwig_files.append('./res/'+f)

	#now hadd them
	cmd = 'hadd -f JJ_nonRes_COND2D_HPHP_l2_altshape2.root '
	for f in mg_files:
	 cmd += f
	 cmd += ' '
	print cmd
	os.system(cmd)

	cmd = 'hadd -f JJ_nonRes_COND2D_HPHP_l2_altshapeUp.root '
	for f in herwig_files:
	 cmd += f
	 cmd += ' '
	print cmd
	os.system(cmd)
 
	cmd = 'hadd -f JJ_nonRes_COND2D_HPHP_l2_nominal.root '
	for f in pythia_files:
	 cmd += f
	 cmd += ' '
	print cmd
	os.system(cmd)

	#now retrieve histos
	fhadd_madgraph = ROOT.TFile.Open('JJ_nonRes_COND2D_HPHP_l2_altshape2.root','READ')
	fhadd_herwig = ROOT.TFile.Open('JJ_nonRes_COND2D_HPHP_l2_altshapeUp.root','READ')
	fhadd_pythia = ROOT.TFile.Open('JJ_nonRes_COND2D_HPHP_l2_nominal.root','READ')

	mjet_mvv_nominal_3D = fhadd_pythia.Get('mjet_mvv_nominal_3D') 
	mjet_mvv_nominal = fhadd_pythia.Get('mjet_mvv_nominal')
	histo_nominal = fhadd_pythia.Get('histo_nominal_coarse')
	#histo_nominal_ScaleUp = fhadd_pythia.Get('histo_nominal_ScaleUp_coarse')
	#histo_nominal_ScaleDown = fhadd_pythia.Get('histo_nominal_ScaleDown_coarse')

	#mjet_mvv_nominal = fhadd_madgraph.Get('mjet_mvv_nominal')
	#histo_nominal = fhadd_madgraph.Get('histo_nominal_coarse')
	#histo_nominal_ScaleUp = fhadd_madgraph.Get('histo_nominal_ScaleUp_coarse')
	#histo_nominal_ScaleDown = fhadd_madgraph.Get('histo_nominal_ScaleDown_coarse')

	mjet_mvv_altshapeUp_3D = fhadd_herwig.Get('mjet_mvv_nominal_3D') 
	mjet_mvv_altshapeUp = fhadd_herwig.Get('mjet_mvv_nominal')
	histo_altshapeUp = fhadd_herwig.Get('histo_nominal_coarse')
	#histo_altshape_ScaleUp = fhadd_herwig.Get('histo_nominal_ScaleUp_coarse')
	#histo_altshape_ScaleDown = fhadd_herwig.Get('histo_nominal_ScaleDown_coarse')

	mjet_mvv_altshape2_3D = fhadd_madgraph.Get('mjet_mvv_nominal_3D') 
	mjet_mvv_altshape2 = fhadd_madgraph.Get('mjet_mvv_nominal')
	histo_altshape2 = fhadd_madgraph.Get('histo_nominal_coarse')

	#mjet_mvv_altshape2 = fhadd_pythia.Get('mjet_mvv_nominal')
	#histo_altshape2 = fhadd_pythia.Get('histo_nominal_coarse')

	#save everything in the final out file after renaming and do usual operations on histos
	outf = ROOT.TFile.Open('JJ_nonRes_COND2D_HPHP_l2.root','RECREATE') 

	mjet_mvv_nominal.Write('mjet_mvv_nominal')
	mjet_mvv_altshapeUp.Write('mjet_mvv_altshapeUp')
	mjet_mvv_altshape2.Write('mjet_mvv_altshape2')
	mjet_mvv_nominal_3D.Write('mjet_mvv_nominal_3D')
	mjet_mvv_altshapeUp_3D.Write('mjet_mvv_altshapeUp_3D')
	mjet_mvv_altshape2_3D.Write('mjet_mvv_altshape2_3D')

	finalHistograms = {}

	histo_nominal.Write('histo_nominal_coarse')
	conditional(histo_nominal)
	expanded=expandHisto(histo_nominal,"")
	conditional(expanded)
	expanded.Write('histo_nominal')
	finalHistograms['histo_nominal'] = expanded

	#histo_nominal_ScaleUp.Write('histo_nominal_ScaleUp_coarse')
	#conditional(histo_nominal_ScaleUp)
	#expanded=expandHisto(histo_nominal_ScaleUp)
	#conditional(expanded)
	#expanded.Write('histo_nominal_ScaleUp')

	#histo_nominal_ScaleDown.Write('histo_nominal_ScaleDown_coarse')
	#conditional(histo_nominal_ScaleDown)
	#expanded=expandHisto(histo_nominal_ScaleDown)
	#conditional(expanded)
	#expanded.Write('histo_nominal_ScaleDown')

	histo_altshapeUp.Write('histo_altshapeUp_coarse')
	conditional(histo_altshapeUp)
	expanded=expandHisto(histo_altshapeUp,"herwig")
	conditional(expanded)
	expanded.Write('histo_altshapeUp')
	finalHistograms['histo_altshapeUp'] = expanded

	#histo_altshape_ScaleUp.Write('histo_altshape_ScaleUp_coarse')
	#conditional(histo_altshape_ScaleUp)
	#expanded=expandHisto(histo_altshape_ScaleUp)
	#conditional(expanded)
	#expanded.Write('histo_altshape_ScaleUp')

	#histo_altshape_ScaleDown.Write('histo_altshape_ScaleDown_coarse')
	#conditional(histo_altshape_ScaleDown)
	#expanded=expandHisto(histo_altshape_ScaleDown)
	#conditional(expanded)
	#expanded.Write('histo_altshape_ScaleDown')

	histo_altshape2.Write('histo_altshape2_coarse')
	conditional(histo_altshape2)
	expanded=expandHisto(histo_altshape2,"madgraph")
	conditional(expanded)
	expanded.Write('histo_altshape2')

	histogram_altshapeDown=mirror(finalHistograms['histo_altshapeUp'],finalHistograms['histo_nominal'],"histo_altshapeDown",2)
	conditional(histogram_altshapeDown)
	histogram_altshapeDown.Write()

	alpha=1.5/610.
	histogram_pt_down,histogram_pt_up=unequalScale(finalHistograms['histo_nominal'],"histo_nominal_PT",alpha,1,2)
	conditional(histogram_pt_down)
	histogram_pt_down.Write()
	conditional(histogram_pt_up)
	histogram_pt_up.Write()

	alpha=1.5*55.
	h1,h2=unequalScale(finalHistograms['histo_nominal'],"histo_nominal_OPT",alpha,-1,2)
	conditional(h1)
	h1.Write()
	conditional(h2)
	h2.Write()

	outf.Close()	