class Alone:
    def __init__(self):
        print("Add")
    def add(self):
        print("First")
class Bone(Alone):
    def __init__(self):
        print("Second")
        super().__init__()

    def show(self,name):
        print("Welcome",name)

class cone(Bone):
    def __init__(self):
        print("Third")
        super().__init__()

    def display(self):
        print("hi")

object=cone()   ##this will call all the deafult construrcter of all base class in sequence from bottom to top coz all default constructer are
# are calling super.__init__() of thier base class


object.add() #will call add function
object.show("MANPREET")
object.display()


'''
o/p

Third
Second
Add
First
Welcome MANPREET
hi

'''