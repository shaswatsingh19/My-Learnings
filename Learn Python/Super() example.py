class Mammal:
    def __init__(self,mammal):
        print(mammal,"is a warm blooded")


class Dog(Mammal):
    def __init__(self):
        print("DOGS Are trustworthy")
        super().__init__('Dog')
        #both are same
        Mammal.__init__(self,'Dog')

        
