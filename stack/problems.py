#problem1:  remove bigger elements
def rem_bigger_ele(arr):
    stack=[]
    for i in range(len(arr)):
        while stack and arr[i]<stack[-1]:
            stack.pop()
        stack.append(arr[i])#5
    return stack
arr=list(map(int,input().split()))
print(rem_bigger_ele(arr))

#previous smaller element
def prev_small_ele(arr):
    stack=[]
    answer=[]
    for i in range(len(arr)):
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)
        stack.append(arr[i])
    return answer
arr=list(map(int,input().split()))
print(prev_small_ele(arr))

#previous Greater element
def prev_greater_ele(arr):
    stack=[]
    ans=[]
    for i in range(len(arr)):
        while stack and stack[-1]<=arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    return ans
arr=list(map(int,input().split()))
print(prev_greater_ele(arr))

#Next Greater Element
def next_grtr_ele(arr):
    stack=[]
    ans=[]
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1]<=arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    ans.reverse()
    return ans
arr=list(map(int,input().split()))
print(next_grtr_ele(arr))

#Next smaller element
def next_smaller_ele(arr):
    stack=[]
    ans=[]
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    ans.reverse()
    return ans
arr=list(map(int,input().split()))
print(next_smaller_ele(arr))

#
class Solution:
    def maxLength(self, s):
        stack=[-1]
        max_len=0
        for right in range(len(s)):
            if s[right]=="(":
                stack.append(right)
            else:
                stack.pop()
                if not stack:
                    stack.append(right)
                else:
                    max_len=max(max_len,right-stack[-1])
        return max_len
                    