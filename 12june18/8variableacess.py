class A:
    def __init__(self,x,y,z):
        self.publicX=x    ##accessible everywhere
        self._protctedY=y
        self.__privateZ=z  # only accessible within the scopr
        print("Private variable inside __init__:",self.__privateZ)

    def add(self):
        print("Public variable inside add:",self.publicX)
        #self.__privateZ+=1   #private variable can't be access coz they don't lie in scope
        #print(self.__privateZ)

ob=A(10,20,30)
print(ob.publicX)
print(ob._protctedY)   #protected variable are those variable which have acess outside the class in whic they are present
ob.add()
#print(ob.__privateZ)