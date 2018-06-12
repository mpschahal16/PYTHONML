a={1,2,3,4,5,6,7}
b={5,6,7,8,9,10,11}

#union
print(a|b)
print(a.union(b))

#intersection
print(a&b)
print(a.intersection(b))

print(a.difference(b))   #a-b
print(a-b)
print(b.difference(a))   #b-a
print(b-a)



#symmetric difference

print(a.symmetric_difference(b))   #those element will be removed which are present in both


'''
o/p

{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
{5, 6, 7}
{5, 6, 7}
{1, 2, 3, 4}
{1, 2, 3, 4}
{8, 9, 10, 11}
{8, 9, 10, 11}
{1, 2, 3, 4, 8, 9, 10, 11}
'''

