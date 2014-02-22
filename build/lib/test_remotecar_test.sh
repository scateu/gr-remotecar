#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/scateu/hackrf/01Book/files/RemoteControlledCar/gr-remotecar/lib
export PATH=/home/scateu/hackrf/01Book/files/RemoteControlledCar/gr-remotecar/build/lib:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-remotecar 
