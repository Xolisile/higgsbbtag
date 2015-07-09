from ROOT import *
import tdrstyle,CMS_lumi
import array
from math import *

#set the tdr style                                                                                                                                                 
tdrstyle.setTDRStyle()

#change the CMS_lumi variables (see CMS_lumi.py)                                                                                                                         #CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
CMS_lumi.lumi_13TeV = "20.1 fb^{-1}"
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"

iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.12

###########################################################################################
 


hs = THStack("hs","Stacked 1D histograms")
hs1 = THStack("hs1","Stacked 1D histograms")
hs2 = THStack("hs2","Stacked 1D histograms")

# creating some 1-D histograms for Zprime
pt_hist_Zprime=TH1F('jet_pt_hist','pt histogram;jet p_{T} [GeV/c]; Events',50,0,8000)
eta_hist_Zprime=TH1F('jet_eta_hist','eta histogram;jet_eta; Events',50,-3,3)
mass_hist_Zprime =TH1F('jet_mass_hist',' mass;m_{jet} [GeV/c^{2}];Events ',100,0,900)
hbbtag_hist_Zprime =TH1F('hbbtag',' Hbbtag;Hbbtag;Events ',100,-1,1)
prunedmass_hist_Zprime=TH1F('prunedmass_hist','prunedmass;prunedmass; ',170,-50,800)
softdropmass_hist_Zprime=TH1F('softdropmass_hist','softdropmass;softdropmass; ',50,-50,800)
prunedmass_hist1_Zprime=TH1F('prunedmass_hist1','prunedmass;prunedmass_Cut1; ',170,-50,800)
softdropmass_hist1_Zprime=TH1F('softdropmass_hist1','softdropmass;softdropmass_Cut1; ',50,-50,800)
prunedmass_hist2_Zprime=TH1F('prunedmass_hist2','prunedmass;prunedmass_Cut2; ',170,-50,800)
softdropmass_hist2_Zprime=TH1F('softdropmass_hist2','softdropmass;softdropmass_Cut2; ',50,-50,800)
prunedmass_hist3_Zprime=TH1F('prunedmass_hist3','prunedmass;prunedmass_Cut3; ',170,-50,800)
softdropmass_hist3_Zprime=TH1F('softdropmass_hist3','softdropmass;softdropmass_Cut3; ',50,-50,800)
prunedmass_hist4_Zprime=TH1F('prunedmass_hist4','prunedmass;prunedmass_Cut4; ',170,-50,800)
softdropmass_hist4_Zprime=TH1F('softdropmass_hist4','softdropmass;softdropmass_Cut4; ',50,-50,800)
prunedmass_hist5_Zprime=TH1F('prunedmass_hist5','prunedmass;prunedmass_Cut5; ',170,-50,800)
softdropmass_hist5_Zprime=TH1F('softdropmass_hist5','softdropmass;softdropmass_Cut5; ',50,-50,800)
prunedmass_hist6_Zprime=TH1F('prunedmass_hist6','prunedmass;prunedmass_Cut6; ',170,-50,800)
softdropmass_hist6_Zprime=TH1F('softdropmass_hist6','softdropmass;softdropmass_Cut6; ',50,-50,800)

# changing to error bars before filling the histogram
#mass_hist.Sumw2()

#Draft paper histograms
SV_mass0_hist=TH1F('SVmass0_hist',';SV_mass_0; ',50,0,7)
SV_EnergyRatio0_hist=TH1F('SVEnergyRatio0_hist',';SV_EnergyRation_0; ',50,0,2)
SV_EnergyRatio1_hist=TH1F('SVEnergyRatio1_hist',';SV_EnergyRation_1; ',50,0,2)

nSL_hist=TH1F('nSL_hist',';nSL; ',50,0,6)
PFL_hist=TH1F('PFL_hist',';PFLepton_ptrel; ',50,0,800)

change_phi=TH1F('Change_phi_hist','phi histogram;SV \Delta\phi ; ',50,-6,6)
change_eta=TH1F('Change_eta_hist','eta histogram;SV \Delta\eta; ',50,-2,2)
change_R=TH1F('Change_R_hist','R histogram;SV \Delta R; ',50,-0.5,2)
zRatio_hist=TH1F('ZRatio_hist',';z_ratio; ',50,0,1)
tauDot_hist=TH1F('TauDot_hist',';tau_dot; ',50,0.9,1)

