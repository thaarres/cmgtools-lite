import ROOT
ROOT.gROOT.SetBatch(True)
import os, sys, re, optparse,pickle,shutil,json
import time

parser = optparse.OptionParser()
parser.add_option("-o","--output",dest="output",help="Output folder name",default='')
parser.add_option("-n","--name",dest="name",help="Input ROOT File name",default='/home/dschaefer/DiBoson3D/test_kernelSmoothing_pythia/workspace_pythia_nominal.root')
parser.add_option("-x","--xrange",dest="xrange",help="set range for x bins in projection",default="0,-1")
parser.add_option("-y","--yrange",dest="yrange",help="set range for y bins in projection",default="0,-1")
parser.add_option("-z","--zrange",dest="zrange",help="set range for z bins in projection",default="0,-1")
parser.add_option("-p","--projection",dest="projection",help="choose which projection should be done",default="z")
parser.add_option("-f","--postfit",dest="postfit",action="store_true",help="make also postfit plots",default=False)
parser.add_option("-l","--label",dest="label",help="add extra label such as pythia or herwig",default="")


(options,args) = parser.parse_args()
ROOT.gStyle.SetOptStat(0)
ROOT.RooMsgService.instance().setGlobalKillBelow(ROOT.RooFit.FATAL)
colors = [ROOT.kBlack,ROOT.kRed-2,ROOT.kRed+1,ROOT.kRed-1,ROOT.kRed+2,ROOT.kGreen-1,ROOT.kGreen-2,ROOT.kGreen+1,ROOT.kGreen+2,ROOT.kBlue]

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




def doZprojection(pdfs,data,proj=0):
    # do some z projections
    h=[]
    lv=[]
    dh = ROOT.TH1F("dh","dh",len(zBins)-2,zBinslowedge[1],zBinslowedge[len(zBins)-1])
    for p in pdfs:
        h.append( ROOT.TH1F("h_"+p.GetName(),"h_"+p.GetName(),len(zBins)-2,zBinslowedge[1],zBinslowedge[len(zBins)-1]))
        lv.append({})
    for i in range(0,len(pdfs)):
        for zk,zv in zBins_redux.iteritems():
            lv[i][zv]=0    
    for xk, xv in xBins_redux.iteritems():
         MJ1.setVal(xv)
         for yk, yv in yBins_redux.iteritems():
             MJ2.setVal(yv)
             for zk,zv in zBins_redux.iteritems():
                 MJJ.setVal(zv)
                 dh.Fill(zv,data.weight(argset))
                 i=0
                 for p in pdfs:
                    lv[i][zv] += p.getVal(argset)
                    i+=1
    for i in range(0,len(pdfs)):
        for zk,zv in zBins_redux.iteritems():                
            h[i].Fill(zv,lv[i][zv])
    leg = ROOT.TLegend(0.88,0.65,0.7,0.88)
    c = ROOT.TCanvas("c","c",800,400)
    if pdf_shape_postfit in pdfs:
        pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
        pad1.SetBottomMargin(0.01)
        pad1.SetLogy()
        pad1.Draw()
        pad1.cd()    
    c.SetLogy()
    n = dh.Integral()
    h[0].SetLineColor(colors[0])
    h[0].SetTitle("Z-Proj. x : "+options.xrange+" y : "+options.yrange)
    h[0].GetXaxis().SetTitle("m_{jj}")
    h[0].GetYaxis().SetTitleOffset(1.3)
    h[0].GetYaxis().SetTitle("events")
    h[0].Scale(n/h[0].Integral())
    if pdf_shape_postfit in pdfs:
        h[0].GetYaxis().SetTitleOffset(0.6)
        h[0].GetYaxis().SetTitle("events")
        h[0].GetYaxis().SetTitleSize(0.06)
        h[0].GetYaxis().SetLabelSize(0.06)
        h[0].GetYaxis().SetNdivisions(5)
    h[0].Draw("hist")
    
    dh.SetMarkerStyle(1)
    dh.Draw("same")
    leg.AddEntry(dh,"data","lp")
    if proj!=0:    
        proj.Scale(n/proj.Integral())
        proj.SetMarkerStyle(1)
        proj.Draw("same")
        leg.AddEntry(proj,"data","lp")
    leg.AddEntry(h[0],"nominal","l")
    for i in range(1,len(h)):
        h[i].Scale(n/h[i].Integral())
        h[i].SetLineColor(colors[i])
        h[i].Draw("histsame")
        name = h[i].GetName().split("_")
        leg.AddEntry(h[i],name[2],"l")
    
    leg.SetLineColor(0)
    leg.Draw("same")
    if pdf_shape_postfit in pdfs:
        c.cd()
        pad2 = ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
        pad2.SetTopMargin(0.1)
        pad2.SetBottomMargin(0.3)
        pad2.SetGridy()
        pad2.Draw()
        pad2.cd()
        graphs = addPullPlot(dh,h[0],h[1])
        graphs[0].Draw("AP")
        graphs[1].Draw("P")
        c.SaveAs(options.output+"PostFit"+options.label+"_x"+(options.xrange.split(","))[0]+"To"+(options.xrange.split(","))[1]+"_y"+(options.yrange.split(","))[0]+"To"+(options.yrange.split(","))[1]+".pdf")
    else:    
        c.SaveAs(options.output+"Zproj"+options.label+"_x"+(options.xrange.split(","))[0]+"To"+(options.xrange.split(","))[1]+"_y"+(options.yrange.split(","))[0]+"To"+(options.yrange.split(","))[1]+".pdf")


