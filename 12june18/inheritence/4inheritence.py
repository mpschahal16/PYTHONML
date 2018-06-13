class Base:    ##parent class
    def __init__(self):
        print("Base")
    def hello(self):
        print("WELCOME")

class Child(Base):
    def __init__(self):
        print("Child")
        super().__init__()#####this is to call construcrter of Base class or parent class
        #only upto one level

    def welcome(self):
        print("hello")

ob=Child()
ob.hello()
ob.welcome()




'''
O/P

Child
Base
WELCOME
hello
'''