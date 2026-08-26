#  Palindrome Checker
def palindrome(num):
    num1=str(num)
    if num>0:
        if num1==num1[::-1]:
            return palindrome
        else:
            return "not a palindrome"
    return "not valid"
print(palindrome(21212))

# count words
def count_words(sentence):
    s=sentence.split()
    return len(s)
sen="Count the number of words in a string"
print(count_words(sen))

# second  largest number in an array
def second_largest(arr):
    fst_largest=float('-inf')
    sec_largest=float('-inf')
    for num in arr:
        if num>fst_largest:
            sec_largest=fst_largest
            fst_largest=num
        elif num>sec_largest and num!=fst_largest:
            sec_largest=num
    return sec_largest
arr=list(map(int,input().split()))
print(second_largest(arr))

# Reverse an Integer
def reverse_digits(num):
    s=str(num)
    new=""
    for i in range(len(s)-1,-1,-1):
        new+=s[i]
    return new
print(reverse_digits(12345))

#count vowels
def vowel_count(word):
    vowels="aeiouAEIOU"
    count=0
    for ch in word:
        if ch in vowels:
            count+=1
    return  count
print(vowel_count("apple"))

#Check Prime
def check_prime(n):
    if  n<2:
        print("Not prime")
    else:
        for i in range(2,n):
            if n%i==0:
                print("Not Prime")
                break
        else:
            print("prime")
print(check_prime(17))

#Maximum Element
def max_ele(arr):
    max_element=float("-inf")
    for num in arr:
        if num>max_element:
            max_element=num
    return max_element
arr=[2,1,4,5,6]
print(max_ele(arr))

#minimum element
def min_ele(arr):
    min_element=float("inf")
    for num in arr:
        if num<min_element:
            min_element=num
    return min_element
arr=[2,1,4,5,6]
print(min_ele(arr))

#binary search
def binary_search(arr,target):
    left=0   
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
arr=[2,3,4,5,6]
target=4
print(binary_search(arr,target))
    
#Reverse a string
def rev_str(s):
    return s[::-1]
print(rev_str("pavani"))

#string palindrome
def palindrome_str(s):
    if s==s[::-1]:
        return True
    else:
        return False
print(palindrome_str("afifa"))

#
def rev_str(s):
    return s[::-1]
p=input()
print(rev_str(p))

#missing number
arr=[1,2,3,5,6]
for num in range(1,len(arr)):
        if num not in arr:
            print(num)
            
#find all duplicates
arr=[1,2,3,3,2]
freq={}
res=[]
for ch in arr:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1
for key in freq:
    if freq[key]>1:
        res.append(key)
print(res)

#Bubble sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(i,n-i-1):
            if  arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input().split()))
print(bubble_sort(arr))

#reverse  a linked  list
class Node:
    def  __init__(self,val):
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
        next_node=current.next
        current.next=prev 
        prev=current 
        current=next_node
    return prev





        
    

        

            
            
