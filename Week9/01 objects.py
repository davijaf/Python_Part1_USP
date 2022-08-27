from operator import ne
from sys import orig_argv


a = "banana"
print(a)
b = a
print(b)
c = "maçã"
print(a is b)
print(a is c)

a = [81,82,83]
b = [81,82,83]
print(a is b)
print(a == b)

origlist = [45,76,34,55]
newlist = (origlist * 3)
print([newlist] * 3)
newlist[1] = 99
print([newlist] * 3)