#ifndef StudyRecHitMatching_h
#define StudyRecHitMatching_h

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/Common/interface/Handle.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

//Simhit stuff
#include "SimDataFormats/TrackingHit/interface/PSimHit.h"

#include "DataFormats/SiPixelCluster/interface/SiPixelCluster.h"
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHitCollection.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "TrackingTools/PatternTools/interface/TrajTrackAssociation.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"

#include "Geometry/CommonTopologies/interface/PixelTopology.h"

//#include "Geometry/TrackerGeometryBuilder/interface/PixelGeomDetUnit.h"
//#include "Geometry/TrackerGeometryBuilder/interface/PixelGeomDetType.h"
#include "Geometry/CommonDetUnit/interface/PixelGeomDetUnit.h"
#include "Geometry/CommonDetUnit/interface/PixelGeomDetType.h"

#include "Geometry/CommonDetUnit/interface/GeomDetType.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/TrackerNumberingBuilder/interface/GeometricDet.h"

//DWM histogram services
//#include "DQMServices/Core/interface/DQMStore.h"
//#include "DQMServices/Core/interface/MonitorElement.h"

#include <string>
#include <vector>

// For ROOT
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TF1.h>
#include <TH2F.h>
#include <TH1F.h>
#include <TProfile.h>
#include <TProfile2D.h>
#include <TVector3.h>


// Hit Associator
#define PIXEL_ASSOCIATOR // use my special pixel associator

#ifdef PIXEL_ASSOCIATOR
#include "SiPixelTools/PixelHitAssociator/interface/PixelHitAssociator.h"
#else 
#include "SimTracker/TrackerHitAssociation/interface/TrackerHitAssociator.h"
//#include "SimTracker/TrackerHitAssociation/interface/TrackerHitAssociator.h"
#endif

class TrackerTopology;

class StudyRecHitMatching : public edm::one::EDAnalyzer<edm::one::SharedResources> {

   public:
	//Constructor
	StudyRecHitMatching(const edm::ParameterSet& conf);

	//Destructor
	~StudyRecHitMatching();

   protected:

	virtual void analyze(const edm::Event& e, const edm::EventSetup& c) override;
	void beginJob() override;
	void endJob() override;

   private:
	//DQMStore* dbe_;
	std::string outputFile_;
	bool verbose_;
	edm::EDGetTokenT<edmNew::DetSetVector<SiPixelRecHit>> tPixelRecHit;
        edm::EDGetTokenT<TrajTrackAssociationCollection> tTracks;
	edm::EDGetTokenT<edm::PSimHitContainer> tPixelSimHits;
    edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> trackerTopoToken_;
    edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> trackerGeomToken_;

	edm::ParameterSet conf_;


	void fillBarrel(const TrackingRecHit*,const PSimHit &, DetId, const PixelGeomDetUnit *,	
			const TrackerTopology *,double,double,double,int);
	void fillForward(const TrackingRecHit*, const PSimHit &, DetId, const PixelGeomDetUnit *,
			 const TrackerTopology *,double,double,double,int);
        float matchToRecs(const PSimHit&, SiPixelRecHitCollection::const_iterator,
			  DetId, const PixelGeomDetUnit*, const TrackerTopology *,double,double,double);
#ifdef PIXEL_ASSOCIATOR
	std::vector<PSimHit> associateHit(const std::vector<PSimHit>&,DetId);
	//PixelHitAssociator::Config trackerHitAssociatorConfig_;
        float matchToSims(const std::vector<PSimHit>&,const TrackingRecHit *,
			    DetId, const PixelGeomDetUnit*, const TrackerTopology *,double,double,double);
#else
	TrackerHitAssociator::Config trackerHitAssociatorConfig_;
        float matchToSims(const TrackerHitAssociator&, const TrackingRecHit *, 
			    DetId, const PixelGeomDetUnit*, const TrackerTopology *,double,double,double);
#endif
        int PhaseIBladeOfflineToOnline(const int&);

	TH1D *hdist1,*hdist2,*hdist3,*hdist4,*hdist5,*hdist6,*hdist7,*hdist8,*hdist9;
	TH1D *hdist10,*hdist11,*hdist12,*hdist13,*hdist14,*hdist15,*hdist16,
	  *hdist17,*hdist18,*hdist19;
	TH1D *hdist20,*hdist21,*hdist22,*hdist23,*hdist24,*hdist25,*hdist26;
	TH1D *hcount1,*hcount2,*hcount3,*hcount4,*hcount5,*hcount6,*hcount7,*hcount8,*hcount9;
	TH1D *hcount10, *hcount11, *hcount12;
	TH2F *htest1, *htest2, *htest3, *htest4, *htest5, *htest6;
	TH1D *hParticleType1,*hTrackId1,*hProcessType1,
	  *hParticleType2,*hTrackId2,*hProcessType2,
	  *hParticleType3,*hTrackId3,*hProcessType3,
	  *hParticleType4,*hTrackId4,*hProcessType4,
	  *hParticleType5,*hTrackId5,*hProcessType5;

