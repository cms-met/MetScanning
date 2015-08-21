import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
process = cms.Process("SKIM")

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
#process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")


##___________________________Global_Tag_______________________________________||
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
#process.GlobalTag.globaltag = 'GR_P_V56::All'
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = '74X_dataRun2_Prompt_v0'



##___________________________Input_Files______________________________________||
process.source = cms.Source(
    "PoolSource",
    #fileNames = cms.untracked.vstring("root://eoscms.cern.ch//store/express/Run2015B/ExpressPhysics/FEVT/Express-v1/000/250/985/00000/04380D9C-0F24-E511-9772-02163E0127EF.root")
    #fileNames = cms.untracked.vstring("root://eoscms.cern.ch//store/express/Run2015B/ExpressPhysics/FEVT/Express-v1/000/250/985/00000/8CB978A3-1024-E511-A2E5-02163E011BC8.root")
    #fileNames = cms.untracked.vstring("root://eoscms.cern.ch//store/express/Run2015B/ExpressPhysics/FEVT/Express-v1/000/250/987/00000/D4337B5F-1224-E511-9969-02163E011BB6.root")
    #fileNames = cms.untracked.vstring("root://eoscms.cern.ch//store/express/Run2015B/ExpressPhysics/FEVT/Express-v1/000/250/985/00000/04380D9C-0F24-E511-9772-02163E0127EF.root")

    # Begona's events
    #fileNames = cms.untracked.vstring("file:EvDisplaysPromptRecoEle.root", "file:EvDisplaysPromptRecoMu.root")
    #fileNames = cms.untracked.vstring("file:SingleElectron.root")
    #fileNames = cms.untracked.vstring("file:SingleMuon.root")

    # Giulia's talk
    #fileNames = cms.untracked.vstring(
    #  "file:private/pickevents_1.root",
    #  "file:private/pickevents_2.root",
    #  "file:private/pickevents_3.root"
    #)

    ## ExpressPhysics 4T 25ns
    fileNames = cms.untracked.vstring(
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/7A8F5522-C347-E511-A2F8-02163E014652.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/4C71411E-C347-E511-848B-02163E01354F.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/90CB99A3-C447-E511-BC2B-02163E0137EF.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/0CEFD0A4-C447-E511-ABF0-02163E0133EC.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/22CE3E48-C847-E511-8BF6-02163E016C4C.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/1AE46E23-C847-E511-81CB-02163E012A4C.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/5647846E-C847-E511-806A-02163E014549.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/E0CB6C1A-C647-E511-A5F5-02163E014103.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/862554B2-C947-E511-980B-02163E014103.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/AE593BC9-C947-E511-8949-02163E0133FE.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/16CC9222-C647-E511-8135-02163E0143DD.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/EE667CAD-CA47-E511-ABB8-02163E012AB5.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/98B6B30C-C747-E511-8FC7-02163E014222.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/3C29EFC0-CA47-E511-8EBE-02163E01354F.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/BC615EBC-CA47-E511-835C-02163E014348.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/7A2B1B20-C847-E511-BE37-02163E01202A.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/46B954BC-CA47-E511-A57B-02163E014348.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/C8DB54B5-CD47-E511-AD96-02163E014222.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/B6FBDAB7-CD47-E511-B681-02163E014376.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/5AC12C1D-C647-E511-BBCF-02163E01475A.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/76CB5B58-CC47-E511-8394-02163E014652.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/3607EA55-CC47-E511-A855-02163E014488.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/26E895BC-CA47-E511-B633-02163E01385E.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/481590B6-CD47-E511-BC0C-02163E014488.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/AC4554DF-CE47-E511-8D6F-02163E014466.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/C67F0EB4-CD47-E511-8817-02163E0143DD.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/5C0D19FC-CF47-E511-9A69-02163E014376.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/7A442DE2-D047-E511-9B26-02163E014466.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/2C7530F6-D147-E511-AFF4-02163E012AAF.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/16FA7D5D-CC47-E511-A27A-02163E01549A.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/A8DBD7E2-CE47-E511-9D4B-02163E011CBD.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/D8427AFD-CF47-E511-8737-02163E014652.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/0495D5E5-D147-E511-B20D-02163E01374D.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/56D2E878-D347-E511-9736-02163E012AAF.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/82AB35F9-CE47-E511-9C8C-02163E01559C.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/EED79768-D347-E511-B854-02163E011851.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/4E34D767-D347-E511-AC1E-02163E0133C6.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/B49A0AC1-D447-E511-BCAD-02163E014222.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/165C8DFF-D147-E511-9A00-02163E015529.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/7C105004-D247-E511-9398-02163E01549A.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/58344BFC-CF47-E511-ACED-02163E014488.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/98C8C2D3-D447-E511-9A0F-02163E014434.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/441DF867-D347-E511-AB00-02163E0133C6.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/A20E077D-D347-E511-9149-02163E012A4C.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/32F0E8F3-D147-E511-BA0A-02163E0143DD.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/CAEA07F7-D147-E511-82D6-02163E014752.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/F22F0F89-D547-E511-A7AE-02163E0134D1.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/EC33FA17-D647-E511-BE63-02163E011CBD.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/DAF2D016-D647-E511-BC8D-02163E0145A2.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/B6B2EF15-D647-E511-83E7-02163E014243.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/DE42A5F7-D147-E511-B301-02163E0137EF.root",
    "root://eoscms.cern.ch//store/express/Run2015C/ExpressPhysics/FEVT/Express-v1/000/254/790/00000/E22F8518-D647-E511-ADC3-02163E012AAF.root"
    )    


    )


