class Alone:
    def add(self):
        print("FIrst")
    def __init__(self):
        print("ADD")
class Bone(Alone):
    def __init__(self):
        print("SeCOND")

    def show(self,name):
        print("WELCOME",name)

class cone(Alone,Bone):
    def __init__(self):
        print("THIRD")
        super().__init__()

    def display(self):
        print("hi")

object=cone()
object.add()
object.show("MANPREET")
object.display()