	TH1D *hptTrack, *hphiTrack, *hetaTrack;

  	TH1D *htheta1,*hbeta1,*hphi1;
  	TH1D *htheta2,*hbeta2,*hphi2;
	TH1D *heta1, *heta2, *heta3, *heta4;
	TH1D *hz1, *hz1_1, *hz1_2, *hz1_3, *hz1_4, *hz1_5;
	TH1D *hz1_11, *hz1_12, *hz1_13,*hz1_14,*hz1_15,*hz1_16,*hz1_17;	
	TH1D *hz1_21, *hz1_22, *hz1_23,*hz1_24,*hz1_25,*hz1_26;	

	TH1D* recHitXResLayer[4];
	TH1D* recHitYResLayer[4];
	TH1D *recHitXResB1,*recHitXResB2,*recHitXResB3,*recHitXResB4,*recHitXResB5,*recHitXResB6;


	TH1D *phiPerDet1,*phiPerDet2,*phiPerDet3,*phiPerDet4 ;
	TH1D *cluXPerDet1,*cluXPerDet2,*cluXPerDet3,*cluXPerDet4;
	TH1D *cluYPerDet1,*cluYPerDet2,*cluYPerDet3,*cluYPerDet4;
	//TH1D *simsXPerDet1,*simsXPerDet2,*simsXPerDet3,*simsXPerDet4;
	//TH1D *simsYPerDet1,*simsYPerDet2,*simsYPerDet3,*simsYPerDet4;

	//RecHits FPIX
	TH1D* recHitXResAllF;
	//TH1D* recHitXResPosZF;
	//TH1D* recHitXResNegZF;
	TH1D* recHitYResAllF;
	//TH1D* recHitYResPosZF;
	//TH1D* recHitYResNegZF;

#ifdef NOT
	//Clusters BPIX
	TH1D* clustYSizeModule[8];
	//TH1D* clustXSizeLayer[4];
	TH1D* clustChargeLayer1Modules[8];
	TH1D* clustChargeLayer2Modules[8];
	TH1D* clustChargeLayer3Modules[8];
	TH1D* clustChargeLayer4Modules[8];

	//Cluster FPIX
	TH1D* clustXSizeDisk1Plaquettes[7];
	TH1D* clustXSizeDisk2Plaquettes[7];
	TH1D* clustXSizeDisk3Plaquettes[7];
	TH1D* clustYSizeDisk1Plaquettes[7];
	TH1D* clustYSizeDisk2Plaquettes[7];
	TH1D* clustYSizeDisk3Plaquettes[7];
	TH1D* clustChargeDisk1Plaquettes[7];
	TH1D* clustChargeDisk2Plaquettes[7];
	TH1D* clustChargeDisk3Plaquettes[7];

	//RecHits BPIX
	TH1D* recHitXResAllB;
	TH1D* recHitYResAllB;
	//TH1D* recHitXFullModules;
	//TH1D* recHitXHalfModules;
	TH1D* recHitYAllModules;
	TH1D* recHitXResFlippedLadderLayers[4];
	TH1D* recHitXResNonFlippedLadderLayers[4];
        TH1D *recHitXResFlippedLadderLayersSide[4][2];
        TH1D *recHitXResNonFlippedLadderLayersSide[4][2];

	TH1D *recHitL1XResSize1,*recHitL1XResSize2,*recHitL1XResSize3;   
	TH1D *recHitL2XResSize1,*recHitL2XResSize2,*recHitL2XResSize3;   
	TH1D *recHitL3XResSize1,*recHitL3XResSize2,*recHitL3XResSize3;   
	TH1D *recHitL4XResSize1,*recHitL4XResSize2,*recHitL4XResSize3;   

	TH1D* recHitYResLayer1Modules[8];
	TH1D* recHitYResLayer2Modules[8];
	TH1D* recHitYResLayer3Modules[8];
	TH1D* recHitYResLayer4Modules[8];

	TH1D* recHitXResLayersP[4];
	TH1D* recHitYResLayersP[4];
	TH1D* recHitXResLayersP1[4];
	TH1D* recHitXResLayersP2[4];
	TH1D* recHitXResLayersP3[4];
	TH1D* recHitYResLayersP1[4];
	TH1D* recHitYResLayersP2[4];
	TH1D* recHitYResLayersP3[4];
	TH1D* recHitYResLayersP4[4];

