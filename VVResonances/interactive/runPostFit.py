import time,sys
import ROOT as rt
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()    
    parser.add_argument('-i','--input', type=str, help="input  ROOT FILE", default = "JJ_BulkGWW_HPHP_13TeV_workspace.root")
    parser.add_argument('-o','--output', type=str, help="label string for output-file names", default = None)
    parser.add_argument('--png', action='store_true', help="save output plots also as .png files")
    parser.add_argument('--genonly', action='store_true', help="stop at generation step")
    args = parser.parse_args()

    rt.gSystem.Load("libHiggsAnalysisCombinedLimit")

    fin = rt.TFile.Open(args.input)
    workspace = fin.Get("w")
    workspace.Print()

    print "----------- Parameter Workspace -------------";
    parameters_workspace = workspace.allVars();
    par = parameters_workspace.createIterator();
    par.Reset();
    param = par.Next()
    newpars = []
    while (param):
        param.Print();
        param=par.Next()
    print "---------------------------------------------";

    print "----------- Pdf in the Workspace -------------";
    pdfs_workspace = workspace.allPdfs();
    par = pdfs_workspace.createIterator();
    par.Reset();
    param=par.Next()
    newpdfs = []
    while (param):
        param.Print();
        param = par.Next()
    print "----------------------------------------------";

    workspace.var('MH').setVal(2000)
    workspace.var('MH').setConstant(1)

    workspace.pdf("model_b").Print()
    model = workspace.pdf("model_b")
    fitResult = model.fitTo(workspace.data("data_obs"),rt.RooFit.NumCPU(8),rt.RooFit.SumW2Error(True),rt.RooFit.Minos(1),rt.RooFit.Verbose(0),rt.RooFit.Save(1))
    fitResult.Print()
    

    #### generate a sample from the roofitresult (same statistics as original)
    Nevt = int(workspace.data("data_obs").sumEntries())
    pdfData = (model.generate(rt.RooArgSet(workspace.var('MJ1'), workspace.var('MJ2'), workspace.var('MJJ')), Nevt))
    print "Done generating %i events" %pdfData.numEntries()

    # dump the generated dataset in a file
    if args.genonly:
        if args.output != None: outName = args.output
        else: outName = args.input.replace(".root", "_GenData.root")
        outFile = rt.TFile.Open(outName, "recreate")
        pdfData.Write()
        outFile.Close()
    # or make the projection plots
    else:
        dataset=workspace.data("data_obs")
        dataset.Print()
        #workspace.var('MJJ').setRange("lowMJJ",1000,1500)
        workspace.var('MJ1').setRange("lowMJ",55,215)
        workspace.var('MJ2').setRange("lowMJ",55,215)
        
        # MJ1
        canvas1 = rt.TCanvas("c1")
        canvas1.cd()

        varMax=workspace.var('MJ1').getMax()
        varMin=workspace.var('MJ1').getMin()
        varBins=workspace.var('MJ1').getBins()

        frame1=workspace.var('MJ1').frame()
        #dataset.plotOn(frame,rt.RooFit.Name("datapoints"),rt.RooFit.CutRange("lowMJJ"))
        #pdfData.plotOn(frame,rt.RooFit.CutRange("lowMJJ"), rt.RooFit.MarkerColor(rt.kBlue))
        dataset.plotOn(frame1,rt.RooFit.Name("DataProjM1"),rt.RooFit.DataError(rt.RooAbsData.SumW2))
        pdfData.plotOn(frame1, rt.RooFit.MarkerColor(rt.kBlue), rt.RooFit.LineColor(rt.kBlue), rt.RooFit.Name("BkgProjM1"),rt.RooFit.DrawOption("C"))

        frame1.Draw("AH")
        if args.png: canvas1.SaveAs("MJ1.png")

        # MJ2
        canvas2 = rt.TCanvas("c2")
        canvas2.cd()

        varMax=workspace.var('MJ2').getMax()
        varMin=workspace.var('MJ2').getMin()
        varBins=workspace.var('MJ2').getBins()
        #workspace.var('MJJ').setRange("lowMJJ",1000,1500)

        frame2=workspace.var('MJ2').frame()
        #dataset.plotOn(frame,rt.RooFit.Name("datapoints"),rt.RooFit.CutRange("lowMJJ"))
        #pdfData.plotOn(frame,rt.RooFit.CutRange("lowMJJ"), rt.RooFit.MarkerColor(rt.kBlue))
        dataset.plotOn(frame2,rt.RooFit.Name("DataProjM2"),rt.RooFit.DataError(rt.RooAbsData.SumW2))
        pdfData.plotOn(frame2, rt.RooFit.MarkerColor(rt.kBlue), rt.RooFit.LineColor(rt.kBlue), rt.RooFit.Name("BkgProjM2"),rt.RooFit.DrawOption("C"))

        frame2.Draw("AH")
        if args.png: canvas2.SaveAs("MJ2.png")

        # MJJ
        canvas3 = rt.TCanvas("c3")
        canvas3.cd()
	canvas3.SetLogy()

        frame3=workspace.var('MJJ').frame()
        selection = "%s>%f && %s<%f && %s>%f && %s<%f" %("MJ1", 55., "MJ1", 215., "MJ2", 55., "MJ2", 215.)
        dataset.reduce(selection).plotOn(frame3,rt.RooFit.Name("DataProjMJJ"),rt.RooFit.DataError(rt.RooAbsData.SumW2))
        pdfData.reduce(selection).plotOn(frame3,rt.RooFit.MarkerColor(rt.kBlue), rt.RooFit.LineColor(rt.kBlue), rt.RooFit.Name("BkgProjMJJ"),rt.RooFit.DrawOption("C"))
 
        frame3.SetMinimum(1E-05)
	frame3.SetMaximum(50000)
        frame3.Draw("AH")
        if args.png: canvas3.SaveAs("MJJ.png")

        fileOUT = rt.TFile.Open(args.input.replace(".root","_ProjPlot.root"), "recreate")
        frame1.Write()
        frame2.Write()
        frame3.Write()
        fileOUT.Close()

time.sleep(1000)
