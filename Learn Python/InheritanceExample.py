class Polygon:
    def __init__(self,no_of_sides):
        self.n = no_of_sides
        self.sides = [ 0 for i in range(self.n)]

    def inputSides(self):
        # taking user input for sides
        for i in range(self.n):
            self.sides[i]  = int(input("Enter Side: "))
       # self.sides = [int(input()) for i in range(self.n)]

    def displaySides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

            
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a,b,c = self.sides
        s = (a+b+c)/2
        area = (s* (s+a)*(s+b)*(s+c))** 0.5
        print("The area of Triangle is",area)

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)

    def findArea(self):
        l,b = self.sides
        
        area = l*b
        print("The area of Triangle is",area)
