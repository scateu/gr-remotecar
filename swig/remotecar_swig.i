/* -*- c++ -*- */

#define REMOTECAR_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "remotecar_swig_doc.i"

%{
#include "remotecar/RemoteCarBaseBand.h"
#include "remotecar/RemoteCarIIBaseBand.h"
%}

%include "remotecar/RemoteCarBaseBand.h"
GR_SWIG_BLOCK_MAGIC2(remotecar, RemoteCarBaseBand);
%include "remotecar/RemoteCarIIBaseBand.h"
GR_SWIG_BLOCK_MAGIC2(remotecar, RemoteCarIIBaseBand);
