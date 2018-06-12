a=(1,2,[4,5,6],3)

print(a[2][1])
print(a[3])
print(a[1:2]) #sub set from index 1 to (2-1)
print(a)
##tuple is not modifiable so none of list moodifying function will work for ex a.del a[5]=new no
print(a[2:])    #sub set from index 2 to last
a[2][1]=56    #access element of inner list 2 present at index 1
print(a)
##a[1]=96  ###this is tuple so modifiying does not work
print(a)


d=(1,2,(56,96,65),[4,5,6],3)
print(d[2][2])


'''
O/P

5
3
(2,)
(1, 2, [4, 5, 6], 3)
([4, 5, 6], 3)
(1, 2, [4, 56, 6], 3)
(1, 2, [4, 56, 6], 3)
65
'''