#we don't need to define default __init__() constructer unless their is a need

class aaa:
    def addO(self,x,y):
        c=x+y
        print("Total :",c)


obj=aaa()
obj.addO(26,56)