#!/usr/bin/env python
# -*- coding: utf-8 -*-
#4-1
s = 'ab;cd|ef##ndds&fd;fdh|f'
#x = !ps aux
res = s.split(";")
#print map(lambda x:x.split('|'),res)

def mySplit(s,ds):
	res = [s]
	for d in ds:
		t = []
		map(lambda x: t.extend(x.split(d)),res)
		res = t
	return [x for x in res if x]

#print 'myslpit:',mySplit(s,';|#&')
# geng you
import re
#print 're split:',re.split(r'[;|#&]+',s)

#4-2 3
import os,stat
#print 'my.sh'.endswith(('sh','py'))

filenames = [name for name in os.listdir(".") if name.endswith(('sh','py'))]
#print os.stat("test.py").st_mode
#print oct(os.stat("test.py").st_mode)
#update prvies
os.chmod('test.py',os.stat("test.py").st_mode | stat.S_IXUSR)

#调整日期格式
f = open("datetest.txt")
log = f.read()
#print re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log)
#print 'name P:',re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',log)

#str join
s1 = "rwfruwufru"
s2 = "3242544353"
#print ";".join([s1,s2])
s3 = 99880
l = [s1,s2,s3]
#print ";".join(str(x) for x in l)

#4-5 字符串对其
dc = {
	"hansan":188,
	"dcds":188,
	"cdsccdscds":188,
	"fdscd":188,
	"dsfb":188,
	"sdcsdc":188,
}
#print 'fdvdf'.rjust(20) # ljust center
maxlen = max(map(len,dc.keys()))
# for k in dc:
# 	print k.rjust(maxlen),':',dc[k]

#去掉不需要的字符
s = "   abd\ttyrer\ter\r cdc\rs\n cdsc \ndcd 123  "
# print s.strip()
# print s.rstrip()
# print "----sds+sd+++".strip("+-") # center not del
# print 'replace:',s.replace('\t','')
# print 'sub:',re.sub('[\r\n]','',s)
# import string
# print 'string translate:',s.translate(string.maketrans("cd","xy"))

# s = u'nā jà kǒ cē'
# print str(s)





