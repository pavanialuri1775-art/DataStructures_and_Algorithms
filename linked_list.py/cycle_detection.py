#detecting start point of the cycle
def detectCycle(head):
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        
        if slow==fast:
            break
    else:
        return None
    #phase 2
    slow=head
    while slow!=fast:
        slow=slow.next 
        fast=fast.next
        
    return slow
    