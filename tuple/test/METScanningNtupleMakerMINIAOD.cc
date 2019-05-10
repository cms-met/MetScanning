// Original Author:  Laurent Thomas
//         Created:  Fri, 26 Apr 2019 12:51:46 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "TH1F.h"
#include "TH2F.h"
#include "TFile.h"
#include "TDirectory.h"
#include "TTree.h"
#include "TString.h"
#include "TMath.h"
#include "TLorentzVector.h"

const int  N_METFilters=16;
enum METFilterIndex{
  idx_Flag_goodVertices,
  idx_Flag_globalTightHalo2016Filter,
  idx_Flag_globalSuperTightHalo2016Filter,
  idx_Flag_HBHENoiseFilter,
  idx_Flag_HBHENoiseIsoFilter,
  idx_Flag_EcalDeadCellTriggerPrimitiveFilter,
  idx_Flag_BadPFMuonFilter,
  idx_Flag_BadChargedCandidateFilter,
  idx_Flag_eeBadScFilter,
  idx_Flag_ecalBadCalibFilter,
  idx_Flag_ecalLaserCorrFilter,
  idx_Flag_EcalDeadCellBoundaryEnergyFilter,
  idx_PassecalBadCalibFilter_Update,
  idx_PassecalLaserCorrFilter_Update,
  idx_PassEcalDeadCellBoundaryEnergyFilter_Update,
  idx_PassBadChargedCandidateFilter_Update
};


//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<>
// This will improve performance in multithreaded jobs.
using namespace edm;
using namespace std;
using namespace reco;



