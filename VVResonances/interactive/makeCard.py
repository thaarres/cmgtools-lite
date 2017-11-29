import sys
import ROOT
ROOT.gSystem.Load("libHiggsAnalysisCombinedLimit")
from CMGTools.VVResonances.statistics.DataCardMaker import DataCardMaker
cmd='combineCards.py '

purities=['HPHP','HPLP','LPLP']
purities=['HPLP']

for p in purities:

 card=DataCardMaker('',p,'13TeV',35900,'JJ')
 cat='_'.join(['JJ',p,'13TeV'])
 cmd=cmd+" "+cat+'=datacard_'+cat+'.txt '

 #SIGNAL
 card.addMVVSignalParametricShape2("BulkGWW_MVV","MJJ","JJ_BulkGWW_MVV.json",{'CMS_scale_j':1},{'CMS_res_j':1.0})

 if p=='HPLP':
     card.addMJJSignalParametricShape("Wqq","MJ","JJ_BulkGWW_MJl1_"+p+".json",{'CMS_scale_prunedj':1},{'CMS_res_prunedj':1.0})
     card.addParametricYieldWithUncertainty("XqW",0,"JJ_BulkGWW_MJl1_"+p+".json",1,'CMS_tau21_PtDependence','((0.054/0.041)*(-log(MH/600)))',0.041)
 else:
     card.addMJJSignalParametricShapeNOEXP("Wqq1","MJ1","JJ_BulkGWW_MJl1_"+p+".json",{'CMS_scale_prunedj':1},{'CMS_res_prunedj':1.0})#
     card.addMJJSignalParametricShapeNOEXP("Wqq2","MJ2","JJ_BulkGWW_MJl2_"+p+".json",{'CMS_scale_prunedj':1},{'CMS_res_prunedj':1.0})#

     card.addParametricYieldWithUncertainty("BulkGWW",0,"JJ_BulkGWW_"+p+"_yield.json",1,'CMS_tau21_PtDependence','log(MH/600)',0.041)
    
 card.product3D("BulkGWW","Wqq1","Wqq2","BulkGWW_MVV")
   
 #QCD
 rootFile="JJ_nonRes_2D_"+p+".root"
 card.addHistoShapeFromFile("nonRes",["MJ1","MJ2","MJJ"],rootFile,"histo",['PTXY:CMS_VV_JJ_nonRes_PTXY','OPTXY:CMS_VV_JJ_nonRes_OPTXY','OPTZ:CMS_VV_JJ_nonRes_OPTZ','PTZ:CMS_VV_JJ_nonRes_PTZ'],False,0)    
 card.addFixedYieldFromFile("nonRes",1,"JJ_"+p+".root","nonRes")

 #DATA
 card.importBinnedData("JJ_"+p+".root","data",["MJ1","MJ2","MJJ"])
 
 #SYSTEMATICS

 #luminosity
 card.addSystematic("CMS_lumi","lnN",{'BulkGWW':1.026})

 #kPDF uncertainty for the signal
 card.addSystematic("CMS_pdf","lnN",{'BulkGWW':1.01})

 #W+jets cross section in acceptance-dominated by pruned mass
 card.addSystematic("CMS_VV_JJ_nonRes_norm_"+p,"lnN",{'nonRes':1.5})

 #tau21 
 if p=='HPHP':
     card.addSystematic("CMS_VV_JJ_tau21_eff","lnN",{'BulkGWW':1+0.14})
 if p=='HPLP':
     card.addSystematic("CMS_VV_JJ_tau21_eff","lnN",{'BulkGWW':1-0.33})
               
 #pruned mass scale    
 card.addSystematic("CMS_scale_j","param",[0.0,0.02])
 card.addSystematic("CMS_res_j","param",[0.0,0.05])
 card.addSystematic("CMS_scale_prunedj","param",[0.0,0.0094])
 card.addSystematic("CMS_res_prunedj","param",[0.0,0.2])

 #alternative shapes
 card.addSystematic("CMS_VV_JJ_nonRes_PTXY","param",[0.0,0.333])
 card.addSystematic("CMS_VV_JJ_nonRes_PTZ","param",[0.0,0.333])
 #card.addSystematic("CMS_VV_JJ_nonRes_PT2","param",[0.0,0.333])
 card.addSystematic("CMS_VV_JJ_nonRes_OPTXY","param",[0.0,0.333])
 card.addSystematic("CMS_VV_JJ_nonRes_OPTZ","param",[0.0,0.333])
 #card.addSystematic("CMS_VV_JJ_nonRes_OPT2","param",[0.0,0.333])
 card.makeCard()

#make combined cards
print cmd
