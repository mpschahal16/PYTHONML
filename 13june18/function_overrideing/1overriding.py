#user defined function overriding is not allowed
#last function will be called if we use more then one function of same name in same class according to python

class Abc:
    def add(self):
        print("1")
    def add(self,x):
        print("2")
ob=Abc()
#ob.add()
#  this will give error coz in python in funtion overriding, last defined function overwrite all other previous defined function
ob.add(12)