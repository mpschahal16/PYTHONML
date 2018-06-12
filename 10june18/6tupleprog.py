a=(10,20,30,40,50)
b=(1,2,3,4,5)
print("Tuple a is =",a)
print("Tuple b is =",b)
c=a+b    ##two tupple combined
print("Tuple c is =",c)
d=a*2
print("Tuple d is =",d)
print(a[2:])
print(b[:3])
print(10 in a)    # x in a      returns true if x is present in a else return false
print(56 in a)
print(10 not in b)      # x not in a      returns true if x is not present in a else return false
print(a[2])

##no deletion is allowed


###del a[3]


print(max(a))
print(min(a))


#enumaration is suppoted

print(tuple(enumerate(a)))       #will from list of tuple item index and tuple item


'''
o/p

Tuple a is = (10, 20, 30, 40, 50)
Tuple b is = (1, 2, 3, 4, 5)
Tuple c is = (10, 20, 30, 40, 50, 1, 2, 3, 4, 5)
Tuple d is = (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
(30, 40, 50)
(1, 2, 3)
True
False
True
30
50
10
((0, 10), (1, 20), (2, 30), (3, 40), (4, 50))

'''
