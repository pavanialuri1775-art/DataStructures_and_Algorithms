#Searching for a value
def search(head,value):
    current=head
    index=0
    while current is not None:
        if current.val==value:
            return index
        current=current.next 
        index+=1
    return -1

#
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.next=n3
n3.next=n4
def search(head,value):
    current=head
    index=0
    while current is not None:
        if current.value==value:
            return index
        current=current.next 
        index+=1
    return -1
res=search(n1,40)    
print(res)
