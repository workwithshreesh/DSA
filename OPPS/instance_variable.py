class Employee:

    def printDetail(self):
        print(f"Name is {self.name} and Id is {self.id}")
        print(f"Work as {self.manager}")

s1=Employee()
a=s1.name='shreesh'
s1.id=2006
s1.manager='manager'
s1.printDetail()