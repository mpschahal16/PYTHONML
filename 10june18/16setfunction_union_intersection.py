a={1,2,3,4,5,6,7}
b={5,6,7,8,9,10,11}
print(a|b)
print(a.union(b))
print(a&b)
print(a.intersection(b))
print(a.difference(b))   #a-b
print(a-b)
print(b.difference(a))   #b-a
print(b-a)



#symmetric difference

print(a.symmetric_difference(b))   #those element will be removed which are present in both


