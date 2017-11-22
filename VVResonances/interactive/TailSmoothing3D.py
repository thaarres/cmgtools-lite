import ROOT
ROOT.gROOT.SetBatch(True)
import os, sys, re, optparse,pickle,shutil,json

parser = optparse.OptionParser()
parser.add_option("-o","--output",dest="output",help="Output ROOT File",default='')
parser.add_option("-i","--infile",dest="infile",help="Input ROOT File",default='')


(options,args) = parser.parse_args()


def smoothTail(proj,hist3D,xbin,ybin):#,xmin,xmax,ymin,ymax):
    if proj.Integral() == 0:
        print "histogram has zero integral "+proj.GetName()
        return 0
    scale = proj.Integral() 
    proj.Scale(1.0/scale)
    
    beginFit = proj.GetBinLowEdge( proj.GetMaximumBin() )
    beginFitX = beginFit + 800. * 1/(beginFit/1000.)
    print beginFit
    print beginFitX
    #beginFitX=beginFit
   #expo=ROOT.TF1("expo","expo",beginFitX,8000)
    expo=ROOT.TF1("expo","[0]*(1-x/13000.)^[1]/(x/13000)^[2]",2000,8000) 
    expo.SetParameters(0,16.,2.)
    expo.SetParLimits(2,1.,20.)
    proj.Fit(expo,"LLMR","",beginFitX,8000)
    c = ROOT.TCanvas("c","c",400,400)
    c.SetLogy()
    proj.Draw("hist")
    proj.Draw("funcsame")
    c.SaveAs(proj.GetName()+"_binX"+str(xbin)+"binY"+str(ybin)+".pdf")
    beginsmooth = False
    print proj.GetNbinsX()+1
    for j in range(1,proj.GetNbinsX()+1):
        x=proj.GetXaxis().GetBinCenter(j)
        if x>beginFitX:
            if beginsmooth==False:
               if x<3000: 
                   #print abs(proj.GetBinContent(j) - expo.Eval(x))
                   if abs(proj.GetBinContent(j) - expo.Eval(x)) < 0.00009:# and abs(expo.Derivative(x)- (hist.GetBinContent(j):
                    print beginFitX
                    print "begin smoothing at " +str(x)
                    beginsmooth = True 
               if abs(proj.GetBinContent(j) - expo.Eval(x)) < 0.00001:# and abs(expo.Derivative(x)- (hist.GetBinContent(j):
                   print beginFitX
                   print "begin smoothing at " +str(x)
                   beginsmooth = True 
            if beginsmooth:
                #xbins = getXbin( xmin,xmax)
                #ybins = getXbin( ymin,ymax)
                #for xbin in xbins:
                #    for ybin in ybins:
                print "set bin content " 
                print xbin
                print ybin
                print j
                print expo.Eval(x)
                hist3D.SetBinContent(xbin,ybin,j,expo.Eval(x)*scale)
    return 1


def getXbin( xmin,xmax):
    bins = []
    for i in range(xmin,xmax):
        bins.append(xmin + i)
    return bins
    
    


if __name__=='__main__':
    
    fromkernel =  options.infile
    f2 = ROOT.TFile(fromkernel,"READ")
    
    names = ["histo","histo_PTUp","histo_PTDown", "histo_PTXUp","histo_PTXDown","histo_PTYUp","histo_PTYDown","histo_PTZUp","histo_PTZDown",  "histo_OPTUp","histo_OPTDown", "histo_OPTXUp","histo_OPTXDown","histo_OPTYUp","histo_OPTYDown","histo_OPTZUp","histo_OPTZDown"]
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
        print "y bins " +str(Ny)
        print "x bins " +str(Nx)
        print "x bins " +str(Nz)
        
        xlist = [1,10,20,30,40,50,60,70,80 ]
        ylist = xlist
    
    
    
    
    
    
    
        for x in range(1,Nx+1):
            for y in range(1,Ny+1):
                p = kernelHisto.ProjectionZ("tmp",x,x,y,y)
                smoothTail(p,kernelHisto,x,y)
                if x==80 and y ==80:
                    p = kernelHisto.ProjectionZ("tmp",x,x,y,y)
                    ctest = ROOT.TCanvas("ctest","ctest",400,400)
                    ctest.SetLogy()
                    p.Draw("Ahist")
                    ctest.SaveAs("bla.pdf")
    
    
    
    
    
        kernelHisto.Write()
    output.Close()
