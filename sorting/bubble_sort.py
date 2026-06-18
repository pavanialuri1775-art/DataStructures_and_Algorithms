#Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.
#algorithm
#For every pass:
'''
1.Compare neighboring elements.
2.Swap if left element is greater than right element.
3.After each pass, one largest element reaches the end.'''

def bubblesort(arr): 
    n = len(arr)
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j]>arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
        
arr = list(map(int,input().split()))
print(bubblesort(arr)) 

