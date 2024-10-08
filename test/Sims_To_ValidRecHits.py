##############################################################################
# start from simhits, do trackerlocal, compare sim and rec-hits
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
#process = cms.Process("TestValid",eras.Run2_2017)
process = cms.Process("TestValid",eras.Run3)

process.load("Configuration.Geometry.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load("FWCore.MessageLogger.MessageLogger_cfi")

# process.load("SimTracker.Configuration.SimTracker_cff")
process.load("SimG4Core.Configuration.SimG4Core_cff")

process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')

# for strips 
process.load("CalibTracker.SiStripESProducers.SiStripGainSimESProducer_cfi")

# clusterizers & rhs 
#process.load("RecoLocalTracker.Configuration.RecoLocalTracker_cff")
# needed for pixel RecHits (templates?)
process.load("Configuration.StandardSequences.Reconstruction_cff")

# Refitter
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
# to use no All 
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_design', '')

#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_design', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_realistic', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_design', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_realistic', '')

#process.GlobalTag.globaltag = '106X_upgrade2018_realistic_v9'
#process.GlobalTag.globaltag = '110X_mcRun3_2021_realistic_v3'
#process.GlobalTag.globaltag = '110X_mcRun3_2023_realistic_v3'
#process.GlobalTag.globaltag = '110X_mcRun3_2024_realistic_v3'

#process.GlobalTag.globaltag = '110X_mcRun3_2021_realistic_Candidate_2019_10_31_12_09_00' # 2000e
process.GlobalTag.globaltag = '110X_mcRun3_2023_realistic_Candidate_2019_11_04_22_24_44' # 2000e
#process.GlobalTag.globaltag = '110X_mcRun3_2024_realistic_Candidate_2019_10_31_12_18_03' # 2000e


process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(
# '/store/user/kotlinski/MC/mu_pt100/simhits/simHits1.root'

# Run3 MC
#"/store/mc/Run3Summer19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/106X_mcRun3_2021_realistic_v3-v2/130000/FF1B6F7B-55F6-2A42-A85B-654E59172A1E.root",
"/store/mc/Run3Summer19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/106X_mcRun3_2023_realistic_v3-v2/50000/FF819EB4-7243-1640-9F3A-21553B718CA9.root",
#"/store/mc/Run3Summer19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/106X_mcRun3_2024_realistic_v4-v2/270000/C0FD668E-2D90-4F4A-A607-9E8FF11B0A9F.root",

# 2018
#"/store/relval/CMSSW_10_6_1_patch3/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_106X_upgrade2018_realistic_v6-v1/20000/FE7FDB90-CC19-244B-B7CE-DDEB9500B5CB.root",

# PU (GEN-SIM-DIGI-RAW)  used in 2/2019
#"/store/relval/CMSSW_10_4_0/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_103X_upgrade2018_design_v4-v1/20000/193FB1CE-333D-E540-995E-1BA38BA1CE3C.root"

# mb
#"/store/relval/CMSSW_10_4_0/RelValMinBias_13/GEN-SIM/103X_mc2017_realistic_v2-v1/20000/F0FF4DFA-613B-4749-BBC3-FB29AD691FA5.root"
#"/store/relval/CMSSW_10_4_0/RelValMinBias_13/GEN-SIM/103X_upgrade2018_design_v4-v1/20000/C9CE0381-F732-4A4F-A263-D445DF99148C.root"
#"/store/relval/CMSSW_10_4_0/RelValMinBias_13/GEN-SIM/103X_upgrade2018_realistic_v8-v1/20000/E0E79FD8-5A76-6145-9816-B7BBC5E79AB1.root" 

#"/store/relval/CMSSW_10_4_0/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_103X_upgrade2018_design_v4-v1/20000/193FB1CE-333D-E540-995E-1BA38BA1CE3C.root"

#"/store/relval/CMSSW_10_4_0/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_103X_upgrade2018_realistic_v8-v1/20000/0D388168-67C8-A544-8A75-8A96D40C396B.root"

#"/store/relval/CMSSW_10_4_0/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_103X_mc2017_realistic_v2-v1/20000/222AF93E-CE66-6342-A266-E78F6FCDD8EC.root"

  )
)

