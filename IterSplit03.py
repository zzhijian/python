#!/usr/bin/env python
# -*- coding: utf-8 -*-
l = [1,2,3,4]
s = "abcd"
# __iter getiter
#print iter(l),iter(s) #is iterater
#
import requests
from collections import Iterable,Iterator
class WeatherIterater(Iterator):
	def __init__(self, citys):
		self.citys = citys
		self.index = 0

	def getWeather(self,city):
		r = requests.get(u"http://wthrcdn.etouch.cn/weather_mini?city="+city)	
		data = r.json()["data"]["forecast"][0]
		return (city,data["low"],data["high"])

	def next(self):
		if self.index == len(self.citys):
			raise StopIteration
		city = self.citys[self.index]
		self.index += 1
		return self.getWeather(city)

class WeatherIterable(Iterable):
	def __init__(self, citys):
		self.citys = citys

	def __iter__(self):
		return WeatherIterater(self.citys)
#3-2 iterater
# for x in WeatherIterable([u'北京',u'上海',u'深圳']):
# 	print 'city:',x

# 3-3 生成器函数实现迭代对象
def f():
	print "in f() 1"
	yield 1

	print "in f() 2"
	yield 2

	print "in f() 3"
	yield 3

g = f()
# for x in g:
# print g.__iter__() is g
# print g.next()
# print g.next()
# print g.next()

class PrimeNumbers:
	def __init__(self,start,end):
		self.start = start
		self.end = end

	def isPrimeNum(self,k):
		if k < 2:
			return False
		for i in xrange(2,k):
			if k % i == 0:
				return False

		return True

	def __iter__(self):
		for k in xrange(self.start,self.end+1):
			if self.isPrimeNum(k):
				yield k
#素数 如果一个大于二的正整数,除了1和它本身之外,不是任何数的倍数,那么它就是一个素数
# for x in PrimeNumbers(1,100):
# 	print x

#3-4 5
l = [1,2,3,4]
# for x in reversed(l):
# 	print 'reversed x:',x
# 	实现反向迭代
class FloatRange:
	def __init__(self,start,end,step=0.1):
		self.start = start
		self.end = end
		self.step = step

	def __iter__(self):
		t = self.start
		while t <= self.end:
			yield t
			t += self.step
	def __reversed__(self):
		t = self.end
		while t >= self.start:
			yield t
			t -= self.step
# for x in FloatRange(1.0,4.0,0.5):
# 	print x

#迭代器切片
f = open("test.txt")
# for line in f:
# 	print line
from itertools import islice
# for line in islice(f,3,6): #silice(f,3,None) end
# 	print "islice:",line

# for x in f: #6 start islice
# 	print x

#迭代多个对象
from random import randint
chinese = [randint(60,100) for x in xrange(40)]
math = [randint(60,100) for x in xrange(40)]
english = [randint(60,100) for x in xrange(40)]
total = []
for i in xrange(len(chinese)):
	total.append( chinese[i]+math[i]+english[i])
print 'total:',total
print zip([1,2,3,4],('a','b','c','d'),[6,7,8,9,10])
#并行  zip
total = []
for c,m,e in zip(chinese,math,english):
	total.append(c+m+e)
print 'zip total:',total

#串行 一个for统计全年级高于90分的学生
from itertools import chain
e1 = [randint(60,100) for x in xrange(40)]
e2 = [randint(60,100) for x in xrange(42)]
e3 = [randint(60,100) for x in xrange(39)]
count = 0
for s in chain(e1,e2,e3):
	if s > 90:
		count += 1
print '>90 count:',count



















