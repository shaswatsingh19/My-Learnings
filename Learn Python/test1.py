class Student:
    
    def __init__(self,name):
        self._name = name
        
class Student1(Student):
    def __init__(self,name):
        super().__init__(name)

s = Student1("saif")
print(s._name)
