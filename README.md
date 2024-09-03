# PixelHitAssociator

A customised version of the SimHit-RecHit comparion, used for resolution testing.


## Software setup

Prepare your working directory with CMSSW

```
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_6_44
cd CMSSW_10_6_44/src
cmsenv
git clone -b CMSSW_10_6_X https://github.com/CMSTrackerDPG/SiPixelTools-PixelHitAssociator.git SiPixelTools/PixelHitAssociator
scram b -j 8
cd SiPixelTools/PixelHitAssociator/test/
