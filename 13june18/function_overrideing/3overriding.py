class FIrst:
    def __init__(self):
        print("Good")

    def calc(self,amt):
        x=amt*30//100
        print(x)

class Second(FIrst):
    def add(self,x,y):
        print(x+y)
    def calc(self,amt):
        x=amt*40//100
        print("Output :",x)

ob=Second()
ob.add(23,55)
ob.calc(1000)