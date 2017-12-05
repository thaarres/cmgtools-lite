import ROOT
ROOT.gROOT.SetBatch(True)
import os, sys, re, optparse,pickle,shutil,json
import time

parser = optparse.OptionParser()
parser.add_option("-o","--output",dest="output",help="Output ROOT File",default='')
parser.add_option("-n","--name",dest="name",help="Input ROOT File name",default='/home/dschaefer/DiBoson3D/test_kernelSmoothing_pythia/workspace_pythia_nominal.root')
parser.add_option("-x","--xrange",dest="xrange",help="set range for x bins in projection",default="0,-1")
parser.add_option("-y","--yrange",dest="yrange",help="set range for y bins in projection",default="0,-1")
parser.add_option("-z","--zrange",dest="zrange",help="set range for z bins in projection",default="0,-1")
parser.add_option("-p","--projection",dest="projection",help="choose which projection should be done",default="z")


(options,args) = parser.parse_args()

def getListFromRange(xyzrange):
    r=[]
    a,b = xyzrange.split(",")
    r.append(float(a))
    r.append(float(b))
    return r


def getListOfBins(hist,dim):
    axis =0
    N = 0
    if dim =="x":
        axis= hist.GetXaxis()
        N = hist.GetNbinsX()
    if dim =="y":
        axis = hist.GetYaxis()
        N = hist.GetNbinsY()
    if dim =="z":
        axis = hist.GetZaxis()
        N = hist.GetNbinsZ()
    if axis==0:
        return {}
    
    mmin = axis.GetXmin()
    mmax = axis.GetXmax()
    r ={}
    for i in range(0,N):
        #v = mmin + i * (mmax-mmin)/float(N)
        r[i] = axis.GetBinCenter(i) 
    return r   


def getListOfBinsLowEdge(hist,dim):
    axis =0
    N = 0
    if dim =="x":
        axis= hist.GetXaxis()
        N = hist.GetNbinsX()
    if dim =="y":
        axis = hist.GetYaxis()
        N = hist.GetNbinsY()
    if dim =="z":
        axis = hist.GetZaxis()
        N = hist.GetNbinsZ()
    if axis==0:
        return {}
    
    mmin = axis.GetXmin()
    mmax = axis.GetXmax()
    r ={}
    for i in range(0,N):
        #v = mmin + i * (mmax-mmin)/float(N)
        r[i] = axis.GetBinLowEdge(i) 
    return r


def getListOfBinsWidth(hist,dim):
    axis =0
    N = 0
    if dim =="x":
        axis= hist.GetXaxis()
        N = hist.GetNbinsX()
    if dim =="y":
        axis = hist.GetYaxis()
        N = hist.GetNbinsY()
    if dim =="z":
        axis = hist.GetZaxis()
        N = hist.GetNbinsZ()
    if axis==0:
        return {}
    
    mmin = axis.GetXmin()
    mmax = axis.GetXmax()
    r ={}
    for i in range(0,N):
        #v = mmin + i * (mmax-mmin)/float(N)
        r[i] = axis.GetBinWidth(i) 
    return r 

    
def reduceBinsToRange(Bins,r):
    if r[0]==0 and r[1]==-1:
        return Bins
    result ={}
    for key, value in Bins.iteritems():
        if value >= r[0] and value <=r[1]:
            result[key]=value
    return result




def doZprojection(pdfs,zBins,proj):
    # do some z projections
    h=[]
    for p in pdfs:
        h.append( ROOT.TH1F("h_"+p.GetName(),"h_"+p.GetName(),len(zBins)-1,zBins[0],zBins[len(zBins)-1]))

    for xk, xv in xBins_redux.iteritems():
         MJ1.setVal(xv)
         for yk, yv in yBins_redux.iteritems():
             MJ2.setVal(yv)
             for zk,zv in zBins_redux.iteritems():
                 MJJ.setVal(zv)
                 i=0
                 for p in pdfs:
                    h[i].Fill(zv,p.getVal(argset))
                    #print zv
                    i+=1
     
    c = ROOT.TCanvas("c","c",400,400)
    c.SetLogy()
    h[0].SetLineColor(ROOT.kRed)
    h[0].Draw("hist")
    i=0
    for hist in h:
        hist.Scale(1/hist.Integral())
        hist.SetLineColor(ROOT.kRed+i)
        i+=1
        hist.Draw("histsame")
    proj.Scale(1/proj.Integral())
    proj.SetMarkerStyle(1)
    proj.Draw("same")
    c.SaveAs("Zproj.pdf")


