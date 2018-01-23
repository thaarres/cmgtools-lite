import ROOT
ROOT.gROOT.SetBatch(True)
import os, sys, re, optparse,pickle,shutil,json

parser = optparse.OptionParser()
parser.add_option("-o","--output",dest="output",help="Output ROOT File",default='')
parser.add_option("-i","--infile",dest="infile",help="Input ROOT File",default='')
parser.add_option("--oneD",dest="OneD",help="do 1D smoothing",default=0)
parser.add_option("--threeD",dest="ThreeD",help="do 3D smoothing",default=0)


(options,args) = parser.parse_args()


def smoothTail(proj,hist3D,xbin,ybin):#,xmin,xmax,ymin,ymax):
    if proj.Integral() == 0:
        print "histogram has zero integral "+proj.GetName()
        return 0
    scale = proj.Integral() 
    proj.Scale(1.0/scale)
    
    beginFit = proj.GetBinLowEdge( proj.GetMaximumBin() )
    beginFitX = beginFit + 1500. * 1/(beginFit/1000.)
    #beginFitX = beginFit + 800. * 1/(beginFit/1000.)
    print beginFit
    print beginFitX
    #beginFitX=beginFit
   #expo=ROOT.TF1("expo","expo",beginFitX,8000)
    expo=ROOT.TF1("expo","[0]*(1-x/13000.)^[1]/(x/13000)^[2]",2000,8000) 
    expo.SetParameters(0,16.,2.)
    expo.SetParLimits(2,1.,20.)
    proj.Fit(expo,"LLMR","",beginFitX,8000)
    #c = ROOT.TCanvas("c","c",400,400)
    #c.SetLogy()
    #proj.Draw("hist")
    #proj.Draw("funcsame")
    #c.SaveAs(proj.GetName()+"_binX"+str(xbin)+"binY"+str(ybin)+".pdf")
    beginsmooth = False
    print proj.GetNbinsX()+1
    for j in range(1,proj.GetNbinsX()+1):
        x=proj.GetXaxis().GetBinCenter(j)
        if x>beginFitX:
            if beginsmooth==False:
               if x<3000: 
                   if abs(proj.GetBinContent(j) - expo.Eval(x)) < 0.00009:# and abs(expo.Derivative(x)- (hist.GetBinContent(j):
                    #print beginFitX
                    #print "begin smoothing at " +str(x)
                    beginsmooth = True 
               if abs(proj.GetBinContent(j) - expo.Eval(x)) < 0.00001:# and abs(expo.Derivative(x)- (hist.GetBinContent(j):
                   #print beginFitX
                   #print "begin smoothing at " +str(x)
                   beginsmooth = True 
            if beginsmooth:
                hist3D.SetBinContent(xbin,ybin,j,expo.Eval(x)*scale)
    return 1


def smoothTail1D(proj):
    if proj.Integral() == 0:
        print "histogram has zero integral "+proj.GetName()
        return 0
    scale = proj.Integral() 
    proj.Scale(1.0/scale)
    
    
    beginFitX = 1000
    expo=ROOT.TF1("expo","[0]*(1-x/13000.)^[1]/(x/13000)^[2]",2000,8000) 
    expo.SetParameters(0,16.,2.)
    expo.SetParLimits(2,1.,20.)
    proj.Fit(expo,"LLMR","",beginFitX,8000)
    c = ROOT.TCanvas("c","c",400,400)
    c.SetLogy()
    proj.Draw("hist")
    proj.Draw("funcsame")
    c.SaveAs(proj.GetName()+".pdf")
    beginsmooth = False
    print proj.GetNbinsX()+1
    for j in range(1,proj.GetNbinsX()+1):
        x=proj.GetXaxis().GetBinCenter(j)
        if x>beginFitX:
            if beginsmooth==False:
               if x<3000: 
                   if abs(proj.GetBinContent(j) - expo.Eval(x)) < 0.00009:# and abs(expo.Derivative(x)- (hist.GetBinContent(j):
                    print beginFitX
                    print "begin smoothing at " +str(x)
                    beginsmooth = True 
               if abs(proj.GetBinContent(j) - expo.Eval(x)) < 0.00001:# and abs(expo.Derivative(x)- (hist.GetBinContent(j):
                   print beginFitX
                   print "begin smoothing at " +str(x)
                   beginsmooth = True 
            if beginsmooth:
                proj.SetBinContent(j,expo.Eval(x))
    return 1




def getXbin( xmin,xmax):
    bins = []
    for i in range(xmin,xmax):
        bins.append(xmin + i)
    return bins
    
    


if __name__=='__main__':
    print options.ThreeD
    
    # try smoothing 3D histogram in each bin ######################################
    if options.ThreeD ==str(1):
        fromkernel =  options.infile
        f2 = ROOT.TFile(fromkernel,"READ")
        
        names = ["histo","histo_PTXYUp","histo_PTXYDown","histo_PTZUp","histo_PTZDown","histo_OPTXYUp","histo_OPTXYDown","histo_OPTZUp", "histo_OPTZDown"]
        histograms = []
        for n in names:
            histograms.append(f2.Get(n))  
    
        nameOutputFile=options.output
        print "make output root file "+nameOutputFile
        output=ROOT.TFile(nameOutputFile,"RECREATE")
    
        for kernelHisto in histograms:
            Ny = kernelHisto.GetNbinsY()
            Nx = kernelHisto.GetNbinsX()
            Nz = kernelHisto.GetNbinsY()
            
            for x in range(1,Nx+1):
                for y in range(1,Ny+1):
                    p = kernelHisto.ProjectionZ("tmp",x,x,y,y)
                    smoothTail(p,kernelHisto,x,y)
        
            kernelHisto.Write()
        names2 = ["histo_PTXYUp","histo_PTXYDown","histo_PTZUp","histo_PTZDown","histo_OPTXYUp","histo_OPTXYDown","histo_OPTZUp", "histo_OPTZDown"]
        histograms = []
        for n in names2:
            smoothed =0
            for o in names:
                if n==o:
                    smoothed=1
            if smoothed:
                continue
            histograms.append(f2.Get(n))
            histograms[-1].Write()
        output.Close()
        
    
    #################################################################################################
    if options.OneD ==str(1):
        fromkernel =  options.infile
        f2 = ROOT.TFile(fromkernel,"READ")
        
        names = ["histo_nominal","histo_nominal_PTUp","histo_nominal_PTDown","histo_nominal_OPTUp","histo_nominal_OPTDown"]
        histograms = []
        for n in names:
            histograms.append(f2.Get(n))  
    
        nameOutputFile=options.output
        print "make output root file "+nameOutputFile
        output=ROOT.TFile(nameOutputFile,"RECREATE")
    
        for kernelHisto in histograms:
            smoothTail1D(kernelHisto)
            ctest = ROOT.TCanvas("ctest","ctest",400,400)
            ctest.SetLogy()
            kernelHisto.Draw("Ahist")
            ctest.SaveAs("bla.pdf")
            kernelHisto.Scale(1/kernelHisto.Integral())
            kernelHisto.Write()
        output.Close()
    
    
