##INHERITENCE SINGLE LEVEL




class Parent1:    #base class
    def __init__(self):
        self.parentvar=10

    def parentfunction(self,varx):  #baseclass function
        print("Parent1 :",varx)



class Child1(Parent1):    #child class
    def __init__(self):
        self.childvar=10


    def childfunction(self,vary):  #child class function
        print("child :",vary)





child1obj=Child1()    #creating instance of child class
child1obj.childfunction(10)       ##acessesing function of child class with the instance of child class
child1obj.parentfunction(25)        ##acessesing function of parent class with the instance of child class  (single level inheritece)
