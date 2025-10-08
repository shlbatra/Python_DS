class DFS_HasPath_Undirected:

    def build_graph(self, edges):
        graph = {}
        for (i,j) in edges:
            if not graph.get(i): 
                graph[i] = []
            if not graph.get(j): 
                graph[j] = []          

            graph[i].append(j)
            graph[j].append(i)
            
        return graph
            
    def hasPath(self, map, source, target, visited):

        if source == target:
            return True
        if source in visited:
            return False  # already gone through cycle once and not found
        visited.add(source)
        for neighbor in map[source]:
            if self.hasPath(map, neighbor, target, visited) == True: # visited global to know what seen in past
                return True
        return False
        
    def dfs_undirectedPath(self, edges, source, target):

            graph = self.build_graph(edges)
            return self.hasPath(graph, source, target, visited=set())
     
        
edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
]

dfs = DFS_HasPath_Undirected()
graph = dfs.build_graph(edges)
print(graph)
ans = dfs.dfs_undirectedPath(edges, 'j','m')  
print(ans)

ans = dfs.dfs_undirectedPath(edges, 'j','o')  
print(ans)