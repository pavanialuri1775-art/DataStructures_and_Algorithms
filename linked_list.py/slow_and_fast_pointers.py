#
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
def middleNode(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
result = middleNode(n1)
print(result.val)

#Cycle detection
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.next=n3
n3.next=n3
def hasCycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
res=hasCycle(n1)
print(res)
