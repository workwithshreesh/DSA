# Every class provide three method
# __init__
# __str__
# __new__

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def __str__(self):
        return 'These is a circle class that take argument as an radius'

C1=Circle(3)
print(C1)
