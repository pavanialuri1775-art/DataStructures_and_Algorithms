#binary search tree
#left side < root < right side--------------

class Node:

    def _init_(self, data):
        self.data =data
        self.left= None
        self.right =None

def insert(root,value):#50,80-70,80-n,80

    if root is None:
        return Node(value)# 80

    if value<root.data:#
        root.left = insert(root.left, value)#n,20

    elif value>root.data:#
        root.right = insert(root.right, value)#n,80

    else:
        print(value, "already existed")

    return root#50



def inorder(root):
    if root is None:
        return

    inorder(root.left)

    print(root.data, end=" ")

    inorder(root.right)

root = None

n = int(input("how many vals do u want to insert"))#7


for i in range(n):#7
    val = int(input("enter val"))#50,30,70,40,60,20,80

    root = insert(root, val)#50,60

print("inorder traversal: ")
inorder(root)

#BST for Preorder
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, value):#50,30,70,40,60,20,80
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)

    elif value > root.data:
        root.right = insert(root.right, value)

    else:
        print(value, "already existed")

    return root


def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)
    
root = None
n = int(input("how many vals do u want to insert: "))
for i in range(n):
    val = int(input("enter val: "))
    root = insert(root, val)

print("preorder traversal:")
preorder(root)