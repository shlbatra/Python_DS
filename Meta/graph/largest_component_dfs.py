class DFS_LargestComponent:

            
    def explore_size(self, graph, node, visited):

        if node in visited:
            return 0  # already gone through cycle once and not found
        visited.add(node)
        size = 1
        for neighbor in graph[node]:
            print(size)
            size += self.explore_size(graph, neighbor, visited)  # visited global to know what seen in past, keep adding to size as component grows
                
        return size

    def dfs_largest_component(self, graph):
        visited = set()
        largest = 0
        for node in graph.keys():
            print(node)
            largest = max(largest, self.explore_size(graph, node, visited))
            print('\n')
        return largest

graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}  # return 4

dfs = DFS_LargestComponent()

ans = dfs.dfs_largest_component(graph)  
print(ans)
