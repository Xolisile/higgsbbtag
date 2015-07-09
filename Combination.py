# python import
from ROOT import *
import tdrstyle,CMS_lumi
import array
from math import *


#change the CMS_lumi variables (see CMS_lumi.py)                                                                                                                         #CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
CMS_lumi.lumi_13TeV = "20.1 fb^{-1}"
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"

iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.12
#SetAtlasStyle();
gStyle.SetPalette(1)
# Read in the histogram for the low-mass region
Wprime = TFile("WprimeToWhToWhadhbb_narrow_M-2000_13TeV-madgraph_1_hists.root")
TTJets = TFile("TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1_hists.root")
QCD = TFile("QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8_2_hists.root")

################################################################################
change_phi_Wprime=Wprime.Get("Change_phi_hist")
change_phi_Wprime.SetLineColor(1)
change_phi_TTJets=TTJets.Get("Change_phi_hist")
change_phi_TTJets.SetLineColor(2)
change_phi_QCD=QCD.Get("Change_phi_hist")
change_phi_QCD.SetLineColor(3)

hs = THStack("hs"," ")

leg = TLegend(0.7, 0.7, .85, .9)
leg.SetTextSize(0.03)
leg.AddEntry(change_phi_Wprime, "Wprime",'L')
leg.AddEntry(change_phi_TTJets, "TTJets",'L')
leg.AddEntry(change_phi_QCD, "QCD",'L')
hs.Add(change_phi_Wprime)
hs.Add(change_phi_TTJets)
hs.Add(change_phi_QCD)
MyC = TCanvas("MyC","Project",1)
hs.Draw()
hs.GetXaxis().SetTitle("\Delta \phi")
leg.Draw('same')
#CMS_lumi.CMS_lumi(MyC2, 14, iPos)
MyC.SaveAs("Change_phi_histos.pdf")
MyC.Update()
################################################################################

change_eta_Wprime=Wprime.Get("Change_eta_hist")
change_eta_Wprime.SetLineColor(1)
change_eta_TTJets=TTJets.Get("Change_eta_hist")
change_eta_TTJets.SetLineColor(2)
change_eta_QCD=QCD.Get("Change_eta_hist")
change_eta_QCD.SetLineColor(3)

hs1 = THStack("hs1"," ")

leg1 = TLegend(0.7, 0.7, .85, .9)
leg1.SetTextSize(0.03)
leg1.AddEntry(change_eta_Wprime, "Wprime",'L')
leg1.AddEntry(change_eta_TTJets, "TTJets",'L')
leg1.AddEntry(change_eta_QCD, "QCD",'L')
hs1.Add(change_eta_Wprime)
hs1.Add(change_eta_TTJets)
hs1.Add(change_eta_QCD)
MyC1 = TCanvas("MyC1","Project",1)
hs1.Draw()
hs1.GetXaxis().SetTitle("\Delta \eta")
leg1.Draw('same')
#CMS_lumi.CMS_lumi(MyC2, 14, iPos)
MyC1.SaveAs("Change_eta_histos.pdf")
MyC1.Update()

###############################################################################

change_R_Wprime=Wprime.Get("Change_R_hist")
change_R_Wprime.SetLineColor(1)
change_R_TTJets=TTJets.Get("Change_R_hist")
change_R_TTJets.SetLineColor(2)
change_R_QCD=QCD.Get("Change_R_hist")
change_R_QCD.SetLineColor(3)

hs2 = THStack("hs2"," ")

leg2 = TLegend(0.7, 0.7, .85, .9)
leg2.SetTextSize(0.03)
leg2.AddEntry(change_R_Wprime, "Wprime",'L')
leg2.AddEntry(change_R_TTJets, "TTJets",'L')
leg2.AddEntry(change_R_QCD, "QCD",'L')
hs2.Add(change_R_Wprime)
hs2.Add(change_R_TTJets)
hs2.Add(change_R_QCD)
MyC2 = TCanvas("MyC2","Project",1)
hs2.Draw()
hs2.GetXaxis().SetTitle("\Delta R")
leg2.Draw('same')
#CMS_lumi.CMS_lumi(MyC2, 14, iPos)
MyC2.SaveAs("Change_R_histos.pdf")
MyC2.Update()

