class ComplexNumbers:
    
    #create your class here.
    def __init__(self,real,img):
        self.real = real # 4
        self.img = img   # 5
    
    def plus(self,real2,img2):
        self.real = self.real + real2
        self.img = self.img + img2
    
    def multiply(self,real2,img2):
        temp = self.real
        self.real = self.real * real2 + self.img * img2*-1
        self.img = temp*img2 + self.img*real2
        
        
        
    def print(self):
        print(str(self.real)+" + i"+str(self.img))
        
#Driver's code goes here.

a,b = input().split()
c1 = ComplexNumbers(int(a),int(b))
m,n = input().split()
c2 = ComplexNumbers(int(m),int(n)) # 6 7
x = int(input())
if(x==1):
    c1.plus(int(m),int(n))
else:
    c1.multiply(int(m),int(n))

c1.print()
    
    
    
    
    
    
    
    
    
