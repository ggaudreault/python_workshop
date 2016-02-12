#!/usr/bin/python

def i_change(a):
	a.append(["bob"])
	print a
	return

me = ["judy", "emma"]
print me
i_change(me)
print me
