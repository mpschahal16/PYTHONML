'''
33 reserved words

True,False,None
and,or,not,is
if,else,elif
while,for,break,continue,return,in,yield
try,except,finally,raise,assert
import, from,as,class,def,pass,global,nonlocal,del,with
'''


import keyword
print(keyword.kwlist)

'''
o/p
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''




# ways to represent int value


a=54

print(id(a))




b=0b1111
c=0B001  #binary no

print(b,c)



a=0o777    #octal no
b=0O777
print(a,b)



a=0xBef  #hexadecimle
print(a)