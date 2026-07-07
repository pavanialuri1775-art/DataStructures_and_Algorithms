#frequency of elements
def frequency(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    for i in range(len(count)):
        if count[i] > 0:
            print(f"{i} -> {count[i]}")
arr = list(map(int, input().split()))
frequency(arr)

#find the maximum freq element
def max_freq_ele(arr):
    max_val=max(arr)
    count=[0]*(max_val + 1)
    for num in arr:
        count[num] += 1
    max_freq = 0
    max_element = -1
    for i in range(len(count)):
        if count[i] >max_freq:
            max_freq=count[i]
            max_element=i
    return max_element
arr = list(map(int, input().split()))
print(max_freq_ele(arr))

#3 remove duplicates
def remove_duplicates(arr):
    max_val=max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    for i in range(len(count)):
        if count[i]>0:
            print(i, end=" ")
arr = list(map(int, input().split()))
remove_duplicates(arr)