###############################################################################

SVmass_0_Wprime=Wprime.Get("SVmass0_hist")
SVmass_0_Wprime.SetLineColor(1)
SVmass_0_TTJets=TTJets.Get("SVmass0_hist")
SVmass_0_TTJets.SetLineColor(2)
SVmass_0_QCD=QCD.Get("SVmass0_hist")
SVmass_0_QCD.SetLineColor(3)

hs3 = THStack("hs3"," ")

leg3 = TLegend(0.7, 0.7, .85, .9)
leg3.SetTextSize(0.03)
leg3.AddEntry(SVmass_0_Wprime, "Wprime",'L')
leg3.AddEntry(SVmass_0_TTJets, "TTJets",'L')
leg3.AddEntry(SVmass_0_QCD, "QCD",'L')
hs3.Add(SVmass_0_Wprime)
hs3.Add(SVmass_0_TTJets)
hs3.Add(SVmass_0_QCD)
MyC3 = TCanvas("MyC3","Project",1)
hs3.Draw()
hs3.GetXaxis().SetTitle("SVmass_0")
leg3.Draw('same')
#CMS_lumi.CMS_lumi(MyC2, 14, iPos)
MyC3.SaveAs("SVmass_0_histos.pdf")
MyC3.Update()

################################################################################

SVEnergyRatio_0_Wprime=Wprime.Get("SVEnergyRatio0_hist")
SVEnergyRatio_0_Wprime.SetLineColor(1)
SVEnergyRatio_0_TTJets=TTJets.Get("SVEnergyRatio0_hist")
SVEnergyRatio_0_TTJets.SetLineColor(2)
SVEnergyRatio_0_QCD=QCD.Get("SVEnergyRatio0_hist")
SVEnergyRatio_0_QCD.SetLineColor(3)

hs4 = THStack("hs4"," ")

leg4 = TLegend(0.7, 0.7, .85, .9)
leg4.SetTextSize(0.03)
leg4.AddEntry(SVEnergyRatio_0_Wprime, "Wprime",'L')
leg4.AddEntry(SVEnergyRatio_0_TTJets, "TTJets",'L')
leg4.AddEntry(SVEnergyRatio_0_QCD, "QCD",'L')
hs4.Add(SVEnergyRatio_0_Wprime)
hs4.Add(SVEnergyRatio_0_TTJets)
hs4.Add(SVEnergyRatio_0_QCD)
MyC4 = TCanvas("MyC4","Project",1)
hs4.Draw()
hs4.GetXaxis().SetTitle("SVEnergyRatio_0")
leg4.Draw('same')
#CMS_lumi.CMS_lumi(MyC2, 14, iPos)
MyC4.SaveAs("SVEnergyRatio_0_histos.pdf")
MyC4.Update()

################################################################################

SVEnergyRatio_1_Wprime=Wprime.Get("SVEnergyRatio1_hist")
SVEnergyRatio_1_Wprime.SetLineColor(1)
SVEnergyRatio_1_TTJets=TTJets.Get("SVEnergyRatio1_hist")
SVEnergyRatio_1_TTJets.SetLineColor(2)
SVEnergyRatio_1_QCD=QCD.Get("SVEnergyRatio1_hist")
SVEnergyRatio_1_QCD.SetLineColor(3)

hs5 = THStack("hs5"," ")

