 def quick_sort(arr):
    n = len(arr)
    if n<=1:
        return arr

    pivot = arr[n//2]
    left = []
    middle=[]
    right = []
    for x in arr:
        if x<pivot:
            left.append(x)
        elif x==pivot:
            middle.append(x)

        else:
            right.append(x)
    return quick_sort(left)+middle+quick_sort(right) 
            
a = [8,6,4,9,1,2]
print(quick_sort(