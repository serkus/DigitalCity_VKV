#-*-coding:UTF-8 -*-
#!/usr/bin/env python

import  os, sys
from  io import StringIO

config={}
location= []
vk =[]
tlg =[]
loc
def parse()::
	with open('./list.txt', 'r') as f:
		for d in f.readlines():
			if d.startswith('#'):
				loc = d.split('#')[1]
				config[d.split('#')[1]][]
			if  d.startswith('https://vk.com/'):
				config[loc]append(d)
			elif d.startswith('https://t.me/'):
				config[loc] = append(d)

if  __name__ == '__main__':
	parse()