class Fruits:
    Fruits_name=['Banana','Apple','Mango','Gwava']

class Mango(Fruits):
    # base class // parent class
    mango='Milkshek'
    def printDetail(self):
        # derived class // chiled class
        print('Chiled class',self.mango)
        print('Parent class ',self.Fruits_name)

obj=Mango()
obj.printDetail()



print()



class Vehicle:
    def __init__(self,maxspeed,color):
        self.maxspeed=maxspeed
        self.color=color
class Car(Vehicle):
    def __init__(self,maxspeed,color,gear,isConvertable):
        super().__init__(maxspeed,color)
        self.gear=gear
        self.isConvertable=isConvertable

    def printDetail(self):
        print('Color: ',self.color)
        print('MaxSpeed: ',self.maxspeed)
        print('Gears: ',self.gear)
        print('isConvertable: ',self.isConvertable)


C1=Car(300,'Red',6,False)
C1.printDetail()
