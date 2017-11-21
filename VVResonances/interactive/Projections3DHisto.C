void Projections3DHisto(){

gStyle->SetOptStat(0);
gStyle->SetOptTitle(0);

TFile* fin = new TFile("JJ_nonRes_2D_HPHP.root","READ");
TH3F* hin = (TH3F*)fin->Get("histo");

TFile* finMC = new TFile("JJ_nonRes_COND2D_HPHP_l1.root","READ");
TH3F* hinMC = (TH3F*)finMC->Get("mjet_mvv_nominal_3D");
//TH3F* hinMChw = (TH3F*)finMC->Get("mjet_mvv_altshapeUp_3D");
//TH3F* hinMCmg = (TH3F*)finMC->Get("mjet_mvv_altshape2_3D");

int binsx = hin->GetNbinsX();
float xmin = hin->GetXaxis()->GetXmin();
float xmax = hin->GetXaxis()->GetXmax();
std::cout << "xmin " << xmin << " xmax " << xmax << " binsx " << binsx << std::endl;

int binsy = hin->GetNbinsY();
float ymin = hin->GetYaxis()->GetXmin();
float ymax = hin->GetYaxis()->GetXmax();
std::cout << "ymin " << ymin << " ymax " << ymax << " binsy " << binsy << std::endl;

int binsz = hin->GetNbinsZ();
float zmin = hin->GetZaxis()->GetXmin();
float zmax = hin->GetZaxis()->GetXmax();
std::cout << "zmin " << zmin << " zmax " << zmax << " binsz " << binsz << std::endl;

std::vector<TH1F*> hx;
std::vector<TH1F*> hy;
std::vector<TH1F*> hz;
std::vector<TH1F*> hxMC;
std::vector<TH1F*> hxMChw;
std::vector<TH1F*> hxMCmg;
std::vector<TH1F*> hyMC;
std::vector<TH1F*> hyMChw;
std::vector<TH1F*> hyMCmg;
std::vector<TH1F*> hzMC;
std::vector<TH1F*> hzMChw;
std::vector<TH1F*> hzMCmg;

int zbinMin[4] = {1,1,hin->GetZaxis()->FindBin(1600),hin->GetZaxis()->FindBin(5000)};
int zbinMax[4] = {binsz,hin->GetZaxis()->FindBin(1600),hin->GetZaxis()->FindBin(5000),binsz};
int colors[5] = {1,99,9,8,94};
float scale[4] = {1.,0.7,5,10000};

for(int i=0; i<4; ++i){

 std::cout << "Plotting mJJ projections " << zbinMin[i] << " " << zbinMax[i] << std::endl;
 std::stringstream ss; ss.str("");
 ss << "px_" << i << std::endl;
 hx.push_back((TH1F*)hin->ProjectionX(ss.str().c_str(),1,binsy,zbinMin[i],zbinMax[i]));
 ss.str(""); ss << "py_" << i << std::endl;
 hy.push_back((TH1F*)hin->ProjectionY(ss.str().c_str(),1,binsx,zbinMin[i],zbinMax[i]));
 ss.str(""); ss << "pxMC_" << i << std::endl;
 hxMC.push_back((TH1F*)hinMC->ProjectionX(ss.str().c_str(),1,binsy,zbinMin[i],zbinMax[i]));
 ss.str(""); ss << "pyMC_" << i << std::endl;
 hyMC.push_back((TH1F*)hinMC->ProjectionY(ss.str().c_str(),1,binsx,zbinMin[i],zbinMax[i])); 

 //ss.str(""); ss << "pxMChw_" << i << std::endl;
 //hxMChw.push_back((TH1F*)hinMChw->ProjectionX(ss.str().c_str(),1,binsy,zbinMin[i],zbinMax[i]));
 //ss.str(""); ss << "pyMChw_" << i << std::endl;
 //hyMChw.push_back((TH1F*)hinMChw->ProjectionY(ss.str().c_str(),1,binsx,zbinMin[i],zbinMax[i])); 
 
 //ss.str(""); ss << "pxMCmg_" << i << std::endl;
 //hxMCmg.push_back((TH1F*)hinMChw->ProjectionX(ss.str().c_str(),1,binsy,zbinMin[i],zbinMax[i]));
 //ss.str(""); ss << "pyMCmg_" << i << std::endl;
 //hyMCmg.push_back((TH1F*)hinMCmg->ProjectionY(ss.str().c_str(),1,binsx,zbinMin[i],zbinMax[i])); 
  
}

for(int i=0; i<4; ++i){
  
 hx[i]->Scale(scale[i]);
 hy[i]->Scale(scale[i]);
 hxMC[i]->Scale(scale[i]);
 hyMC[i]->Scale(scale[i]);
  
 hx[i]->SetLineColor(colors[i]);
 hx[i]->SetMarkerColor(colors[i]);
 hy[i]->SetLineColor(colors[i]);
 hy[i]->SetMarkerColor(colors[i]);
 hxMC[i]->SetLineColor(colors[i]);
 hxMC[i]->SetMarkerColor(colors[i]);
 hxMC[i]->SetMarkerSize(0.5);
 hyMC[i]->SetLineColor(colors[i]);
 hyMC[i]->SetMarkerColor(colors[i]); 
 hyMC[i]->SetMarkerSize(0.5);

}

TLegend* leg = new TLegend(0.6,0.6,0.85,0.8);
leg->AddEntry(hxMC[0],"Simulation","P");
leg->AddEntry(hx[0],"Template","L");
leg->AddEntry(hx[1],"1 < m_{jj} < 1.6 TeV");
leg->AddEntry(hx[2],"1.6 < m_{jj} < 5 TeV");
leg->AddEntry(hx[3],"5 < m_{jj} < 7 TeV");
 
TCanvas* cx = new TCanvas("cx","cx");
cx->cd();
for(int i=0; i<4; ++i){ hx[i]->Draw("HISTsame"); hxMC[i]->Draw("PEsame");}
hx[0]->GetXaxis()->SetTitle("m_{jet1} (proj. x) [GeV]");
leg->Draw();

TCanvas* cy = new TCanvas("cy","cy");
cy->cd();
for(int i=0; i<4; ++i){ hy[i]->Draw("HISTsame"); hyMC[i]->Draw("PEsame");}
hy[0]->GetXaxis()->SetTitle("m_{jet2} (proj. y) [GeV]");
leg->Draw();

int xbinMin[5] = {1,hin->GetXaxis()->FindBin(55),hin->GetXaxis()->FindBin(100),hin->GetXaxis()->FindBin(150),hin->GetXaxis()->FindBin(300)};
int xbinMax[5] = {binsx,hin->GetXaxis()->FindBin(100),hin->GetXaxis()->FindBin(150),hin->GetXaxis()->FindBin(300),binsx};

float scalez[5] = {1.,1.,1.,1.,1.};

for(int i=0; i<5; ++i){

 std::cout << "Plotting mJ projections " << xbinMin[i] << " " << xbinMax[i] << std::endl;
 std::stringstream ss; ss.str("");
 ss << "pz_" << i << std::endl;
 hz.push_back((TH1F*)hin->ProjectionZ(ss.str().c_str(),xbinMin[i],xbinMax[i],xbinMin[i],xbinMax[i]));
 ss.str(""); ss << "pzMC_" << i << std::endl;
 hzMC.push_back((TH1F*)hinMC->ProjectionZ(ss.str().c_str(),xbinMin[i],xbinMax[i],xbinMin[i],xbinMax[i]));

 //ss.str(""); ss << "pzMChw_" << i << std::endl;
 //hzMChw.push_back((TH1F*)hinMChw->ProjectionZ(ss.str().c_str(),xbinMin[i],xbinMax[i],xbinMin[i],xbinMax[i]));
 //ss.str(""); ss << "pzMCmg_" << i << std::endl;
 //hzMCmg.push_back((TH1F*)hinMCmg->ProjectionZ(ss.str().c_str(),xbinMin[i],xbinMax[i],xbinMin[i],xbinMax[i]));
  
}

for(int i=0; i<5; ++i){
 
 hz[i]->Scale(scalez[i]);
 hzMC[i]->Scale(scalez[i]);
  
 hz[i]->SetLineColor(colors[i]);
 hz[i]->SetMarkerColor(colors[i]);
 hzMC[i]->SetLineColor(colors[i]);
 hzMC[i]->SetMarkerColor(colors[i]);
 hzMC[i]->SetMarkerSize(0.5);
  
}

TLegend* leg2 = new TLegend(0.6,0.55,0.85,0.8);
leg2->AddEntry(hzMC[0],"Simulation","P");
leg2->AddEntry(hz[0],"Template","L");
leg2->AddEntry(hz[1],"55 < m_{jet} < 100 GeV");
leg2->AddEntry(hz[2],"100 < m_{jet} < 150 GeV");
leg2->AddEntry(hz[3],"150 < m_{jet} < 210 GeV");
leg2->AddEntry(hz[4],"300 < m_{jet} < 610 GeV");

TCanvas* cz = new TCanvas("cz","cz");
cz->SetLogy();
cz->cd();
for(int i=0; i<5; ++i){ hz[i]->Draw("HISTsame"); hzMC[i]->Draw("PEsame");}
hz[0]->GetXaxis()->SetTitle("m_{jj} (proj. z) [GeV]");
leg2->Draw();


TH3F* hin_PTZUp = (TH3F*)fin->Get("histo_PTZUp");
TH3F* hin_PTZDown = (TH3F*)fin->Get("histo_PTZDown");
TH3F* hin_OPTZUp = (TH3F*)fin->Get("histo_OPTZUp");
TH3F* hin_OPTZDown = (TH3F*)fin->Get("histo_OPTZDown");

TH1F* hz_PTZUp = (TH1F*)hin_PTZUp->ProjectionZ("pz_PTZUp",xbinMin[0],xbinMax[0],xbinMin[0],xbinMax[0]);
hz_PTZUp->SetLineColor(kMagenta);
TH1F* hz_PTZDown = (TH1F*)hin_PTZDown->ProjectionZ("pz_PTZDown",xbinMin[0],xbinMax[0],xbinMin[0],xbinMax[0]);
hz_PTZDown->SetLineColor(kMagenta);
TH1F* hz_OPTZUp = (TH1F*)hin_OPTZUp->ProjectionZ("pz_OPTZUp",xbinMin[0],xbinMax[0],xbinMin[0],xbinMax[0]);
hz_OPTZUp->SetLineColor(210);
TH1F* hz_OPTZDown = (TH1F*)hin_OPTZDown->ProjectionZ("pz_OPTZDown",xbinMin[0],xbinMax[0],xbinMin[0],xbinMax[0]);
hz_OPTZDown->SetLineColor(210);

//hzMCmg[0]->SetLineColor(kBlack);
//hzMCmg[0]->SetLineStyle(2);
//hzMChw[0]->SetLineColor(kRed);
//hzMChw[0]->SetLineStyle(2);

TLegend* leg3 = new TLegend(0.6,0.55,0.95,0.8);
leg3->AddEntry(hzMC[0],"Simulation","P");
leg3->AddEntry(hz[0],"Template nominal","L");
leg3->AddEntry(hz_PTZUp,"p_{T} syst. up/down","L");
leg3->AddEntry(hz_OPTZUp,"1/p_{T} syst. up/down","L");

TCanvas* czSyst = new TCanvas("czSyst","czSyst");
czSyst->cd();
czSyst->SetLogy();

hz[0]->Draw("HIST");
hz_PTZUp->Draw("HISTsame");
hz_PTZDown->Draw("HISTsame"); 
hz_OPTZUp->Draw("HISTsame");
hz_OPTZDown->Draw("HISTsame");
hzMC[0]->Draw("same");
leg3->Draw();


TH3F* hin_PTXUp = (TH3F*)fin->Get("histo_PTXUp");
TH3F* hin_PTXDown = (TH3F*)fin->Get("histo_PTXDown");
TH3F* hin_OPTXUp = (TH3F*)fin->Get("histo_OPTXUp");
TH3F* hin_OPTXDown = (TH3F*)fin->Get("histo_OPTXDown");

TH1F* hx_PTXUp = (TH1F*)hin_PTXUp->ProjectionX("px_PTXUp",1,binsy,zbinMin[0],zbinMax[0]);
hx_PTXUp->SetLineColor(kMagenta);
TH1F* hx_PTXDown = (TH1F*)hin_PTXDown->ProjectionX("px_PTXDown",1,binsy,zbinMin[0],zbinMax[0]);
hx_PTXDown->SetLineColor(kMagenta);
TH1F* hx_OPTXUp = (TH1F*)hin_OPTXUp->ProjectionX("px_OPTXUp",1,binsy,zbinMin[0],zbinMax[0]);
hx_OPTXUp->SetLineColor(210);
TH1F* hx_OPTXDown = (TH1F*)hin_OPTXDown->ProjectionX("px_OPTXDown",1,binsy,zbinMin[0],zbinMax[0]);
hx_OPTXDown->SetLineColor(210);

TCanvas* cxSyst = new TCanvas("cxSyst","cxSyst");
cxSyst->cd();
hx[0]->Draw("HIST");
hx_PTXUp->Draw("HISTsame");
hx_PTXDown->Draw("HISTsame"); 
hx_OPTXUp->Draw("HISTsame");
hx_OPTXDown->Draw("HISTsame");
hxMC[0]->Draw("same");
leg3->Draw();

TH3F* hin_PTYUp = (TH3F*)fin->Get("histo_PTYUp");
TH3F* hin_PTYDown = (TH3F*)fin->Get("histo_PTYDown");
TH3F* hin_OPTYUp = (TH3F*)fin->Get("histo_OPTYUp");
TH3F* hin_OPTYDown = (TH3F*)fin->Get("histo_OPTYDown");

TH1F* hy_PTYUp = (TH1F*)hin_PTYUp->ProjectionY("py_PTYUp",1,binsy,zbinMin[0],zbinMax[0]);
hy_PTYUp->SetLineColor(kMagenta);
TH1F* hy_PTYDown = (TH1F*)hin_PTYDown->ProjectionY("py_PTYDown",1,binsy,zbinMin[0],zbinMax[0]);
hy_PTYDown->SetLineColor(kMagenta);
TH1F* hy_OPTYUp = (TH1F*)hin_OPTYUp->ProjectionY("py_OPTYUp",1,binsy,zbinMin[0],zbinMax[0]);
hy_OPTYUp->SetLineColor(210);
TH1F* hy_OPTYDown = (TH1F*)hin_OPTYDown->ProjectionY("py_OPTYDown",1,binsy,zbinMin[0],zbinMax[0]);
hy_OPTYDown->SetLineColor(210);

TCanvas* cySyst = new TCanvas("cySyst","cySyst");
cySyst->cd();
hy[0]->Draw("HIST");
hy_PTYUp->Draw("HISTsame");
hy_PTYDown->Draw("HISTsame"); 
hy_OPTYUp->Draw("HISTsame");
hy_OPTYDown->Draw("HISTsame");
hyMC[0]->Draw("same");

TCanvas* cxz = new TCanvas("cxz","cxz");
cxz->cd();
TH2F* hxz = (TH2F*)hin->Project3D("zx");
hxz->Draw("COLZ");

TCanvas* cyz = new TCanvas("cyz","cyz");
cyz->cd();
TH2F* hyz = (TH2F*)hin->Project3D("zy");
hyz->Draw("COLZ");

}
