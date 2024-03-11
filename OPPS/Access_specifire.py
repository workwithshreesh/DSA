class School:
    def __init__(self,name,rollno):
        self._name=name #Protected changed by derived class! access in class or derived class

        self.__rollno=rollno #Private can't changed by drived class! access in class only
        print('My RollNo is: ',self.__rollno)

    def printDetail(self):
        print('Name=',self._name)
        print('RollNo=',self.__rollno)

class Student(School):
    def __init__(self,name,rollno):
        super().__init__(name,rollno)

    def changeAccess(self):
        self._name='harish' #Changed
        self.__rollno=24 #Not Changed

s1=School('shreesh',206)
s1.printDetail()
s2=Student('Mahesh',100)
s2.printDetail()
s2.changeAccess()
s2.printDetail()
