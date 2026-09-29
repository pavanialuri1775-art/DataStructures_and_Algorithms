#You are given n nodes labeled 0 to n-1 and an array of edges.

'''n = 3
edges = [[0,1], [1,2]]
source = 0
destination = 2'''

from collections import deque

class Solution:
    def validPath(self, n, edges, source, destination):
        graph=[[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue=deque([source])
        visited={source}
        while queue:
            node=queue.popleft()
            
            if node==destination:
                return True
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return False
    



                    
            