class METScanningNtupleMakerMINIAOD : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit METScanningNtupleMakerMINIAOD(const edm::ParameterSet&);
      ~METScanningNtupleMakerMINIAOD();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;
  virtual bool GetMETFilterDecision(const edm::Event& iEvent, edm::Handle<TriggerResults> METFilterResults, TString studiedfilter);
  virtual bool GetIdxFilterDecision(int it);
  virtual TString GetIdxFilterName(int it);
  virtual void InitandClearStuff();
  
 
  // ----------member data ---------------------------
  edm::EDGetTokenT<TriggerResults> metfilterspatToken_; 
  edm::EDGetTokenT<TriggerResults> metfiltersrecoToken_; 
  edm::EDGetTokenT<bool> ecalBadCalibFilterUpdateToken_;
  edm::EDGetTokenT<bool> ecalLaserCorrFilterUpdateToken_;  
  edm::EDGetTokenT<bool> ecalDeadCellBoundaryEnergyFilterUpdateToken_;
  edm::EDGetTokenT<bool> badChargedCandidateFilterUpdateToken_;
  edm::EDGetTokenT<std::vector<Vertex> > verticesToken_; 

  edm::EDGetTokenT<std::vector< pat::Jet> > jetToken_;
  edm::EDGetTokenT<pat::PackedCandidateCollection> pfcandsToken_;
  
  edm::EDGetTokenT<std::vector< pat::MET> > metToken_;
  edm::EDGetTokenT<std::vector< pat::MET> > puppimetToken_;


  //  edm::Service<TFileService> fs;


  //Some histos to be saved for simple checks 
  TH1F *h_PFMet, *h_PuppiMet, *h_nvtx, *h_leadjetpt;
  TH1F *h_PFMet_num[N_METFilters], *h_PuppiMet_num[N_METFilters], *h_nvtx_num[N_METFilters], *h_leadjetpt_num[N_METFilters];
  TH2F *h_jet200etavsphi_fail[N_METFilters];
  //The output TTree
  TTree* outputTree;

  //Variables associated to leaves of the TTree

  unsigned long _eventNb;
  unsigned long _runNb;
  unsigned long _lumiBlock;
  unsigned long _bx;

  //Nb of primary vertices
  int _n_PV;

  //MINIAOD original MET filters decisions
  bool Flag_goodVertices;
  bool Flag_globalTightHalo2016Filter;
  bool Flag_globalSuperTightHalo2016Filter;
  bool Flag_HBHENoiseFilter;
  bool Flag_HBHENoiseIsoFilter;
  bool Flag_EcalDeadCellTriggerPrimitiveFilter;
  bool Flag_BadPFMuonFilter;
  bool Flag_BadChargedCandidateFilter;
  bool Flag_eeBadScFilter;
  bool Flag_ecalBadCalibFilter;
  bool Flag_ecalLaserCorrFilter; 
  bool Flag_EcalDeadCellBoundaryEnergyFilter;

  //Decision obtained rerunning the filters on top of MINIAOD
  bool PassecalBadCalibFilter_Update;
  bool PassecalLaserCorrFilter_Update;  
  bool PassEcalDeadCellBoundaryEnergyFilter_Update;
  bool PassBadChargedCandidateFilter_Update;
  //Jets 
  vector<double> _jetEta;
  vector<double>  _jetPhi;
  vector<double>  _jetPt;
  vector<double>  _jetRawPt;
  vector<double>  _jet_CHEF;
  vector<double>  _jet_NHEF;
  vector<double>  _jet_NEEF;
  vector<double>  _jet_CEEF;
  vector<double>  _jet_MUEF;
  vector <int>  _jet_CHM;
  vector <int>  _jet_NHM;
  vector <int>  _jet_PHM;
  vector <int>  _jet_NM;

  //PF candidates
  vector <double> _PFcand_pt;
  vector <double> _PFcand_eta;
  vector <double> _PFcand_phi;
  vector <int> _PFcand_pdgId;
  vector <int> _PFcand_fromPV;

  //MET
  double _met;
  double _met_phi;
  double _puppimet;
  double _puppimet_phi;



};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
METScanningNtupleMakerMINIAOD::METScanningNtupleMakerMINIAOD(const edm::ParameterSet& iConfig)
 :
  metfilterspatToken_(consumes<TriggerResults>(iConfig.getParameter<edm::InputTag>("METFiltersPAT"))),
  metfiltersrecoToken_(consumes<TriggerResults>(iConfig.getParameter<edm::InputTag>("METFiltersRECO"))),
  ecalBadCalibFilterUpdateToken_(consumes<bool>(iConfig.getParameter<edm::InputTag>("ECALBadCalibFilterUpdate"))),
  ecalLaserCorrFilterUpdateToken_(consumes<bool>(iConfig.getParameter<edm::InputTag>("ECALLaserCorrFilterUpdate"))),
  ecalDeadCellBoundaryEnergyFilterUpdateToken_(consumes<bool>(iConfig.getParameter<edm::InputTag>("ECALDeadCellBoundaryEnergyFilterUpdate"))),
  badChargedCandidateFilterUpdateToken_(consumes<bool>(iConfig.getParameter<edm::InputTag>("BadChargedCandidateFilterUpdate"))),
  verticesToken_(consumes<std::vector<Vertex> > (iConfig.getParameter<edm::InputTag>("Vertices"))),
  jetToken_(consumes< std::vector< pat::Jet> >(iConfig.getParameter<edm::InputTag>("Jets"))),
  pfcandsToken_(consumes<pat::PackedCandidateCollection>(iConfig.getParameter<edm::InputTag>("PFCandCollection"))),
  metToken_(consumes<std::vector<pat::MET> > (iConfig.getParameter<edm::InputTag>("PFMet"))),
  puppimetToken_(consumes<std::vector<pat::MET> > (iConfig.getParameter<edm::InputTag>("PuppiMet")))
{
   //now do what ever initialization is needed
  edm::Service<TFileService> fs; 
  h_nvtx  = fs->make<TH1F>("h_nvtx" , "Number of reco vertices (MET>200);N_{vtx};Events"  ,    100, 0., 100.);
  h_PFMet  = fs->make<TH1F>("h_PFMet" , "Type 1 PFMET (GeV);Type 1 PFMET (GeV);Events"  ,    1000, 0., 5000.);
  h_PuppiMet  = fs->make<TH1F>("h_PuppiMet" , "PUPPI MET (GeV);PUPPI MET (GeV);Events"  ,    1000, 0., 5000.);
  h_leadjetpt  = fs->make<TH1F>("h_leadjetpt" , "Leading jet p_T (GeV);p_{T} (leading jet) (GeV) (MET<100);Events"  ,    1000, 0., 5000.);
  
  for(int i =0; i< N_METFilters;i++){
    TString filtername = GetIdxFilterName(i);
    h_nvtx_num[i]  = fs->make<TH1F>("h_nvtx_" +filtername , "Number of reco vertices, events passing "+filtername+";N_{vtx};Events", 100, 0., 100.);
    h_PFMet_num[i]  = fs->make<TH1F>("h_PFMet_" +filtername , "Type 1 PFMET (GeV), events passing "+filtername+";Type 1 PFMET (GeV);Events"  ,    1000, 0., 5000.);
    h_PuppiMet_num[i]  = fs->make<TH1F>("h_PuppiMet_" +filtername , "PUPPI MET (GeV), events passing "+filtername+";PUPPI MET (GeV);Events"  ,    1000, 0., 5000.);
    h_leadjetpt_num[i]  = fs->make<TH1F>("h_leadjetpt_" +filtername , "Leading jet p_T (GeV), events passing "+filtername+";p_{T} (leading jet) (GeV) (MET<100);Events"  ,    1000, 0., 5000.);
    h_jet200etavsphi_fail[i] = fs->make<TH2F>("h_jet200etavsphi_fail_" +filtername , "Jet (pt>200) occupancy map, events failing "+filtername+";#eta(jet);#phi(jet);Events"  ,    200, -5,5,200,-3.1416,3.1416);
  }
  outputTree = fs->make<TTree>("tree","tree");

}


