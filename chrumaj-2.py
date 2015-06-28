#!/usr/bin/python
import pickle
import random

wordlength = 4

def process_word(w,g):
	w=w.lower()
	for i in range(0,len(w)-(wordlength-1)):
		chunk=w[i:i+wordlength]
		if g.has_key(chunk) and g[chunk]:
			g[chunk]+=1
		else:
			g[chunk]=1

def process_text(filename,g):
	f=open(filename,"r")
	for s in f.readlines():
		s=s.strip()
		s=s.split()
		for w in s:
			if len(w)>=wordlength:
				process_word(w,g)


def normalize(g,l):
	m=0
	h=[]
	for k in g.keys():
		if g[k]<l:
			del g[k]
		else:
			h.append(g[k])
			#if g[k]>m:
			#	m=g[k]

	h.sort()

	# spocitajme median
	m=h[len(h)/2]

	for k in g.keys():
		g[k]=(float(g[k])/m)
		if g[k]>1:
			g[k]=1
		#g[k]=(float(g[k])/(m)) + 0.75
		#g[k]=1

def print_for_ruby(g):
	for w in g.keys():
		print "'"+w+"',"+str(g[w])+","

g={}
process_text("data/words.txt",g)

normalize(g,2)

print "fourtets = ["
print_for_ruby(g)
print "]"
