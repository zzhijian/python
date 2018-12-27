#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = u'你好'
# print s.encode('utf-8')
# f = open('py2.txt','w')
# f.write(u'你好'.encode('gb2312'))
# f.close()

# f = open('py2.txt','r')
# print f.read()

# f = open('py3.txt','wt',endcoding='utf8')
# f.write('你好')
# f.close()

# f = open('py3.txt','rt',endcoding='utf8')
# print f.read()


#5-5
import os 
import stat
import time
s = os.stat('test.txt')

# print stat.S_ISDIR(s.st_mode) # dir
# print stat.S_ISREG(s.st_mode)

# print s.st_mode & stat.S_IXUSR #访问权限
# print time.localtime(s.st_atime) #最后访问时间
# print s.st_size #文件大小

#快捷方法

# print os.path.isdir('test.txt')
# print os.path.islink('test.txt')
# print os.path.isfile('test.txt')
# print os.path.getatime('test.txt')#访问时间
# print os.path.getmtime('test.txt')#最后访问时间

#临时文件
from tempfile import NamedTemporaryFile, TemporaryFile
f = TemporaryFile()
f.write('sfetrhtr'*10000)

f.seek(0)
print f.read(100)

ntf = NamedTemporaryFile()#有名字
print ntf.name
ntf = NamedTemporaryFile(delete=False)#not delete
print ntf.name