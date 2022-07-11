#collections-counter

import collections
from collections import Counter


#containers
#list
#set
#dict
#tuple- inmuttable
#Types
#1 counter <- this video
#2 deque
#3 namedTuple()
#4 orderDict
#5 defaultdict 


a = Counter('gallad')
print(a)
print(a.most_common(3))
b = Counter(['a','a','c','c'])
print(b)
print(b.most_common(2))
c = Counter(cats=4,dogs=7)
print(c.most_common(2))

print(list(c.elements()))
d = Counter({'cat': 2})
print(c['pet'])
print(d['pet'])

f = Counter(a=4,b=7,c=6,d=-2)
g  = ('a','b','b','c')
f.subtract(g)
print(f)
f.update(g)
print(f)

