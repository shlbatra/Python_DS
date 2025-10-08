from collections import deque

class BFS_ShortestPath:
        
    def build_graph(self, edges):
        graph = {}
        
        for (i, j) in edges:
            if not graph.get(i):
                graph[i] = []
            if not graph.get(j):
                graph[j] = []
            graph[i].append(j)
            graph[j].append(i)
            
        return graph
    
    def bfs_shortest_path(self, edges , source, target):
        graph = self.build_graph(edges)
        
        visited = set(source)  # As undirected graph so cycle prevention
        
        queue = deque()
        queue.append((source, 0))
        
        while (len(queue) > 0):
            (node, dist) = queue.popleft()  # Queue - first in first out
            
            if node == target:
                return dist
            
            for neighbor in graph[node]:
                if neighbor not in visited: # check for cycle here
                    visited.add(node) # add node to visited as added to queue
                    queue.append((neighbor, dist+1)) 
                
        return -1 # default case if no path found
        
edges = [
    ['w','x'],
    ['x','y'],
    ['z','y'],
    ['z','v'],
    ['w','v']
]

bfs = BFS_ShortestPath()
graph = bfs.build_graph(edges)
print(graph)
ans = bfs.bfs_shortest_path(edges, 'w', 'z')  # 2
print(ans)

ans = bfs.bfs_shortest_path(edges, 'w', 'v')  # 2
print(ans)

ans = bfs.bfs_shortest_path(edges, 'w', 'n')  # 2
print(ans)