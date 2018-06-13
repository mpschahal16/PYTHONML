#example of multilevel inheritence


class GrandParent:    ###super parent class
    def Grandparentfunction(self):
        print("Grand_Parent")



class Parent(GrandParent): #class inheriting from Grand parent (super parent class)
    def Parentfunction(self):
        print("Parent")


class Child(Parent):    ##class inheriting from parent
    def Childfunction(self):
        print("CHILD")




object=Child()              #creating object of child class
object.Childfunction()           ##acessesing function of parent class with the instance of child class
object.Parentfunction()
object.Grandparentfunction()        ##acessesing function of superparent class with the instance of child class



'''
in this program child class is inheriting properties from parent class and parent
e class is inheriting properties from superparent(grandparent) and we are able to access
the functions of parent and super parent class with the instance of child class
'''



