import ROOT
import os,sys
ROOT.gROOT.SetBatch(True)




def plotTwoHisto(hist1,outname,dolog=False, label=""):
    c= ROOT.TCanvas("c","c",400,400)
    hist1.SetLineColor(ROOT.kBlue)
    hist1.SetLineWidth(2)
    hist1.Draw("hist")
    
    leg = ROOT.TLegend(0.5,0.8,0.7,0.9)
    leg.AddEntry(hist1,"nominal","l")
    leg.Draw("same")
    if dolog:
        c.SetLogy()
    text = ROOT.TLatex() 
    if label.find("mjet")!=-1:
        text.DrawLatex(1100,0.003,label)
    else:
        text.DrawLatex(32,0.01,label)
    c.SaveAs("2DKernel/"+outname)




if __name__=="__main__":

    fromkernel = 'JJ_nonRes_2D_HPHP.root'# 'test.root'# 'JJ_nonRes_2D_HPHP.root' #'JJ_nonRes_COND2D_HPHP_l1.root'#"JJ_nonRes_2D_HP.root"
    f2 = ROOT.TFile(fromkernel,"READ")
    kernelHisto = f2.Get("histo")  
    
    # for 3D histograms 
    
    Nx = kernelHisto.GetNbinsX()
    Ny = kernelHisto.GetNbinsY()
    Nz = kernelHisto.GetNbinsZ()

    for i in range(1,Nz+1):
        proj = kernelHisto.ProjectionX("projx",i,i)
        label = "mjet "+str(round(kernelHisto.GetYaxis().GetBinCenter(i),1))
        plotTwoHisto(proj,"XprojectionYbin"+str(i)+".pdf",False,label)
    for j in range(1,Nz+1):
        projy = kernelHisto.ProjectionY("projy",j,j)
        label = "mVV "+str(round(kernelHisto.GetXaxis().GetBinCenter(j),1))
        plotTwoHisto(projy,"YprojectionXbin"+str(j)+".pdf",False,label) 

    xlist = [1,10,20,30,40,50,60,70,80 ]
    ylist = xlist


    for x in range(2,len(xlist)):
        for y in range(2,len(ylist)):
    #for z in range(1,Nx+1):
    #    for z2 in range(z,Ny+1):
            projz = kernelHisto.ProjectionZ("projz",xlist[x-1],xlist[x],ylist[y-1],ylist[y])
            plotTwoHisto(projz,"ZprojectionXbin"+str(x)+"Ybin"+str(y)+".pdf",True)
            
    for z in range(1,Nz):        
            projzTox = kernelHisto.ProjectionX("projzTox",0,-1,z,z)
            projzToy = kernelHisto.ProjectionY("projzToy",0,-1,z,z)
            plotTwoHisto(projzTox,"ZtoX_Zbin"+str(z)+"YbinAll.pdf")
            plotTwoHisto(projzToy,"ZtoY_Zbin"+str(z)+"XbinAll.pdf")

    px = kernelHisto.ProjectionX("x")
    plotTwoHisto(px,"XprojectionYbinAll.pdf",False)
    
    py = kernelHisto.ProjectionY("y")
    plotTwoHisto(py,"YprojectionXbinAll.pdf",False)
    
    pz = kernelHisto.ProjectionZ("z")
    plotTwoHisto(pz,"ZprojectionXYbinAll.pdf",True)
    
    
    # for 2D histograms 
    
    #Nx = kernelHisto.GetNbinsX()
    #Ny = kernelHisto.GetNbinsY()
    
    #for i in range(1,Ny+1):
        #proj = kernelHisto.ProjectionX("projx",i,i)
        #label = "mjet "+str(round(kernelHisto.GetYaxis().GetBinCenter(i),1))
        #plotTwoHisto(proj,"XprojectionYbin"+str(i)+".pdf",False,label)
    #for j in range(1,Nx+1):
        #projy = kernelHisto.ProjectionY("projy",j,j)
        #label = "mVV "+str(round(kernelHisto.GetXaxis().GetBinCenter(j),1))
        #plotTwoHisto(projy,"YprojectionXbin"+str(j)+".pdf",False,label) 


    #px = kernelHisto.ProjectionX("x")
    #plotTwoHisto(px,"XprojectionYbinAll.pdf",False)
    
    #py = kernelHisto.ProjectionY("y")
    #plotTwoHisto(py,"YprojectionXbinAll.pdf",False)
    
   
