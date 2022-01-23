class Student:
    def store_details(self):
        self.age = 60
        self.name = ‘Parikh’
    def print_details(self):
        print(self.name, end=” ”)
        print(self.age)

s = Student()
s.store_details()
s.print_details()
# Parikh 60
# In the above code snippet when we create the constructor will be called immediately and two instance attributes will be created i.e name and age.


