#stack is a linear data structure which follows LIFO principle.
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print("stack:",stack)
#pop()-Removes top element
stack.pop()
print("stack:",stack)
#peek()-to view top element
print(stack[-1])
#isEmpty:check if empty
print(len(stack)==0)

#1 using oops
class stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)==0
stk=stack()
stk.push(10)
stk.push(20)
stk.push(30)
print(stk.stack)
stk.pop()
print(stk.stack)
