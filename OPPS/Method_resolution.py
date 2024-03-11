class Mother:
    def __init__(self):
        self.name='Manju'
        super().__init__()

    def print(self):
        print("Print of mother called")

class Father:
    def __init__(self):
        self.name='Ajay'
        super().__init__()

    def print(self):
        print('print of father called')

class Child(Mother,Father):

    def __init__(self):
        super().__init__()

    def print(self):
        print('Parent name is',self.name)

C=Child()
C.print()