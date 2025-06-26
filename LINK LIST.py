class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkList:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head == None:
            print("the linklist is empty")
        else:
            n = self.head
            while n!= None:
                print(n.data)
                n = n.ref
node = Node()
print(node)

LL1 = LinkList()
LL1.print_LL()



