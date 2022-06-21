class A:    
    def __init__(self):
        print('init of A called') 
class B:
    def __init__(self):
        print('init of B called')

class C(B,A):
    def __init__(self):
        super().__init__()

c = C()