def doXprojection(pdfs,data,hin=0):
    h=[]
    lv=[]
    proj = ROOT.TH1F("px","px",len(xBins)-2,xBinslowedge[1],xBinslowedge[len(xBins)-1])
    for p in pdfs:
        h.append( ROOT.TH1F("hx_"+p.GetName(),"hx_"+p.GetName(),len(xBins)-2,xBinslowedge[1],xBinslowedge[len(xBins)-1]))
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
                 proj.Fill(xv,data.weight(argset))
                 for p in pdfs:
                    lv[i][xv] += p.getVal(argset)
                    i+=1
    for i in range(0,len(pdfs)):
        for key, value in lv[i].iteritems():
            h[i].Fill(key,value)
    leg = ROOT.TLegend(0.88,0.65,0.77,0.89)
    c = ROOT.TCanvas("c","c",800,400)
    if pdf_shape_postfit in pdfs:
        pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
        pad1.SetBottomMargin(0.01)
        pad1.Draw()
        pad1.cd()     
    n = proj.Integral()
    h[0].SetLineColor(colors[0])
    h[0].SetTitle("X-Proj. y : "+options.yrange+" z : "+options.zrange)
    h[0].GetXaxis().SetTitle("m_{jet1}")
    h[0].GetYaxis().SetTitleOffset(1.3)
    h[0].GetYaxis().SetTitle("events")
    if pdf_shape_postfit in pdfs:
        h[0].GetYaxis().SetTitleOffset(0.6)
        h[0].GetYaxis().SetTitle("events")
        h[0].GetYaxis().SetTitleSize(0.06)
        h[0].GetYaxis().SetLabelSize(0.06)
        h[0].GetYaxis().SetNdivisions(5)
    h[0].Scale(n/h[0].Integral())
    h[0].Draw("hist")
    leg.AddEntry(proj,"data","lp")
    leg.AddEntry(h[0],"nominal","l")
    for i in range(1,len(h)):
        h[i].SetLineColor(colors[i])
        h[i].Scale(n/h[i].Integral())
        h[i].Draw("histsame")
        name = h[i].GetName().split("_")
        leg.AddEntry(h[i],name[2],"l")
    if hin!=0:    
        hin.Scale(n/hin.Integral())
        hin.SetMarkerStyle(1)
        hin.Draw("same")
    proj.SetMarkerStyle(1)
    proj.Draw("same")
    leg.SetLineColor(0)
    leg.Draw("same")
    if pdf_shape_postfit in pdfs:
        c.cd()
        pad2 = ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
        pad2.SetTopMargin(0.1)
        pad2.SetBottomMargin(0.3)
        pad2.SetGridy()
        pad2.Draw()
        pad2.cd()
        graphs = addPullPlot(proj,h[0],h[1])
        graphs[0].Draw("AP")
        graphs[1].Draw("P")
        c.SaveAs(options.output+"PostFit"+options.label+"_y"+(options.yrange.split(","))[0]+"To"+(options.yrange.split(","))[1]+"_z"+(options.zrange.split(","))[0]+"To"+(options.zrange.split(","))[1]+".pdf") 
    else:    
        c.SaveAs(options.output+"Xproj"+options.label+"_y"+(options.yrange.split(","))[0]+"To"+(options.yrange.split(","))[1]+"_z"+(options.zrange.split(","))[0]+"To"+(options.zrange.split(","))[1]+".pdf")   
    

