class Student:
    def __init__(self,name,age):
        self.name = 'rohan'
        self.age = 202

    def print_student_details(self):
        print(self.name, end= " ")
        print(self.age)

s = Student("saif",20)
s.print_student_details() # rohan 202
