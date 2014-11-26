#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import ArtusTools.Tools.logger as logger
log = logging.getLogger(__name__)

import array
import argparse
import os

import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(True)

import HiggsAnalysis.KITHiggsToTauTau.triggerTurnOnParametrisation as triggerTurnOnParametrisation


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Store correction factors in ROOT histograms. Here: trigger efficiencies (Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL / Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL, Data2012ABCD)",
	                                 parents=[logger.loggingParser])

	parser.add_argument("-n", "--histogram-name", default="triggerEfficiency",
	                    help="Histogram name. [Default: %(default)s]")
	parser.add_argument("-o", "--output",
	                    default="$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_Mu17_Ele8_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Data2012ABCD_electronLeg.root",
	                    help="Output ROOT file. [Default: %(default)s]")

	args = parser.parse_args()
	logger.initLogger(args)
	
	args.output = os.path.expandvars(args.output)
	dirname = os.path.dirname(args.output)
	if dirname != "" and not os.path.exists(dirname):
		os.makedirs(dirname)

	root_file = ROOT.TFile(args.output, "RECREATE")
	
	# https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013#Electron_Muon_Trigger
	# https://svnweb.cern.ch/cern/wsvn/desycmshiggs/HiggsToTauTau/trunk/DesyHTauTau/HTauTauElecMuonAnalysis/bin/FillTriggerEfficiencyMap.C
	pt_bins = array.array("d", [10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 1000.0])
	eta_bins = array.array("d", [-2.3, -1.5, -0.8, 0.0, 0.8, 1.5, 2.3])
	histogram = ROOT.TH2F(args.histogram_name, args.histogram_name,
	                      len(pt_bins)-1, pt_bins, len(eta_bins)-1, eta_bins)
	
	histogram.SetBinContent(histogram.FindBin(10.0, 0.0), 0.7270)
	histogram.SetBinContent(histogram.FindBin(10.0, 0.8), 0.7380)
	histogram.SetBinContent(histogram.FindBin(10.0, 1.5), 0.6899)
	histogram.SetBinContent(histogram.FindBin(15.0, 0.0), 0.8752)
	histogram.SetBinContent(histogram.FindBin(15.0, 0.8), 0.9059)
	histogram.SetBinContent(histogram.FindBin(15.0, 1.5), 0.8635)
	histogram.SetBinContent(histogram.FindBin(20.0, 0.0), 0.9142)
	histogram.SetBinContent(histogram.FindBin(20.0, 0.8), 0.9484)
	histogram.SetBinContent(histogram.FindBin(20.0, 1.5), 0.9356)
	histogram.SetBinContent(histogram.FindBin(25.0, 0.0), 0.9368)
	histogram.SetBinContent(histogram.FindBin(25.0, 0.8), 0.9630)
	histogram.SetBinContent(histogram.FindBin(25.0, 1.5), 0.9466)
	histogram.SetBinContent(histogram.FindBin(30.0, 0.0), 0.9499)
	histogram.SetBinContent(histogram.FindBin(30.0, 0.8), 0.9642)
	histogram.SetBinContent(histogram.FindBin(30.0, 1.5), 0.9735)
	histogram.SetBinContent(histogram.FindBin(35.0, 0.0), 0.9689)
	histogram.SetBinContent(histogram.FindBin(35.0, 0.8), 0.9809)
	histogram.SetBinContent(histogram.FindBin(35.0, 1.5), 0.9802)
	
	histogram.SetBinError(histogram.FindBin(10.0, 0.0), 0.0086)
	histogram.SetBinError(histogram.FindBin(10.0, 0.8), 0.0100)
	histogram.SetBinError(histogram.FindBin(10.0, 1.5), 0.0224)
	histogram.SetBinError(histogram.FindBin(15.0, 0.0), 0.0052)
	histogram.SetBinError(histogram.FindBin(15.0, 0.8), 0.0057)
	histogram.SetBinError(histogram.FindBin(15.0, 1.5), 0.0118)
	histogram.SetBinError(histogram.FindBin(20.0, 0.0), 0.0042)
	histogram.SetBinError(histogram.FindBin(20.0, 0.8), 0.0045)
	histogram.SetBinError(histogram.FindBin(20.0, 1.5), 0.0089)
	histogram.SetBinError(histogram.FindBin(25.0, 0.0), 0.0038)
	histogram.SetBinError(histogram.FindBin(25.0, 0.8), 0.0041)
	histogram.SetBinError(histogram.FindBin(25.0, 1.5), 0.0079)
	histogram.SetBinError(histogram.FindBin(30.0, 0.0), 0.0037)
	histogram.SetBinError(histogram.FindBin(30.0, 0.8), 0.0042)
	histogram.SetBinError(histogram.FindBin(30.0, 1.5), 0.0059)
	histogram.SetBinError(histogram.FindBin(35.0, 0.0), 0.0012)
	histogram.SetBinError(histogram.FindBin(35.0, 0.8), 0.0013)
	histogram.SetBinError(histogram.FindBin(35.0, 1.5), 0.0021)
	
	# fill histograms symmetrically in eta
	for pt_bin in xrange(1, len(pt_bins)+1):
		for eta_bin in xrange(1, (len(pt_bins)/2)+2):
			histogram.SetBinContent(pt_bin, eta_bin, histogram.GetBinContent(pt_bin, len(eta_bins)-eta_bin))
			histogram.SetBinError(pt_bin, eta_bin, histogram.GetBinError(pt_bin, len(eta_bins)-eta_bin))
	
	#histogram.Write()
	root_file.Write()
	root_file.Close()
	log.info("Correction factors have been stored in histogram \"%s/%s\"." % (args.output, args.histogram_name))

