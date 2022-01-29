class A:
    def test1(self):
        print(" method named test1 of A called ")

class B(A):

    def test1(self):
        print(" method named test1 of B called ")

class C(A):

    def test1(self):
        print(" method named test1 of C called ")

class D(B,C):

    def test2(self):
        print(" method named test2 of D called ")        


object1=D()
object1.test1()


