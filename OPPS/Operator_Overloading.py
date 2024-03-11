import math
class Point:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def __str__(self):
        return 'This point is at (' + str(self.__x) +','+str(self.__y) +')'

    def __add__(self,point_obj):
        return Point(self.__x+point_obj.__x,self.__y+point_obj.__y)

    def __lt__(self,point_obj):
        return math.sqrt(self.__x**2 + self.__y**2) < math.sqrt(point_obj.__x**2 + point_obj.__y**2)

P1=Point(1,2)
P2=Point(3,4)
print(P1+P2)
print(P1<P2)
