#Graph Intro
#Present Graph using Adjacency list
#Array of vertices   A,B,C
#Linked List for edges; Use Dictionary with value as list 
#A -> B -> C
#B -> A
#C -> A

#BFS
# Start at arbitary node of graph and explore neighbor nodes at 
# current level before moving to next level neigbors
#Use queue
#Cautious about cycle in Graph using visited set & queue data structure

#DFS
#Start at arbitary node and explores as far as possible along each
#edge before backtracking
# Use Stack 


class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            self.gdict = {}
        else:
            self.gdict=gdict

    def addVertex(self,vertex):
        self.gdict[vertex]=[]

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def bfs(self,vertex):
        visited_set=set(vertex)
        queue=[vertex]

        while queue:
            devertex=queue.pop(0)
            print(devertex)
            for adjVertex in self.gdict[devertex]:
                if adjVertex not in visited_set:
                    visited_set.add(adjVertex)
                    queue.append(adjVertex)

    def dfs(self,vertex):
        visited_set=set(vertex)
        stack=[vertex]

        while stack:
            devertex=stack.pop()
            print(devertex)
            for adjvertex in self.gdict[devertex]:
                if adjvertex not in visited_set:
                    visited_set.add(adjvertex)
                    stack.append(adjvertex)
        
customDict ={
            "a" : ["b","c"],
            "b" : ["a","d","e"],
            "c" : ["a","e"],
            "d" : ["b","e","f"],
            "e" : ["d"],
            "f" : ["d","e"]
            }


g=Graph(customDict)
g.addVertex("g")
g.addEdge("g","c")
g.addEdge("g","a")
g.addEdge("e","g")
print(g.gdict)
print('bfs')
g.bfs("a")
print('dfs')
g.dfs("a")




