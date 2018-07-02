#immutability check

x=10
y=10
print(id(x),"/",id(y))  #same id coz same object is used according to python concept

x=25
print(id(x))    #new object is created for new value that,s why id is
#different from earlier