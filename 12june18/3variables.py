class Abc:
    staticX=10      #(staticX )static variable are global variable means value change for whole program
    def __init__(self,x):

       self.x1=10   #(x1) Instance variable : these are accessable every where in the class with self keyword their valued is copied means
       #enery time we self.instancevariable a new copy of that variable is created with initial value
       y=25
       print(x)    ##x and ylocal variable only accessable inside the block where it is declared
       print(y)
       print()  #extra

    def add(self):
        Abc.staticX+=1
        self.x1+=1
        #x+=1  this will give error coz declared outside the scope
        print("Static variable :",Abc.staticX)
        print("Instance VAriable:",self.x1)


#print(y)  y can't be access here coz it is a local variable of default constructer


obj1 = Abc(23)
#print(obj1.x)
print(obj1.x1)
obj1.add()
obj2=Abc(23)
obj2.add()


'''
o/p

23
25

10

Static variable : 11
Instance VAriable: 11
23
25

Static variable : 12
Instance VAriable: 11
'''