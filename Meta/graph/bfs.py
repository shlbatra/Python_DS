from collections import deque

class BFS:

    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
    
    def bfs_print(self):
        queue = deque()
        queue.append(self.source)
        
        while (len(queue) > 0):
            node = queue.popleft() # Queue - first in first out
            print(node)
            
            for neighbor in self.graph[node]:
                queue.append(neighbor)
        
graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

bfs = BFS(graph, 'a')
bfs.bfs_print()  # acbedf