PFLI_hist=TH1F('PFLepI_hist',';PFLepton_IP2D; ',50,0,28)
tauRatio_hist=TH1F('TauRatio_hist',';tau2/tau1; ',50,0,1)


sampleName = "QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8"
sampleNumber = 3
myfile=TFile("%s/JetTree_mc_subjets_%i.root" %(sampleName, sampleNumber))
ntuple=myfile.Get("btaganaFatJets/ttree")
nEntries=ntuple.GetEntries()
print 'There are ' , nEntries,'entries in your ntuple'


# loop over each event/entry in the ntuple
eventCounter=0
for event in range(nEntries):
    eventCounter += 1
    if ((eventCounter % 1000) == 0):
        print "Event %i" %eventCounter
    # copy next entry into memory and verify
    entrycheck=ntuple.GetEntry(event)
    if entrycheck<=0: continue
    #print getattr(ntuple,"FatJetInfo.nJet")
    for i in range(getattr(ntuple,"FatJetInfo.nJet")):
        pt_hist_Zprime.Fill(getattr(ntuple,"FatJetInfo.Jet_pt")[i])
        eta_hist_Zprime.Fill(getattr(ntuple,"FatJetInfo.Jet_eta")[i])
        mass_hist_Zprime.Fill(getattr(ntuple,"FatJetInfo.Jet_mass")[i])
        hbbtag_hist_Zprime.Fill(getattr(ntuple,"FatJetInfo.Jet_BDTG_Cascade")[i])
        #####################################################################
        SV_mass0_hist.Fill(getattr(ntuple,"FatJetInfo.Jet_SV_mass_0")[i])
        SV_EnergyRatio0_hist.Fill(getattr(ntuple,"FatJetInfo.Jet_SV_EnergyRatio_0")[i])
        SV_EnergyRatio1_hist.Fill(getattr(ntuple,"FatJetInfo.Jet_SV_EnergyRatio_1")[i])
        nSL_hist.Fill(getattr(ntuple,"FatJetInfo.Jet_nSE")[i]+ getattr(ntuple,"FatJetInfo.Jet_nSM")[i])
        PFL_hist.Fill(getattr(ntuple,"FatJetInfo.Jet_PFLepton_ptrel")[i])
        zRatio_hist.Fill(getattr(ntuple,"FatJetInfo.Jet_z_ratio")[i])
        tauDot_hist.Fill(getattr(ntuple,"FatJetInfo.Jet_tau_dot")[i])
        PFLI_hist.Fill(getattr(ntuple,"FatJetInfo.Jet_PFLepton_IP2D")[i])
        tauRatio_hist.Fill(getattr(ntuple,"FatJetInfo.Jet_tau2")[i]/getattr(ntuple,"FatJetInfo.Jet_tau1")[i])
        ######################################################################
        for n in range(getattr(ntuple,"FatJetInfo.nSV")):
            for m in range(getattr(ntuple,"FatJetInfo.nSV")):
                change_phi.Fill(getattr(ntuple,"FatJetInfo.SV_vtx_phi")[n]-getattr(ntuple,"FatJetInfo.SV_vtx_phi")[m])
                change_eta.Fill(getattr(ntuple,"FatJetInfo.SV_vtx_eta")[n]-getattr(ntuple,"FatJetInfo.SV_vtx_eta")[m])
                change_R.Fill(sqrt((getattr(ntuple,"FatJetInfo.SV_vtx_eta")[n]-getattr(ntuple,"FatJetInfo.SV_vtx_eta")[m])**2+(getattr(ntuple,"FatJetInfo.SV_vtx_phi")[n]-getattr(ntuple,"FatJetInfo.SV_vtx_phi")[m])**2))
        
##########################################################################################

# creating ROOT plots
outFile = TFile("%s_%i_hists.root" %(sampleName, sampleNumber), "recreate")

pt_hist_Zprime.Write()
eta_hist_Zprime.Write()
mass_hist_Zprime.Write()
hbbtag_hist_Zprime.Write()

change_phi.Write()
change_eta.Write()
change_R.Write()

SV_mass0_hist.Write()
SV_EnergyRatio0_hist.Write()
SV_EnergyRatio1_hist.Write()
nSL_hist.Write()
PFL_hist.Write()
zRatio_hist.Write()
tauDot_hist.Write()
PFLI_hist.Write()
tauRatio_hist.Write()

outFile.Write()
outFile.Close()

###########################################################################################