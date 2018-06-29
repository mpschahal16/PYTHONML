#conversion of base of numbers

#To binary

print("\n",bin(15))  #base 10 to base 2
print("\n",bin(0o777))#octal base to base 2
print("\n",bin(0xfff))  #hexadecimal to base 2


'''
similarly 

# hex() is available for hexadecimal conversion
#oct() is available for octal conversion
'''


print("\n",hex(156))



#float data type

f=156.5
print("\n",f)


#f=0x156.665 # not allowed in python




#exponantial form is allowed

f=15.58e3
print("\n",f)



#complex data type

'''
a+bj form

where a is real and b is imaginary

and j^2 is -1

'''


x=3+2j
y=2+5j

print("\n",x+y)

print("\n",x-y)

print("\n",x*y)

print("\n",x/y)


print(type(x))


print("\n",x.real)     # to print the real part

print("\n",x.imag)      #to print thr imaginary part





## boolean data type

a=True
print("\n",a)

print("\n",type(a))



a=25
b=1
c=b>a
print("\n",c)


print("\n",True+True)

#o/p is 2 coz internally in python True is treated as 1 and False 0

print("\n",True+False)





##String data type
'''
any sequence of characters is string
'''


s="MANPREET"

print("\n",type(s))

l='Singh'

print("\n",s+" "+l)

print('\n',s+l)


#for multiline

f=''' MAnpreet
singh'''

print('\n',f)




f='''hello "sir" '''
print('\n',f)


print('\n',f[:3])  #sliceing in string