METScanningNtupleMakerMINIAOD::~METScanningNtupleMakerMINIAOD()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
METScanningNtupleMakerMINIAOD::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  
  InitandClearStuff();
  
  
  _runNb = iEvent.id().run();
  _eventNb = iEvent.id().event();
  _lumiBlock = iEvent.luminosityBlock();
  _bx=iEvent.bunchCrossing();
  
  //Vertices
  edm::Handle<std::vector<Vertex> > theVertices;
  iEvent.getByToken(verticesToken_,theVertices) ;
  _n_PV = theVertices->size();

  
  //MET filters are stored in TriggerResults::RECO or TriggerResults::PAT . Should take the latter if it exists
  edm::Handle<TriggerResults> METFilterResults;
  iEvent.getByToken(metfilterspatToken_, METFilterResults);
  if(!(METFilterResults.isValid())) iEvent.getByToken(metfiltersrecoToken_, METFilterResults);
  
  Flag_goodVertices= GetMETFilterDecision(iEvent,METFilterResults,"Flag_goodVertices");
  Flag_globalTightHalo2016Filter= GetMETFilterDecision(iEvent,METFilterResults,"Flag_globalTightHalo2016Filter");
  Flag_globalSuperTightHalo2016Filter= GetMETFilterDecision(iEvent,METFilterResults,"Flag_globalSuperTightHalo2016Filter");
  Flag_HBHENoiseFilter= GetMETFilterDecision(iEvent,METFilterResults,"Flag_HBHENoiseFilter");
  Flag_HBHENoiseIsoFilter= GetMETFilterDecision(iEvent,METFilterResults,"Flag_HBHENoiseIsoFilter");
  Flag_EcalDeadCellTriggerPrimitiveFilter= GetMETFilterDecision(iEvent,METFilterResults,"Flag_EcalDeadCellTriggerPrimitiveFilter");
  Flag_BadPFMuonFilter= GetMETFilterDecision(iEvent,METFilterResults,"Flag_BadPFMuonFilter");
  Flag_BadChargedCandidateFilter= GetMETFilterDecision(iEvent,METFilterResults,"Flag_BadChargedCandidateFilter");
  Flag_eeBadScFilter= GetMETFilterDecision(iEvent,METFilterResults,"Flag_eeBadScFilter");
  Flag_ecalBadCalibFilter= GetMETFilterDecision(iEvent,METFilterResults,"Flag_ecalBadCalibFilter");
  Flag_EcalDeadCellBoundaryEnergyFilter= GetMETFilterDecision(iEvent,METFilterResults,"Flag_EcalDeadCellBoundaryEnergyFilter");
  Flag_ecalLaserCorrFilter= GetMETFilterDecision(iEvent,METFilterResults,"Flag_ecalLaserCorrFilter");
  

  //Now accessing the decisions of some filters that we reran on top of MINIAOD
  edm::Handle<bool> handle_PassecalBadCalibFilter_Update ;
  iEvent.getByToken(ecalBadCalibFilterUpdateToken_,handle_PassecalBadCalibFilter_Update);
  if(handle_PassecalBadCalibFilter_Update.isValid()) PassecalBadCalibFilter_Update =  (*handle_PassecalBadCalibFilter_Update );
  else PassecalBadCalibFilter_Update = true;
  
  edm::Handle<bool> handle_PassecalLaserCorrFilter_Update ;
  iEvent.getByToken(ecalLaserCorrFilterUpdateToken_,handle_PassecalLaserCorrFilter_Update);
  if(handle_PassecalLaserCorrFilter_Update.isValid())PassecalLaserCorrFilter_Update =  (*handle_PassecalLaserCorrFilter_Update );
  else PassecalLaserCorrFilter_Update = true;
  
  edm::Handle<bool> handle_PassEcalDeadCellBoundaryEnergyFilter_Update;
  iEvent.getByToken(ecalDeadCellBoundaryEnergyFilterUpdateToken_,handle_PassEcalDeadCellBoundaryEnergyFilter_Update);
  if(handle_PassEcalDeadCellBoundaryEnergyFilter_Update.isValid())PassEcalDeadCellBoundaryEnergyFilter_Update =  (*handle_PassEcalDeadCellBoundaryEnergyFilter_Update );
  else{  std::cout <<"handle_PassEcalDeadCellBoundaryEnergyFilter_Update.isValid =false" <<endl; PassEcalDeadCellBoundaryEnergyFilter_Update = true;}

  edm::Handle<bool> handle_PassBadChargedCandidateFilter_Update;
  iEvent.getByToken(badChargedCandidateFilterUpdateToken_,handle_PassBadChargedCandidateFilter_Update);
  if(handle_PassBadChargedCandidateFilter_Update.isValid())PassBadChargedCandidateFilter_Update =  (*handle_PassBadChargedCandidateFilter_Update );
  else{  std::cout <<"handle_PassBadChargedCandidateFilter_Update.isValid =false" <<endl; PassBadChargedCandidateFilter_Update = true;}

    
  //Jets
  edm::Handle< std::vector< pat::Jet> > theJets;
  iEvent.getByToken(jetToken_,theJets );

  double leadjetpt (0.);
  for( std::vector<pat::Jet>::const_iterator jet = (*theJets).begin(); jet != (*theJets).end(); jet++ ) {
    if((&*jet)->pt() >leadjetpt) leadjetpt = (&*jet)->pt();
    if((&*jet)->pt()<200) continue;
    _jetEta.push_back((&*jet)->eta());
    _jetPhi.push_back((&*jet)->phi());
    _jetPt.push_back((&*jet)->pt());
    _jetRawPt.push_back( (&*jet)->correctedP4("Uncorrected").Pt() );
    _jet_CHEF.push_back((&*jet)->chargedHadronEnergyFraction());
    _jet_NHEF.push_back((&*jet)->neutralHadronEnergyFraction() );
    _jet_NEEF.push_back((&*jet)->neutralEmEnergyFraction() );
    _jet_CEEF.push_back((&*jet)->chargedEmEnergyFraction() );
    _jet_MUEF.push_back((&*jet)->muonEnergyFraction() );
    _jet_CHM.push_back((&*jet)->chargedMultiplicity());
    _jet_NHM.push_back((&*jet)->neutralHadronMultiplicity());
    _jet_PHM.push_back((&*jet)->photonMultiplicity());
    _jet_NM.push_back((&*jet)->neutralMultiplicity());

     for(int i = 0; i< N_METFilters ;i++){
       if(!GetIdxFilterDecision(i) ){
	 h_jet200etavsphi_fail[i]->Fill((&*jet)->eta(),(&*jet)->phi());
       }
     }
  }
  
  
  
  //Type 1 PFMET
  edm::Handle< vector<pat::MET> > ThePFMET;
  iEvent.getByToken(metToken_, ThePFMET);
  const vector<pat::MET> *pfmetcol = ThePFMET.product();
  const pat::MET *pfmet;
  pfmet = &(pfmetcol->front());
  _met = pfmet->pt();
  _met_phi = pfmet->phi();
  
  //PUPPI MET
  edm::Handle< vector<pat::MET> > ThePUPPIMET;
  iEvent.getByToken(puppimetToken_, ThePUPPIMET);
  const vector<pat::MET> *puppimetcol = ThePUPPIMET.product();
  const pat::MET *puppimet;
  puppimet = &(puppimetcol->front());
  _puppimet = puppimet->pt();
  _puppimet_phi = puppimet->phi();
  
  //PF candidates
  edm::Handle<pat::PackedCandidateCollection> pfcands;
  iEvent.getByToken(pfcandsToken_ ,pfcands);
  for(pat::PackedCandidateCollection::const_reverse_iterator p = pfcands->rbegin() ; p != pfcands->rend() ; p++ ) {
    if(p->pt()<200)continue;
    _PFcand_pt.push_back(p->pt());
    _PFcand_eta.push_back(p->eta());
    _PFcand_phi.push_back(p->phi());
    _PFcand_pdgId.push_back(p->pdgId());
    _PFcand_fromPV.push_back(p->fromPV(0));//See https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2017#Packed_ParticleFlow_Candidates
  }
  
  
  
  //Filling trees and histos   
  outputTree->Fill();
  //For effcy vs MET: 
  h_PFMet->Fill(_met);
  h_PuppiMet->Fill(_puppimet);
  for(int i = 0; i< N_METFilters ;i++){
    if( GetIdxFilterDecision(i) ){
      h_PFMet_num[i]->Fill(_met);
      h_PuppiMet_num[i]->Fill(_puppimet);
    }
  }
  //For accept rate vs leading jet (events with low MET)
  //This is to measure the mistag rate
  if(_met<100) {
    h_leadjetpt->Fill(leadjetpt);
    for(int i = 0; i< N_METFilters ;i++){
    if( GetIdxFilterDecision(i) )    h_leadjetpt_num[i]->Fill(leadjetpt);
    }
  }
  //For accept rate vs Nvtx 
  //This is to measure the efficiency 
  if(_met>200){
    h_nvtx->Fill(_n_PV);
    for(int i = 0; i< N_METFilters ;i++){
      if( GetIdxFilterDecision(i) ) h_nvtx_num[i]->Fill(_n_PV);
    }
  }
  
   
}


