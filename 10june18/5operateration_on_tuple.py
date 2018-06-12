c=(56,658,65,68)
a=(56,95,56,"hello")
b=(56,95,96,"hjf","world")
print(a+b)
#print(a-b) not working
print(3*c)
print((a+b).__len__())  #length of a+b tuple
print(max(c))
print(min(c))
st=("manpreet","singh","chahal")
print(st)
print(st.__sizeof__())
print(b.__sizeof__())


'''
o/p
(56, 95, 56, 'hello', 56, 95, 96, 'hjf', 'world')
(56, 658, 65, 68, 56, 658, 65, 68, 56, 658, 65, 68)
9
658
56
('manpreet', 'singh', 'chahal')
48
64

'''