def doYprojection(pdfs,data):
    h=[]
    lv=[]
    proj = ROOT.TH1F("py","py",len(yBins)-2,yBinslowedge[1],yBinslowedge[len(yBins)-1])
    for p in pdfs:
        h.append( ROOT.TH1F("hy_"+p.GetName(),"hy_"+p.GetName(),len(yBins)-2,yBinslowedge[1],yBinslowedge[len(yBins)-1]))
        lv.append({})
    for yk, yv in yBins_redux.iteritems():
         MJ2.setVal(yv)
         for i in range(0,len(pdfs)):
            lv[i][yv]=0
         for xk, xv in xBins_redux.iteritems():
             MJ1.setVal(xv)
             for zk,zv in zBins_redux.iteritems():
                 MJJ.setVal(zv)
                 i=0
                 proj.Fill(yv,data.weight(argset))
                 for p in pdfs:
                    lv[i][yv] += p.getVal(argset)
                    i+=1
    for i in range(0,len(pdfs)):
        for key, value in lv[i].iteritems():
            h[i].Fill(key,value)
    leg = ROOT.TLegend(0.88,0.65,0.77,0.89)
    c = ROOT.TCanvas("c","c",800,400)
    if pdf_shape_postfit in pdfs:
        pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
        pad1.SetBottomMargin(0.01)
        pad1.Draw()
        pad1.cd()               
    n = proj.Integral()
    h[0].SetLineColor(colors[0])
    h[0].SetTitle("Y-Proj. x : "+options.xrange+" z : "+options.zrange)
    h[0].GetXaxis().SetTitle("m_{jet2}")
    h[0].GetYaxis().SetTitleOffset(1.3)
    h[0].GetYaxis().SetTitle("events")
    if pdf_shape_postfit in pdfs:
        h[0].GetYaxis().SetTitleOffset(0.6)
        h[0].GetYaxis().SetTitle("events")
        h[0].GetYaxis().SetTitleSize(0.06)
        h[0].GetYaxis().SetLabelSize(0.06)
        h[0].GetYaxis().SetNdivisions(5)
    h[0].Scale(n/h[0].Integral())
    h[0].Draw("hist")
    leg.AddEntry(proj,"data","lp")
    leg.AddEntry(h[0],"nominal","l")
    for i in range(1,len(h)):
        h[i].SetLineColor(colors[i])
        h[i].Scale(n/h[i].Integral())
        h[i].Draw("histsame")
        name = h[i].GetName().split("_")
        leg.AddEntry(h[i],name[2],"l")
    proj.SetMarkerStyle(1)
    leg.SetLineColor(0)
    leg.Draw("same")
    proj.Scale(n/proj.Integral())
    proj.Draw("same")
    if pdf_shape_postfit in pdfs:
        c.cd()
        pad2 = ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
        pad2.SetTopMargin(0.1)
        pad2.SetBottomMargin(0.3)
        pad2.SetGridy()
        pad2.Draw()
        pad2.cd()
        graphs = addPullPlot(proj,h[0],h[1])
        graphs[0].Draw("AP")
        graphs[1].Draw("P")
        c.SaveAs(options.output+"PostFit"+options.label+"_x"+(options.xrange.split(","))[0]+"To"+(options.xrange.split(","))[1]+"_z"+(options.zrange.split(","))[0]+"To"+(options.zrange.split(","))[1]+".pdf")
    else:
        c.SaveAs(options.output+"Yproj"+options.label+"_x"+(options.xrange.split(","))[0]+"To"+(options.xrange.split(","))[1]+"_z"+(options.zrange.split(","))[0]+"To"+(options.zrange.split(","))[1]+".pdf")   
 

