class Class:
    def __init__(self,CName,Cno):
        self.CName=CName
        self.Cno=Cno

    def printd(self):
        print(f"My name is {self.CName} is and RollNo is {self.Cno}")

class Student(Class):
    def __init__(self,CNmae,Cno,Name,rollno):
        super().__init__(CNmae,Cno)
        self.Name=Name
        self.rollno=rollno

    def detail(self):
        self.printd() #Call Base class func using self
        super().printd() #Call Base class func using Super() func


S1=Student('CS',344,'Suraj',206)
S1.detail()