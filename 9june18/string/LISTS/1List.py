a=[1,2,3]
print(a)
print(type(a))
print(type(a[1]))

b=['hello' ,'world',1 ,2, 5]
print(b)
print(b[1])
print(b[1][4])

print(b[1:4])

c=a+b
print(c)
print(a.__len__())
print(c.__len__())

c.append(5)
print(c)