# allow for events to have the same event number 
process.source.duplicateCheckMode=cms.untracked.string("noDuplicateCheck")


process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('pixRecHitsValid'),
    destinations = cms.untracked.vstring('cout'),
#    destinations = cms.untracked.vstring("log","cout"),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR')
#        threshold = cms.untracked.string('DEBUG')
    )
#    log = cms.untracked.PSet(
#        threshold = cms.untracked.string('DEBUG')
#    )
)



process.o1 = cms.OutputModule("PoolOutputModule",
      outputCommands = cms.untracked.vstring('drop *','keep *_*_*_TestValid'),
#      outputCommands = cms.untracked.vstring('keep *_*_*_*'),
      fileName = cms.untracked.string('file:dummy.root')
)


# DB stuff 
# GenError
useLocalDB = False
if useLocalDB :
    process.DBReaderFrontier = cms.ESSource("PoolDBESSource",
     DBParameters = cms.PSet(
         messageLevel = cms.untracked.int32(0),
         authenticationPath = cms.untracked.string('')
     ),
     toGet = cms.VPSet(
 	 cms.PSet(
          record = cms.string('SiPixelGenErrorDBObjectRcd'),
#          tag = cms.string('SiPixelGenErrorDBObject38Tv1')
#          tag = cms.string('SiPixelGenErrorDBObject38TV10')
          tag = cms.string('SiPixelGenErrorDBObject_38T_v1_mc')
 	 ),
 	),
#     connect = cms.string('sqlite_file:siPixelGenErrors38T.db')
#     connect = cms.string('frontier://FrontierProd/CMS_COND_PIXEL_000')
     connect = cms.string('frontier://FrontierPrep/CMS_COND_PIXEL')
    ) # end process
    process.myprefer = cms.ESPrefer("PoolDBESSource","DBReaderFrontier")
# endif


process.g4SimHits.Generator.HepMCProductLabel = 'source'

# for direct digis
#process.siPixelClustersPreSplitting.src = 'simSiPixelDigis' # for V5, direct
# process.siPixelClusters.src = 'mix'
# modify digitizer parameters
#process.simSiPixelDigis.digitizers.pixel.ThresholdInElectrons_BPix = 3500.0 
#process.simSiPixelDigis.digitizers.pixel.AddPixelInefficiencyFromPython = cms.bool(False)
# use inefficiency from DB Gain calibration payload?
#process.simSiPixelDigis.digitizers.pixel.useDB = cms.bool(False) 
# use LA from file 
#process.simSiPixelDigis.digitizers.pixel.LorentzAngle_DB = cms.bool(False)
#process.simSiPixelDigis.digitizers.pixel.TanLorentzAnglePerTesla_BPix = 0.106 
#process.simSiPixelDigis.digitizers.pixel.TanLorentzAnglePerTesla=FPix = 0.106 

# Additional output definition
# modify digitizer parameters
#process.mix.digitizers.pixel.TofUpperCut = 9999.5  # 12.5
#process.mix.digitizers.pixel.TofLowerCut =-9999.5  # -12.5
#process.mix.digitizers.pixel.ThresholdInElectrons_FPix    = cms.double(1500.0)
#process.mix.digitizers.pixel.ThresholdInElectrons_BPix    = cms.double(1500.0)
#process.mix.digitizers.pixel.ThresholdInElectrons_BPix_L1 = cms.double(2000.0)
#process.mix.digitizers.pixel.ThresholdInElectrons_BPix_L2 = cms.double(1500.0)
#process.mix.digitizers.pixel.ThresholdSmearing_FPix    = cms.double(1.0)
#process.mix.digitizers.pixel.ThresholdSmearing_BPix    = cms.double(1.0)
#process.mix.digitizers.pixel.ThresholdSmearing_BPix_L1 = cms.double(1.0)
#process.mix.digitizers.pixel.ThresholdSmearing_BPix_L2 = cms.double(1.0)


