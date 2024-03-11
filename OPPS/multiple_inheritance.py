# Example
class Base1:
    pass
class Base2:
    pass
class Derivedclass(Base1,Base2):
    pass


class Mother:
    def print(self):
        print("Print of mother called")

class Father:
    def print(self):
        print("Print of father called")

class Chiled(Father,Mother):
    def __init__(self,name):
        self.name=name

    def printChiled(self):
        print("Name of chiled is",self.name)

c=Chiled("Suraj")
c.printChiled()
c.print()  #--> It will depend on order which you will given to chiled(father,mother)