leg5 = TLegend(0.7, 0.7, .85, .9)
leg5.SetTextSize(0.03)
leg5.AddEntry(SVEnergyRatio_1_Wprime, "Wprime",'L')
leg5.AddEntry(SVEnergyRatio_1_TTJets, "TTJets",'L')
leg5.AddEntry(SVEnergyRatio_1_QCD, "QCD",'L')
hs5.Add(SVEnergyRatio_1_Wprime)
hs5.Add(SVEnergyRatio_1_TTJets)
hs5.Add(SVEnergyRatio_1_QCD)
MyC5 = TCanvas("MyC5","Project",1)
hs5.Draw()
hs5.GetXaxis().SetTitle("SVEnergyRatio_1")
leg5.Draw('same')
#CMS_lumi.CMS_lumi(MyC2, 14, iPos)
MyC5.SaveAs("SVEnergyRatio_1_histos.pdf")
MyC5.Update()

################################################################################

nSL_Wprime=Wprime.Get("nSL_hist")
nSL_Wprime.SetLineColor(1)
nSL_TTJets=TTJets.Get("nSL_hist")
nSL_TTJets.SetLineColor(2)
nSL_QCD=QCD.Get("nSL_hist")
nSL_QCD.SetLineColor(3)

hs6 = THStack("hs6"," ")

leg6 = TLegend(0.7, 0.7, .85, .9)
leg6.SetTextSize(0.03)
leg6.AddEntry(nSL_Wprime, "Wprime",'L')
leg6.AddEntry(nSL_TTJets, "TTJets",'L')
leg6.AddEntry(nSL_QCD, "QCD",'L')
hs6.Add(nSL_Wprime)
hs6.Add(nSL_TTJets)
hs6.Add(nSL_QCD)
MyC6 = TCanvas("MyC6","Project",1)
hs6.Draw()
hs6.GetXaxis().SetTitle("nSL")
leg6.Draw('same')
#CMS_lumi.CMS_lumi(MyC2, 14, iPos)
MyC6.SaveAs("nSL_histos.pdf")
MyC6.Update()

################################################################################

PFL_Wprime=Wprime.Get("PFL_hist")
PFL_Wprime.SetLineColor(1)
PFL_TTJets=TTJets.Get("PFL_hist")
PFL_TTJets.SetLineColor(2)
PFL_QCD=QCD.Get("PFL_hist")
PFL_QCD.SetLineColor(3)

hs7 = THStack("hs7"," ")

leg7 = TLegend(0.7, 0.7, .85, .9)
leg7.SetTextSize(0.03)
leg7.AddEntry(PFL_Wprime, "Wprime",'L')
leg7.AddEntry(PFL_TTJets, "TTJets",'L')
leg7.AddEntry(PFL_QCD, "QCD",'L')
hs7.Add(PFL_Wprime)
hs7.Add(PFL_TTJets)
hs7.Add(PFL_QCD)
MyC7 = TCanvas("MyC7","Project",1)
hs7.Draw()
hs7.GetXaxis().SetTitle("PFLepton_ptrel")
leg7.Draw('same')
#CMS_lumi.CMS_lumi(MyC2, 14, iPos)
MyC7.SaveAs("PFL_histos.pdf")
MyC7.Update()

################################################################################

ZRatio_Wprime=Wprime.Get("ZRatio_hist")
ZRatio_Wprime.SetLineColor(1)
ZRatio_TTJets=TTJets.Get("ZRatio_hist")
ZRatio_TTJets.SetLineColor(2)
ZRatio_QCD=QCD.Get("ZRatio_hist")
ZRatio_QCD.SetLineColor(3)

hs8 = THStack("hs8"," ")

leg8 = TLegend(0.7, 0.7, .85, .9)
leg8.SetTextSize(0.03)
leg8.AddEntry(ZRatio_Wprime, "Wprime",'L')
leg8.AddEntry(ZRatio_TTJets, "TTJets",'L')
leg8.AddEntry(ZRatio_QCD, "QCD",'L')
hs8.Add(ZRatio_Wprime)
hs8.Add(ZRatio_TTJets)
hs8.Add(ZRatio_QCD)
MyC8 = TCanvas("MyC8","Project",1)
hs8.Draw()
hs8.GetXaxis().SetTitle("ZRatio")
leg8.Draw('same')
#CMS_lumi.CMS_lumi(MyC2, 14, iPos)
MyC8.SaveAs("ZRatio_histos.pdf")
MyC8.Update()

