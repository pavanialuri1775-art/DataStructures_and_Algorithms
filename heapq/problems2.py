#Problem 1: Find K Smallest Elements
'''import heapq
arr=[7, 10, 4, 3, 20, 15]
heap=[]
k=3
for num in arr:
    heapq.heappush(heap,num)
for i in range(k):
    print(heapq.heappop(heap))

#kth smallest Element
import heapq
arr=[7, 10, 4, 3, 20, 15]
heap=[]
k=3
for num in arr:
    heapq.heappush(heap,num)
for i in range(k):
    ans=heapq.heappop(heap)
print(ans)'''

#Kth largest element
import heapq
arr = [3, 2, 1, 5, 6, 4]
heap=[]
k=2
for num in arr:
    heapq.heappush(heap,-num)
for i in range(k):
    ans=-heapq.heappop(heap)
print(ans)