def doXprojection(pdfs,xBins,hin):
    # do some z projections
    h=[]
    lv=[]
    for p in pdfs:
        h.append( ROOT.TH1F("hx_"+p.GetName(),"hx_"+p.GetName(),len(xBins)-1,xBins[0],xBins[len(xBins)-1]))
        lv.append({})
    for xk, xv in xBins_redux.iteritems():
         MJ1.setVal(xv)
         for i in range(0,len(pdfs)):
            lv[i][xv]=0
         for yk, yv in yBins_redux.iteritems():
             MJ2.setVal(yv)
             for zk,zv in zBins_redux.iteritems():
                 MJJ.setVal(zv)
                 i=0
                 for p in pdfs:
                    #print "xv "+str(xv)
                    #print "yv "+str(yv)
                    #print "zv "+str(zv)
                    #print p.getVal(argset)
                    #print lv[i][xv] 
                    lv[i][xv] += p.getVal(argset)
                 #for p in pdfs:
                 #   h[i].Fill(zv,p.getVal(argset))
                 #   #print zv
                    i+=1
    for i in range(0,len(pdfs)):
        for key, value in lv[i].iteritems():
            h[i].Fill(key,value)
    print lv[0]
    c = ROOT.TCanvas("c","c",400,400)
    #c.SetLogy()
    h[0].SetLineColor(ROOT.kRed)
    h[0].Draw("hist")
    i=0
    for hist in h:
        hist.SetLineColor(ROOT.kRed+i)
        hist.Scale(1/hist.Integral())
        i+=1
        hist.Draw("histsame")
    hin.Scale(1/hin.Integral())
    hin.Draw("same")
    c.SaveAs("Xproj.pdf")    
    

if __name__=="__main__":
     finMC = ROOT.TFile("JJ_pythia_HPHP.root","READ");
     hinMC = finMC.Get("nonRes");
     xBins= getListOfBins(hinMC,"x")
     yBins= getListOfBins(hinMC,"y")
     zBins= getListOfBins(hinMC,"z")
     #finMC.Close()
    
     xBinslowedge = getListOfBinsLowEdge(hinMC,'x')
     xBinsWidth   = getListOfBinsWidth(hinMC,"x")
     
     yBinslowedge = getListOfBinsLowEdge(hinMC,'y')
     yBinsWidth   = getListOfBinsWidth(hinMC,"y")
     
     zBinslowedge = getListOfBinsLowEdge(hinMC,'z')
     zBinsWidth   = getListOfBinsWidth(hinMC,"z")
     
     print xBinslowedge
     print xBinsWidth
     
     print zBinslowedge
     print zBinsWidth
    
     f = ROOT.TFile(options.name,"READ")
     workspace = f.Get("w")
     model = workspace.pdf("model_b")
     # try to get kernel Components 
     args  = model.getComponents()
     pdf = args["nonResNominal_JJ_HPHP_13TeV"]
     pdf_PTZDown = args["nonRes_PTZDown_JJ_HPHP_13TeV"]
     pdf_OPTZUp  = args["nonRes_OPTZUp_JJ_HPHP_13TeV"]
     pdf_PTZUp = args["nonRes_PTZUp_JJ_HPHP_13TeV"]
     pdf_OPTZDown  = args["nonRes_OPTZDown_JJ_HPHP_13TeV"]
     
     pdf_shape   = args["shapeBkg_nonRes_JJ_HPHP_13TeV"]
     pdf_PTXYUp   = args["nonRes_PTXYUp_JJ_HPHP_13TeV"]
     pdf_PTXYDown = args["nonRes_PTXYDown_JJ_HPHP_13TeV"]
     #args.Print()
     
     pdfhist = workspace.obj("shapeBkg_nonRes_JJ_HPHP_13TeV")
     
     # get data from workspace 
     data = workspace.data("data_obs")
     
     # get variables from workspace 
     MJ1= workspace.var("MJ1");
     MJ2= workspace.var("MJ2");
     MJJ= workspace.var("MJJ");
    
    
     argset = ROOT.RooArgSet();
     argset.add(MJJ);
     argset.add(MJ2);
     argset.add(MJJ);
     
     
     x = getListFromRange(options.xrange)
     y = getListFromRange(options.yrange)
     z = getListFromRange(options.zrange)
     
     print x
     print y
     print z
     
     xBins_redux = reduceBinsToRange(xBins,x)
     yBins_redux = reduceBinsToRange(yBins,y)
     zBins_redux = reduceBinsToRange(zBins,z)
     print xBins_redux
     print yBins_redux
     print zBins_redux
     
     pdfs = [pdf,pdf_PTZDown,pdf_OPTZUp,pdf_OPTZDown,pdf_PTZUp]
     #make projections onto MJJ axis
     if options.projection =="z":
         keys = xBins_redux.keys()
         keys.sort()
         zkeys = yBins_redux.keys()
         zkeys.sort()
         
         proj= hinMC.ProjectionZ("projx",keys[0],keys[-1],zkeys[0],zkeys[-1])
         doZprojection(pdfs,zBins,proj)
         
     #make projections onto MJ1 axis
     if options.projection =="x":
         if y[0]==0 and y[1]==-1 and z[0]==0 and z[1]==-1:
             print "project all " 
             proj= hinMC.ProjectionX("projx",0,-1,0,-1)
         else:
            keys = yBins_redux.keys()
            keys.sort()
            zkeys = zBins_redux.keys()
            zkeys.sort()
         
            proj= hinMC.ProjectionX("projx",keys[0],keys[-1],zkeys[0],zkeys[-1])
         doXprojection(pdfs,xBins,proj)    
     
