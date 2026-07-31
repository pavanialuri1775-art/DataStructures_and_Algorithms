#  Queue
queue=[]
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:",queue)#Queue: [10, 20, 30]

#Front
print("Front:", queue[0])#Front: 10

#Dequeue
print("Removed:", queue.pop(0))#Removed: 10

#  Empty Check
if not queue:
    print("Queue is empty")#Queue: [20, 30]
else:
    print("Queue is not empty")#Queue is not empty
    
    
