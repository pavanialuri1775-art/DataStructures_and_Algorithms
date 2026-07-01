#Quick sort:Quick Sort is a divide-and-conquer sorting algorithm that works by:
#Selecting a pivot element.
#Partitioning the array so:
#Elements smaller than the pivot go to the left.
#Elements larger than the pivot go to the right.
#Recursively applying the same process to the left and right subarrays.
#pivot=arr[len(arr)//2]

#code
def quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[n//2]
    left=[]
    middle=[]
    right=[]
    for x in arr:
        if x<pivot:
            left.append(x)
        elif x==pivot:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort(left)+middle+quick_sort(right)
arr=[4,2,6,1,9]
print(quick_sort(arr))


#1st element as a pivot
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[]
    middle=[]
    right=[]
    for x in arr:
        if x<pivot:
            left.append(x)
        elif x==pivot:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort(left)+middle+quick_sort(right)
arr=list(map(int,input().split()))
print(quick_sort(arr))

#last element as pivot
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[]
    middle=[]
    right=[]
    for x in arr:
        if x<pivot:
            left.append(x)
        elif x==pivot:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort(left)+middle+quick_sort(right)
arr=list(map(int,input().split()))
print(quick_sort(arr))