// ------------ method called once each job just before starting event loop  ------------
void
METScanningNtupleMakerMINIAOD::beginJob()
{

  outputTree->Branch("_eventNb",   &_eventNb,   "_eventNb/l");
  outputTree->Branch("_runNb",     &_runNb,     "_runNb/l");
  outputTree->Branch("_lumiBlock", &_lumiBlock, "_lumiBlock/l");
  outputTree->Branch("_bx", &_bx, "_bx/l");
  outputTree->Branch("_n_PV", &_n_PV, "_n_PV/I");

  outputTree->Branch("Flag_goodVertices",&Flag_goodVertices,"Flag_goodVertices/O");
  outputTree->Branch("Flag_globalTightHalo2016Filter",&Flag_globalTightHalo2016Filter,"Flag_globalTightHalo2016Filter/O");
  outputTree->Branch("Flag_globalSuperTightHalo2016Filter",&Flag_globalSuperTightHalo2016Filter,"Flag_globalSuperTightHalo2016Filter/O");
  outputTree->Branch("Flag_HBHENoiseFilter",&Flag_HBHENoiseFilter,"Flag_HBHENoiseFilter/O");
  outputTree->Branch("Flag_HBHENoiseIsoFilter",&Flag_HBHENoiseIsoFilter,"Flag_HBHENoiseIsoFilter/O");
  outputTree->Branch("Flag_EcalDeadCellTriggerPrimitiveFilter",&Flag_EcalDeadCellTriggerPrimitiveFilter,"Flag_EcalDeadCellTriggerPrimitiveFilter/O");
  outputTree->Branch("Flag_BadPFMuonFilter",&Flag_BadPFMuonFilter,"Flag_BadPFMuonFilter/O");
  outputTree->Branch("Flag_BadChargedCandidateFilter",&Flag_BadChargedCandidateFilter,"Flag_BadChargedCandidateFilter/O");
  outputTree->Branch("Flag_eeBadScFilter",&Flag_eeBadScFilter,"Flag_eeBadScFilter/O");
  outputTree->Branch("Flag_ecalBadCalibFilter",&Flag_ecalBadCalibFilter,"Flag_ecalBadCalibFilter/O");
  outputTree->Branch("Flag_ecalLaserCorrFilter",&Flag_ecalLaserCorrFilter,"Flag_ecalLaserCorrFilter/O");
  outputTree->Branch("Flag_EcalDeadCellBoundaryEnergyFilter",&Flag_EcalDeadCellBoundaryEnergyFilter,"Flag_EcalDeadCellBoundaryEnergyFilter/O");

  outputTree->Branch("PassecalBadCalibFilter_Update",&PassecalBadCalibFilter_Update,"PassecalBadCalibFilter_Update/O");
  outputTree->Branch("PassecalLaserCorrFilter_Update",&PassecalLaserCorrFilter_Update,"PassecalLaserCorrFilter_Update/O");
  outputTree->Branch("PassEcalDeadCellBoundaryEnergyFilter_Update",&PassEcalDeadCellBoundaryEnergyFilter_Update,"PassEcalDeadCellBoundaryEnergyFilter_Update/O");
  outputTree->Branch("PassBadChargedCandidateFilter_Update",&PassBadChargedCandidateFilter_Update,"PassBadChargedCandidateFilter_Update/O");


  outputTree->Branch("_jetEta",&_jetEta);
  outputTree->Branch("_jetPhi",&_jetPhi);
  outputTree->Branch("_jetPt",&_jetPt);
  outputTree->Branch("_jetRawPt",&_jetRawPt);
  outputTree->Branch("_jet_CHEF",&_jet_CHEF);
  outputTree->Branch("_jet_NHEF",&_jet_NHEF);
  outputTree->Branch("_jet_NEEF",&_jet_NEEF);
  outputTree->Branch("_jet_CEEF",&_jet_CEEF);
  outputTree->Branch("_jet_MUEF",&_jet_MUEF);
  outputTree->Branch("_jet_CHM",&_jet_CHM);
  outputTree->Branch("_jet_NHM",&_jet_NHM);
  outputTree->Branch("_jet_PHM",&_jet_PHM);
  outputTree->Branch("_jet_NM",&_jet_NM);

  outputTree->Branch("_PFcand_pt",&_PFcand_pt);
  outputTree->Branch("_PFcand_eta",&_PFcand_eta);
  outputTree->Branch("_PFcand_phi",&_PFcand_phi);
  outputTree->Branch("_PFcand_pdgId",&_PFcand_pdgId);
  outputTree->Branch("_PFcand_fromPV",&_PFcand_fromPV);
   


  outputTree->Branch("_met", &_met, "_met/D");
  outputTree->Branch("_met_phi", &_met_phi, "_met_phi/D");
  outputTree->Branch("_puppimet", &_puppimet, "_puppimet/D");
  outputTree->Branch("_puppimet_phi", &_puppimet_phi, "_puppimet_phi/D");
  
}

