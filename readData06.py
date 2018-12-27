#!/usr/bin/env python
# -*- coding: utf-8 -*-
#6-1 read csv
from urllib import urlretrieve
# urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz','pp.csv')
# rf = open('pp.csv','rb')
# reader = csv.reader(rf)
# print reader.next()
# wf = open('pp.csv','wb')
# writer = csv.write(wf)
# print write.writerRow(["e7fuwe7u","h9iefjr"])

# with open('pp.csv','rb') as rf:
# 	reader = csv.reader(rf)

import json
l = [1,3,'dscw',{'df','csd','jom'}]
print json.dumps(l,separators=[',',':']) #rever json

print json.loads("[1,3,'dscw',{'df','csd','jom'}]")





