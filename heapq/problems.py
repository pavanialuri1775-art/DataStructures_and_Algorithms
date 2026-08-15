#Create a min-priority queue using heapq.
import heapq
heap=[]
heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heappush(heap,30)
heapq.heappush(heap,40)
heapq.heappush(heap,50)
print(heap[0])
heapq.heappop(heap)
print(heap)

#2
import heapq
heap=[]
heapq.heappush(heap,30)
heapq.heappush(heap,50)
heapq.heappush(heap,10)
heapq.heappush(heap,40)
heapq.heappush(heap,20)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

#3
import heapq
heap=[]
heapq.heappush(heap,(2,"Task A"))
heapq.heappush(heap,(1,"Task B"))
heapq.heappush(heap,(2,"Task C"))
heapq.heappush(heap,(1,"Task D"))
heapq.heappush(heap,(2,"Task E"))
item=heapq.heappop(heap)
print(item[1])
item=heapq.heappop(heap)
print(item[1])
item=heapq.heappop(heap)
print(item[1])
item=heapq.heappop(heap)
print(item[1])
item=heapq.heappop(heap)
print(item[1])


#itertools:built in python module that provides tools for working with iterators
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#
import heapq
from itertools import count
heap=[]
counter=count()
heapq.heappush(heap,(2,next(counter),"Task A"))
heapq.heappush(heap,(1,next(counter),"Task B"))
heapq.heappush(heap,(1,next(counter),"Task C"))
heapq.heappush(heap,(3,next(counter),"Task D"))
heapq.heappush(heap,(1,next(counter),"Task E"))
while heap:
    priority, order, task=heapq.heappop(heap)
    print(task)
    


