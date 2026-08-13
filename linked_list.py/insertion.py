#Insertion at beginning
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
def insertAtBeginning(head, value):
    new_node=Node(value)
    new_node.next=head
    head=new_node
    return head
head=insertAtBeginning(n1,5)
current=head
while  current is not None:
    print(current.val)
    current=current.next
    
#Insertion at the END
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
def insertAtEnd(head, value):
    new_node=Node(value)
    current=head
    while current.next is not None:
        current=current.next
    current.next=new_node
    return head
head=insertAtEnd(n1,40)
current=head
while current is not None:
    print(current.val)
    current=current.next
    
#Insertion at position
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(40)
n1.next=n2
n2.next=n3
def insertAtPosition(head, value, pos):
    new_node=Node(value)
    current=head
    for i in range(pos-1):
        current=current.next
    new_node.next=current.next 
    current.next=new_node
    return head
head=insertAtPosition(n1,30,2)
current=head
while current is not None:
    print(current.val)
    current=current.next


    


    