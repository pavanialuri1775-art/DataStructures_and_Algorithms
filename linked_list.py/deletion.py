#Deletion in Linked List
#Delete from the Beginning
def deleteAtBeginning(head):
    head = head.next
    return head

#Delete at the End
def deleteAtEnd(head):
    current=head
    while current.next.next is not None:
        current=current.next
    current.next=None
    return head

#Delete at a specific position
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
def deleteAtPosition(head, pos):
    current = head
    for i in range(pos - 1):
        current = current.next
    current.next = current.next.next
    return head
head=deleteAtPosition(n1,2)
current=head
while current is not None:
    print(current.val)
    current=current.next
    
#
def deleteAtPosition(head, pos):
    if pos == 0:
        return head.next
    current = head
    for i in range(pos - 1):
        current = current.next
    current.next = current.next.next
    return head
