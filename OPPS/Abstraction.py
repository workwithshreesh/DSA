# 1. Object abstract class cannot be created
# 2. Implemented all the abstract method in the chiled class

from abc import ABC,abstractmethod

class Automobile(ABC):

     def __init__(self):
         print("Automobile Created!")

     @abstractmethod
     def start(self):
         print("Start of Automobile called")
     @abstractmethod
     def stop(self):
         pass
     @abstractmethod
     def drive(self):
         pass

class Car(Automobile):

    def __init__(self,name):
        print('Car created')
        self.name=name

    def start(self):
        super().start()
        print('Start of car called')
        pass

    def stop(self):
        pass

    def drive(self):
        pass
class Buss(Automobile):
   def start(self):
       pass
   def stop(self):
       pass
   def drive(self):
       pass

# class Truck(Automobile): Error because abstract method not implemented
#     def __init__(self):
#         print("Truck is created")

c=Car('Honda')
b=Buss()
# d=Truck()
c.start()