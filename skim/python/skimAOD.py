import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
process = cms.Process("SKIM")


##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
#process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.load("RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi")



##___________________________Global_Tag_______________________________________||
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("RecoLuminosity.LumiProducer.bunchSpacingProducer_cfi")
process.GlobalTag.globaltag = "100X_dataRun2_Prompt_v1"


##___________________________Input_Files______________________________________||
HEADER = "root://cms-xrd-global.cern.ch///"
_HEADER = "root://xrootd-cms.infn.it///"

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/CA917C5F-F64B-E811-8959-02163E019F7D.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/C8FE4866-F44B-E811-81C3-02163E00F7A2.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/60D41EF9-F54B-E811-AF04-FA163EA7E306.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/D09C2D84-F64B-E811-9549-FA163ECF85D2.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/D29E83B7-F54B-E811-9DAC-02163E01A024.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/802175E8-F74B-E811-95EC-FA163E3E5663.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/565BF6C0-F74B-E811-8C8A-FA163EC6E533.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/E20951FE-F74B-E811-B6B7-FA163EEFAEF0.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/C2DE3D0C-F84B-E811-9677-FA163E3EF566.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/E8AF7951-F84B-E811-B249-02163E019FC2.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/7017676E-F94B-E811-85F5-02163E00CE78.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/20AFC318-FB4B-E811-B7A4-FA163ED1245E.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/A061BB02-FB4B-E811-ABDD-FA163E74AA78.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/80A9D88E-FC4B-E811-BD24-FA163E5A2C36.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/7A8ACBD7-FE4B-E811-947C-02163E019F00.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/AC195C94-044C-E811-8DED-FA163EE13AA2.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/D09B34A5-F24B-E811-B5C9-FA163EA5977C.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/C6C7B8B7-F34B-E811-9E0C-FA163E47E71E.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/E8679A9A-F44B-E811-BB6F-FA163E706B48.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/7679BB3C-F64B-E811-BAC4-FA163EA9CD07.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/3AEB84FA-F74B-E811-B010-FA163E23E7A6.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/DA3A59D2-F74B-E811-851E-FA163ED6B86C.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/82E30CF1-F74B-E811-8C21-FA163E424E2B.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/EA7DE596-F94B-E811-AC9C-FA163E0972CE.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/74F49379-F94B-E811-86CE-FA163E963D8E.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/5417019B-F94B-E811-8CE7-FA163E3FC8B9.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/98DBBF84-F84B-E811-81F8-FA163EF673CF.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/DA4EF359-F94B-E811-AD9A-FA163E27C622.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/6E766769-FB4B-E811-AE17-FA163EC318C1.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/4815BC1B-EF4B-E811-BC71-FA163E90677B.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/063A35EB-F04B-E811-91F4-FA163ECB9FF9.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/6ED792AE-F24B-E811-BC88-FA163EDF5715.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/A4F0E38A-F34B-E811-B40F-FA163E0549C8.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/B2A0F28E-F54B-E811-A4E0-FA163E54FAC8.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/B41216D4-F54B-E811-99B4-FA163E23E7A6.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/0015B149-F64B-E811-B1AF-FA163E73C97A.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/D0AB1272-F64B-E811-A3EA-FA163E395E49.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/946D7A94-F54B-E811-B68A-FA163EED3BED.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/9C000E0E-F84B-E811-BB4B-02163E00AFEF.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/961E4384-F84B-E811-A1E9-FA163EE835E3.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/F27C02F9-FA4B-E811-BC42-FA163E39B2A0.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/3CEAF20A-FB4B-E811-B533-FA163E509F79.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/5862E2B3-144C-E811-B2DD-FA163EEE0E46.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/24C1A550-EE4B-E811-B00E-02163E0153F2.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/1CE3F58E-F54B-E811-ABCC-FA163E3EF566.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/46623A6E-F64B-E811-BDBB-FA163E85A8D0.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/465CDCC6-F74B-E811-8BA7-02163E017671.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/CE148AC9-F74B-E811-B721-FA163EA2F461.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/7674F81B-F84B-E811-851B-FA163EEF6020.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/8095137B-F84B-E811-8480-FA163EFF09A4.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/F6F0EF3B-F84B-E811-8E4A-FA163E1A09D0.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/56064934-FA4B-E811-82FD-FA163E78AC9F.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/D8F2485C-F04B-E811-A8AD-FA163E5189D4.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/EAE59818-F34B-E811-BFA5-FA163ED6F9B4.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/EE5F90CA-F34B-E811-8949-FA163E395E49.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/261689F2-F34B-E811-AC88-FA163ECB7D75.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/BA690C05-F44B-E811-95A5-FA163E7DB053.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/32AC4410-F64B-E811-8E8D-02163E00F687.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/90EE74D9-F74B-E811-9E0C-FA163E9472C7.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/3AE6CEB6-F64B-E811-AE88-FA163E6C430C.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/86D010F7-F74B-E811-88B5-FA163EAE298E.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/EC7A46CA-F74B-E811-8B88-FA163E78AC9F.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/3EE62186-F84B-E811-B9DB-FA163EEF5CE4.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/A84C488A-F84B-E811-9C03-02163E019FAE.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/7836029D-F94B-E811-BD86-FA163EA2F461.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/2CE058BB-F94B-E811-B700-FA163E39B5AA.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/023384F7-FA4B-E811-90FC-FA163E100866.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/0E4D9421-FA4B-E811-A0AD-FA163E723F79.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/F0C55B17-FB4B-E811-82CC-FA163E756520.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/5A94275D-F24B-E811-8FAE-FA163EA968FD.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/1CFB37CE-F24B-E811-81C9-FA163E5189D4.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/D22FD630-F34B-E811-8BCA-FA163EEEA301.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/8EAFE083-F54B-E811-B248-FA163E3CB51E.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/DE998C1B-F54B-E811-B4AC-FA163ED36045.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/2058C502-F84B-E811-9C24-FA163E3CB51E.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/E005B6C7-F74B-E811-B221-FA163EEAC093.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/4AF6CE49-F84B-E811-86A3-02163E00F687.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/84E41F62-F84B-E811-981D-FA163EB108A8.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/2C41ED9D-F94B-E811-A9B9-FA163E3F1A44.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/2CD0B337-FB4B-E811-8C74-FA163E6B4584.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/48C891C3-EB4B-E811-AB7E-FA163E57FDA9.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/6E110105-EF4B-E811-B815-FA163E605311.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/BAD4AE32-F04B-E811-B840-FA163EA5977C.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/6EBFA948-F04B-E811-B1B1-FA163EFF00DA.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/1C99241D-F14B-E811-8C25-FA163E946805.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/CEA6145D-F24B-E811-92B4-FA163E11135C.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/760EAD46-F24B-E811-B980-FA163E5EF510.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/445E7461-F24B-E811-8357-FA163E7A20D7.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/ACEE6625-F34B-E811-B5EB-02163E019ECF.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/FE87B88E-F24B-E811-98D5-FA163E7D2F6C.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/68BD0294-F44B-E811-A0AF-FA163E3E5663.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/36C0AB88-F44B-E811-B2F3-FA163E39B5AA.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/9A1E26A6-F44B-E811-B0FA-02163E019FC2.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/9206F0A1-F44B-E811-B962-FA163E503204.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/107BF49E-F64B-E811-854F-FA163EA30F9A.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/26FCA81A-F84B-E811-B5B4-FA163EC338B1.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/5E298448-F84B-E811-BDE3-FA163E8B499F.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/FE2DC5B1-F94B-E811-B784-FA163E58F803.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/F018BA1A-FB4B-E811-B49A-FA163EA274D0.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/D696BF10-FB4B-E811-8FCA-02163E019F7D.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/984B9545-F24B-E811-8CE9-FA163E29E31F.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/7C57820F-F14B-E811-8E46-FA163EB0FD9C.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/8A13462A-F34B-E811-A002-FA163EF69597.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/DA3D59F6-F34B-E811-A686-02163E019F7D.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/3CF19F8A-F44B-E811-9B41-FA163E3F1A44.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/847CF583-F54B-E811-91DD-FA163E09F985.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/3C62C7C8-F54B-E811-B11D-FA163E25A55A.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/C08030BB-F74B-E811-860E-FA163E82A06B.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/A4D3301A-F84B-E811-8C4B-FA163EABE0AA.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/CC2FFFFE-F74B-E811-9F0D-FA163E3F1A44.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/145996D8-F74B-E811-8FAA-FA163E1C405C.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/BC2236C7-F74B-E811-AFE6-FA163EC2E2FE.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/2450C592-F84B-E811-8E63-FA163E9EE1C2.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/1C133103-F84B-E811-8669-FA163E09F985.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/8408D73F-F94B-E811-9C11-FA163E32ED67.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/E49ED3BD-FB4B-E811-9CEA-FA163E6A7294.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/06E9E1AC-FB4B-E811-8913-FA163E478E88.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/64E7945C-FB4B-E811-8078-FA163E3A6268.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/4855AE58-F84B-E811-9455-02163E00F7A3.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/C440BA5E-FC4B-E811-B0E2-FA163E980891.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/5EC33B84-064C-E811-B20E-FA163E6D856B.root",
 HEADER+"/store/data/Run2018A/SingleMuon/AOD/PromptReco-v1/000/315/270/00000/0E6F043B-124C-E811-8812-FA163E1D6363.root"
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
#process.options = cms.untracked.PSet(SkipEvent = cms.untracked.vstring('ProductNotFound'))
process.MessageLogger.cerr.FwkReport.reportEvery = 50
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(20000) )


