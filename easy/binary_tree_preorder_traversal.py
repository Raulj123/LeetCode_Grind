# Binary tree == 2 max childern per node
# Binary search tree == left child is less than root and right chil greater than root
# postorder == vist 'Root', 'Left', 'Right'

class Binary:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

def printTree(node):
    if node is not None:
        print(f"Node Value: {node.val}")
        printTree(node.left)
        printTree(node.right)

def preorder(root):
    res = []
    def pre(root):
        if root == None:
            return 
        res.append(root.val)
        pre(root.left)
        pre(root.right)
    pre(root)
    return res
n1 = Binary(1)
n2 = Binary(2)
n3 = Binary(3)

n1.right = n2
n2.left = n3
printTree(n1)
a = preorder(n1)
print(f"result {a}")



