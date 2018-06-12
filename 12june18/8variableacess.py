class A:
    def __init__(self,x,y,z):
        self.publicX=x
        self._protctedY=y
        self.__privateZ=z

        def add(self):
            self.__privateZ+=1
            print(self.__privateZ)

ob=A(10,20,30)
print(ob.publicX)
print(ob._protctedY)
'''ob.add()
print(ob.__privateZ)'''