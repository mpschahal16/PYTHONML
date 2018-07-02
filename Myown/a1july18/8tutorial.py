#Type casting or type coersion converion of data type to one another


#conversion to int

print('Coversion to int')
print(int(120.123))#120

#x=int(10+20j)
#print(x)#error

print(int(True)) #1
print(int(False))#0


print(int('10'))  #10
#print(int('10.5')) error




#conversion to float

print('\n\nCoversion to float')

print(float(10))#10.0
#print(float(10+5j))  error
print(float(True))  #1.0
print(float(False))  #0.0
print(float('10')) #10.0
print(float('10.5'))#10.5
#print(float('ten'))  error
#print(float('0b1111'))  error
print(float(0b1111)) #15.0



#conversion to complex

print('\n\nCoversion to complex')

print(complex(1))#10+20j
print(complex(2,2))#(2+2j)
print(complex(2.2,0.0))#(2.2+0j)
print(complex(True)) #1+0J
print(complex(False)) #0+0J or 0j
x=complex('10')
print(x)#(10+2j)
print(complex(True,False))#(1+0J)




#to bool
print('\n\nCoversion to bool')

print(bool(0))  #false
print(bool(1))  #True
print(bool(56),bool(-25)) #True,True
print(bool(0.000))  #False
print(bool(0.1))  #True
print(bool(0.01))#True
print(bool(1+0j))  #True
print(bool(0+0j))  #False
print(bool(''))  #False
print(bool('mps'))#True
print(bool(' ')) #True


#conversion to string

print('\n\nCoversion to string')

print(str(10.2))  #10.2
print(str(10+20j))  #(10+20j)
print(str(10+20))  #30



#all fundamental data type is immutable



