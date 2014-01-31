
#pragma once

#include "Artus/Core/interface/Cpp11Support.h"
#include "Artus/Provider/interface/RootEventProvider.h"

#include "HttTypes.h"

/*
 * Will load the corresponding ntuple from a root file
 * The memory locations are passed to ROOT one time, in the
 * WireEvent() method call.
 */

class HttEventProvider: public RootEventProvider<HttTypes::event_type> {
public:
	HttEventProvider(stringvector const & fileNames) :
			RootEventProvider<HttTypes::event_type>(fileNames,
			// hardcode the root treename already here
					"ec") {

		WireEvent();
	}

private:
	void WireEvent() {
		// set up the ROOT pointers to our local memory regions
		m_rootChain->SetBranchAddress("theSim", &m_event.m_floatTheSim);
		m_rootChain->SetBranchAddress("pSim", &m_event.m_floatPSim);
		m_rootChain->SetBranchAddress("ptSim", &m_event.m_floatPtSim);
		m_rootChain->SetBranchAddress("pzSim", &m_event.m_floatPzSim);
	}
};
