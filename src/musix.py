#!/usr/bin/python3
#Author: danielchc

import math,getopt,sys,random
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def getKey(videoid):
	key=""
	for n in range (len(videoid)):
		preset=""
		for t in range(random.randrange(1,4)):
			preset+=alphabet[int(math.floor(random.random()* len(alphabet)))]
		key+=str(ord(videoid[n])+ 13) + preset
	return key

if (len(sys.argv[1:])==1) and (len(sys.argv[1])==11):
	print("https://extension.musixmatch.com/?res={0}".format(getKey(sys.argv[1])))
else:
	print('Get lyrics from Youtube Video via MusiXmatch')
	print('musix.py <videoid>')
	quit(0)
