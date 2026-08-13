#reversing a linked list
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3    
def reverse(head):
    prev=None
    current=head
    while current is not None:
        next_node =current.next
        current.next=prev
        prev=current
        current=next_node
    head=prev
    return head
head=reverse(n1)
current=head
while current is not None:
    print(current.val)
    current=current.next