##___________________________EDM_Output_File__________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('skim.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'keep *'
#        'keep *_pfClusterMet_*_*', 'keep *_CSCTightHaloFilter_*_*', 'keep *_HBHENoiseFilterResultProducer_*_*'
        )
    )


##____________________________________________________________________________||
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 50
process.maxEvents = cms.untracked.PSet()#input = cms.untracked.int32(10))


##___________________________CSC_Halo_Filter__________________________________||
process.load('RecoMET.METFilters.CSCTightHaloFilter_cfi')
process.CSCTightHaloFilter.taggingMode = cms.bool(False)


##___________________________HCAL_Noise_Filter________________________________||
process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
process.HBHENoiseFilterResultProducer.minZeros = cms.int32(99999)
process.HBHENoiseFilterResultProducer.defaultDecision = cms.string("HBHENoiseFilterResultRun2Tight")
process.HBHENoiseFilterResultProducer.IgnoreTS4TS5ifJetInLowBVRegion = cms.bool(False)
process.ApplyBaselineHBHENoiseFilter = cms.EDFilter('BooleanFlagFilter',
    inputLabel = cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResult'),
    reverseDecision = cms.bool(False)
)
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')


##___________________________PFClusterMet_____________________________________||
process.load('RecoMET.METProducers.PFClusterMET_cfi')
process.pfClusterRefsForJetsHCAL = cms.EDProducer("PFClusterRefCandidateProducer",
  src          = cms.InputTag('particleFlowClusterHCAL'),
  particleType = cms.string('pi+')
)
process.pfClusterRefsForJetsECAL = cms.EDProducer("PFClusterRefCandidateProducer",
  src          = cms.InputTag('particleFlowClusterECAL'),
  particleType = cms.string('pi+')
)
process.pfClusterRefsForJetsHF = cms.EDProducer("PFClusterRefCandidateProducer",
  src          = cms.InputTag('particleFlowClusterHF'),
  particleType = cms.string('pi+')
)
process.pfClusterRefsForJetsHO = cms.EDProducer("PFClusterRefCandidateProducer",
  src          = cms.InputTag('particleFlowClusterHO'),
  particleType = cms.string('pi+')
)
process.pfClusterRefsForJets = cms.EDProducer("PFClusterRefCandidateMerger",
  src = cms.VInputTag("pfClusterRefsForJetsHCAL", "pfClusterRefsForJetsECAL", "pfClusterRefsForJetsHF", "pfClusterRefsForJetsHO")
)
process.pfClusterMetSequence = cms.Sequence(
 process.particleFlowRecHitECAL*
 process.particleFlowRecHitHBHE*
 process.particleFlowRecHitHF*
 process.particleFlowRecHitHO*
 process.particleFlowClusterECALUncorrected*
 process.particleFlowClusterECAL*
 process.particleFlowClusterHBHE*
 process.particleFlowClusterHCAL*
 process.particleFlowClusterHF*
 process.particleFlowClusterHO*
 process.pfClusterRefsForJetsHCAL*
 process.pfClusterRefsForJetsECAL*
 process.pfClusterRefsForJetsHF*
 process.pfClusterRefsForJetsHO*
 process.pfClusterRefsForJets*
#   process.ak4PFClusterJets
 process.pfClusterMet
)


