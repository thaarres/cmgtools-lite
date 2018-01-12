void Projections3DHisto(){

gStyle->SetOptStat(0);
gStyle->SetOptTitle(0);

TFile* fin = new TFile("JJ_nonRes_2D_HPHP.root","READ");
TH3F* hin = (TH3F*)fin->Get("histo");
hin->Scale(1./hin->Integral());


TFile* finMC = new TFile("JJ_nonRes_HPHP.root","READ");
TH3F* hinMC = (TH3F*)finMC->Get("nonRes");
hinMC->Scale(1./hinMC->Integral());

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
std::vector<TH1F*> hyMC;
std::vector<TH1F*> hzMC;

int zbinMin[4] = {1,1,hin->GetZaxis()->FindBin(1300),hin->GetZaxis()->FindBin(2000)};
int zbinMax[4] = {binsz,hin->GetZaxis()->FindBin(1300),hin->GetZaxis()->FindBin(2000),binsz};
int colors[5] = {1,99,9,8,94};

float scale[4] = {1.,0.8,2.,30.};

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
 hxMC[i]->SetMarkerStyle(20);
 hxMC[i]->SetMarkerSize(0.5);
 hyMC[i]->SetLineColor(colors[i]);
 hyMC[i]->SetMarkerColor(colors[i]); 
 hyMC[i]->SetMarkerStyle(20);
 hyMC[i]->SetMarkerSize(0.5);

}

TLegend* leg = new TLegend(0.6,0.6,0.85,0.8);
leg->AddEntry(hxMC[0],"Simulation (Pythia8)","LP");
leg->AddEntry(hx[0],"Template","L");
leg->AddEntry(hx[1],"1 < m_{jj} < 1.3 TeV");
leg->AddEntry(hx[2],"1.3 < m_{jj} < 2 TeV");
leg->AddEntry(hx[3],"2 < m_{jj} < 5 TeV");
 
TCanvas* cx = new TCanvas("cx","cx");
cx->cd();
hx[0]->SetMinimum(0);
for(int i=0; i<4; ++i){ hx[i]->Draw("HISTsame"); hxMC[i]->Draw("PEsame");}
hx[0]->GetXaxis()->SetTitle("m_{jet1} (proj. x) [GeV]");
leg->Draw();

TCanvas* cy = new TCanvas("cy","cy");
cy->cd();
hy[0]->SetMinimum(0);
for(int i=0; i<4; ++i){ hy[i]->Draw("HISTsame"); hyMC[i]->Draw("PEsame");}
hy[0]->GetXaxis()->SetTitle("m_{jet2} (proj. y) [GeV]");
leg->Draw();

int xbinMin[5] = {1,hin->GetXaxis()->FindBin(55),hin->GetXaxis()->FindBin(70),hin->GetXaxis()->FindBin(100),hin->GetXaxis()->FindBin(150)};
int xbinMax[5] = {binsx,hin->GetXaxis()->FindBin(70),hin->GetXaxis()->FindBin(100),hin->GetXaxis()->FindBin(150),binsx};

float scalez[5] = {1.,1.,0.1,0.01,0.001};

for(int i=0; i<5; ++i){

 std::cout << "Plotting mJ projections " << xbinMin[i] << " " << xbinMax[i] << std::endl;
 std::stringstream ss; ss.str("");
 ss << "pz_" << i << std::endl;
 hz.push_back((TH1F*)hin->ProjectionZ(ss.str().c_str(),xbinMin[i],xbinMax[i],xbinMin[i],xbinMax[i]));
 ss.str(""); ss << "pzMC_" << i << std::endl;
 hzMC.push_back((TH1F*)hinMC->ProjectionZ(ss.str().c_str(),xbinMin[i],xbinMax[i],xbinMin[i],xbinMax[i]));
   
}

for(int i=0; i<5; ++i){
 
 hz[i]->Scale(scalez[i]);
 hzMC[i]->Scale(scalez[i]);
   
 hz[i]->SetLineColor(colors[i]);
 hz[i]->SetMarkerColor(colors[i]);
 hzMC[i]->SetLineColor(colors[i]);
 hzMC[i]->SetMarkerColor(colors[i]);
 hzMC[i]->SetMarkerStyle(20);
 hzMC[i]->SetMarkerSize(0.5);
    
}

