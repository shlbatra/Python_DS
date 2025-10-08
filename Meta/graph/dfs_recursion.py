class DFS:

    def __init__(self, graph):
        self.graph = graph
    
    def dfs_print(self, source):
        
            print(source)
            
            for neighbor in self.graph[source]:
                self.dfs_print(neighbor)
        
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

dfs = DFS(graph)
dfs.dfs_print('a')  # abdfce