// ------------ method called once each job just after ending the event loop  ------------
void
METScanningNtupleMakerMINIAOD::endJob()
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
METScanningNtupleMakerMINIAOD::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addDefault(desc);
}

bool METScanningNtupleMakerMINIAOD::GetMETFilterDecision(const edm::Event& iEvent,edm::Handle<TriggerResults> METFilterResults, TString studiedfilter){
  
  if( !METFilterResults.failedToGet() ) {
    int N_MetFilters = METFilterResults->size();
    const edm::TriggerNames & metfilterName = iEvent.triggerNames(*METFilterResults);
    for( int i_Metfilter = 0; i_Metfilter < N_MetFilters; ++i_Metfilter ) {
      TString MetfilterPath =metfilterName.triggerName(i_Metfilter);
      if(MetfilterPath.Index(studiedfilter) >=0)  return METFilterResults.product()->accept(i_Metfilter);
      
    }
  }
   return true; 
}


bool METScanningNtupleMakerMINIAOD::GetIdxFilterDecision(int it){
  if(it== idx_Flag_goodVertices)return  Flag_goodVertices;
  else if(it==  idx_Flag_globalTightHalo2016Filter)return   Flag_globalTightHalo2016Filter;
  else if(it==  idx_Flag_globalSuperTightHalo2016Filter)return   Flag_globalSuperTightHalo2016Filter;
  else if(it==  idx_Flag_HBHENoiseFilter)return   Flag_HBHENoiseFilter;
  else if(it==  idx_Flag_HBHENoiseIsoFilter)return   Flag_HBHENoiseIsoFilter;
  else if(it==  idx_Flag_EcalDeadCellTriggerPrimitiveFilter)return   Flag_EcalDeadCellTriggerPrimitiveFilter;
  else if(it==  idx_Flag_BadPFMuonFilter)return   Flag_BadPFMuonFilter;
  else if(it==  idx_Flag_BadChargedCandidateFilter)return   Flag_BadChargedCandidateFilter;
  else if(it==  idx_Flag_eeBadScFilter)return   Flag_eeBadScFilter;
  else if(it==  idx_Flag_ecalBadCalibFilter)return   Flag_ecalBadCalibFilter;
  else if(it==  idx_Flag_ecalLaserCorrFilter)return   Flag_ecalLaserCorrFilter;
  else if(it==  idx_Flag_EcalDeadCellBoundaryEnergyFilter)return   Flag_EcalDeadCellBoundaryEnergyFilter;
  else if(it==  idx_PassecalBadCalibFilter_Update)return   PassecalBadCalibFilter_Update;
  else if(it==  idx_PassecalLaserCorrFilter_Update)return   PassecalLaserCorrFilter_Update;
  else if(it==  idx_PassEcalDeadCellBoundaryEnergyFilter_Update)return   PassEcalDeadCellBoundaryEnergyFilter_Update;
  else if(it==  idx_PassBadChargedCandidateFilter_Update)return   PassBadChargedCandidateFilter_Update;
  else return false;
}

