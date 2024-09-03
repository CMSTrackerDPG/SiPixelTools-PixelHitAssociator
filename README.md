# PixelHitAssociator

A customised version of the SimHit-RecHit comparion, used for resolution testing.


## Software setup

Prepare your working directory with CMSSW

```
export SCRAM_ARCH=el9_amd64_gcc12
cmsrel CMSSW_14_0_15
cd CMSSW_14_0_15/src
cmsenv
git clone https://github.com/CMSTrackerDPG/SiPixelTools-PixelHitAssociator.git SiPixelTools/PixelHitAssociator
scram b -j 8
cd SiPixelTools/PixelHitAssociator/test/
```
