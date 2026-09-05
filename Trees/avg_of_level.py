#average of each level.
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
from  collections   import  deque
def avg_of_level(root):
    if root is None:
        return []
    q=deque([root])
    res=[]
    while  q:
        level_size=len(q)
        total=0
        for i in range(level_size):
            node=q.popleft()
            total+=node.data
        
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        res.append(total/level_size)   
    return res  
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(6)

print(avg_of_level(root))


    