TLegend* leg2 = new TLegend(0.6,0.55,0.85,0.8);
leg2->AddEntry(hzMC[0],"Simulation (Pythia8)","LP");
leg2->AddEntry(hz[0],"Template","L");
leg2->AddEntry(hz[1],"55 < m_{jet} < 70 GeV");
leg2->AddEntry(hz[2],"70 < m_{jet} < 100 GeV");
leg2->AddEntry(hz[3],"100 < m_{jet} < 150 GeV");
leg2->AddEntry(hz[4],"150 < m_{jet} < 215 GeV");

TCanvas* cz = new TCanvas("cz","cz");
cz->SetLogy();
cz->cd();
hz[0]->SetMinimum(1E-09);
hz[0]->SetMaximum(0.5);
for(int i=0; i<5; ++i){ hz[i]->Draw("HISTsame"); hzMC[i]->Draw("PEsame");}
hz[0]->GetXaxis()->SetTitle("m_{jj} (proj. z) [GeV]");
leg2->Draw();

TH3F* hin_PTZUp = (TH3F*)fin->Get("histo_PTZUp"); hin_PTZUp->Scale(1./hin_PTZUp->Integral());
TH3F* hin_PTZDown = (TH3F*)fin->Get("histo_PTZDown"); hin_PTZDown->Scale(1./hin_PTZDown->Integral());
TH3F* hin_OPTZUp = (TH3F*)fin->Get("histo_OPTZUp"); hin_OPTZUp->Scale(1./hin_OPTZUp->Integral());
TH3F* hin_OPTZDown = (TH3F*)fin->Get("histo_OPTZDown"); hin_OPTZDown->Scale(1./hin_OPTZDown->Integral());

TH1F* hz_PTZUp = (TH1F*)hin_PTZUp->ProjectionZ("pz_PTZUp",xbinMin[0],xbinMax[0],xbinMin[0],xbinMax[0]);
hz_PTZUp->SetLineColor(kMagenta);
TH1F* hz_PTZDown = (TH1F*)hin_PTZDown->ProjectionZ("pz_PTZDown",xbinMin[0],xbinMax[0],xbinMin[0],xbinMax[0]);
hz_PTZDown->SetLineColor(kMagenta);
TH1F* hz_OPTZUp = (TH1F*)hin_OPTZUp->ProjectionZ("pz_OPTZUp",xbinMin[0],xbinMax[0],xbinMin[0],xbinMax[0]);
hz_OPTZUp->SetLineColor(210);
TH1F* hz_OPTZDown = (TH1F*)hin_OPTZDown->ProjectionZ("pz_OPTZDown",xbinMin[0],xbinMax[0],xbinMin[0],xbinMax[0]);
hz_OPTZDown->SetLineColor(210);

TLegend* leg3 = new TLegend(0.6,0.55,0.95,0.8);
leg3->AddEntry(hzMC[0],"Simulation (Pythia8)","LP");
leg3->AddEntry(hz[0],"Template","L");
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


TH3F* hin_PTXUp = (TH3F*)fin->Get("histo_PTXYUp"); hin_PTXUp->Scale(1./hin_PTXUp->Integral());
TH3F* hin_PTXDown = (TH3F*)fin->Get("histo_PTXYDown"); hin_PTXDown->Scale(1./hin_PTXDown->Integral());
TH3F* hin_OPTXUp = (TH3F*)fin->Get("histo_OPTXYUp"); hin_OPTXUp->Scale(1./hin_OPTXUp->Integral());
TH3F* hin_OPTXDown = (TH3F*)fin->Get("histo_OPTXYDown"); hin_OPTXDown->Scale(1./hin_OPTXDown->Integral());

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

TH3F* hin_PTYUp = (TH3F*)fin->Get("histo_PTYUp"); hin_PTYUp->Scale(1./hin_PTYUp->Integral());
TH3F* hin_PTYDown = (TH3F*)fin->Get("histo_PTYDown"); hin_PTYDown->Scale(1./hin_PTYDown->Integral());
TH3F* hin_OPTYUp = (TH3F*)fin->Get("histo_OPTYUp"); hin_OPTYUp->Scale(1./hin_OPTYUp->Integral());
TH3F* hin_OPTYDown = (TH3F*)fin->Get("histo_OPTYDown"); hin_OPTYDown->Scale(1./hin_OPTYDown->Integral());

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
