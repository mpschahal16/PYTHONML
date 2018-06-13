# example of multiple inheritence


class Parent1:

    def __init__(self):
        print("Default 1")
    def Parent1function(self):
        print("Parent 1")


class Parent2:
    def __init__(self):
        print("Default 2")

    def Parent2function(self):
        print("Parent 2")


class Child1(Parent1,Parent2):    #inhereting parent1 and parent2
    def Childfunction(self, varx):
        print("Child1 :", varx)

class Child2(Parent2,Parent1):    #inhereting parent2 and parent1
    def Childfunction(self, varx):
        print("Child1 :", varx)


object = Child1()  # creating object of child class
object.Parent1function()
object.Parent2function()

### Note : when we inherit properties from more then one class and we call the default construter by super.__init__()
# then the condtructer of first inheritred parent in the child class is called


#  example


object1=Child1()     #this will call default constructer of Parent2 coz parent2 in given as 1st input in Child1
object2=Child2()    #this will call default constructer of Parent2 coz parent2 in given as 1st input in Child2







'''
in this program child class is inheriting properties from parent1 and parent2 class,and we are able to access
the functions of parent1 and parent2 class with the instance of child class
'''



