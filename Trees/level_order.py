#level order====BFS
# level wise -l0,l1,l2---

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


from collections import deque

def levorder(root):#1

    if root is None:
        return

    que = deque([root])#[1]

    while que:#[6]

        node = que.popleft()#6

        print(node.data, end=" ")#6


        if node.left:
            que.append(node.left)#[4,5,6]

        if node.right:
            que.append(node.right)#[4,5,6,6]



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(6)

#res = []

levorder(root)
#print(*res)

#printing array  level by level
from collections import deque

def level_order(root):
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        level_size = len(q)
        level = []

        for i in range(level_size):
            node = q.popleft()

            level.append(node.data)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        res.append(level)

    return res