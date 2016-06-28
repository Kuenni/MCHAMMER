from submit import Submitter
import os,sys,math

batchNumber = int(raw_input("Wich batchnumber to submit?"))

submitter = Submitter('T2_DE_RWTH',40,batchNumber)
submitter.submit()
print "Exiting..."
sys.exit(0)
