class Abc:
    staticX=10
    def __init__(self,x):
       self.x1=10

    def add(self):
        Abc.staticX+1
        self.x1+=1
        #x+=1  this will give error coz declared outside the scope
        print("Static variable :",Abc.staticX)
        print("Instance VAriable:",self.x1)


obj1 = Abc(23)
#print(obj1.x)
print(obj1.x1)
obj1.add()
obj2=Abc(23)
obj2.add()