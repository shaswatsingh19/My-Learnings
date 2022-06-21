import math
class Fraction:
    def __init__(self,num,den):
        self.num = num
        self.den = den
    
    def plus(self,f):
        numerator = f.den*self.num + f.num*self.den
        denominator = self.den * f.den
        
        self.num = numerator
        self.den = denominator
    
    def multiply(self,f):
        numerator = self.num * f.num
        denominator = self.den * f.den
        
        self.num = numerator
        self.den = denominator
    
    def simplify(self):
        numerator = self.num
        denominator = self.den
        g  = math.gcd(numerator,denominator)
        
        self.num = self.num // g
        self.den = self.den // g
        
        
    def print(self):
        print(str(self.num)+"/"+str(self.den))


fir_num,fir_den = map(int,input().split())
f1 = Fraction(fir_num,fir_den)
t = int(input())
while t:
    q,sec_num ,sec_den = map(int,input().split())
    f2 = Fraction(sec_num,sec_den)
    if(q==1):
        f1.plus(f2)
    else:
        f1.multiply(f2)
    f1.simplify()
    f1.print()
    t-=1









