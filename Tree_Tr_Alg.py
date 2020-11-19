class Node:
    def __init__(self,nodedata):
        self.leftchild = None
        self.rightchild = None
        self.nodedata = nodedata
    
    def PrintTree(self):
        if self.leftchild:
            self.leftchild.PrintTree()
        print(self.nodedata)
        if self.rightchild:
            self.rightchild.PrintTree()


# Creating an instance of the Node class
root = Node(27)
root.leftchild = Node(14)
root.rightchild = Node(35)
root.leftchild.leftchild = Node(10)
root.leftchild.rightchild = Node(19)
root.rightchild.leftchild = Node(31)
root.rightchild.rightchild = Node(42)

# In-Order Tree Traversal:
#    visits the left nodes followed by
#    the root and then right nodes

def inOrder(root):
    if root:
        inOrder(root.leftchild)
        print(root.nodedata)
        inOrder(root.rightchild)

# inOrder(root)

# Pre-Order Tree Traversal:
#    visits the root nodes followed by
#    the left nodes and then right nodes
def preOrder(root):
    if root:
        print(root.nodedata)
        preOrder(root.leftchild)
        preOrder(root.rightchild)
    
# preOrder(root)


# Post-Order Tree Traversal:
#    visits the left nodes followed by
#    the right nodes and then the root nodes
def postOrder(root):
    if root:
        postOrder(root.leftchild)
        postOrder(root.rightchild)
        print(root.nodedata)

# postOrder(root)

root.PrintTree()