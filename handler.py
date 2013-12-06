#!/usr/bin/python

import sys
import json

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
with open('/home/steve/uservoice/output.txt','w') as f:
	for arg in sys.argv[1:]:
		f.write(arg)
		try:
			arg = json.loads(arg)
			print arg
		except:
			print ":("

