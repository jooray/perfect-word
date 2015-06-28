#!/usr/bin/python
import pickle
import random

wordlength = 3

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

def random_fourtets(g):
	a="abcdefghijklmnopqrstuvwxyz"
	l=len(g)/5
	for i in range(0,l):
		s=''
		while len(s)<wordlength or g.has_key(s):
			if len(s) == wordlength:
				s=''
			s = s + a[random.randrange(0,len(a))]
		g[s]=0
		
	
	
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

def print_for_training(g):
	a="abcdefghijklmnopqrstuvwxyz"

	print str(len(g))+" "+str(26*wordlength)+" 1"

	for w in g.keys():
		s=''
		for c in w:
			p=a.index(c)
			for i in range(0,26):
				if p==i:
					s=s+"1 "
				else:
					s=s+"0 "
		print s.strip()
		print g[w]

		
g={}
process_text("data/words.txt",g)

normalize(g,2)
random_fourtets(g)

f=file('structs/fourtets.dmp','w')
pickle.dump(g,f,1)
f.close()

print_for_training(g)
