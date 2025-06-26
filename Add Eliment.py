class Node:
    def __init__(self,data):
        self.data = data
        self.ref  = None
class LinkedList:#Here we created a linked list class
    def __init__(self):
        self.head = None
    def Print_LL(self):
        self.head  = None
        if self.head == None:
            print("its empty")
        else:
             n = self.head
             print(n.data)
             n = n.ref

    def add_begin(self,data):#When you add a node  begining of a linked list
        new_node = Node(data)
        new_node.ref  = self.head
        self.head  = new_node
    def add_end(self,data):#When you add a node end of a linked list
        new_node = Node(data)
        if self.head is None :
            self.haed = new_node
        else:
            n =self.haed
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def add_after(self,data,x):#When you add node between of the linked list basically after the target node
        n  = self.haed
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is not None :
            print("n is emptyty")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def delete_begin(self):#when you deleted the node from the linked list in beagining
        if self.head is None :
            print("the linked list is empty")
        else:
            head  = self.head.ref
    def delete_end(self):#When you delet the node from the linked list in th end
        if self.head is None :
            print("its empty")
        else:
            n= self.head
            while n.ref.ref is not None :
                n = n.ref
            n.ref = None









LL1  = LinkedList()
LL1.delete_end()
LL1.add_begin(10)
LL1.add_begin(20)