# to run rechit "official" validation
#process.load("Validation.TrackerRecHits.trackerRecHitsValidation_cff")
#process.load("Validation.TrackerRecHits.SiPixelRecHitsValid_cfi")

# my rec-sim hit compare 
process.load("SiPixelTools.PixelHitAssociator.SiPixelRecHitsValid_cff")
#process.load("SiPixelTools.PixelHitAssociator.StudyRecHitResolution_cff")
# not on track 
process.pixRecHitsValid.outputFile="pixelrechits.root"
process.pixRecHitsValid.verbose=False 
#process.pixRecHitsValid.muOnly=True  # 
process.pixRecHitsValid.ptCut=1.      #  
process.pixRecHitsValid.src="siPixelRecHitsPreSplitting"
#process.pixRecHitsValid.src="siPixelRecHits"
#process.pixRecHitsValid.associatePixel = True
#process.pixRecHitsValid.associateStrip = False
#process.pixRecHitsValid.associateRecoTracks = False

# on track 
process.pixRecHitsValid.useTracks = True  # use hits on tracks only, from track refit
#process.pixRecHitsValid.useTracks = False # use all hits, from rechit containers 
process.pixRecHitsValid.tracks = 'TrackRefitter'


process.StudyRecHitMatching = cms.EDAnalyzer("StudyRecHitMatching",
                                             outputFile=cms.untracked.string("rechitmatching.root"),
                                             verbose=cms.untracked.bool(False),
                                             muOnly=cms.untracked.bool(False),
                                             ptCut=cms.untracked.double(1.),
                                             src=cms.InputTag("siPixelRecHitsPreSplitting"),
                                             #src = cms.InputTag("siPixelRecHits"),
                                             # on track 
                                             useTracks = cms.untracked.bool(True),
                                             tracks = cms.untracked.InputTag('TrackRefitter'),
                                             #tracks = cms.untracked.InputTag("generalTracks"),
                                             pixelSimLinkSrc = cms.InputTag("simSiPixelDigis"),
                                             ROUList = cms.vstring(
                                                 'TrackerHitsPixelBarrelLowTof', 
                                                 'TrackerHitsPixelBarrelHighTof', 
                                                 'TrackerHitsPixelEndcapLowTof', 
                                                 'TrackerHitsPixelEndcapHighTof'),
                                             associatePixel = cms.bool(True),
                                             associateStrip = cms.bool(False),
                                             associateRecoTracks = cms.bool(False),
)



process.TrackRefitter.src = "generalTracks"
process.TrackRefitter.TTRHBuilder = 'WithAngleAndTemplate'
#process.TrackRefitter.TTRHBuilder = 'WithTrackAngle'


process.d = cms.EDAnalyzer("PixClusterAna",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    #src = cms.InputTag("siPixelClustersForLumi"),   # from the lumi stream
    src = cms.InputTag("siPixelClusters"),
    #src = cms.InputTag("siPixelClustersPreSplitting"),
    #src = cms.InputTag("ALCARECOTkAlMinBias"), # ALCARECO
    Tracks = cms.InputTag("generalTracks"),
    # additional selections, e.g. select bx=1 -> (2,1)
    Select1 = cms.untracked.int32(9998),  # select the cut type, 0 no cut
    Select2 = cms.untracked.int32(0),  # select the cut value   
)

process.c = cms.EDAnalyzer("PixClustersWithTracks",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("generalTracks"),
# for cosmics 
#    src = cms.InputTag("ctfWithMaterialTracksP5"),
#     PrimaryVertexLabel = cms.untracked.InputTag("offlinePrimaryVertices"),
#     trajectoryInput = cms.string("TrackRefitterP5")
#     trajectoryInput = cms.string('cosmictrackfinderP5')
# additional selections
    Select1 = cms.untracked.int32(9998),  # select the cut type, o no cut
    Select2 = cms.untracked.int32(0),  # select the cut value   
)


