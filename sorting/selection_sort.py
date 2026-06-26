#Selection sort:repeatedly selecting minimum element
#idea:find the smallest element in unsorted part and place it at the beginning.

#Algorithm
'''For every position:

1.Assume current position has minimum.
2.Search the remaining array for a smaller element.
3.Swap minimum element with current position.'''

#1
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=list(map(int,input().split()))
print(selection_sort(arr))
