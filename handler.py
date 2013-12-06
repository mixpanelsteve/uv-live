#!/usr/bin/python

import sys
import json
import time

with open('/home/steve/uservoice/output.txt','a') as f:
    f.write(str(time.time()) + '\n')
    for k, v in json.loads(sys.argv[1]).items():
        writestring = "%s : %s\n" % (k, v)
        f.write(writestring)
    f.write('\n \%----------\% \n')
