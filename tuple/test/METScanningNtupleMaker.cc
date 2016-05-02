#include "MetScanning/tuple/test/METScanningNtupleMaker.h"
#include <iostream>

METScanningNtupleMaker::METScanningNtupleMaker(const edm::ParameterSet& iConfig) {


  //the input tags
  CaloMET_token = consumes<reco::CaloMETCollection>(iConfig.getParameter<edm::InputTag>("caloMET"));
  PFCaloMET_token = consumes<reco::PFMETCollection>(iConfig.getParameter<edm::InputTag>("pfCaloMET"));
  PFClusterMET_token = consumes<reco::PFClusterMETCollection>(iConfig.getParameter<edm::InputTag>("pfClusterMET"));
  PFMET_token          = consumes<reco::PFMETCollection>(iConfig.getParameter<edm::InputTag>("pfMET"                  ));
  EcalPFClusters_token = consumes<reco::PFClusterCollection>(iConfig.getParameter<edm::InputTag>("EcalPFClusterCollection"));
  HcalPFClusters_token = consumes<reco::PFClusterCollection>(iConfig.getParameter<edm::InputTag>("HcalPFClusterCollection"));
  HBHEPFClusters_token = consumes<reco::PFClusterCollection>(iConfig.getParameter<edm::InputTag>("HBHEPFClusterCollection"));
  HOPFClusters_token = consumes<reco::PFClusterCollection>(iConfig.getParameter<edm::InputTag>("HOPFClusterCollection"));
  HFPFClusters_token = consumes<reco::PFClusterCollection>(iConfig.getParameter<edm::InputTag>("HFPFClusterCollection"));
  Tracks_token = consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("tracksCollection"));
  CSC2015_token = consumes<bool>(iConfig.getParameter<edm::InputTag>("CSC2015filter"));
  GlobalTightHalo2016_token = consumes<bool>(iConfig.getParameter<edm::InputTag>("GlobalHalofilterTight"));
  GlobalSuperTightHalo2016_token = consumes<bool>(iConfig.getParameter<edm::InputTag>("GlobalHalofilterSuperTight"));
  HcalStripHalo_token = consumes<bool>(iConfig.getParameter<edm::InputTag>("HcalStripHaloFilter"));
  HBHER1_token = consumes<bool>(iConfig.getParameter<edm::InputTag>("HBHEfilterR1"));
  HBHER2L_token = consumes<bool>(iConfig.getParameter<edm::InputTag>("HBHEfilterR2L"));
  HBHER2T_token = consumes<bool>(iConfig.getParameter<edm::InputTag>("HBHEfilterR2T"));
  ECALTP_token = consumes<bool>(iConfig.getParameter<edm::InputTag>("ECALTPfilter"));
  ECALSC_token = consumes<bool>(iConfig.getParameter<edm::InputTag>("ECALSCfilter"));
  RecHitsEB_token = consumes<EcalRecHitCollection>(iConfig.getParameter<edm::InputTag>("EBRecHits"));
  RecHitsEE_token = consumes<EcalRecHitCollection>(iConfig.getParameter<edm::InputTag>("EERecHits"));
  RecHitsES_token = consumes<EcalRecHitCollection>(iConfig.getParameter<edm::InputTag>("ESRecHits"));
  hSummary_token = consumes<HcalNoiseSummary>(iConfig.getParameter<edm::InputTag>("HcalNoise"));


  // The root tuple
  outputfile_ = iConfig.getParameter<std::string>("rootOutputFile"); 
  tf1 = new TFile(outputfile_.c_str(), "RECREATE");  
  s = new TTree("tree","tree");




  //basic informations ==========================
  s->Branch("run",&run,"run/l");  
  s->Branch("lumi",&lumiBlock,"lumi/l");  
  s->Branch("event",&event,"event/l");  
  s->Branch("time",&time,"time/l");

  s->Branch("filter_csc2015",&filtercsc2015,"filter_csc2015/O");
  s->Branch("filter_globaltighthalo2016",&filterglobaltighthalo2016,"filter_globaltighthalo2016/O");
  s->Branch("filter_globalsupertighthalo2016",&filterglobalsupertighthalo2016,"filter_globalsupertighthalo2016/O");
  s->Branch("filter_hcalstriphalo",&filterhcalstriphalo,"filter_hcalstriphalo/O");
  s->Branch("filter_hbher1",&filterhbher1,"filter_hbher1/O");
  s->Branch("filter_hbher2l",&filterhbher2l,"filter_hbher2l/O");
  s->Branch("filter_hbher2t",&filterhbher2t,"filter_hbher2t/O");
  s->Branch("filter_hbheiso",&filterhbheiso,"filter_hbheiso/O");
  s->Branch("filter_ecaltp",&filterecaltp,"filter_ecaltp/O");
  s->Branch("filter_ecalsc",&filterecalsc,"filter_ecalsc/O");

  //METs ========================================
  s->Branch("caloMETPt",&caloMETPt,"caloMETPt/F");  
  s->Branch("caloMETPhi",&caloMETPhi,"caloMETPhi/F"); 
  s->Branch("caloMETSumEt",&caloMETSumEt,"caloMETSumEt/F");  

  s->Branch("pfCaloMETPt",&pfCaloMETPt,"pfCaloMETPt/F");  
  s->Branch("pfCaloMETPhi",&pfCaloMETPhi,"pfCaloMETPhi/F"); 
  s->Branch("pfCaloMETSumEt",&pfCaloMETSumEt,"pfCaloMETSumEt/F");  

  s->Branch("pfClusterMETPt",&pfClusterMETPt,"pfClusterMETPt/F");  
  s->Branch("pfClusterMETPhi",&pfClusterMETPhi,"pfClusterMETPhi/F"); 
  s->Branch("pfClusterMETSumEt",&pfClusterMETSumEt,"pfClusterMETSumEt/F"); 

  s->Branch("pfMETPt",&pfMETPt,"pfMETPt/F");  
  s->Branch("pfMETPhi",&pfMETPhi,"pfMETPhi/F"); 
  s->Branch("pfMETSumEt",&pfMETSumEt,"pfMETSumEt/F"); 
  
  //clusters ==========================================
  s->Branch("pfClusterEcal_energy",&pfClusterEcal_energy);
  s->Branch("pfClusterEcal_time",&pfClusterEcal_time);
  s->Branch("pfClusterEcal_eta",&pfClusterEcal_eta);
  s->Branch("pfClusterEcal_phi",&pfClusterEcal_phi);
  s->Branch("pfClusterEcal_status13",&pfClusterEcal_status13);
  s->Branch("pfClusterEcal_status14",&pfClusterEcal_status14);

  s->Branch("pfClusterHcal_energy",&pfClusterHcal_energy);
  s->Branch("pfClusterHcal_time",&pfClusterHcal_time);
  s->Branch("pfClusterHcal_eta",&pfClusterHcal_eta);
  s->Branch("pfClusterHcal_phi",&pfClusterHcal_phi);

  s->Branch("pfClusterHBHE_energy",&pfClusterHBHE_energy);
  s->Branch("pfClusterHBHE_time",&pfClusterHBHE_time);
  s->Branch("pfClusterHBHE_eta",&pfClusterHBHE_eta);
  s->Branch("pfClusterHBHE_phi",&pfClusterHBHE_phi);

  s->Branch("pfClusterHO_energy",&pfClusterHO_energy);
  s->Branch("pfClusterHO_time",&pfClusterHO_time);
  s->Branch("pfClusterHO_eta",&pfClusterHO_eta);
  s->Branch("pfClusterHO_phi",&pfClusterHO_phi);

  s->Branch("pfClusterHF_energy",&pfClusterHF_energy);
  s->Branch("pfClusterHF_time",&pfClusterHF_time);
  s->Branch("pfClusterHF_eta",&pfClusterHF_eta);
  s->Branch("pfClusterHF_phi",&pfClusterHF_phi);
  
  //tracks ============================================
  s->Branch("track_pt",&track_pt);
  s->Branch("track_eta",&track_eta);
  s->Branch("track_phi",&track_phi);
  

}