##___________________________CSC_Halo_Filter__________________________________||
process.load('RecoMET.METFilters.CSCTightHaloFilter_cfi')
process.CSCTightHaloFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.CSCTightHaloTrkMuUnvetoFilter_cfi')
process.CSCTightHaloTrkMuUnvetoFilter.taggingMode = cms.bool(True)

##___________________________Global_Halo_Filter__________________________________||
process.load('RecoMET.METFilters.globalTightHalo2016Filter_cfi')
process.globalTightHalo2016Filter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.globalSuperTightHalo2016Filter_cfi')
process.globalSuperTightHalo2016Filter.taggingMode = cms.bool(True)

##___________________________HCAL_Noise_Filter________________________________||
process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
process.HBHENoiseFilterResultProducer.minZeros = cms.int32(99999)
process.HBHENoiseFilterResultProducer.IgnoreTS4TS5ifJetInLowBVRegion=cms.bool(False)


#process.ApplyBaselineHBHENoiseFilter = cms.EDFilter('BooleanFlagFilter',
#    inputLabel = cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResult'),
#    reverseDecision = cms.bool(False)
#)

process.load('RecoMET.METFilters.HcalStripHaloFilter_cfi')
process.HcalStripHaloFilter.taggingMode = cms.bool(True)

process.goodVertices = cms.EDFilter(
  "VertexSelector",
  filter = cms.bool(False),
  src = cms.InputTag("offlinePrimaryVertices"),
  cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.rho < 2")
)
process.load('RecoMET.METFilters.trackingFailureFilter_cfi')
process.trackingFailureFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi')
process.EcalDeadCellTriggerPrimitiveFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.eeBadScFilter_cfi')
process.eeBadScFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
process.BadChargedCandidateFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
process.BadPFMuonFilter.taggingMode = cms.bool(True)
#process.BadPFMuonFilter.debug = cms.bool(True) 

