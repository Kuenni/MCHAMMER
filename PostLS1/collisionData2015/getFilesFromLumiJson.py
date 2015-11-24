import subprocess 
import json
import sys

from plotting.OutputModule import CommandLineHandler

cli = CommandLineHandler('[getFilesFromLumiJson] ')

jsonFile = sys.argv[1]
dataset = sys.argv[2]

inputJson = json.load(open(jsonFile))
output = file('files%s' % (dataset.replace('/','_')),'w+')

cli.output('Searching files for dataset')

for i,key in enumerate(inputJson.keys()):
	cmd = 'das_client.py --query=\"file dataset=%s run=%s\"' % (dataset,key)
	p = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
	res,err = p.communicate()
	for line in res.split():
		if line.find('.root') == -1:
			pass
		else:
			output.write('root://xrootd.unl.edu/' + line + '\n')
			print line
	cli.printProgress(i+1,len(inputJson.keys()))
print