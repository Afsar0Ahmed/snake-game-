class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self,data):
        if self.key is None:
            self.key = data
        elif self.key<data:
            self.lchild = insert(self.lchild,data)
        else:
            self.rchild = insert(self.rchild,data)





