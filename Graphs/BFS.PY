#creating graph manually
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

#create graph when edges are given
edges=[
    [0,1],
    [0,2],
    [1,3],
    [2,3]
]
graph=[[] for i in range(4)]
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
    
print(graph)