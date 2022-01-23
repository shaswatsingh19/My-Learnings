class Rectangle:
    def __init__(self):
        # here length and breadth are data member
        self.length = 0
        self.breadth = 0
        
    def getArea(self):
        # here getArea are  member function
        area = self.length * self.breadth
        return area


R = Rectangle()
R.length = 12
R.breadth = 2
print(R.getArea())
