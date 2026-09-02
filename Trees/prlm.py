#trees
#general tree  can have any number  of children

#Binary Tree:can have atmost 2 children
class Node:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

root = Node(10)

root.left = Node(20)
root.right = Node(30)

print(root.data)
print(root.left.data)
print(root.right.data)

#preorder traversal    
#-->>root-->left-->right

class Node:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None
        
def preorder(node,res):
    if not node:
        return
    res.append(node.data) #root

    preorder(node.left,res)

    preorder(node.right,res)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(6)

res = []

preorder(root, res)
print(*res)

#inorder traversal
#left-->root-->right
class Node:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None
        
def inorder(node,res):
    if not node:
        return
    inorder(node.left,res)
    
    res.append(node.data) #root

    inorder(node.right,res)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(6)

res = []

inorder(root, res)
print(*res)

#postorder
#-->left-->right-->root
class Node:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None
        
def postorder(node,res):
    if not node:
        return
    postorder(node.left,res)

    postorder(node.right,res)
    
    res.append(node.data) #root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(6)

res = []

postorder(root, res)
print(*res)
