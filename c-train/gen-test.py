#!/usr/bin/python

from pyfann import fann

def value_fourtet(s):
	a="abcdefghijklmnopqrstuvwxyz"
	input=[]
	for l in s:
		i=a.index(l)
		for h in range(0,len(a)):
			if h==i:
				input.append(1)
			else:
				input.append(0)
	h=0
	for l in input:
		print "input["+str(h)+"]="+str(l)+";"
		h=h+1

value_fourtet("wel")
value_fourtet("bbh")
