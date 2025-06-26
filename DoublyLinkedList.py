class Node:
    def __init__(self,data):
        self.data   = data
        self.nref = None
        self.pref = None
class DoublyLL:
    def __init__(self):
        self.head = None
    def print_LL(self):
        n = self.head
        if n==None:
            print("the linked list is empty")
        else:
            while n is not None:
                print(n.data)
                n = n.ref
    def reverse_LL(self):
        n = self.head
        if n==None:
            print("the linked list is empty")
        else:
            while n.ref is not None:
                n = n.ref
            while n is not None:
                print(n.data)





ll1  = Node(10)
ll1  =DoublyLL()
ll1.print_LL()



