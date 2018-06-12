x=(1,2,3,4)
a=frozenset(x)  ##forzen set means non modifiable set

y=(2,5,5)
b=frozenset(y)

z=(5,6,7)
c=frozenset(z)

print(a)

print(a.isdisjoint(b))
print(a.isdisjoint(c))


'''
o/p

frozenset({1, 2, 3, 4})
False
True
'''