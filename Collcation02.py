#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2-1
from random import randint
data = range(20)
#data = filter(lambda x:x>0,data)
data = [x for x in data if x>0]
#print 'list:',data
data = {x:randint(60,100) for x in xrange(1,40)} 
#print 'dict:',{k:v for k,v in data.iteritems() if v > 90}
data = set([x for x in range(-10,10)])
#print 'set:',{x for x in data if x%3 == 0 }

#2-2
from collections import namedtuple
from collections import Counter
import re
NAME,SEX,AGE = xrange(3)
student = ('jim','m',23)
#print 'student.name:',student[NAME]
Student = namedtuple('Student',['name','sex','age'])
Student = Student('jim','m',23)
#print 'Student.name:',Student.name
#count
data = [randint(0,20) for _ in xrange(30)]
c = dict.fromkeys(data,0)
for x in data:
	c[x] += 1
#print 'cont:',c
#counter
c2 = Counter(data)
#print 'counter:',c2.most_common(3)
txt = open('test.txt').read()
c3 = Counter(re.split(r'\W+',txt))
#print 'counter c3:',c3.most_common(3)
#sorded
dc = {x: randint(60,100) for x in 'xmdhds'}
# sorted(zip(dc.itervalues(),dc.iterkeys())) #iter you
#error
#sorted(dc.items(),key=lambda s:s[1])
#print dc

#2-5 public key
from random import randint,sample
s1 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s2 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
#for if k in s2 and k in s3
#print s1.viewkeys()&s2.viewkeys()
mdc = map(dict.viewkeys,[s1,s2])
#print s1,s2
#print 'public key:',reduce(lambda a,b:a & b,mdc)

#2-6
from collections import OrderedDict
d = OrderedDict() #{} 
d['Jim'] = (1,3)
d['Leo'] = (2,46)
d['Bob'] = (3,83)
# for x in d:
# 	print x

#deque
from collections import deque
import pickle
q = deque([],3)
q.append(3)
q.append(2)
q.append(1)
#print q
q.append(5)
#print q
pickle.dump(q,open('history','w'))

q2 = pickle.load(open('history'))
print q2
























