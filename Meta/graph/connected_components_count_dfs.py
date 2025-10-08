class DFS_ConnectedComponentsCount:

            
    def explore(self, graph, node, visited):

        if node in visited:
            return 0  # already gone through cycle once and not found
        visited.add(node)
        
        for neighbor in graph[node]:
            self.explore(graph, neighbor, visited)  # visited global to know what seen in past
                
        return 1

    def dfs_connected_components_counts(self, graph):
        visited = set()
        cnt = 0
        for node in graph.keys():
            cnt += self.explore(graph, node, visited)
        return cnt

graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}  # return 2 components

dfs = DFS_ConnectedComponentsCount()

ans = dfs.dfs_connected_components_counts(graph)  
print(ans)
