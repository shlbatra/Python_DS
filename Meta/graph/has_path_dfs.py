class DFS_HasPath:

    def __init__(self, graph):
        self.graph = graph
    
    def dfs_hasPath(self, source, target):
        
            if source == target:
                return True
            
            for neighbor in self.graph[source]:

                if self.dfs_hasPath(neighbor, target) == True:
                    return True
                
            return False
        
graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['k'],
    'j': ['i'],
    'k': []
}

dfs = DFS_HasPath(graph)
ans = dfs.dfs_hasPath('f','k')  # abdfce
print(ans)

ans = dfs.dfs_hasPath('f','j')  # abdfce
print(ans)