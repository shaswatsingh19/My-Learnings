from sys import stdin

class Car:
    def __init__(self,no_of_gear,color):
        self.n = no_of_gear
        self.c = color

class RaceCar(Car):

    def __init__(self,no_of_gear,color,maxSpeed):
        super().__init__(no_of_gear,color)
        self.m  = maxSpeed
        
    def printInfo(self):
        print("noOfGear:",self.n)
        print("color:",self.c)
        print("maxSpeed:",self.m)



        
#Driver's code

noOfGear = int(stdin.readline().rstrip())
color = stdin.readline().rstrip()
maxSpeed = int(stdin.readline().rstrip())
        
raceCar = RaceCar(noOfGear,color,maxSpeed)
raceCar.printInfo()
