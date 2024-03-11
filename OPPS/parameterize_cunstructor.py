class Books:

    def __init__(self,stream,nameOfBooks):
        self.stream=stream
        self.nameOfBooks=nameOfBooks

    def printDetail(self):
        print("Stream: ",self.stream)
        print("Books List: ",self.nameOfBooks)


obj1=Books('Cs',['DBMS','DSA','Java','C++'])
obj1.printDetail()