process.a0 = cms.EDAnalyzer("PixDigisTest",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
# after the digitizer 
    src = cms.InputTag("mix"),
# after raw
#    src = cms.InputTag("siPixelDigis"),
)

process.a = cms.EDAnalyzer("PixDigisTest",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
# after the digitizer 
#    src = cms.InputTag("mix"),
# after raw
    src = cms.InputTag("siPixelDigis"),
)


# use the test from SiTracker
process.b =  cms.EDAnalyzer("PixSimHitsTest",
                                   src = cms.string("g4SimHits"),
        mode = cms.untracked.string("bpix"),
        list = cms.string("TrackerHitsPixelBarrelLowTof"),
        #list = cms.string("TrackerHitsPixelBarrelHighTof"),
#        mode = cms.untracked.string("fpix"),
                                   #list = cms.string("TrackerHitsPixelEndcapLowTof"),
                                   #list = cms.string("TrackerHitsPixelEndcapHighTof"),
        Verbosity = cms.untracked.bool(False),
        phase1 = cms.untracked.bool(True),
)
# use the test from SiTracker
process.bf =  cms.EDAnalyzer("PixSimHitsTest",
                             src = cms.string("g4SimHits"),
                             #mode = cms.untracked.string("bpix"),
                             #list = cms.string("TrackerHitsPixelBarrelLowTof"),
                             #list = cms.string("TrackerHitsPixelBarrelHighTof"),
                             mode = cms.untracked.string("fpix"),
                             list = cms.string("TrackerHitsPixelEndcapLowTof"),
                             #list = cms.string("TrackerHitsPixelEndcapHighTof"),
                             Verbosity = cms.untracked.bool(False),
                             phase1 = cms.untracked.bool(True),
)


process.r = cms.EDAnalyzer("SiPixelRawDump", 
    Timing = cms.untracked.bool(False),
    IncludeErrors = cms.untracked.bool(True),
#   In 2015 data, label = rawDataCollector, extension = _LHC                                
    InputLabel = cms.untracked.string('rawDataCollector'),
# for MC
#    InputLabel = cms.untracked.string('siPixelRawData'),
#   For PixelLumi stream                           
#    InputLabel = cms.untracked.string('hltFEDSelectorLumiPixels'),
# for dump files 
#    InputLabel = cms.untracked.string('source'),
# old
#    InputLabel = cms.untracked.string('siPixelRawData'),
#    InputLabel = cms.untracked.string('source'),
#    InputLabel = cms.untracked.string("ALCARECOTkAlMinBias"), # does not work
    CheckPixelOrder = cms.untracked.bool(False),
# 0 - nothing, 1 - error , 2- data, 3-headers, 4-hex
    Verbosity = cms.untracked.int32(0),
# threshold, print fed/channel num of errors if tot_errors > events * PrintThreshold, default 0,001 
    PrintThreshold = cms.untracked.double(0.001)
)



process.TFileService = cms.Service("TFileService",
    fileName = cms.string('simtorec.root')
)


#process.p1 = cms.Path(process.pdigi_valid*process.a)
# go through raw
#process.p1 = cms.Path(process.pdigi_valid*process.SimL1Emulator*process.DigiToRaw*process.RawToDigi*process.reconstruction*process.TrackRefitter*process.pixRecHitsValid)

#process.p1 = cms.Path(process.b*process.bf*process.pdigi_valid*process.a0*process.SimL1Emulator*process.DigiToRaw*process.RawToDigi*process.a*process.reconstruction*process.TrackRefitter*process.d*process.c*process.pixRecHitsValid)

process.p1 = cms.Path(process.b*process.bf*process.pdigi_valid*process.a0*process.SimL1Emulator*process.DigiToRaw*process.RawToDigi*process.a*process.reconstruction*process.TrackRefitter*process.d*process.c*process.StudyRecHitMatching)

# go directly - fails for muons 
#process.p1 = cms.Path(process.pdigi_valid*process.SimL1Emulator*process.reconstruction*process.TrackRefitter*process.pixRecHitsValid)


#process.outpath = cms.EndPath(process.o1)