TString METScanningNtupleMakerMINIAOD::GetIdxFilterName(int it){
  if(it==idx_Flag_goodVertices)return "Flag_goodVertices";
  else if(it== idx_Flag_globalTightHalo2016Filter)return "Flag_globalTightHalo2016Filter";
  else if(it== idx_Flag_globalSuperTightHalo2016Filter)return "Flag_globalSuperTightHalo2016Filter";
  else if(it== idx_Flag_HBHENoiseFilter)return "Flag_HBHENoiseFilter";
  else if(it== idx_Flag_HBHENoiseIsoFilter)return "Flag_HBHENoiseIsoFilter";
  else if(it== idx_Flag_EcalDeadCellTriggerPrimitiveFilter)return "Flag_EcalDeadCellTriggerPrimitiveFilter";
  else if(it== idx_Flag_BadPFMuonFilter)return "Flag_BadPFMuonFilter";
  else if(it== idx_Flag_BadChargedCandidateFilter)return "Flag_BadChargedCandidateFilter";
  else if(it== idx_Flag_eeBadScFilter)return "Flag_eeBadScFilter";
  else if(it== idx_Flag_ecalBadCalibFilter)return "Flag_ecalBadCalibFilter";
  else if(it== idx_Flag_ecalLaserCorrFilter)return "Flag_ecalLaserCorrFilter";
  else if(it== idx_Flag_EcalDeadCellBoundaryEnergyFilter)return "Flag_EcalDeadCellBoundaryEnergyFilter";
  else if(it== idx_PassecalBadCalibFilter_Update)return "PassecalBadCalibFilter_Update";
  else if(it== idx_PassecalLaserCorrFilter_Update)return "PassecalLaserCorrFilter_Update";
  else if(it== idx_PassEcalDeadCellBoundaryEnergyFilter_Update )return "PassEcalDeadCellBoundaryEnergyFilter_Update";
  else if(it== idx_PassBadChargedCandidateFilter_Update )return "PassBadChargedCandidateFilter_Update";
  else return "";
}