################################################################################

TauDot_Wprime=Wprime.Get("TauDot_hist")
TauDot_Wprime.SetLineColor(1)
TauDot_TTJets=TTJets.Get("TauDot_hist")
TauDot_TTJets.SetLineColor(2)
TauDot_QCD=QCD.Get("TauDot_hist")
TauDot_QCD.SetLineColor(3)

hs9 = THStack("hs9"," ")

leg9 = TLegend(0.7, 0.7, .85, .9)
leg9.SetTextSize(0.03)
leg9.AddEntry(TauDot_Wprime, "Wprime",'L')
leg9.AddEntry(TauDot_TTJets, "TTJets",'L')
leg9.AddEntry(TauDot_QCD, "QCD",'L')
hs9.Add(TauDot_Wprime)
hs9.Add(TauDot_TTJets)
hs9.Add(TauDot_QCD)
MyC9 = TCanvas("MyC9","Project",1)
hs9.Draw()
hs9.GetXaxis().SetTitle("TauDot")
leg9.Draw('same')
#CMS_lumi.CMS_lumi(MyC2, 14, iPos)
MyC9.SaveAs("TauDot_histos.pdf")
MyC9.Update()

################################################################################

PFLepI_Wprime=Wprime.Get("PFLepI_hist")
PFLepI_Wprime.SetLineColor(1)
PFLepI_TTJets=TTJets.Get("PFLepI_hist")
PFLepI_TTJets.SetLineColor(2)
PFLepI_QCD=QCD.Get("PFLepI_hist")
PFLepI_QCD.SetLineColor(3)

hs10 = THStack("hs10"," ")

leg10 = TLegend(0.7, 0.7, .85, .9)
leg10.SetTextSize(0.03)
leg10.AddEntry(PFLepI_Wprime, "Wprime",'L')
leg10.AddEntry(PFLepI_TTJets, "TTJets",'L')
leg10.AddEntry(PFLepI_QCD, "QCD",'L')
hs10.Add(PFLepI_Wprime)
hs10.Add(PFLepI_TTJets)
hs10.Add(PFLepI_QCD)
MyC10 = TCanvas("MyC10","Project",1)
hs10.Draw()
hs10.GetXaxis().SetTitle("PFLepton_I2PD")
leg10.Draw('same')
#CMS_lumi.CMS_lumi(MyC2, 14, iPos)
MyC10.SaveAs("PFLepton_I2PD_histos.pdf")
MyC10.Update()

################################################################################

TauRatio_Wprime=Wprime.Get("TauRatio_hist")
TauRatio_Wprime.SetLineColor(1)
TauRatio_TTJets=TTJets.Get("TauRatio_hist")
TauRatio_TTJets.SetLineColor(2)
TauRatio_QCD=QCD.Get("TauRatio_hist")
TauRatio_QCD.SetLineColor(3)

hs11 = THStack("hs11"," ")

leg11 = TLegend(0.7, 0.7, .85, .9)
leg11.SetTextSize(0.03)
leg11.AddEntry(TauRatio_Wprime, "Wprime",'L')
leg11.AddEntry(TauRatio_TTJets, "TTJets",'L')
leg11.AddEntry(TauRatio_QCD, "QCD",'L')
hs11.Add(TauRatio_Wprime)
hs11.Add(TauRatio_TTJets)
hs11.Add(TauRatio_QCD)
MyC11 = TCanvas("MyC11","Project",1)
hs11.Draw()
hs11.GetXaxis().SetTitle("TauRatio")
leg11.Draw('same')
#CMS_lumi.CMS_lumi(MyC2, 14, iPos)
MyC11.SaveAs("TauRatio_histos.pdf")
MyC11.Update()

################################################################################
