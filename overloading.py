class A:
    def show(self):
        print("A is show")
class B(A):
    pass

a1 = B()
a1.show()