process.load('RecoMET.METFilters.BadChargedCandidateSummer16Filter_cfi')
process.BadChargedCandidateSummer16Filter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.BadPFMuonSummer16Filter_cfi')
process.BadPFMuonSummer16Filter.taggingMode = cms.bool(True)

#introduced in 2017

process.load("RecoMET.METFilters.EcalBadCalibFilter_cfi")
process.EcalBadCalibFilter.taggingMode = cms.bool(True)

process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag('offlinePrimaryVertices'),
                                           minimumNDOF = cms.uint32(4) ,
                                           maxAbsZ = cms.double(24),
                                           maxd0 = cms.double(2)
                                           )

process.load('RecoMET.METFilters.EcalDeadCellBoundaryEnergyFilter_cfi')
process.EcalDeadCellBoundaryEnergyFilter.taggingMode = cms.bool(True)
process.EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEB=cms.vint32(12, 13, 14)
process.EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEE=cms.vint32(12, 13, 14)

process.condMETSelector = cms.EDProducer(
   "CandViewShallowCloneCombiner",
   isReco = cms.bool(False),
   decay = cms.string("caloMet pfMet"),
   cut = cms.string("(daughter(0).pt > -100) || (daughter(1).pt > -100)" ) 
   )

process.metCounter = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("condMETSelector"),
    minNumber = cms.uint32(1),
    )
    




