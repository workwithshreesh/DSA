class Vehicle:
    def __init__(self,color,maxSpeed):
        self.color=color
        self.__maxSpeed=maxSpeed #Private Var

    def getMaxSpeed(self):
            return self.__maxSpeed
    def setMaxSpeed(self,maxSpeed):
            self.__maxSpeed=maxSpeed

class Car(Vehicle):

    def __init__(self,color,maxSpeed,Gears,isConvertable):
        super().__init__(color,maxSpeed)
        self.Gears=Gears
        self.isConvertable=isConvertable

    def printDetail(self):
        print('Color: ',self.color)
        print('maxSpeed: ',self.getMaxSpeed())
        print('Gears: ', self.Gears)
        print('isConvertable: ', self.isConvertable)


s1=Car('Red',300,6,False)
s1.printDetail()
s2=Vehicle('Red',300)
