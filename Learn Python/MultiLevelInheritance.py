class A:
    
    def __init__(self,name):
        self.name = name
        
class B(A):
    
    def __init__(self,name,age):
        A.__init__(self,name)
        self.age = age
    
class C(B):
    def __init__(self,name,age,rollno):
        B.__init__(self,name,age)
        self.rollno = rollno
        
        
s = C("Sam",9,12)
print(s.name)
print(s.age)
print(s.rollno)
