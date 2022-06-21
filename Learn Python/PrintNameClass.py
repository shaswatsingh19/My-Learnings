class Person:
    def __init__(self):
        
        self.name = ""
        self.age = ""
        
    def setValue(self,name,age):
        self.name = name
        self.age = age
        
    def getValue(self):
        ans = 'The name of the person is '+self.name+' and the age is '+str(self.age)+"."
        return ans

    
    
name = input()
age = int(input())
obj = Person()
obj.setValue(name,age)
print(obj.getValue())