void METScanningNtupleMakerMINIAOD::InitandClearStuff(){

  Flag_goodVertices=false;
  Flag_globalTightHalo2016Filter=false;
  Flag_globalSuperTightHalo2016Filter=false;
  Flag_HBHENoiseFilter=false;
  Flag_HBHENoiseIsoFilter=false;
  Flag_EcalDeadCellTriggerPrimitiveFilter=false;
  Flag_BadPFMuonFilter=false;
  Flag_BadChargedCandidateFilter=false;
  Flag_eeBadScFilter=false;
  Flag_ecalBadCalibFilter=false;
  Flag_ecalLaserCorrFilter=false;
  Flag_EcalDeadCellBoundaryEnergyFilter=false;
  PassecalBadCalibFilter_Update=false;
  PassecalLaserCorrFilter_Update=false;
  PassEcalDeadCellBoundaryEnergyFilter_Update=false;
  PassBadChargedCandidateFilter_Update=false;
  
  _jetEta.clear();
  _jetPhi.clear();
  _jetPt.clear();
  _jetRawPt.clear();
  _jet_CHEF.clear();
  _jet_NHEF.clear();
  _jet_NEEF.clear();
  _jet_CEEF.clear();
  _jet_MUEF.clear();
  _jet_CHM.clear();
  _jet_NHM.clear();
  _jet_PHM.clear();
  _jet_NM.clear();

  _PFcand_pt.clear();
  _PFcand_eta.clear();
  _PFcand_phi.clear();
  _PFcand_pdgId.clear();
  _PFcand_fromPV.clear();
  
}

//define this as a plug-in
DEFINE_FWK_MODULE(METScanningNtupleMakerMINIAOD);
