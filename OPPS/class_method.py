from datetime import date
class Student:
    passingPercentage=40
    def __init__(self,name,age,percentage):
        self.name=name
        self.age=age
        self.percentage=percentage

    def isPass(self):
        if self.percentage>self.passingPercentage:
            print('pass')
        else:
            print('fail')

    def studenDetail(self):
        print('Name is: '+self.name)
        print('Age is: ',self.age)
        print('Percentage is: ',self.percentage)

    @staticmethod
    def isTeen(age):
        return age>16

    @classmethod
    def isDetail(cls,name,year,percentage):
        return cls(name,date.today().year-year,percentage)

s1=Student.isDetail('shreesh',2003,40)
s1.studenDetail()