METScanningNtupleMaker::~METScanningNtupleMaker() { 
  
  tf1->cd();
  s->Write();
  tf1->Write();
  tf1->Close();  
}



void 
METScanningNtupleMaker::beginRun(const edm::Run& run, 
				  const edm::EventSetup & es) { }


void 
METScanningNtupleMaker::analyze(const Event& iEvent, 
				 const EventSetup& iSetup) {
  

  edm::ESHandle<EcalSeverityLevelAlgo> sevlv;
  iSetup.get<EcalSeverityLevelAlgoRcd>().get(sevlv);

  irun  = iEvent.id().run();
  ievent  = iEvent.id().event();
  ilumiBlock = iEvent.id().luminosityBlock();
  itime = iEvent.time();

  run = (size_t)irun;
  event = (size_t)ievent;
  lumiBlock = (size_t)ilumiBlock;
  time = (size_t)((iEvent.time().value())>>32);

  
  //get filters
  Handle<bool> ifiltercsc2015;
  iEvent.getByToken(CSC2015_token, ifiltercsc2015);
  filtercsc2015 = *ifiltercsc2015;

  Handle<bool> ifilterglobaltighthalo2016;
  iEvent.getByToken(GlobalTightHalo2016_token, ifilterglobaltighthalo2016);
  filterglobaltighthalo2016 = *ifilterglobaltighthalo2016;

  Handle<bool> ifilterglobalsupertighthalo2016;
  iEvent.getByToken(GlobalSuperTightHalo2016_token, ifilterglobalsupertighthalo2016);
  filterglobalsupertighthalo2016 = *ifilterglobalsupertighthalo2016;

  Handle<bool> ifilterhcalstriphalo;
  iEvent.getByToken(HcalStripHalo_token, ifilterhcalstriphalo);
  filterhcalstriphalo = *ifilterhcalstriphalo;

  Handle<bool> ifilterhbher1;
  iEvent.getByToken(HBHER1_token, ifilterhbher1);
  filterhbher1 = *ifilterhbher1;

  Handle<bool> ifilterhbher2l;
  iEvent.getByToken(HBHER2L_token, ifilterhbher2l);
  filterhbher2l = *ifilterhbher2l;

  Handle<bool> ifilterhbher2t;
  iEvent.getByToken(HBHER2T_token, ifilterhbher2t);
  filterhbher2t = *ifilterhbher2t;

  //Handle<bool> ifilterhbheiso;
  //iEvent.getByToken(HBHEISO_token, ifilterhbheiso);
  //filterhbheiso = *ifilterhbheiso;

  Handle<bool> ifilterecaltp;
  iEvent.getByToken(ECALTP_token, ifilterecaltp);
  filterecaltp = *ifilterecaltp;

  Handle<bool> ifilterecalsc;
  iEvent.getByToken(ECALSC_token, ifilterecalsc);
  filterecalsc = *ifilterecalsc;

  edm::Handle<HcalNoiseSummary> hSummary;
  iEvent.getByToken(hSummary_token, hSummary);

  filterhbheiso = true;
  if( hSummary->numIsolatedNoiseChannels() >= 10 ) filterhbheiso = false;
  if( hSummary->isolatedNoiseSumE()        >= 50 ) filterhbheiso = false;
  if( hSummary->isolatedNoiseSumEt()       >= 25 ) filterhbheiso = false;



  // get METs
  Handle<reco::CaloMETCollection> caloMET;
  iEvent.getByToken(CaloMET_token, caloMET);

  Handle<reco::PFMETCollection> pfCaloMET;
  iEvent.getByToken(PFCaloMET_token, pfCaloMET);

  Handle<reco::PFClusterMETCollection> pfClusterMET;
  iEvent.getByToken(PFClusterMET_token, pfClusterMET);

  Handle<reco::PFMETCollection> pfMET;
  iEvent.getByToken(PFMET_token, pfMET);
  
  //get PFClusters
  Handle<reco::PFClusterCollection> pfClustersEcal;
  iEvent.getByToken(EcalPFClusters_token,pfClustersEcal);

  Handle<reco::PFClusterCollection> pfClustersHcal;
  iEvent.getByToken(HcalPFClusters_token,pfClustersHcal);

  Handle<reco::PFClusterCollection> pfClustersHBHE;
  iEvent.getByToken(HBHEPFClusters_token,pfClustersHBHE);

  Handle<reco::PFClusterCollection> pfClustersHO;
  iEvent.getByToken(HOPFClusters_token,pfClustersHO);

  Handle<reco::PFClusterCollection> pfClustersHF;
  iEvent.getByToken(HFPFClusters_token,pfClustersHF);

  //get tracks
  Handle<reco::TrackCollection> tracks;
  iEvent.getByToken(Tracks_token,tracks);

  //get Ecal RecHits
  //not super sure it is useful, keep commeted for now
  //edm::ESHandle<EcalChannelStatus> chStatus_;
  //iSetup.get<EcalChannelStatusRcd>().get(chStatus_);

  // Barrel
  edm::Handle< EcalRecHitCollection > ebRecHits_h_;
  iEvent.getByToken( RecHitsEB_token, ebRecHits_h_ );

  // Endcaps
  edm::Handle< EcalRecHitCollection > eeRecHits_h_;
  iEvent.getByToken( RecHitsEE_token, eeRecHits_h_ );

  // Preshower
  edm::Handle< EcalRecHitCollection > esRecHits_h_;
  iEvent.getByToken( RecHitsES_token, esRecHits_h_ );

  pfClusterEcal_energy.clear();
  pfClusterEcal_eta.clear();
  pfClusterEcal_phi.clear();
  pfClusterEcal_time.clear();
  pfClusterEcal_status13.clear();
  pfClusterEcal_status14.clear();

  pfClusterHcal_energy.clear();
  pfClusterHcal_eta.clear();
  pfClusterHcal_phi.clear();
  pfClusterHcal_time.clear();

  pfClusterHBHE_energy.clear();
  pfClusterHBHE_eta.clear();
  pfClusterHBHE_phi.clear();
  pfClusterHBHE_time.clear();

  pfClusterHO_energy.clear();
  pfClusterHO_eta.clear();
  pfClusterHO_phi.clear();
  pfClusterHO_time.clear();

  pfClusterHF_energy.clear();
  pfClusterHF_eta.clear();
  pfClusterHF_phi.clear();
  pfClusterHF_time.clear();

  track_pt.clear();
  track_eta.clear();
  track_phi.clear();

  


  //================================================================

  //METs =======================
  caloMETPt = caloMET->begin()->pt();
  caloMETPhi = caloMET->begin()->phi();
  caloMETSumEt = caloMET->begin()->sumEt();

  pfCaloMETPt = pfCaloMET->begin()->pt();
  pfCaloMETPhi = pfCaloMET->begin()->phi();
  pfCaloMETSumEt = pfCaloMET->begin()->sumEt();

  pfClusterMETPt = pfClusterMET->begin()->pt();
  pfClusterMETPhi = pfClusterMET->begin()->phi();
  pfClusterMETSumEt = pfClusterMET->begin()->sumEt();

  //ECAL clusters
  for( size_t ibc=0; ibc<pfClustersEcal->size(); ++ibc ) {
    reco::PFClusterRef bcRef( pfClustersEcal, ibc );
    pfClusterEcal_energy.push_back( bcRef->energy() );
    pfClusterEcal_time.push_back( bcRef->time() );
    pfClusterEcal_eta.push_back( bcRef->eta() );
    pfClusterEcal_phi.push_back( bcRef->phi() );

    // retrieve the id in the list of rechits and get the severity level
    bool status13 = false;
    bool status14 = false;
    vector<std::pair<DetId, float> > detId_v = bcRef->hitsAndFractions();
    unsigned nhits = detId_v.size();
    for ( size_t ihit=0; ihit<nhits; ihit++ ) {
      int sev = 0;
      if( (detId_v[ihit].first).subdetId() == EcalBarrel) {
        EBDetId id( (detId_v[ihit].first).rawId() ); 
        sev =  (Int_t) sevlv->severityLevel( id, *ebRecHits_h_);
        //sev =  (Int_t) sevlv->severityLevel( id, *(ebRecHits_h_.product()) );
      }
      else if( (detId_v[ihit].first).subdetId() == EcalEndcap) {
        EEDetId id( (detId_v[ihit].first).rawId() );
        sev =  (Int_t) sevlv->severityLevel( id, *eeRecHits_h_ );
        //sev =  (Int_t) sevlv->severityLevel( id, *(eeRecHits_h_.product()) );
      }
      else if( (detId_v[ihit].first).subdetId() == EcalPreshower) {
        ESDetId id( (detId_v[ihit].first).rawId() );
        sev =  (Int_t) sevlv->severityLevel( id, *esRecHits_h_ );
        //sev =  (Int_t) sevlv->severityLevel( id, *(esRecHits_h_.product()) );
      }
      if     (sev == 13) status13 = true;
      else if(sev == 14) status14 = true;
    }

    pfClusterEcal_status13.push_back( status13 );
    pfClusterEcal_status14.push_back( status14 );
  }

  //HCAL clusters
  for( size_t ibc=0; ibc<pfClustersHcal->size(); ++ibc ) {
    reco::PFClusterRef bcRef( pfClustersHcal, ibc );
    pfClusterHcal_energy.push_back( bcRef->energy() );
    pfClusterHcal_time.push_back( bcRef->time() );
    pfClusterHcal_eta.push_back( bcRef->eta() );
    pfClusterHcal_phi.push_back( bcRef->phi() );
  }

  //HBHE clusters
  for( size_t ibc=0; ibc<pfClustersHBHE->size(); ++ibc ) {
    reco::PFClusterRef bcRef( pfClustersHBHE, ibc );
    pfClusterHBHE_energy.push_back( bcRef->energy() );
    pfClusterHBHE_time.push_back( bcRef->time() );
    pfClusterHBHE_eta.push_back( bcRef->eta() );
    pfClusterHBHE_phi.push_back( bcRef->phi() );
  }

  //HO clusters
  for( size_t ibc=0; ibc<pfClustersHO->size(); ++ibc ) {
    reco::PFClusterRef bcRef( pfClustersHO, ibc );
    pfClusterHO_energy.push_back( bcRef->energy() );
    pfClusterHO_time.push_back( bcRef->time() );
    pfClusterHO_eta.push_back( bcRef->eta() );
    pfClusterHO_phi.push_back( bcRef->phi() );
  }

  //HF clusters
  for( size_t ibc=0; ibc<pfClustersHF->size(); ++ibc ) {
    reco::PFClusterRef bcRef( pfClustersHF, ibc );
    pfClusterHF_energy.push_back( bcRef->energy() );
    pfClusterHF_time.push_back( bcRef->time() );
    pfClusterHF_eta.push_back( bcRef->eta() );
    pfClusterHF_phi.push_back( bcRef->phi() );
  }


  //tracks
  for( size_t ibc=0; ibc<tracks->size(); ++ibc ) {
    reco::TrackRef trkRef( tracks, ibc );
    track_pt.push_back( trkRef->pt() );
    track_eta.push_back( trkRef->eta() );
    track_phi.push_back( trkRef->phi() );
  }


  //tree filling ===========================
  s->Fill();

}


DEFINE_FWK_MODULE(METScanningNtupleMaker);
