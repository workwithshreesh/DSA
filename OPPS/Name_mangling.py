class Fruits:

    __name=['Mango','Banana','Graps']
    myname='shreesh'
    _mystr='krish'

    def printDetail(self):
        print(self.__name)

class Mango(Fruits):
    def printDet(self):
        # print(self.__name)
        print(self.myname)
        print(self._mystr)

s=Mango()
s.printDet()

s1=Fruits()
s1.printDetail()
# s1._mystr=8
print(s1._mystr)
# s._Fruits__name=0
print(s._Fruits__name)  #Name Mangling