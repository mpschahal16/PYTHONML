class A:
    def __init__(self):
        print("A")
class B:
    def __init__(self):
        print("B")

class C:
    def __init__(self):
        print("C")

class D(A,B,C):
    def __init__(self):

        print("D")
