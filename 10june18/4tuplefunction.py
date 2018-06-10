a=(1,2,[4,5,6],3)
print(a[2][1])
print(a[3])
print(a[2][1])
print(a)
##tuple is not modifiable so none of list moodifying function will work for ex a.del a[5]=new no
print(a[2:])
a[2][1]=56
print(a)
##a[1]=96  ###modifiying does not work
print(a)