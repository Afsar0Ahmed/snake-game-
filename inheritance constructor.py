 class A: #its aparents class or super class
    def __init__(self):
        print("is a busy ady")

    def pogram1(self):
        print("the first pogramma ")
    def pogram2(self):
        print("the secon programming")

class B(A):#its a child class of super class

    def __init__(self):#its constaractor its call automatically
        super().__init__()
        print("its a free day")

    def pogramm3(self):
        print("teh third pogramm")
    def pogramm(self):
        print("the 4th pogrammin gis running")

a1 = B()