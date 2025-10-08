from collections import deque

class BFS_HasPath:

    def __init__(self, graph, source, target):
        self.graph = graph
        self.source = source
        self.target = target
    
    def bfs_has_path(self):
        queue = deque()
        queue.append(self.source)
        
        while (len(queue) > 0):
            node = queue.popleft() # Queue - first in first out
            
            if node == self.target:
                return True
            
            for neighbor in self.graph[node]:
                queue.append(neighbor)
                
        return False
        
graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['k'],
    'j': ['i'],
    'k': []
}

bfs = BFS_HasPath(graph,'f','k')
ans = bfs.bfs_has_path()  # abdfce
print(ans)

bfs = BFS_HasPath(graph,'f','j')  # abdfce
ans = bfs.bfs_has_path()  # abdfce
print(ans)