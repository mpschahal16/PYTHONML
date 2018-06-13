## example of function overloading

class Abc:
    def __init__(self,x,y):    #default constructer with two input variablea x and y
        self.x=x                # assigning value in instance variable
        self.y=y                # assigning value in instance variable


    def __str__(self):            #built in __str__
        return "({0},{1})".format(self.x,self.y)  #changing the functinality of build in function




    def __add__(self, other):      #built in add function
        x=self.x+other.x            #changing the functinality of build in function
        y=self.y+other.y
        return(x,y)




obj=Abc(23,24)   ##calling default constructer of overloading functions
obj1=Abc(2,3)       ##calling default constructer of overloading functions

print(obj)
print(obj1)
print(obj+obj1)    ## overloading add operater