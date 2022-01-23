class Student:
    name = “Parikh”

    def store_details(self):
        self.age = 60
    def print_age(self):
        print(self.age) 

s = Student()
s.store_details()
s1 = Student()
s1.print_age()

# AttributeError
# In the above code snippet object s1 has no attribute age.

