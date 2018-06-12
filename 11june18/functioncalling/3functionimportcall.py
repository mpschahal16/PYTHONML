from functioncall import add
x=add(56,58,655,588)
print(x)

print()   ##extra print
print()

#x=add0(56,96)  will not work because we have imoported apecific function i.e add only

from functioncall import*
x=add(56,58,655,588)
print(x)


x=add0(56,96)   ##will work becasuse we have imported all the function with *
print(x)

'''
o/p
1357


1357
152

'''