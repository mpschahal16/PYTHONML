a=(10,20,30,40,50)
b=(1,2,3,4,5)
print("Tuple a is =",a)
print("Tuple b is =",b)
c=a+b
print("Tuple c is =",c)
d=a*2
print("Tuple d is =",d)
print(a[2:])
print(b[:3])
print(10 in a)
print(56 in a)
print(10 not in b)
print(a[2])

##no deletion is allowed


###del a[3]


print(max(a))
print(min(a))


#enumaration is suppoted

print(tuple(enumerate(a)))


