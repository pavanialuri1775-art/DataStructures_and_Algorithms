#AVL Tree
#An AVL tree is a self-balancing Binary Search Tree (BST).
#Balance Factor = Height of left subtree − Height of right subtree
#For an AVL tree, the balance factor of every node must be:
#-1, 0, or +1
#AVL Rotations
#Right Rotation
#Left Rotation
#Left+Right Rotation
#Right + Left Rotation

#AVL Tree 
#Step 1 — AVL Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1#AVL needs to know the height of subtrees so it can calculate the balance factor.

#Step 2 — BST Insertion
def insert(root,value):
    if root is None:
        return Node(value)
    
    if value<root.data:
        root.left=insert(root.left,value)
    
    else:
        root.right=insert(root.right,value)
    
    return root

#Step 3: Height Calculation
def height(node):
    if node is None:
        return 0

    return node.height# root.height=1+max(height(root.left),height(root.right))

#Step 4: Balance Factor
def get_balance(root):
    if root is None:
        return 0

    return height(root.left) - height(root.right)

#Step 5: Right Rotation — LL Case
