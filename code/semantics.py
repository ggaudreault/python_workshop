#!/usr/bin/python
#from functools import partial

world_ext = ["c1", "c2", "c3", "c4", "d1", "d2", "d3", "d4", "john", "mary", "paul"]
love_ext = [("john", "agnes"), ("c1", "agnes"), ()]
cat_ext = ["c1", "c2", "c3"]
black_ext = ["c1", "c3", "d3", "d5"]
dance_ext = ["c1", "c2", "c3", "c4", "d1", "d2", "john", "mary", "paul"]

love = lambda y: (lambda x: (x,y) in love_ext)
dance = lambda x: x in dance_ext
cat = lambda x: x in cat_ext
black = lambda P: (lambda x: (x in black_ext) and (P(x)))
some = lambda P:(lambda Q: [x for x in world_ext if Q(x) and P(x)])


print love("john") ("agnes")
print love("john")
print dance("john")
print some(cat) (dance)
print some(cat) (love("agnes"))
print black(cat)

print some(black(cat))(love("agnes"))