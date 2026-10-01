#dijstras algorithm:it is used to find shortest path from source node to all other nodes.
#step1:represent the graph
#in python we use adjacency list to represent the graph

def dijkstra(graph,source):
#step2:Create our distance table
    dist={
        "A":float('inf'),
        "B":float("inf"),
        "C":float('inf')
    }
#step3:we need to repeatedly pick the smallest distance
#Data structure that efficiently supports this:Min-heap / priority queue
    dist[source]=0
    import heapq
    heap=[(0,source)]
    while heap:
#Step 4: Take the smallest-distance node
        distance, node = heapq.heappop(heap)
        if distance>dist[node]:
            continue##skip the entry
#   step5:look at A's neighours
        for neighbor,weight in graph[node]:
            new_distance=distance+weight
            if new_distance<dist[neighbor]:
                dist[neighbor]=new_distance
                heapq.heappush(heap,(new_distance,neighbor))
    return dist 
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 1)],
    'C': [('A', 5), ('B', 1)]
}
print(dijkstra(graph,'A'))