def addPullPlot(hdata,hprefit,hpostfit):
    print "make pull plots: (data-fit)/sigma_data"
    N = hdata.GetNbinsX()
    gpost = ROOT.TGraph(0)
    gpre  = ROOT.TGraph(0)
    for i in range(1,N):
        m = hdata.GetXaxis().GetBinCenter(i)
        if hdata.GetBinContent(i) == 0:
            continue
        ypostfit = (hdata.GetBinContent(i) - hpostfit.GetBinContent(i))/hdata.GetBinError(i)
        yprefit  = (hdata.GetBinContent(i) - hprefit.GetBinContent(i))/hdata.GetBinError(i)
        gpost.SetPoint(i-1,m,ypostfit)
        gpre.SetPoint(i-1,m,yprefit)
    gpost.SetLineColor(colors[1])
    gpre.SetLineColor(colors[0])
    gpost.SetMarkerColor(colors[1])
    gpre.SetMarkerColor(colors[0])
    gpost.SetMarkerSize(1)
    gpre.SetMarkerSize(1)
    gpre.SetTitle("")
    gpre.SetMarkerStyle(4)
    gpost.SetMarkerStyle(3)
    gpre.GetXaxis().SetTitle(hprefit.GetXaxis().GetTitle())
    gpre.GetYaxis().SetTitle("#frac{data-fit}{#sigma}")
    gpre.GetYaxis().SetTitleSize(0.15)
    gpre.GetYaxis().SetTitleOffset(0.2)
    gpre.GetXaxis().SetTitleSize(0.15)
    gpre.GetXaxis().SetTitleOffset(0.7)
    gpre.GetXaxis().SetLabelSize(0.15)
    gpre.GetYaxis().SetLabelSize(0.15)
    gpre.GetXaxis().SetNdivisions(6)
    gpre.GetYaxis().SetNdivisions(4)
    gpre.SetMaximum(2.5)
    gpre.SetMinimum(-4.5)
    gpre.GetXaxis().SetRangeUser(hdata.GetXaxis().GetBinLowEdge(1),hdata.GetXaxis().GetBinLowEdge(N))
    return [gpre,gpost] 
 

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
     
     f = ROOT.TFile(options.name,"READ")
     workspace = f.Get("w")
     f.Close()
     #workspace.Print()
     norm = workspace.obj("CMS_VV_JJ_nonRes_norm_HPHP_Pdf")
     print norm.getVal()
     model = workspace.pdf("model_b")
     # try to get kernel Components 
     args  = model.getComponents()
     pdf = args["nonResNominal_JJ_HPHP_13TeV"]
     pdf_PTZDown = args["nonRes_PTZDown_JJ_HPHP_13TeV"]
     pdf_OPTZUp  = args["nonRes_OPTZUp_JJ_HPHP_13TeV"]
     pdf_PTZUp = args["nonRes_PTZUp_JJ_HPHP_13TeV"]
     pdf_OPTZDown  = args["nonRes_OPTZDown_JJ_HPHP_13TeV"]
     
     pdf_shape_postfit   = args["shapeBkg_nonRes_JJ_HPHP_13TeV"]
     pdf_shape_postfit.SetName("pdf_postfit_shape")
     pdf_PTXYUp   = args["nonRes_PTXYUp_JJ_HPHP_13TeV"]
     pdf_PTXYDown = args["nonRes_PTXYDown_JJ_HPHP_13TeV"]
     pdf_OPTXYUp   = args["nonRes_OPTXYUp_JJ_HPHP_13TeV"]
     pdf_OPTXYDown = args["nonRes_OPTXYDown_JJ_HPHP_13TeV"]
     #pdfhist = workspace.obj("shapeBkg_nonRes_JJ_HPHP_13TeV")
     
     data = workspace.data("data_obs")
     if options.postfit:
        model.fitTo(data,ROOT.RooFit.NumCPU(8),ROOT.RooFit.SumW2Error(True),ROOT.RooFit.Minos(0),ROOT.RooFit.Verbose(0),ROOT.RooFit.Save(1))
     # get data from workspace 
     
     data.Print()
     # get variables from workspace 
     MJ1= workspace.var("MJ1");
     MJ2= workspace.var("MJ2");
     MJJ= workspace.var("MJJ");
     del workspace
    
     argset = ROOT.RooArgSet();
     argset.add(MJJ);
     argset.add(MJ2);
     argset.add(MJ1);
     
     x = getListFromRange(options.xrange)
     y = getListFromRange(options.yrange)
     z = getListFromRange(options.zrange)
     
     
     xBins_redux = reduceBinsToRange(xBins,x)
     yBins_redux = reduceBinsToRange(yBins,y)
     zBins_redux = reduceBinsToRange(zBins,z)
     #print xBins_redux
     #print yBins_redux
     #print zBins_redux
     
     #make projections onto MJJ axis
     if options.projection =="z":
         pdfs = [pdf,pdf_PTZDown,pdf_OPTZUp,pdf_OPTZDown,pdf_PTZUp]
         #keys = xBins_redux.keys()
         #keys.sort()
         #zkeys = yBins_redux.keys()
         #zkeys.sort()
         #if y[0]==0 and y[1]==-1 and x[0]==0 and x[1]==-1:
             #print "project all " 
             #proj= hinMC.ProjectionZ("projz",0,-1,0,-1)
         #else:    
             #proj= hinMC.ProjectionZ("projz",keys[0],keys[-1],zkeys[0],zkeys[-1])
         doZprojection(pdfs,data)
         if options.postfit == True:
             postfit = [pdf,pdf_shape_postfit]
             doZprojection(postfit,data)
         
     #make projections onto MJ1 axis
     if options.projection =="x":
         pdfs = [pdf,pdf_PTXYDown,pdf_OPTXYDown,pdf_OPTXYUp,pdf_PTXYUp]
         #if y[0]==0 and y[1]==-1 and z[0]==0 and z[1]==-1:
             #print "project all " 
             #proj= hinMC.ProjectionX("projx",0,-1,0,-1)
         #else:
            #keys = yBins_redux.keys()
            #keys.sort()
            #zkeys = zBins_redux.keys()
            #zkeys.sort()
         
            #proj= hinMC.ProjectionX("projx",keys[0],keys[-1],zkeys[0],zkeys[-1])
         doXprojection(pdfs,data)
         if options.postfit == True:
             postfit = [pdf,pdf_shape_postfit]
             doXprojection(postfit,data)
         
         
     #make projections onto MJ2 axis
     if options.projection =="y":
         pdfs = [pdf,pdf_PTXYDown,pdf_OPTXYDown,pdf_OPTXYUp,pdf_PTXYUp]
         #if x[0]==0 and x[1]==-1 and z[0]==0 and z[1]==-1:
             #print "project all " 
             #proj= hinMC.ProjectionY("projy",0,-1,0,-1)
         #else:
            #keys = xBins_redux.keys()
            #keys.sort()
            #zkeys = zBins_redux.keys()
            #zkeys.sort()
            #proj= hinMC.ProjectionY("projy",keys[0],keys[-1],zkeys[0],zkeys[-1])
         doYprojection(pdfs,data)
         
         if options.postfit == True:
             postfit = [pdf,pdf_shape_postfit]
             doYprojection(postfit,data)
         
         
     