	TH1D* recHitXResVsPhiP[4];
	TH1D* recHitXResVsPhiP1[4];
	TH1D* recHitXResVsPhiP2[4];
	TH1D* recHitXResVsPhiP3[4];

	TH1D* recHitXResLayer1Eta[25];
	TH1D* recHitXResLayer2Eta[25];
	TH1D* recHitXResLayer3Eta[25];
	TH1D* recHitXResLayer4Eta[25];
	TH1D* recHitYResLayer1Eta[25];
	TH1D* recHitYResLayer2Eta[25];
	TH1D* recHitYResLayer3Eta[25];
	TH1D* recHitYResLayer4Eta[25];


	//TH1D *recHitX11, *recHitX12; // *recHitX21, *recHitX22;

	//TH1D* recHitXPlaquetteSize1;
	//TH1D* recHitXPlaquetteSize2;
	//TH1D* recHitYPlaquetteSize2;
	//TH1D* recHitYPlaquetteSize3;
	//TH1D* recHitYPlaquetteSize4;
	//TH1D* recHitYPlaquetteSize5;
	TH1D* recHitXResDisk1[7];
	TH1D* recHitYResDisk1[7];
	TH1D* recHitXResDisk2[7];
	TH1D* recHitYResDisk2[7];
	TH1D* recHitXResDisk3[7];
	TH1D* recHitYResDisk3[7];
	TH1D* recHitXResRingSidePanel[2][2][2];
	TH1D* recHitYResRingSidePanel[2][2][2];
	TH1D* recHitXResRingSide[2][2];
	TH1D* recHitYResRingPanel[2][2];

	// Pull distributions
	//RecHits BPIX
	TH1D* recHitXPullAllB;
	TH1D* recHitYPullAllB;
	TH1D *recHitXError1B,*recHitXError2B,*recHitXError3B,*recHitXError4B;
	TH1D *recHitYError1B,*recHitYError2B,*recHitYError3B,*recHitYError4B;

	TH1D* recHitXPullFlippedLadderLayers[4];
	TH1D* recHitXPullNonFlippedLadderLayers[4];
	TH1D* recHitYPullLayer1Modules[8];
	TH1D* recHitYPullLayer2Modules[8];
	TH1D* recHitYPullLayer3Modules[8];
	TH1D* recHitYPullLayer4Modules[8];

	//RecHits FPIX
	TH1D* recHitXPullAllF;
	TH1D* recHitYPullAllF;
	TH1D* recHitXErrorAllF;
	TH1D* recHitYErrorAllF;

	TH1D* recHitXPullDisk1Plaquettes[7];
	TH1D* recHitYPullDisk1Plaquettes[7];
	TH1D* recHitXPullDisk2Plaquettes[7];
	TH1D* recHitYPullDisk2Plaquettes[7];
	TH1D* recHitXPullDisk3Plaquettes[7];
	TH1D* recHitYPullDisk3Plaquettes[7];

	// Alignment errors 
	TH1D *recHitXAlignError1, *recHitXAlignError2, *recHitXAlignError3;
	TH1D *recHitXAlignError4, *recHitXAlignError5, *recHitXAlignError6, *recHitXAlignError7;
	TH1D *recHitYAlignError1, *recHitYAlignError2, *recHitYAlignError3;
	TH1D *recHitYAlignError4, *recHitYAlignError5, *recHitYAlignError6, *recHitYAlignError7;

	// cluster size vs phi
	TH1D* clusizeXVsX[4];
	TH1D* clusizeXVsPhi[4];
	TH1D* clusizeX1VsPhi[4];
	TH1D* clusizeX2VsPhi[4];
	TH1D* clusizeX3VsPhi[4];

	TH1D *cluSizeXVsPhi1; // large scale ,*clusizeX22VsPhi,*clusizeX23VsPhi,*clusizeX24VsPhi ;
	TH1D *size1_mz_f,*size1_mz_nf,*size1_pz_f,*size1_pz_nf;
	TH1D *size2_mz_f,*size2_mz_nf,*size2_pz_f,*size2_pz_nf;
	TH1D *size3_mz_f,*size3_mz_nf,*size3_pz_f,*size3_pz_nf;



#endif // NOT

        edm::InputTag src_;
        bool useTracks_;
        edm::InputTag tracks_;
        bool phase_;
	bool quick_;
	bool muOnly_;
	bool useSimHits_;
	double ptCut_;
	int count1, count2, count3, count4, count5, count6, count9;
	int count10, count11, count12;

};

#endif
