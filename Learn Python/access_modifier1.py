class Student:
    def __init__(self,name,age):
        self.__name = name
        self.age = age

s = Student("Rohan",60)
s.__name
# private member can't be accessed outside the class

#AttributeError: 'Student' object has no attribute '__name'


class Student:
    def __init__(self,name,age):
        self.__name = name
        self.age = age
    def print_student_details(self):
        print(self.__name, end= “ “)
        print(self.age)
s = Student(“Rohan”,20)
s.print_student_details()

# Rohan 20
# now we can access those private as public function are inside class
