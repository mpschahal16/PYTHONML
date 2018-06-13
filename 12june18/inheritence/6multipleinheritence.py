class Aone:
    def __init__(self):
        print("Add")
    def add(self):
        print("First")

class Bone():
    def __init__(self):
        print("Second")
    def show(self,name):
        print("Welcome",name)

class cone(Aone,Bone):
    def __init__(self):
        print("THIRD")
        super().__init__()    ###will call the default constructer of Aone mean first input

    def display(self):
        print("hi")

class cone2(Bone,Aone):
    def __init__(self):
        print("THIRD")
        super().__init__() ###will call the default constructer of Bone mean first input

    def display(self):
        print("hi")

object=cone()
ob=cone2()


object.add()
object.show("MANPREET")
object.display()



'''
o/p

THIRD
Add
THIRD
Second
First
Welcome MANPREET
hi

'''