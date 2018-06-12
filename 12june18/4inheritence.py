class Base:
    def __init__(self):
        print("Base")
    def hello(self):
        print("WELCOME")


class Child(Base):
    def __init__(self):
        print("Child")
        #applying multilevel inheritence
        super().__init__()

    def welcome(self):
        print("hello")

ob=Child()
ob.hello()
ob.welcome()