#!/bin/bash

#Add the python directory to the path and the Pythonpath
BASEDIR="$( cd "$( dirname "$BASH_SOURCE[0]" )" && pwd )"
echo "$BASEDIR"
export HOMUONTRIGGER_BASE=$BASEDIR/src/HoMuonTrigger
export PATH=$HOMUONTRIGGER_BASE/python:$PATH
export PYTHONPATH=$HOMUONTRIGGER_BASE/python:$PYTHONPATH


