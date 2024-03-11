# Polymorphism is achived using mathod overriding its also refers different form of things
def printDetail(a,b):
    c=a*b
    print(c)

def printDetail(a,b): #Overrided Method
    c=a+b #overrided Variable
    print(c)

printDetail(2,4)

print()


class Vehicle:
    def __init__(self,maxspeed,color):
        self.maxspeed=maxspeed
        self.color=color

    def printDetail(self):
        print('Color: ', self.color)
        print('MaxSpeed: ', self.maxspeed)

class Car(Vehicle):
    def __init__(self,maxspeed,color,gear,isConvertable):

        super().__init__(maxspeed,color)
        self.gear=gear
        self.isConvertable=isConvertable

    def printDetail(self):
        print('Gears: ',self.gear)
        print('isConvertable: ',self.isConvertable)


C1=Car(300,'Red',6,False)
C1.printDetail()
print()
V1=Vehicle(300,'Red')
V1.printDetail()

