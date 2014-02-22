#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/scateu/hackrf/01Book/files/RemoteControlledCar/gr-remotecar/python
export PATH=/home/scateu/hackrf/01Book/files/RemoteControlledCar/gr-remotecar/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=/home/scateu/hackrf/01Book/files/RemoteControlledCar/gr-remotecar/build/swig:$PYTHONPATH
/usr/bin/python2 /home/scateu/hackrf/01Book/files/RemoteControlledCar/gr-remotecar/python/qa_RemoteCarBaseBand.py 
