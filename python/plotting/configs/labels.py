
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import Artus.HarryPlotter.utility.labels as labels


class LabelsDict(labels.LabelsDict):
	def __init__(self, latex_version="latex", additional_labels=None):
		super(LabelsDict, self).__init__(latex_version=latex_version, additional_labels=additional_labels)
		
		if latex_version == "root":
			self.labels_dict["data"] = "Data"
			self.labels_dict["zll"] = "Z #rightarrow ll"
			self.labels_dict["zmm"] = "Z #rightarrow #mu#mu"
			self.labels_dict["zee"] = "Z #rightarrow ee"
			self.labels_dict["ztt"] = "Z #rightarrow #tau#tau"
			self.labels_dict["tt"] = "t#bar{t} + jets"
			self.labels_dict["wj"] = "W + jets"
			self.labels_dict["vv"] = "Di-boson"
			self.labels_dict["qcd"] = "QCD"
			self.labels_dict["htt"] = "H #rightarrow #tau#tau"
			self.labels_dict["ggh"] = "ggH"
			self.labels_dict["qqh"] = "qqH"
			self.labels_dict["vh"] = "VH"
			self.labels_dict["hww"] = "H #rightarrow WW"
			self.labels_dict["hww125"] = "H(125) #rightarrow WW"
			
			self.labels_dict["channel_tt"] = "#tau_{h}#tau_{h}"
			self.labels_dict["channel_mt"] = "#mu#tau_{h}"
			self.labels_dict["channel_et"] = "e#tau_{h}"
			self.labels_dict["channel_em"] = "e#mu"
			self.labels_dict["channel_mm"] = "#mu#mu"
			self.labels_dict["channel_ee"] = "ee"
			
			self.labels_dict["channel_tt_large"] = "#scale[1.5]{#tau_{h}#tau_{h}}"
			self.labels_dict["channel_mt_large"] = "#scale[1.5]{#mu#tau_{h}}"
			self.labels_dict["channel_et_large"] = "#scale[1.5]{e#tau_{h}}"
			self.labels_dict["channel_em_large"] = "#scale[1.5]{e#mu}"
			self.labels_dict["channel_mm_large"] = "#scale[1.5]{#mu#mu}"
			self.labels_dict["channel_ee_large"] = "#scale[1.5]{ee}"
			
			self.labels_dict["diLepMass"] = "visible mass m_{ll} / GeV"
			self.labels_dict["svfitMass"] = "di-#tau mass m_{#tau#tau} / GeV"
			
			self.labels_dict["tt_decayMode_1"] = "Leading Tau DM"
			self.labels_dict["tt_decayMode_2"] = "Trailing Tau DM"
			self.labels_dict["tt_eta_1"] = "Leading Tau #eta"
			self.labels_dict["tt_eta_2"] = "Trailing Tau #eta"
			self.labels_dict["tt_eta_ll"] = "#eta^{ll}"
			self.labels_dict["tt_eta_llmet"] = "#eta^{ll,MEt}"
			self.labels_dict["tt_eta_sv"] = "SVfit #eta(#tau#tau)"
			self.labels_dict["tt_inclusive"] = "Inclusive"
			self.labels_dict["tt_iso_1"] = "Leading Tau Isolation"
			self.labels_dict["tt_iso_2"] = "Trailing Tau Isolation"
			self.labels_dict["tt_jdeta"] = "#Delta#eta_{jj}"
			self.labels_dict["tt_jeta_1"] = "Leading Jet #eta"
			self.labels_dict["tt_jeta_2"] = "Trailing Jet #eta"
			self.labels_dict["tt_jphi_1"] = "Leading Jet #phi"
			self.labels_dict["tt_jphi_2"] = "Trailing Jet #phi"
			self.labels_dict["tt_jpt_1"] = "Leading Jet p_{T} / GeV"
			self.labels_dict["tt_jpt_2"] = "Trailing Jet p_{T} / GeV"
			self.labels_dict["tt_m_1"] = "Leading Tau Mass / GeV"
			self.labels_dict["tt_m_2"] = "Trailing Tau Mass / GeV"
			self.labels_dict["tt_m_ll"] = "Visible Mass m_{ll} / GeV"
			self.labels_dict["tt_m_llmet"] = "m_{ll,MEt} / GeV"
			self.labels_dict["tt_m_sv"] = "SVfit Mass m_{#tau#tau} / GeV"
			self.labels_dict["tt_met"] = "PFlow E^{miss}_{T}"
			self.labels_dict["tt_metcov00"] = "Cov_{0,0}(E^{miss}_{T})"
			self.labels_dict["tt_metcov01"] = "Cov_{0,1}(E^{miss}_{T})"
			self.labels_dict["tt_metcov10"] = "Cov_{1,0}(E^{miss}_{T})"
			self.labels_dict["tt_metcov11"] = "Cov_{1,1}(E^{miss}_{T})"
			self.labels_dict["tt_metphi"] = "PFlow E^{miss}_{T} #phi"
			self.labels_dict["tt_mjj"] = "Di-jet Mass m_{jj} / GeV"
			self.labels_dict["tt_mt_1"] = "Transverse Mass m_{T} (#tau, E^{miss}_{T}) / GeV"
			self.labels_dict["tt_mt_lep1met"] = "Transverse Mass m_{T} (#tau, E^{miss}_{T}) / GeV"
			self.labels_dict["tt_mt_ll"] = "m_{T}^{ll} / GeV"
			self.labels_dict["tt_mt_llmet"] = "m_{T}^{ll,MEt} / GeV"
			self.labels_dict["tt_mvacov00"] = "Cov_{0,0}(MVA E^{miss}_{T})"
			self.labels_dict["tt_mvacov01"] = "Cov_{0,1}(MVA E^{miss}_{T})"
			self.labels_dict["tt_mvacov10"] = "Cov_{1,0}(MVA E^{miss}_{T})"
			self.labels_dict["tt_mvacov11"] = "Cov_{1,1}(MVA E^{miss}_{T})"
			self.labels_dict["tt_mvamet"] = "MVA E^{miss}_{T} / GeV"
			self.labels_dict["tt_mvametcov00"] = "Cov_{0,0}(MVA E^{miss}_{T})"
			self.labels_dict["tt_mvametcov01"] = "Cov_{0,1}(MVA E^{miss}_{T})"
			self.labels_dict["tt_mvametcov10"] = "Cov_{1,0}(MVA E^{miss}_{T})"
			self.labels_dict["tt_mvametcov11"] = "Cov_{1,1}(MVA E^{miss}_{T})"
			self.labels_dict["tt_mvametphi"] = "#phi(MVA E^{miss}_{T})"
			self.labels_dict["tt_m_vis"] = "Visible Mass m^{vis}_{#tau#tau} / GeV"
			self.labels_dict["tt_nJets30"] = "Number of Jets (p_{T} > 30)"
			self.labels_dict["tt_njets"] = "Number of Jets (p_{T} > 30)"
			self.labels_dict["tt_npu"] = "NPU"
			self.labels_dict["tt_npv"] = "NPV"
			self.labels_dict["tt_phi_1"] = "Leading Tau #phi"
			self.labels_dict["tt_phi_2"] = "Trailing Tau #phi"
			self.labels_dict["tt_phi_ll"] = "#phi^{ll}"
			self.labels_dict["tt_phi_llmet"] = "#phi^{ll,MEt}"
			self.labels_dict["tt_phi_sv"] = "SVfit #phi(#tau#tau)"
			self.labels_dict["tt_pt_1"] = "Leading Tau p_{T} / GeV"
			self.labels_dict["tt_pt_2"] = "Trailing Tau p_{T} / GeV"
			self.labels_dict["tt_pt_ll"] = "p_{T}^{ll} / GeV"
			self.labels_dict["tt_pt_llmet"] = "p_{T}^{ll,MEt}"
			self.labels_dict["tt_pt_sv"] = "SVfit p_{T}(#tau#tau) / GeV"
			self.labels_dict["tt_pt_tt"] = "p_{T}(#tau#tau) / GeV"
			self.labels_dict["tt_puweight"] = "PU Weight"
			self.labels_dict["tt_rho"] = "rho"
			self.labels_dict["tt_metProjectionPar"] = "#nu_{#parallel} / GeV"
			self.labels_dict["tt_metProjectionPerp"] = "#nu_{#perp}  / GeV"
			self.labels_dict["tt_metProjectionPhi"] = "#nu_{#phi}"
			self.labels_dict["tt_svfitMass"] = "SVfit Mass m_{#tau#tau} / GeV"
			self.labels_dict["tt_trigweight_1"] = "Leading Tau Trigger Weight"
			self.labels_dict["tt_trigweight_2"] = "Trailing Tau Trigger Weight"
			self.labels_dict["tt_pZetaMissVis"] = "#left(p^{miss}_{#zeta} #minus 0.85 p^{vis}_{#zeta}#right) / GeV"
			self.labels_dict["tt_pzetamiss"] = "p^{miss}_{#zeta} / GeV"
			self.labels_dict["tt_pzetavis"] = "p^{vis}_{#zeta} / GeV"
			self.labels_dict["mt_decayMode_2"] = "Tau DM"
			self.labels_dict["mt_eta_1"] = "Muon #eta"
			self.labels_dict["mt_eta_2"] = "Tau #eta"
			self.labels_dict["mt_eta_ll"] = "#eta^{ll}"
			self.labels_dict["mt_eta_llmet"] = "#eta^{ll,MEt}"
			self.labels_dict["mt_eta_sv"] = "SVfit #eta(#tau#tau)"
			self.labels_dict["mt_inclusive"] = "Inclusive"
			self.labels_dict["mt_iso_1"] = "Muon Isolation"
			self.labels_dict["mt_iso_2"] = "Tau Isolation"
			self.labels_dict["mt_jdeta"] = "#Delta#eta_{jj}"
			self.labels_dict["mt_jeta_1"] = "Leading Jet #eta"
			self.labels_dict["mt_jeta_2"] = "Trailing Jet #eta"
			self.labels_dict["mt_jphi_1"] = "Leading Jet #phi"
			self.labels_dict["mt_jphi_2"] = "Trailing Jet #phi"
			self.labels_dict["mt_jpt_1"] = "Leading Jet p_{T} / GeV"
			self.labels_dict["mt_jpt_2"] = "Trailing Jet p_{T} / GeV"
			self.labels_dict["mt_m_1"] = "Muon Mass / GeV"
			self.labels_dict["mt_m_2"] = "Tau Mass / GeV"
			self.labels_dict["mt_m_ll"] = "Visible Mass m_{ll} / GeV"
			self.labels_dict["mt_m_llmet"] = "m_{ll,MEt} / GeV"
			self.labels_dict["mt_m_sv"] = "SVfit Mass m_{#tau#tau} / GeV"
			self.labels_dict["mt_met"] = "PFlow E^{miss}_{T}"
			self.labels_dict["mt_metcov00"] = "Cov_{0,0}(E^{miss}_{T})"
			self.labels_dict["mt_metcov01"] = "Cov_{0,1}(E^{miss}_{T})"
			self.labels_dict["mt_metcov10"] = "Cov_{1,0}(E^{miss}_{T})"
			self.labels_dict["mt_metcov11"] = "Cov_{1,1}(E^{miss}_{T})"
			self.labels_dict["mt_metphi"] = "PFlow E^{miss}_{T} #phi"
			self.labels_dict["mt_mjj"] = "Di-jet Mass m_{jj} / GeV"
			self.labels_dict["mt_mt_1"] = "Transverse Mass m_{T} (#mu, E^{miss}_{T}) / GeV"
			self.labels_dict["mt_mt_lep1met"] = "Transverse Mass m_{T} (#mu, E^{miss}_{T}) / GeV"
			self.labels_dict["mt_mt_ll"] = "m_{T}^{ll} / GeV"
			self.labels_dict["mt_mt_llmet"] = "m_{T}^{ll,MEt} / GeV"
			self.labels_dict["mt_mvacov00"] = "Cov_{0,0}(MVA E^{miss}_{T})"
			self.labels_dict["mt_mvacov01"] = "Cov_{0,1}(MVA E^{miss}_{T})"
			self.labels_dict["mt_mvacov10"] = "Cov_{1,0}(MVA E^{miss}_{T})"
			self.labels_dict["mt_mvacov11"] = "Cov_{1,1}(MVA E^{miss}_{T})"
			self.labels_dict["mt_mvamet"] = "MVA E^{miss}_{T} / GeV"
			self.labels_dict["mt_mvametcov00"] = "Cov_{0,0}(MVA E^{miss}_{T})"
			self.labels_dict["mt_mvametcov01"] = "Cov_{0,1}(MVA E^{miss}_{T})"
			self.labels_dict["mt_mvametcov10"] = "Cov_{1,0}(MVA E^{miss}_{T})"
			self.labels_dict["mt_mvametcov11"] = "Cov_{1,1}(MVA E^{miss}_{T})"
			self.labels_dict["mt_mvametphi"] = "#phi(MVA E^{miss}_{T})"
			self.labels_dict["mt_m_vis"] = "Visible Mass m^{vis}_{#tau#tau} / GeV"
			self.labels_dict["mt_nJets30"] = "Number of Jets (p_{T} > 30)"
			self.labels_dict["mt_njets"] = "Number of Jets (p_{T} > 30)"
			self.labels_dict["mt_npu"] = "NPU"
			self.labels_dict["mt_npv"] = "NPV"
			self.labels_dict["mt_phi_1"] = "Muon #phi"
			self.labels_dict["mt_phi_2"] = "Tau #phi"
			self.labels_dict["mt_phi_ll"] = "#phi^{ll}"
			self.labels_dict["mt_phi_llmet"] = "#phi^{ll,MEt}"
			self.labels_dict["mt_phi_sv"] = "SVfit #phi(#tau#tau)"
			self.labels_dict["mt_pt_1"] = "Muon p_{T} / GeV"
			self.labels_dict["mt_pt_2"] = "Tau p_{T} / GeV"
			self.labels_dict["mt_pt_ll"] = "p_{T}^{ll} / GeV"
			self.labels_dict["mt_pt_llmet"] = "p_{T}^{ll,MEt}"
			self.labels_dict["mt_pt_sv"] = "SVfit p_{T}(#tau#tau) / GeV"
			self.labels_dict["mt_pt_tt"] = "p_{T}(#tau#tau) / GeV"
			self.labels_dict["mt_puweight"] = "PU Weight"
			self.labels_dict["mt_rho"] = "rho"
			self.labels_dict["mt_svfitMass"] = "SVfit Mass m_{#tau#tau} / GeV"
			self.labels_dict["mt_trigweight_1"] = "Muon Trigger Weight"
			self.labels_dict["mt_trigweight_2"] = "Tau Trigger Weight"
			self.labels_dict["mt_pZetaMissVis"] = "#left(p^{miss}_{#zeta} #minus 0.85 p^{vis}_{#zeta}#right) / GeV"
			self.labels_dict["mt_pzetamiss"] = "p^{miss}_{#zeta} / GeV"
			self.labels_dict["mt_pzetavis"] = "p^{vis}_{#zeta} / GeV"
			self.labels_dict["mt_metProjectionPar"] = "#nu_{#parallel} / GeV"
			self.labels_dict["mt_metProjectionPerp"] = "#nu_{#perp}  / GeV"
			self.labels_dict["mt_metProjectionPhi"] = "#nu_{#phi}"
			self.labels_dict["et_decayMode_2"] = "Tau DM"
			self.labels_dict["et_eta_1"] = "Electron #eta"
			self.labels_dict["et_eta_2"] = "Tau #eta"
			self.labels_dict["et_eta_ll"] = "#eta^{ll}"
			self.labels_dict["et_eta_llmet"] = "#eta^{ll,MEt}"
			self.labels_dict["et_eta_sv"] = "SVfit #eta(#tau#tau)"
			self.labels_dict["et_inclusive"] = "Inclusive"
			self.labels_dict["et_iso_1"] = "Electron Isolation"
			self.labels_dict["et_iso_2"] = "Tau Isolation"
			self.labels_dict["et_jdeta"] = "#Delta#eta_{jj}"
			self.labels_dict["et_jeta_1"] = "Leading Jet #eta"
			self.labels_dict["et_jeta_2"] = "Trailing Jet #eta"
			self.labels_dict["et_jphi_1"] = "Leading Jet #phi"
			self.labels_dict["et_jphi_2"] = "Trailing Jet #phi"
			self.labels_dict["et_jpt_1"] = "Leading Jet p_{T} / GeV"
			self.labels_dict["et_jpt_2"] = "Trailing Jet p_{T} / GeV"
			self.labels_dict["et_m_1"] = "Electron Mass / GeV"
			self.labels_dict["et_m_2"] = "Tau Mass / GeV"
			self.labels_dict["et_m_ll"] = "Visible Mass m_{ll} / GeV"
			self.labels_dict["et_m_llmet"] = "m_{ll,MEt} / GeV"
			self.labels_dict["et_m_sv"] = "SVfit Mass m_{#tau#tau} / GeV"
			self.labels_dict["et_met"] = "PFlow E^{miss}_{T}"
			self.labels_dict["et_metcov00"] = "Cov_{0,0}(E^{miss}_{T})"
			self.labels_dict["et_metcov01"] = "Cov_{0,1}(E^{miss}_{T})"
			self.labels_dict["et_metcov10"] = "Cov_{1,0}(E^{miss}_{T})"
			self.labels_dict["et_metcov11"] = "Cov_{1,1}(E^{miss}_{T})"
			self.labels_dict["et_metphi"] = "PFlow E^{miss}_{T} #phi"
			self.labels_dict["et_mjj"] = "Di-jet Mass m_{jj} / GeV"
			self.labels_dict["et_mt_1"] = "Transverse Mass m_{T} (e, E^{miss}_{T}) / GeV"
			self.labels_dict["et_mt_lep1met"] = "Transverse Mass m_{T} (e, E^{miss}_{T}) / GeV"
			self.labels_dict["et_mt_ll"] = "m_{T}^{ll} / GeV"
			self.labels_dict["et_mt_llmet"] = "m_{T}^{ll,MEt} / GeV"
			self.labels_dict["et_mvacov00"] = "Cov_{0,0}(MVA E^{miss}_{T})"
			self.labels_dict["et_mvacov01"] = "Cov_{0,1}(MVA E^{miss}_{T})"
			self.labels_dict["et_mvacov10"] = "Cov_{1,0}(MVA E^{miss}_{T})"
			self.labels_dict["et_mvacov11"] = "Cov_{1,1}(MVA E^{miss}_{T})"
			self.labels_dict["et_mvamet"] = "MVA E^{miss}_{T} / GeV"
			self.labels_dict["et_mvametcov00"] = "Cov_{0,0}(MVA E^{miss}_{T})"
			self.labels_dict["et_mvametcov01"] = "Cov_{0,1}(MVA E^{miss}_{T})"
			self.labels_dict["et_mvametcov10"] = "Cov_{1,0}(MVA E^{miss}_{T})"
			self.labels_dict["et_mvametcov11"] = "Cov_{1,1}(MVA E^{miss}_{T})"
			self.labels_dict["et_mvametphi"] = "#phi(MVA E^{miss}_{T})"
			self.labels_dict["et_m_vis"] = "Visible Mass m^{vis}_{#tau#tau} / GeV"
			self.labels_dict["et_nJets30"] = "Number of Jets (p_{T} > 30)"
			self.labels_dict["et_njets"] = "Number of Jets (p_{T} > 30)"
			self.labels_dict["et_npu"] = "NPU"
			self.labels_dict["et_npv"] = "NPV"
			self.labels_dict["et_phi_1"] = "Electron #phi"
			self.labels_dict["et_phi_2"] = "Tau #phi"
			self.labels_dict["et_phi_ll"] = "#phi^{ll}"
			self.labels_dict["et_phi_llmet"] = "#phi^{ll,MEt}"
			self.labels_dict["et_phi_sv"] = "SVfit #phi(#tau#tau)"
			self.labels_dict["et_pt_1"] = "Electron p_{T} / GeV"
			self.labels_dict["et_pt_2"] = "Tau p_{T} / GeV"
			self.labels_dict["et_pt_ll"] = "p_{T}^{ll} / GeV"
			self.labels_dict["et_pt_llmet"] = "p_{T}^{ll,MEt}"
			self.labels_dict["et_pt_sv"] = "SVfit p_{T}(#tau#tau) / GeV"
			self.labels_dict["et_pt_tt"] = "p_{T}(#tau#tau) / GeV"
			self.labels_dict["et_puweight"] = "PU Weight"
			self.labels_dict["et_rho"] = "rho"
			self.labels_dict["et_svfitMass"] = "SVfit Mass m_{#tau#tau} / GeV"
			self.labels_dict["et_trigweight_1"] = "Electron Trigger Weight"
			self.labels_dict["et_trigweight_2"] = "Tau Trigger Weight"
			self.labels_dict["et_pZetaMissVis"] = "#left(p^{miss}_{#zeta} #minus 0.85 p^{vis}_{#zeta}#right) / GeV"
			self.labels_dict["et_pzetamiss"] = "p^{miss}_{#zeta} / GeV"
			self.labels_dict["et_pzetavis"] = "p^{vis}_{#zeta} / GeV"
			self.labels_dict["et_metProjectionPar"] = "#nu_{#parallel} / GeV"
			self.labels_dict["et_metProjectionPerp"] = "#nu_{#perp}  / GeV"
			self.labels_dict["et_metProjectionPhi"] = "#nu_{#phi}"
			self.labels_dict["em_eta_1"] = "Electron #eta"
			self.labels_dict["em_eta_2"] = "Muon #eta"
			self.labels_dict["em_eta_ll"] = "#eta^{ll}"
			self.labels_dict["em_eta_llmet"] = "#eta^{ll,MEt}"
			self.labels_dict["em_eta_sv"] = "SVfit #eta(#tau#tau)"
			self.labels_dict["em_inclusive"] = "Inclusive"
			self.labels_dict["em_iso_1"] = "Electron Isolation"
			self.labels_dict["em_iso_2"] = "Muon Isolation"
			self.labels_dict["em_jdeta"] = "#Delta#eta_{jj}"
			self.labels_dict["em_jeta_1"] = "Leading Jet #eta"
			self.labels_dict["em_jeta_2"] = "Trailing Jet #eta"
			self.labels_dict["em_jphi_1"] = "Leading Jet #phi"
			self.labels_dict["em_jphi_2"] = "Trailing Jet #phi"
			self.labels_dict["em_jpt_1"] = "Leading Jet p_{T} / GeV"
			self.labels_dict["em_jpt_2"] = "Trailing Jet p_{T} / GeV"
			self.labels_dict["em_m_1"] = "Electron Mass / GeV"
			self.labels_dict["em_m_2"] = "Muon Mass / GeV"
			self.labels_dict["em_m_ll"] = "Visible Mass m_{ll} / GeV"
			self.labels_dict["em_m_llmet"] = "m_{ll,MEt} / GeV"
			self.labels_dict["em_m_sv"] = "SVfit Mass m_{#tau#tau} / GeV"
			self.labels_dict["em_met"] = "PFlow E^{miss}_{T}"
			self.labels_dict["em_metcov00"] = "Cov_{0,0}(E^{miss}_{T})"
			self.labels_dict["em_metcov01"] = "Cov_{0,1}(E^{miss}_{T})"
			self.labels_dict["em_metcov10"] = "Cov_{1,0}(E^{miss}_{T})"
			self.labels_dict["em_metcov11"] = "Cov_{1,1}(E^{miss}_{T})"
			self.labels_dict["em_metphi"] = "PFlow E^{miss}_{T} #phi"
			self.labels_dict["em_mjj"] = "Di-jet Mass m_{jj} / GeV"
			self.labels_dict["em_mt_1"] = "Transverse Mass m_{T} (e, E^{miss}_{T}) / GeV"
			self.labels_dict["em_mt_lep1met"] = "Transverse Mass m_{T} (e, E^{miss}_{T}) / GeV"
			self.labels_dict["em_mt_ll"] = "m_{T}^{ll} / GeV"
			self.labels_dict["em_mt_llmet"] = "m_{T}^{ll,MEt} / GeV"
			self.labels_dict["em_mvacov00"] = "Cov_{0,0}(MVA E^{miss}_{T})"
			self.labels_dict["em_mvacov01"] = "Cov_{0,1}(MVA E^{miss}_{T})"
			self.labels_dict["em_mvacov10"] = "Cov_{1,0}(MVA E^{miss}_{T})"
			self.labels_dict["em_mvacov11"] = "Cov_{1,1}(MVA E^{miss}_{T})"
			self.labels_dict["em_mvamet"] = "MVA E^{miss}_{T} / GeV"
			self.labels_dict["em_mvametcov00"] = "Cov_{0,0}(MVA E^{miss}_{T})"
			self.labels_dict["em_mvametcov01"] = "Cov_{0,1}(MVA E^{miss}_{T})"
			self.labels_dict["em_mvametcov10"] = "Cov_{1,0}(MVA E^{miss}_{T})"
			self.labels_dict["em_mvametcov11"] = "Cov_{1,1}(MVA E^{miss}_{T})"
			self.labels_dict["em_mvametphi"] = "#phi(MVA E^{miss}_{T})"
			self.labels_dict["em_m_vis"] = "Visible Mass m^{vis}_{#tau#tau} / GeV"
			self.labels_dict["em_nJets30"] = "Number of Jets (p_{T} > 30)"
			self.labels_dict["em_njets"] = "Number of Jets (p_{T} > 30)"
			self.labels_dict["em_npu"] = "NPU"
			self.labels_dict["em_npv"] = "NPV"
			self.labels_dict["em_phi_1"] = "Electron #phi"
			self.labels_dict["em_phi_2"] = "Muon #phi"
			self.labels_dict["em_phi_ll"] = "#phi^{ll}"
			self.labels_dict["em_phi_llmet"] = "#phi^{ll,MEt}"
			self.labels_dict["em_phi_sv"] = "SVfit #phi(#tau#tau)"
			self.labels_dict["em_pt_1"] = "Electron p_{T} / GeV"
			self.labels_dict["em_pt_2"] = "Muon p_{T} / GeV"
			self.labels_dict["em_pt_ll"] = "p_{T}^{ll} / GeV"
			self.labels_dict["em_pt_llmet"] = "p_{T}^{ll,MEt}"
			self.labels_dict["em_pt_sv"] = "SVfit p_{T}(#tau#tau) / GeV"
			self.labels_dict["em_pt_tt"] = "p_{T}(#tau#tau) / GeV"
			self.labels_dict["em_puweight"] = "PU Weight"
			self.labels_dict["em_rho"] = "rho"
			self.labels_dict["em_svfitMass"] = "SVfit Mass m_{#tau#tau} / GeV"
			self.labels_dict["em_trigweight_1"] = "Electron Trigger Weight"
			self.labels_dict["em_trigweight_2"] = "Muon Trigger Weight"
			self.labels_dict["em_pZetaMissVis"] = "#left(p^{miss}_{#zeta} #minus 0.85 p^{vis}_{#zeta}#right) / GeV"
			self.labels_dict["em_pzetamiss"] = "p^{miss}_{#zeta} / GeV"
			self.labels_dict["em_pzetavis"] = "p^{vis}_{#zeta} / GeV"
			self.labels_dict["em_metProjectionPar"] = "#nu_{#parallel} / GeV"
			self.labels_dict["em_metProjectionPerp"] = "#nu_{#perp}  / GeV"
			self.labels_dict["em_metProjectionPhi"] = "#nu_{#phi}"
			self.labels_dict["mm_eta_1"] = "Leading Muon #eta"
			self.labels_dict["mm_eta_2"] = "Trailing Muon #eta"
			self.labels_dict["mm_eta_ll"] = "#eta^{ll}"
			self.labels_dict["mm_eta_llmet"] = "#eta^{ll,MEt}"
			self.labels_dict["mm_eta_sv"] = "SVfit #eta(#tau#tau)"
			self.labels_dict["mm_inclusive"] = "Inclusive"
			self.labels_dict["mm_iso_1"] = "Leading Muon Isolation"
			self.labels_dict["mm_iso_2"] = "Trailing Muon Isolation"
			self.labels_dict["mm_jdeta"] = "#Delta#eta_{jj}"
			self.labels_dict["mm_jeta_1"] = "Leading Jet #eta"
			self.labels_dict["mm_jeta_2"] = "Trailing Jet #eta"
			self.labels_dict["mm_jphi_1"] = "Leading Jet #phi"
			self.labels_dict["mm_jphi_2"] = "Trailing Jet #phi"
			self.labels_dict["mm_jpt_1"] = "Leading Jet p_{T} / GeV"
			self.labels_dict["mm_jpt_2"] = "Trailing Jet p_{T} / GeV"
			self.labels_dict["mm_m_1"] = "Leading Muon Mass / GeV"
			self.labels_dict["mm_m_2"] = "Trailing Muon Mass / GeV"
			self.labels_dict["mm_m_ll"] = "Visible Mass m_{ll} / GeV"
			self.labels_dict["mm_m_llmet"] = "m_{ll,MEt} / GeV"
			self.labels_dict["mm_m_sv"] = "SVfit Mass m_{#tau#tau} / GeV"
			self.labels_dict["mm_met"] = "PFlow E^{miss}_{T}"
			self.labels_dict["mm_metcov00"] = "Cov_{0,0}(E^{miss}_{T})"
			self.labels_dict["mm_metcov01"] = "Cov_{0,1}(E^{miss}_{T})"
			self.labels_dict["mm_metcov10"] = "Cov_{1,0}(E^{miss}_{T})"
			self.labels_dict["mm_metcov11"] = "Cov_{1,1}(E^{miss}_{T})"
			self.labels_dict["mm_metphi"] = "PFlow E^{miss}_{T} #phi"
			self.labels_dict["mm_mjj"] = "Di-jet Mass m_{jj} / GeV"
			self.labels_dict["mm_mt_1"] = "Transverse Mass m_{T} (#mu, E^{miss}_{T}) / GeV"
			self.labels_dict["mm_mt_lep1met"] = "Transverse Mass m_{T} (#mu, E^{miss}_{T}) / GeV"
			self.labels_dict["mm_mt_ll"] = "m_{T}^{ll} / GeV"
			self.labels_dict["mm_mt_llmet"] = "m_{T}^{ll,MEt} / GeV"
			self.labels_dict["mm_mvacov00"] = "Cov_{0,0}(MVA E^{miss}_{T})"
			self.labels_dict["mm_mvacov01"] = "Cov_{0,1}(MVA E^{miss}_{T})"
			self.labels_dict["mm_mvacov10"] = "Cov_{1,0}(MVA E^{miss}_{T})"
			self.labels_dict["mm_mvacov11"] = "Cov_{1,1}(MVA E^{miss}_{T})"
			self.labels_dict["mm_mvamet"] = "MVA E^{miss}_{T} / GeV"
			self.labels_dict["mm_mvametcov00"] = "Cov_{0,0}(MVA E^{miss}_{T})"
			self.labels_dict["mm_mvametcov01"] = "Cov_{0,1}(MVA E^{miss}_{T})"
			self.labels_dict["mm_mvametcov10"] = "Cov_{1,0}(MVA E^{miss}_{T})"
			self.labels_dict["mm_mvametcov11"] = "Cov_{1,1}(MVA E^{miss}_{T})"
			self.labels_dict["mm_mvametphi"] = "#phi(MVA E^{miss}_{T})"
			self.labels_dict["mm_m_vis"] = "Visible Mass m^{vis}_{#tau#tau} / GeV"
			self.labels_dict["mm_nJets30"] = "Number of Jets (p_{T} > 30)"
			self.labels_dict["mm_njets"] = "Number of Jets (p_{T} > 30)"
			self.labels_dict["mm_npu"] = "NPU"
			self.labels_dict["mm_npv"] = "NPV"
			self.labels_dict["mm_phi_1"] = "Leading Muon #phi"
			self.labels_dict["mm_phi_2"] = "Trailing Muon #phi"
			self.labels_dict["mm_phi_ll"] = "#phi^{ll}"
			self.labels_dict["mm_phi_llmet"] = "#phi^{ll,MEt}"
			self.labels_dict["mm_phi_sv"] = "SVfit #phi(#tau#tau)"
			self.labels_dict["mm_pt_1"] = "Leading Muon p_{T} / GeV"
			self.labels_dict["mm_pt_2"] = "Trailing Muon p_{T} / GeV"
			self.labels_dict["mm_pt_ll"] = "p_{T}^{ll} / GeV"
			self.labels_dict["mm_pt_llmet"] = "p_{T}^{ll,MEt}"
			self.labels_dict["mm_pt_sv"] = "SVfit p_{T}(#tau#tau) / GeV"
			self.labels_dict["mm_pt_tt"] = "p_{T}(#tau#tau) / GeV"
			self.labels_dict["mm_puweight"] = "PU Weight"
			self.labels_dict["mm_rho"] = "rho"
			self.labels_dict["mm_svfitMass"] = "SVfit Mass m_{#tau#tau} / GeV"
			self.labels_dict["mm_trigweight_1"] = "Leading Muon Trigger Weight"
			self.labels_dict["mm_trigweight_2"] = "Trailing Muon Trigger Weight"
			self.labels_dict["mm_metProjectionPar"] = "#nu_{#parallel} / GeV"
			self.labels_dict["mm_metProjectionPerp"] = "#nu_{#perp}  / GeV"
			self.labels_dict["mm_metProjectionPhi"] = "#nu_{#phi}"
			self.labels_dict["ee_eta_1"] = "Electron #eta"
			self.labels_dict["ee_eta_2"] = "Muon #eta"
			self.labels_dict["ee_eta_ll"] = "#eta^{ll}"
			self.labels_dict["ee_eta_llmet"] = "#eta^{ll,MEt}"
			self.labels_dict["ee_eta_sv"] = "SVfit #eta(#tau#tau)"
			self.labels_dict["ee_inclusive"] = "Inclusive"
			self.labels_dict["ee_iso_1"] = "Electron Isolation"
			self.labels_dict["ee_iso_2"] = "Muon Isolation"
			self.labels_dict["ee_jdeta"] = "#Delta#eta_{jj}"
			self.labels_dict["ee_jeta_1"] = "Leading Jet #eta"
			self.labels_dict["ee_jeta_2"] = "Trailing Jet #eta"
			self.labels_dict["ee_jphi_1"] = "Leading Jet #phi"
			self.labels_dict["ee_jphi_2"] = "Trailing Jet #phi"
			self.labels_dict["ee_jpt_1"] = "Leading Jet p_{T} / GeV"
			self.labels_dict["ee_jpt_2"] = "Trailing Jet p_{T} / GeV"
			self.labels_dict["ee_m_1"] = "Electron Mass / GeV"
			self.labels_dict["ee_m_2"] = "Muon Mass / GeV"
			self.labels_dict["ee_m_ll"] = "Visible Mass m_{ll} / GeV"
			self.labels_dict["ee_m_llmet"] = "m_{ll,MEt} / GeV"
			self.labels_dict["ee_m_sv"] = "SVfit Mass m_{#tau#tau} / GeV"
			self.labels_dict["ee_met"] = "PFlow E^{miss}_{T}"
			self.labels_dict["ee_metcov00"] = "Cov_{0,0}(E^{miss}_{T})"
			self.labels_dict["ee_metcov01"] = "Cov_{0,1}(E^{miss}_{T})"
			self.labels_dict["ee_metcov10"] = "Cov_{1,0}(E^{miss}_{T})"
			self.labels_dict["ee_metcov11"] = "Cov_{1,1}(E^{miss}_{T})"
			self.labels_dict["ee_metphi"] = "PFlow E^{miss}_{T} #phi"
			self.labels_dict["ee_mjj"] = "Di-jet Mass m_{jj} / GeV"
			self.labels_dict["ee_mt_1"] = "Transverse Mass m_{T} (e, E^{miss}_{T}) / GeV"
			self.labels_dict["ee_mt_lep1met"] = "Transverse Mass m_{T} (e, E^{miss}_{T}) / GeV"
			self.labels_dict["ee_mt_ll"] = "m_{T}^{ll} / GeV"
			self.labels_dict["ee_mt_llmet"] = "m_{T}^{ll,MEt} / GeV"
			self.labels_dict["ee_mvacov00"] = "Cov_{0,0}(MVA E^{miss}_{T})"
			self.labels_dict["ee_mvacov01"] = "Cov_{0,1}(MVA E^{miss}_{T})"
			self.labels_dict["ee_mvacov10"] = "Cov_{1,0}(MVA E^{miss}_{T})"
			self.labels_dict["ee_mvacov11"] = "Cov_{1,1}(MVA E^{miss}_{T})"
			self.labels_dict["ee_mvamet"] = "MVA E^{miss}_{T} / GeV"
			self.labels_dict["ee_mvametcov00"] = "Cov_{0,0}(MVA E^{miss}_{T})"
			self.labels_dict["ee_mvametcov01"] = "Cov_{0,1}(MVA E^{miss}_{T})"
			self.labels_dict["ee_mvametcov10"] = "Cov_{1,0}(MVA E^{miss}_{T})"
			self.labels_dict["ee_mvametcov11"] = "Cov_{1,1}(MVA E^{miss}_{T})"
			self.labels_dict["ee_mvametphi"] = "#phi(MVA E^{miss}_{T})"
			self.labels_dict["ee_m_vis"] = "Visible Mass m^{vis}_{#tau#tau} / GeV"
			self.labels_dict["ee_nJets30"] = "Number of Jets (p_{T} > 30)"
			self.labels_dict["ee_njets"] = "Number of Jets (p_{T} > 30)"
			self.labels_dict["ee_npu"] = "NPU"
			self.labels_dict["ee_npv"] = "NPV"
			self.labels_dict["ee_phi_1"] = "Electron #phi"
			self.labels_dict["ee_phi_2"] = "Muon #phi"
			self.labels_dict["ee_phi_ll"] = "#phi^{ll}"
			self.labels_dict["ee_phi_llmet"] = "#phi^{ll,MEt}"
			self.labels_dict["ee_phi_sv"] = "SVfit #phi(#tau#tau)"
			self.labels_dict["ee_pt_1"] = "Electron p_{T} / GeV"
			self.labels_dict["ee_pt_2"] = "Muon p_{T} / GeV"
			self.labels_dict["ee_pt_ll"] = "p_{T}^{ll} / GeV"
			self.labels_dict["ee_pt_llmet"] = "p_{T}^{ll,MEt}"
			self.labels_dict["ee_pt_sv"] = "SVfit p_{T}(#tau#tau) / GeV"
			self.labels_dict["ee_pt_tt"] = "p_{T}(#tau#tau) / GeV"
			self.labels_dict["ee_puweight"] = "PU Weight"
			self.labels_dict["ee_rho"] = "rho"
			self.labels_dict["ee_svfitMass"] = "SVfit Mass m_{#tau#tau} / GeV"
			self.labels_dict["ee_trigweight_1"] = "Electron Trigger Weight"
			self.labels_dict["ee_trigweight_2"] = "Muon Trigger Weight"
			self.labels_dict["ee_metProjectionPar"] = "#nu_{#parallel} / GeV"
			self.labels_dict["ee_metProjectionPerp"] = "#nu_{#perp}  / GeV"
			self.labels_dict["ee_metProjectionPhi"] = "#nu_{#phi}"
		else:
			# put labels for MPL plots here
			pass
		
		self.labels_dict["data_obs"] = self.labels_dict["data"]
		self.labels_dict["zl"] = self.labels_dict["zll"]
		self.labels_dict["zj"] = self.labels_dict["zll"]
		self.labels_dict["ttj"] = self.labels_dict["tt"]
		self.labels_dict["ttbar"] = self.labels_dict["tt"]
		self.labels_dict["wjets"]  = self.labels_dict["wj"]
		self.labels_dict["dibosons"]  = self.labels_dict["vv"]
		self.labels_dict["ewk"] = self.labels_dict["vv"]
		self.labels_dict["fakes"] = self.labels_dict["qcd"]
		self.labels_dict["qcdwj"] = self.labels_dict["qcd"]
		self.labels_dict["totalsig"] = self.labels_dict["htt"]
		
		for higgs_mass in xrange(90, 161, 5):
			self.labels_dict["htt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["htt"].replace("H", "H({mass:d})".format(mass=higgs_mass))
			self.labels_dict["ggh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["ggh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
			self.labels_dict["qqh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["qqh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
			self.labels_dict["vh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["vh"].replace("H", "H({mass:d})".format(mass=higgs_mass))

