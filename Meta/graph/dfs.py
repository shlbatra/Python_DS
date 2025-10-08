class DFS:

    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
    
    def dfs_print(self):
        lst = [self.source] # Stack - last in and first out
        
        while (len(lst) > 0):
            node = lst.pop()
            print(node)
            
            for neighbor in self.graph[node]:
                lst.append(neighbor)
        
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

dfs = DFS(graph, 'a')
dfs.dfs_print()  # abdfce