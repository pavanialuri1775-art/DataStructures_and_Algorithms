class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next =next
class Solution:
    def middleNode(self, head):
        s=[]
        current=head
        while current is not None:
            s.append(current)
            current=current.next
        n=len(s)//2
        return s[n]