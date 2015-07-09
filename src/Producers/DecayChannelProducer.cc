
#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string/trim.hpp>

#include "Artus/Consumer/interface/LambdaNtupleConsumer.h"
#include "Artus/Utility/interface/DefaultValues.h"
#include "Artus/Utility/interface/Utility.h"

#include "HiggsAnalysis/KITHiggsToTauTau/interface/HttEnumTypes.h"
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Producers/DecayChannelProducer.h"
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Utility/Quantities.h"


void DecayChannelProducer::Init(setting_type const& settings)
{
	ProducerBase<HttTypes>::Init(settings);

	HttEnumTypes::DecayChannel decayChannel = HttEnumTypes::ToDecayChannel(boost::algorithm::to_lower_copy(boost::algorithm::trim_copy(settings.GetChannel())));
	
	// add possible quantities for the lambda ntuples consumers
	LambdaNtupleConsumer<HttTypes>::AddIntQuantity("decayChannelIndex", [](event_type const& event, product_type const& product) {
		return Utility::ToUnderlyingValue(product.m_decayChannel);
	});
	
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("leadingLepCharge", [](event_type const& event, product_type const& product)
	{
		return product.m_ptOrderedLeptons[0]->charge();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("leadingLepPt", [](event_type const& event, product_type const& product)
	{
		return product.m_ptOrderedLeptons[0]->p4.Pt();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("leadingLepEta", [](event_type const& event, product_type const& product)
	{
		return product.m_ptOrderedLeptons[0]->p4.Eta();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("leadingLepPhi", [](event_type const& event, product_type const& product)
	{
		return product.m_ptOrderedLeptons[0]->p4.Phi();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("leadingLepMass", [](event_type const& event, product_type const& product)
	{
		return product.m_ptOrderedLeptons[0]->p4.mass();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("leadingLepMt", [](event_type const& event, product_type const& product)
	{
		return product.m_ptOrderedLeptons[0]->p4.Mt();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("leadingLepIso", [](event_type const& event, product_type const& product) {
		return SafeMap::GetWithDefault(product.m_leptonIsolation, product.m_ptOrderedLeptons[0], DefaultValues::UndefinedDouble);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("leadingLepIsoOverPt", [](event_type const& event, product_type const& product) {
		return SafeMap::GetWithDefault(product.m_leptonIsolationOverPt, product.m_ptOrderedLeptons[0], DefaultValues::UndefinedDouble);
	});
	
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1Charge", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[0]->charge();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1Dz", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[0]->track.getDz(&event.m_vertexSummary->pv);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1D0", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[0]->track.getDxy(&event.m_vertexSummary->pv);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1Pt", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[0]->p4.Pt();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1Eta", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[0]->p4.Eta();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1Phi", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[0]->p4.Phi();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1Mass", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[0]->p4.mass();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1Mt", [](event_type const& event, product_type const& product)
	{
		return Quantities::CalculateMtH2Tau(product.m_flavourOrderedLeptons[0]->p4, product.m_met->p4); 
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1Iso", [](event_type const& event, product_type const& product) {
		return SafeMap::GetWithDefault(product.m_leptonIsolation, product.m_flavourOrderedLeptons[0], DefaultValues::UndefinedDouble);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1IsoOverPt", [](event_type const& event, product_type const& product) {
		return SafeMap::GetWithDefault(product.m_leptonIsolationOverPt, product.m_flavourOrderedLeptons[0], DefaultValues::UndefinedDouble);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1MetPt", [](event_type const& event, product_type const& product)
	{
		return (product.m_flavourOrderedLeptons[0]->p4 + product.m_met->p4).Pt();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1MetEta", [](event_type const& event, product_type const& product)
	{
		return (product.m_flavourOrderedLeptons[0]->p4 + product.m_met->p4).Eta();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1MetPhi", [](event_type const& event, product_type const& product)
	{
		return (product.m_flavourOrderedLeptons[0]->p4 + product.m_met->p4).Phi();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1MetMass", [](event_type const& event, product_type const& product)
	{
		return (product.m_flavourOrderedLeptons[0]->p4 + product.m_met->p4).mass();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep1MetMt", [](event_type const& event, product_type const& product)
	{
		return Quantities::CalculateMt(product.m_flavourOrderedLeptons[0]->p4, product.m_met->p4);
	});
	
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("trailingLepCharge", [](event_type const& event, product_type const& product)
	{
		return product.m_ptOrderedLeptons[1]->charge();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("trailingLepPt", [](event_type const& event, product_type const& product)
	{
		return product.m_ptOrderedLeptons[1]->p4.Pt();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("trailingLepEta", [](event_type const& event, product_type const& product)
	{
		return product.m_ptOrderedLeptons[1]->p4.Eta();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("trailingLepPhi", [](event_type const& event, product_type const& product)
	{
		return product.m_ptOrderedLeptons[1]->p4.Phi();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("trailingLepMass", [](event_type const& event, product_type const& product)
	{
		return product.m_ptOrderedLeptons[1]->p4.mass();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("trailingLepMt", [](event_type const& event, product_type const& product)
	{
		return product.m_ptOrderedLeptons[1]->p4.Mt();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("trailingLepIso", [](event_type const& event, product_type const& product) {
		return SafeMap::GetWithDefault(product.m_leptonIsolation, product.m_ptOrderedLeptons[1], DefaultValues::UndefinedDouble);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("trailingLepIsoOverPt", [](event_type const& event, product_type const& product) {
		return SafeMap::GetWithDefault(product.m_leptonIsolationOverPt, product.m_ptOrderedLeptons[1], DefaultValues::UndefinedDouble);
	});
	
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep2Charge", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[1]->charge();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep2Dz", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[1]->track.getDz(&event.m_vertexSummary->pv);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep2D0", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[1]->track.getDxy(&event.m_vertexSummary->pv);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep2Pt", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[1]->p4.Pt();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep2Eta", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[1]->p4.Eta();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep2Phi", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[1]->p4.Phi();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep2Mass", [](event_type const& event, product_type const& product)
	{
		return product.m_flavourOrderedLeptons[1]->p4.mass();
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep2Mt", [](event_type const& event, product_type const& product)
	{
		return Quantities::CalculateMtH2Tau(product.m_flavourOrderedLeptons[1]->p4, product.m_met->p4); 
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep2Iso", [](event_type const& event, product_type const& product) {
		return SafeMap::GetWithDefault(product.m_leptonIsolation, product.m_flavourOrderedLeptons[1], DefaultValues::UndefinedDouble);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep2IsoOverPt", [](event_type const& event, product_type const& product) {
		return SafeMap::GetWithDefault(product.m_leptonIsolationOverPt, product.m_flavourOrderedLeptons[1], DefaultValues::UndefinedDouble);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("lep2MetMt", [](event_type const& event, product_type const& product)
	{
		return Quantities::CalculateMt(product.m_flavourOrderedLeptons[1]->p4, product.m_met->p4);
	});

	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("byCombinedIsolationDeltaBetaCorrRaw3Hits_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("byCombinedIsolationDeltaBetaCorrRaw3Hits", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("byCombinedIsolationDeltaBetaCorrRaw3Hits_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("byCombinedIsolationDeltaBetaCorrRaw3Hits", event.m_tauMetadata) :  product.m_validTaus[0]->getDiscriminator("byCombinedIsolationDeltaBetaCorrRaw3Hits", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("trigweight_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("trigweight", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("trigweight_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("trigweight", event.m_tauMetadata) : product.m_validTaus[0]->getDiscriminator("trigweight", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstElectronLooseMVA5_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("againstElectronLooseMVA5", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstElectronLooseMVA5_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("againstElectronLooseMVA5", event.m_tauMetadata) : product.m_validTaus[0]->getDiscriminator("againstElectronLooseMVA5", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstElectronMediumMVA5_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("againstElectronMediumMVA5", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstElectronMediumMVA5_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("againstElectronMediumMVA5", event.m_tauMetadata) : product.m_validTaus[0]->getDiscriminator("againstElectronMediumMVA5", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstElectronTightMVA5_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("againstElectronTightMVA5", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstElectronTightMVA5_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("againstElectronTightMVA5", event.m_tauMetadata) :  product.m_validTaus[0]->getDiscriminator("againstElectronTightMVA5", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstElectronVLooseMVA5_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("againstElectronVLooseMVA5", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstElectronVLooseMVA5_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("againstElectronVLooseMVA5", event.m_tauMetadata) : product.m_validTaus[0]->getDiscriminator("againstElectronVLooseMVA5", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstElectronVTightMVA5_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("againstElectronVTightMVA5", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstElectronVTightMVA5_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("againstElectronVTightMVA5", event.m_tauMetadata) : product.m_validTaus[0]->getDiscriminator("againstElectronVTightMVA5", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstMuonLoose3_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("againstMuonLoose3", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstMuonLoose3_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("againstMuonLoose3", event.m_tauMetadata) :  product.m_validTaus[0]->getDiscriminator("againstMuonLoose3", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstMuonTight3_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("againstMuonTight3", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("againstMuonTight3_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("againstMuonTight3", event.m_tauMetadata) : product.m_validTaus[0]->getDiscriminator("againstMuonTight3", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("byIsolationMVA3newDMwoLTraw_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("byIsolationMVA3newDMwoLTraw", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("byIsolationMVA3newDMwoLTraw_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("byIsolationMVA3newDMwoLTraw", event.m_tauMetadata) : product.m_validTaus[0]->getDiscriminator("byIsolationMVA3newDMwoLTraw", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("byIsolationMVA3oldDMwoLTraw_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("byIsolationMVA3oldDMwoLTraw", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("byIsolationMVA3oldDMwoLTraw_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("byIsolationMVA3oldDMwoLTraw", event.m_tauMetadata) : product.m_validTaus[0]->getDiscriminator("byIsolationMVA3oldDMwoLTraw", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("byIsolationMVA3newDMwLTraw_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("byIsolationMVA3newDMwLTraw", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("byIsolationMVA3newDMwLTraw_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("byIsolationMVA3newDMwLTraw", event.m_tauMetadata) :  product.m_validTaus[0]->getDiscriminator("byIsolationMVA3newDMwLTraw", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("byIsolationMVA3oldDMwLTraw_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("byIsolationMVA3oldDMwLTraw", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("byIsolationMVA3oldDMwLTraw_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("byIsolationMVA3oldDMwLTraw", event.m_tauMetadata) : product.m_validTaus[0]->getDiscriminator("byIsolationMVA3oldDMwLTraw", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("chargedIsoPtSum_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("chargedIsoPtSum", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("chargedIsoPtSum_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("chargedIsoPtSum", event.m_tauMetadata) : product.m_validTaus[0]->getDiscriminator("chargedIsoPtSum", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("decayModeFinding_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("decayModeFinding", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("decayModeFinding_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("decayModeFinding", event.m_tauMetadata) : product.m_validTaus[0]->getDiscriminator("decayModeFinding", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("decayModeFindingNewDMs_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("decayModeFindingNewDMs", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("decayModeFindingNewDMs_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("decayModeFindingNewDMs", event.m_tauMetadata) : product.m_validTaus[0]->getDiscriminator("decayModeFindingNewDMs", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("neutralIsoPtSum_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("neutralIsoPtSum", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("neutralIsoPtSum_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("neutralIsoPtSum", event.m_tauMetadata): product.m_validTaus[0]->getDiscriminator("neutralIsoPtSum", event.m_tauMetadata);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("puCorrPtSum_1", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[0]->getDiscriminator("puCorrPtSum", event.m_tauMetadata) : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("puCorrPtSum_2", [decayChannel](event_type const& event, product_type const& product)
	{
		return (decayChannel == HttEnumTypes::DecayChannel::TT) ? product.m_validTaus[1]->getDiscriminator("puCorrPtSum", event.m_tauMetadata) : product.m_validTaus[0]->getDiscriminator("puCorrPtSum", event.m_tauMetadata);
	});
}

void DecayChannelProducer::Produce(event_type const& event, product_type& product,
	                               setting_type const& settings) const
{
	
	product.m_decayChannel = HttEnumTypes::DecayChannel::NONE;
	
	KLepton* lepton1 = 0;
	KLepton* lepton2 = 0;
	
	size_t nElectrons = product.m_validElectrons.size();
	size_t nMuons = product.m_validMuons.size();
	size_t nTaus = product.m_validTaus.size();
	
	if (nElectrons == 2)
	{
		lepton1 = product.m_validElectrons[0];
		lepton2 = product.m_validElectrons[1];
		product.m_decayChannel = HttEnumTypes::DecayChannel::EE;
	}
	else if (nElectrons == 1)
	{
		if (nMuons == 1)
		{
			lepton1 = product.m_validElectrons[0];
			lepton2 = product.m_validMuons[0];

			// require that in the EM channel at least one of the leptons has a pT > 20 GeV
			if (lepton1->p4.Pt() > 20. || lepton2->p4.Pt() > 20.) {
				product.m_decayChannel = HttEnumTypes::DecayChannel::EM;
			}
		}
		else if (nTaus >= 1)
		{
			lepton1 = product.m_validElectrons[0];
			lepton2 = product.m_validTaus[0];
			product.m_decayChannel = HttEnumTypes::DecayChannel::ET;
		}
	}
	else if (nElectrons == 0)
	{
		if (nMuons == 2)
		{
			lepton1 = product.m_validMuons[0];
			lepton2 = product.m_validMuons[1];
			product.m_decayChannel = HttEnumTypes::DecayChannel::MM;
		}
		else if (nMuons == 1 && nTaus >= 1)
		{
			lepton1 = product.m_validMuons[0];
			lepton2 = product.m_validTaus[0];
			product.m_decayChannel = HttEnumTypes::DecayChannel::MT;
		}
		else if (nTaus >= 2)
		{
			lepton1 = product.m_validTaus[0];
			lepton2 = product.m_validTaus[1];
			product.m_decayChannel = HttEnumTypes::DecayChannel::TT;
		}
	}
	
	// fill tau energy scale weights
	if (! product.m_tauEnergyScaleWeight.empty())
	{
		if ((product.m_decayChannel == HttEnumTypes::DecayChannel::ET) ||
			(product.m_decayChannel == HttEnumTypes::DecayChannel::MT) ||
			(product.m_decayChannel == HttEnumTypes::DecayChannel::TT))
		{
			product.m_weights["tauEnergyScaleWeight"] = SafeMap::Get(product.m_tauEnergyScaleWeight, static_cast<KTau*>(lepton2));
			if (product.m_decayChannel == HttEnumTypes::DecayChannel::TT)
			{
				product.m_weights["tauEnergyScaleWeight"] *= SafeMap::Get(product.m_tauEnergyScaleWeight, static_cast<KTau*>(lepton1));
			}
		}
	}

	if (product.m_decayChannel != HttEnumTypes::DecayChannel::NONE)
	{
		
		// fill leptons ordered by pt (high pt first)
		if (lepton1->p4.Pt() >= lepton2->p4.Pt())
		{
			product.m_ptOrderedLeptons.push_back(lepton1);
			product.m_ptOrderedLeptons.push_back(lepton2);
		}
		else
		{
			product.m_ptOrderedLeptons.push_back(lepton2);
			product.m_ptOrderedLeptons.push_back(lepton1);
		}
		
		// fill leptons ordered by flavour (according to channel definition)
		product.m_flavourOrderedLeptons.push_back(lepton1);
		product.m_flavourOrderedLeptons.push_back(lepton2);
		
		// fill leptons ordered by charge (positive charges first)
		if (lepton1->charge() >= lepton2->charge())
		{
			product.m_chargeOrderedLeptons.push_back(lepton1);
			product.m_chargeOrderedLeptons.push_back(lepton2);
		}
		else
		{
			product.m_chargeOrderedLeptons.push_back(lepton2);
			product.m_chargeOrderedLeptons.push_back(lepton1);
		}
	}
}

void TTHDecayChannelProducer::Produce(event_type const& event, product_type& product,
	                              setting_type const& settings) const
{
	
	product.m_decayChannel = HttEnumTypes::DecayChannel::NONE;
	
	KLepton* lepton1 = 0;
	KLepton* lepton2 = 0;
	KLepton* lepton3 = 0;
	
	size_t nElectrons = product.m_validElectrons.size();
	size_t nMuons = product.m_validMuons.size();
	size_t nTaus = product.m_validTTHTaus.size();
	
	if (nElectrons == 1)
	{
		if (nTaus == 2) {
			lepton1 = product.m_validTTHTaus[0];
			lepton2 = product.m_validTTHTaus[1];
			lepton3 = product.m_validElectrons[0];
			product.m_decayChannel = HttEnumTypes::DecayChannel::TTH_TTE;
		}
	}
	else if (nMuons == 1)
	{
		if (nTaus == 2) {
			lepton1 = product.m_validTTHTaus[0];
			lepton2 = product.m_validTTHTaus[1];
			lepton3 = product.m_validMuons[0];
			product.m_decayChannel = HttEnumTypes::DecayChannel::TTH_TTM;
		}
	}
	
	// fill tau energy scale weights
	if (! product.m_tauEnergyScaleWeight.empty())
	{
		if ((product.m_decayChannel == HttEnumTypes::DecayChannel::TTH_TTE) ||
		    (product.m_decayChannel == HttEnumTypes::DecayChannel::TTH_TTM))
		{
			product.m_weights["tauEnergyScaleWeight"] = SafeMap::Get(product.m_tauEnergyScaleWeight, static_cast<KTau*>(lepton1));
			product.m_weights["tauEnergyScaleWeight"] *= SafeMap::Get(product.m_tauEnergyScaleWeight, static_cast<KTau*>(lepton2));
		}
	}

	if (product.m_decayChannel != HttEnumTypes::DecayChannel::NONE)
	{
		// fill leptons ordered by pt (high pt first)
		product.m_ptOrderedLeptons.push_back(lepton1);
		product.m_ptOrderedLeptons.push_back(lepton2);
		product.m_ptOrderedLeptons.push_back(lepton3);
		
		std::sort(product.m_ptOrderedLeptons.begin(), product.m_ptOrderedLeptons.end(),
	          [](KLepton const* lepton1, KLepton const* lepton2) -> bool
	          { return lepton1->p4.Pt() > lepton2->p4.Pt(); });


		// fill leptons ordered by flavour (according to channel definition)
		product.m_flavourOrderedLeptons.push_back(lepton1);
		product.m_flavourOrderedLeptons.push_back(lepton2);
		product.m_flavourOrderedLeptons.push_back(lepton3);


		// fill leptons ordered by charge (positive charges first)
		product.m_chargeOrderedLeptons.push_back(lepton1);
		product.m_chargeOrderedLeptons.push_back(lepton2);
		product.m_chargeOrderedLeptons.push_back(lepton3);
		
		std::sort(product.m_chargeOrderedLeptons.begin(), product.m_chargeOrderedLeptons.end(),
	          [](KLepton const* lepton1, KLepton const* lepton2) -> bool
	          { return lepton1->charge() > lepton2->charge(); });
	}
}


void Run2DecayChannelProducer::Produce(event_type const& event, product_type& product,
	                              setting_type const& settings) const
{
	product.m_decayChannel = HttEnumTypes::DecayChannel::NONE;
	
	KLepton* lepton1 = 0;
	KLepton* lepton2 = 0;

	//size_t nElectrons = product.m_validElectrons.size();
	size_t nMuons = product.m_validMuons.size();
	size_t nTaus = product.m_validTaus.size();

	// TT channel
	if (HttEnumTypes::ToDecayChannel(boost::algorithm::to_lower_copy(boost::algorithm::trim_copy(settings.GetChannel()))) ==
	    HttEnumTypes::DecayChannel::TT)
	{
		KTau* tau1 = 0;
		KTau* tau2 = 0;

		if (nTaus < 2)
			return;
		else if (nTaus == 2)
		{
			// sort the pair (first tau is the most isolated)
			const std::string idString = "byCombinedIsolationDeltaBetaCorrRaw3Hits";
			auto compareTaus = [&] (KTau* tau1, KTau* tau2) 
				{ return (tau1->getDiscriminator(idString, event.m_tauMetadata) < tau2->getDiscriminator(idString, event.m_tauMetadata)); };
			std::sort(product.m_validTaus.begin(), product.m_validTaus.end(), compareTaus);
		
			product.m_decayChannel = HttEnumTypes::DecayChannel::TT;
			tau1 = product.m_validTaus[0];
			tau2 = product.m_validTaus[1];
		
			// require the pair to pass a separation requirement
			if (ROOT::Math::VectorUtil::DeltaR(tau1->p4, tau2->p4) < 0.5)
				product.m_decayChannel = HttEnumTypes::DecayChannel::NONE;
		}
		else
		{
			std::vector<std::pair<KTau*, KTau*>> allDiTauPairs;
			std::vector<std::pair<KTau*, KTau*>> osDiTauPairs;
			// Produce di-tau pairs
			for(size_t i = 0; i < nTaus - 1; ++i)
			{
				for(size_t j = i+1; j < nTaus; ++j)
				{
					// require the pair to pass a separation requirement
					if (ROOT::Math::VectorUtil::DeltaR(product.m_validTaus[i]->p4, product.m_validTaus[j]->p4) < 0.5)
						continue;

					std::pair<KTau*, KTau*> diTauPair = std::make_pair(product.m_validTaus[i], product.m_validTaus[j]);
					allDiTauPairs.push_back(diTauPair);
					if(diTauPair.first->charge() == - diTauPair.second->charge())
						osDiTauPairs.push_back(diTauPair);
				}
			}

			if (allDiTauPairs.size() == 0)
				return;

			product.m_decayChannel = HttEnumTypes::DecayChannel::TT;
			auto diTauPairs = osDiTauPairs.size() > 0 ? osDiTauPairs : allDiTauPairs;
			const std::string idString = "byCombinedIsolationDeltaBetaCorrRaw3Hits";
			auto compareDiTauPairs = [&] (std::pair<KTau*, KTau*> pair1, std::pair<KTau*, KTau*> pair2) 
				{ return (std::max(pair1.first->getDiscriminator(idString, event.m_tauMetadata), pair1.second->getDiscriminator(idString, event.m_tauMetadata)) < std::max(pair2.first->getDiscriminator(idString, event.m_tauMetadata), pair2.second->getDiscriminator(idString, event.m_tauMetadata))); };
			std::sort(diTauPairs.begin(), diTauPairs.end(), compareDiTauPairs);
		
			tau1 = diTauPairs[0].first;
			tau2 = diTauPairs[0].second;

			product.m_validTaus.clear();
			product.m_validTaus.push_back(tau1);
			product.m_validTaus.push_back(tau2);
		}

		lepton1 = tau1;
		lepton2 = tau2;
	}

	// ET channel
	else if (HttEnumTypes::ToDecayChannel(boost::algorithm::to_lower_copy(boost::algorithm::trim_copy(settings.GetChannel()))) ==
	         HttEnumTypes::DecayChannel::ET)
	{
		product.m_decayChannel = HttEnumTypes::DecayChannel::NONE;
	}

	// MT channel
	else if (HttEnumTypes::ToDecayChannel(boost::algorithm::to_lower_copy(boost::algorithm::trim_copy(settings.GetChannel()))) ==
	         HttEnumTypes::DecayChannel::MT)
	{
		KMuon* muon = 0;
		KTau* tau = 0;
		
		if (nMuons == 1 && nTaus == 1)
		{
			product.m_decayChannel = HttEnumTypes::DecayChannel::MT;
			muon = product.m_validMuons[0];
			tau = product.m_validTaus[0];

			// require the pair to pass a separation requirement
			if (ROOT::Math::VectorUtil::DeltaR(muon->p4, tau->p4) < 0.5)
				product.m_decayChannel = HttEnumTypes::DecayChannel::NONE;
		}
		else
		{
			std::vector<std::pair<KMuon*, KTau*>> allMuonTauPairs;
			std::vector<std::pair<KMuon*, KTau*>> osMuonTauPairs;
			// Produce muon-tau pairs
			for(size_t i = 0; i < nMuons; i++)
			{
				for(size_t j = 0; j < nTaus; j++)
				{
					// require the pair to pass a separation requirement
					if (ROOT::Math::VectorUtil::DeltaR(product.m_validMuons[i]->p4, product.m_validTaus[j]->p4) < 0.5)
						continue;

					std::pair<KMuon*, KTau*> muonTauPair = std::make_pair(product.m_validMuons[i], product.m_validTaus[j]);
					allMuonTauPairs.push_back(muonTauPair);
					if(muonTauPair.first->charge() == - muonTauPair.second->charge())
						osMuonTauPairs.push_back(muonTauPair);
				}
			}
	
			if (allMuonTauPairs.size() == 0)
				return;

			product.m_decayChannel = HttEnumTypes::DecayChannel::MT;
			auto muonTauPairs = osMuonTauPairs.size() > 0 ? osMuonTauPairs : allMuonTauPairs;
			const std::string idString = "byCombinedIsolationDeltaBetaCorrRaw3Hits";
			auto compareMuonTauPairs = [&] (std::pair<KMuon*, KTau*> pair1, std::pair<KMuon*, KTau*> pair2) 
				{ return (std::max(float(pair1.first->pfIso()), pair1.second->getDiscriminator(idString, event.m_tauMetadata)) < std::max(float(pair2.first->pfIso()), pair2.second->getDiscriminator(idString, event.m_tauMetadata))); };
			std::sort(muonTauPairs.begin(), muonTauPairs.end(), compareMuonTauPairs);
		
			muon = muonTauPairs[0].first;
			tau = muonTauPairs[0].second;

			product.m_validMuons.clear();
			product.m_validTaus.clear();
			product.m_validMuons.push_back(muon);
			product.m_validTaus.push_back(tau);
		}

		lepton1 = muon;
		lepton2 = tau;	
	}

	else
	{
		LOG(FATAL) << "Run2DecayChannelProducer: The given channel (" << settings.GetChannel() << ") is not included in the producer";
	}


	// fill the lepton vectors
	if (product.m_decayChannel != HttEnumTypes::DecayChannel::NONE)
	{
		// fill leptons ordered by pt (high pt first)
		if (lepton1->p4.Pt() >= lepton2->p4.Pt())
		{
			product.m_ptOrderedLeptons.push_back(lepton1);
			product.m_ptOrderedLeptons.push_back(lepton2);
		}
		else
		{
			product.m_ptOrderedLeptons.push_back(lepton2);
			product.m_ptOrderedLeptons.push_back(lepton1);
		}
	
		// fill leptons ordered by flavour (according to channel definition)
		product.m_flavourOrderedLeptons.push_back(lepton1);
		product.m_flavourOrderedLeptons.push_back(lepton2);
	
		// fill leptons ordered by charge (positive charges first)
		if (lepton1->charge() >= lepton2->charge())
		{
			product.m_chargeOrderedLeptons.push_back(lepton1);
			product.m_chargeOrderedLeptons.push_back(lepton2);
		}
		else
		{
			product.m_chargeOrderedLeptons.push_back(lepton2);
			product.m_chargeOrderedLeptons.push_back(lepton1);
		}
	}
}
