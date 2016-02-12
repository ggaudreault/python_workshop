#!/usr/bin/python
from functools import partial

world_ext = ["c1", "c2", "c3", "c4", "d1", "d2", "d3", "d4", "john", "mary", "paul"]

love_ext = [("john", "agnes"), ("c1", "agnes"), ()]

love = lambda x,y: (x,y) in love_ext
love2 = lambda y: (lambda x: (x,y) in love_ext)

print love("john", "agnes")
print love2("john") ("agnes")

part_love = partial(love, "john")

print part_love("agnes")


cat_ext = ["c1", "c2", "c3"]
black_ext = ["c1", "c3", "d3", "d5"]

cat = lambda x: x in cat_ext
black = lambda P, x: (x in black_ext) and (P(x))
black2 = lambda P: (lambda x: (x in black_ext) and (P(x)))
#some = lambda P, Q: [x for x in P if x in Q]
some = lambda P, Q: [x for x in world_ext if Q(x) and P(x)]
some2 = lambda P:(lambda Q: [x for x in world_ext if Q(x) and P(x)])

#print some(["a", "b"], ["b", "c"])
print some2(cat) (love2("agnes"))

#print black(cat)
print some(cat, partial(love,"agnes"))
#print some(black(cat), partial(love, "agnes"))
print some(cat, (lambda x:love(x,"agnes")))