process.metScanNtupleMaker = cms.EDAnalyzer("METScanningNtupleMaker",
                                            isReco = cms.bool(False),
                                            rootOutputFile=cms.string("tuple.root"),
                                            muonCandidates=cms.InputTag("muons"),
                                            pfCandidates=cms.InputTag("particleFlow"),
                                            pfJets=cms.InputTag("ak4PFJets"),
                                            caloMET=cms.InputTag("caloMet"),
                                            pfCaloMET=cms.InputTag("pfCaloMet"), 
                                            pfClusterMET=cms.InputTag("pfClusterMet"),
                                            pfMET=cms.InputTag("pfMet"),
                                            EcalPFClusterCollection=cms.InputTag("particleFlowClusterECAL"),
                                            HcalPFClusterCollection=cms.InputTag("particleFlowClusterHCAL"),
                                            HBHEPFClusterCollection=cms.InputTag("particleFlowClusterHBHE"),
                                            HOPFClusterCollection=cms.InputTag("particleFlowClusterHO"),
                                            HFPFClusterCollection=cms.InputTag("particleFlowClusterHF"),
                                            tracksCollection=cms.InputTag("generalTracks"),
                                            TRKfilterLETMC=cms.InputTag("logErrorTooManyClusters"),
                                            TRKfilterLETMS=cms.InputTag("logErrorTooManySeeds"),
                                            TRKfilterMSC=cms.InputTag("manystripclus53X"),
                                            TRKfilterTMSC=cms.InputTag("toomanystripclus53X"),
                                            GlobalHalofilterTight=cms.InputTag("globalTightHalo2016Filter"),
                                            GlobalHalofilterSuperTight=cms.InputTag("globalSuperTightHalo2016Filter"),
                                            HcalStripHaloFilter=cms.InputTag("HcalStripHaloFilter"),
                                            HBHEfilterR1=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun1"),
                                            HBHEfilterR2L=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Loose"),
                                            HBHEfilterR2T=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Tight"),
                                            HBHEfilterISO=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun1"),
                                            ECALTPfilter=cms.InputTag("EcalDeadCellTriggerPrimitiveFilter"),
                                            ECALSCfilter=cms.InputTag("eeBadScFilter"),
                                            EBRecHits=cms.InputTag("reducedEcalRecHitsEB"),
                                            EERecHits=cms.InputTag("reducedEcalRecHitsEE"),
                                            ESRecHits=cms.InputTag("reducedEcalRecHitsES"),
                                            BadChCandFilter=cms.InputTag("BadChargedCandidateFilter"),
                                            BadPFMuon=cms.InputTag("BadPFMuonFilter"),                                            
                                            EcalBadCalibFilter=cms.InputTag("EcalBadCalibFilter"),
					    OfflinePrimaryVertices = cms.InputTag("offlinePrimaryVertices"),
                                            HcalNoise=cms.InputTag("hcalnoise")
                                            
)

# This part is needed if you want to update the BeamHaloSummary information
from RecoMET.METProducers.CSCHaloData_cfi import *
from RecoMET.METProducers.EcalHaloData_cfi import *
from RecoMET.METProducers.HcalHaloData_cfi import *
from RecoMET.METProducers.GlobalHaloData_cfi import *
from RecoMET.METProducers.BeamHaloSummary_cfi import *

#process.BeamHaloId = cms.Sequence(CSCHaloData*EcalHaloData*HcalHaloData*GlobalHaloData*BeamHaloSummary)


##___________________________PATH______________________________________________||
process.p = cms.Path(
#    process.BeamHaloId* #Uncomment this if you want to rerun the BeamHaloSummary. By default this line should remain commented
    process.primaryVertexFilter*
    process.bunchSpacingProducer *
    process.condMETSelector *
#   process.metCounter* #uncomment this line to apply a met cut
    process.CSCTightHaloFilter*
    process.HBHENoiseFilterResultProducer* #produces bools    
#   process.ApplyBaselineHBHENoiseFilter* 
    process.EcalDeadCellTriggerPrimitiveFilter*
    process.eeBadScFilter*
    process.goodVertices*
    process.trackingFailureFilter*
    process.EcalDeadCellBoundaryEnergyFilter*
    process.CSCTightHaloTrkMuUnvetoFilter*
    process.globalTightHalo2016Filter * 
    process.globalSuperTightHalo2016Filter * 
    process.HcalStripHaloFilter*
    process.BadChargedCandidateFilter*
    process.BadPFMuonFilter*
    process.EcalBadCalibFilter*
    process.metScanNtupleMaker ##CH: writes a flat tree
    )

process.e1 = cms.EndPath(
    process.out ##CH: write the skimmed edm file 
    )
