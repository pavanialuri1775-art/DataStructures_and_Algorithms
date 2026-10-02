#dijkshtra algo-----------------


import heapq
def dij(graph, st): #g, A  

    dis = {}
    prev = {}

    for node in graph:
        dis[node] = float("inf")
        prev[node] = None

    dis[st] = 0 #dis[A]=0

    pri_que = [(0,st)]

    while pri_que:

        curr_dis, curr_node = heapq.heappop(pri_que)#cd=12,cn=c

        if curr_dis>dis[curr_node]:#12>12
            continue

        for nei, wt in graph[curr_node]:

            new_dis = curr_dis+wt #12

            if new_dis<dis[nei]:#12<17

                dis[nei]= new_dis #dis[C]=12

                prev[nei] = curr_node #F


                heapq.heappush(pri_que, (new_dis,nei)) #(8,d),(12,C)

    return dis, prev

graph = {

    "A": [("B",2),("D",8)],
    "B":[("A",2),("D",5),("E",6)],
    "D":[("A",8),("B",5),("E",3),("F",2)],
    "E":[("B",6),("D",3),("F",1),("C",9)],
    "F":[("D",2),("E",1),("C",3)],
    "C":[("E",9),("F",3)]

    }

                

                
st = "A"
tar = "C"

dis, prev = dij(graph, st)
print(dis, prev)