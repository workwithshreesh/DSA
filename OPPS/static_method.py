class Student:

    student_grade='A+'

    def __init__(self,name,RollNo):
        self.aname=name
        self.aRollNo=RollNo

    # In static decoretar wee dont required to put self within it. like normal Function
    @staticmethod
    def static_method(aname,aRollNo):
        print(f"My name is {aname} and Roll Number is {aRollNo}")

    @staticmethod
    def sec_static_method():
        print("Hello wellcome to school")

    def normal_func(self):
        print(f"My name is {self.aname} and Roll Number is {self.aRollNo}")


s1=Student('Shreesh',200701)
s1.static_method('Shreesh',200701)
s1.sec_static_method()
s2=Student('Harish',400703)
s2.normal_func()
s2.Student_grade('O')
print(Student.student_grade)