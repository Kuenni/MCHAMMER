#!/bin/bash
INSTANCE=$1

LOGDIR=log

#First make sure the directory for logging exists
mkdir -p $LOGDIR
if [ ! $? -eq 0 ]; then
	echo "Could not create log dir " $LOGDIR
	exit 1

fi

#Then create a file for logging this job
LOGFILE=$LOGDIR/`date +%y_%m_%d_%H_%M_%S`-INSTANCE_$INSTANCE.log
touch $LOGFILE

if [ ! -f $LOGFILE ]; then
	echo "Could not create log file " $LOGFILE
	exit 1
fi

#Gather information about the machine, we are running on
MACHINE=`hostname`
USERNAME=`whoami`
echo "Job executed on: "`date` >> $LOGFILE
echo "Running on machine: "$MACHINE >> $LOGFILE
echo "Username: "$USERNAME >> $LOGFILE
echo >> $LOGFILE

echo "Files available in execution directory:" >> $LOGFILE
echo `ls -1` >> $LOGFILE
echo >> $LOGFILE

echo "Sourcing root" >> $LOGFILE
source /usr/lib/root-5.34.25/bin/thisroot.sh
echo >> $LOGFILE

echo "Staring simulation now..." >> $LOGFILE
if ./analyzeFull.py --instance $INSTANCE; then
	echo "finished" >> $LOGFILE
else
	echo "Error occured during script execution" >> $LOGFILE
	exit 1
fi
echo "Files available in execution directory after execution:" >> $LOGFILE
echo `ls -1` >> $LOGFILE
echo >> $LOGFILE