##___________________________PFCaloMet_____________________________________||
process.hltParticleFlowBlock = cms.EDProducer("PFBlockProducer",
  debug = cms.untracked.bool(False),
  verbose = cms.untracked.bool(False),
  elementImporters = cms.VPSet(
      cms.PSet(
          source = cms.InputTag("particleFlowClusterECAL"),
          #source = cms.InputTag("particleFlowClusterECALUncorrected"), #we use uncorrected
          importerName = cms.string('GenericClusterImporter')
      ),
      cms.PSet(
          source = cms.InputTag("particleFlowClusterHCAL"),
          importerName = cms.string('GenericClusterImporter')
      ),
      cms.PSet(
          source = cms.InputTag("particleFlowClusterHO"),
          importerName = cms.string('GenericClusterImporter')
      ),
      cms.PSet(
          source = cms.InputTag("particleFlowClusterHF"),
          importerName = cms.string('GenericClusterImporter')
      )
  ),
  linkDefinitions = cms.VPSet(
      cms.PSet(
          linkType = cms.string('ECAL:HCAL'),
          useKDTree = cms.bool(False),
          #linkerName = cms.string('ECALAndHCALLinker')
          linkerName = cms.string('ECALAndHCALCaloJetLinker') #new ECal and HCal Linker for PFCaloJets
      ),
      cms.PSet(
          linkType = cms.string('HCAL:HO'),
          useKDTree = cms.bool(False),
          linkerName = cms.string('HCALAndHOLinker')
      ),
      cms.PSet(
          linkType = cms.string('HFEM:HFHAD'),
          useKDTree = cms.bool(False),
          linkerName = cms.string('HFEMAndHFHADLinker')
      ),
      cms.PSet(
          linkType = cms.string('ECAL:ECAL'),
          useKDTree = cms.bool(False),
          linkerName = cms.string('ECALAndECALLinker')
      )
   )
)
from RecoParticleFlow.PFProducer.particleFlow_cfi import particleFlowTmp
process.hltParticleFlow = particleFlowTmp.clone(
    GedPhotonValueMap = cms.InputTag(""),
    useEGammaFilters = cms.bool(False),
    useEGammaElectrons = cms.bool(False), 
    useEGammaSupercluster = cms.bool(False),
    rejectTracks_Step45 = cms.bool(False),
    usePFNuclearInteractions = cms.bool(False),  
    blocks = cms.InputTag("hltParticleFlowBlock"), 
    egammaElectrons = cms.InputTag(""),
    useVerticesForNeutral = cms.bool(False),
    PFEGammaCandidates = cms.InputTag(""),
    useProtectionsForJetMET = cms.bool(False),
    usePFConversions = cms.bool(False),
    rejectTracks_Bad = cms.bool(False),
    muons = cms.InputTag(""),
    postMuonCleaning = cms.bool(False),
    usePFSCEleCalib = cms.bool(False)
    )
process.load("RecoMET.METProducers.PFMET_cfi")
process.pfCaloMet = process.pfMet.clone(
  src = cms.InputTag("hltParticleFlow"),
  alias = cms.string('pfCaloMet')
)
process.pfCaloMetSequence = cms.Sequence(
   process.hltParticleFlowBlock *
   process.hltParticleFlow *
   process.pfCaloMet
)

##__________________________Tracking_POG_Filters___________________________||
process.load('RecoMET.METFilters.trackingPOGFilters_cfi')

##___________________________ECAL_TP_Filter____________________________________||
process.load('RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi')
process.EcalDeadCellTriggerPrimitiveFilter.taggingMode = cms.bool(False)

##__________________________ECAL_DC_BE_Filter______________________________||
process.load('RecoMET.METFilters.EcalDeadCellBoundaryEnergyFilter_cfi')
process.EcalDeadCellBoundaryEnergyFilter.taggingMode = cms.bool(True)
process.EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEB=cms.vint32(12, 13, 14)
process.EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEE=cms.vint32(12, 13, 14)

##___________________________EE_SC_Filter______________________________________||
process.load('RecoMET.METFilters.eeBadScFilter_cfi')
process.eeBadScFilter.taggingMode = cms.bool(False)

##___________________________PV_Filter_________________________________________||
process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag('offlinePrimaryVertices'),
                                           minimumNDOF = cms.uint32(4) ,
                                           maxAbsZ = cms.double(15),
                                           maxd0 = cms.double(2)
                                           )


##_________________________Good_Vertex_Filter______________________________||
process.goodVertices = cms.EDFilter("VertexSelector",
                                    filter = cms.bool(False),
                                    src = cms.InputTag("offlinePrimaryVertices"),
                                    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.rho < 2")
)


##___________________________MET_Skim__________________________________________||
process.condMETSelector = cms.EDProducer(
   "CandViewShallowCloneCombiner",
   decay = cms.string("caloMet pfMet"),
   cut = cms.string("(daughter(0).pt > 50) || (daughter(1).pt > 50)" ) 
   )

process.metCounter = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("condMETSelector"),
    minNumber = cms.uint32(1),
    )



##___________________________PATH______________________________________________||
process.p = cms.Path(
    process.primaryVertexFilter*
    process.CSCTightHaloFilter*
    process.HBHENoiseFilterResultProducer* #produces bools
    process.ApplyBaselineHBHENoiseFilter* 
    process.EcalDeadCellTriggerPrimitiveFilter*
    #process.EcalDeadCellBoundaryEnergyFilter*
    process.eeBadScFilter*
    #~process.logErrorTooManyClusters* # adviced by V.Innocente
    #~process.logErrorTooManySeeds*    # adviced by V.Innocente
    #~process.manystripclus53X*        # adviced by V.Innocente
    #~process.toomanystripclus53X*     # adviced by V.Innocente
    #~process.logErrorTooManyTripletsPairs*
    #~process.logErrorTooManySeedsDefault*
    #~process.logErrorTooManyTripletsPairsMainIterations*
    #~process.logErrorTooManySeedsMainIterations*
    #process.tobtecfakesfilter*
    #process.goodVertices*
    #process.trackingFailureFilter*
    process.pfClusterMetSequence*
    process.pfCaloMetSequence*
    process.condMETSelector*
    process.metCounter
    )

process.e1 = cms.EndPath(
    process.out
    )

##____________________________________________________________________________||

