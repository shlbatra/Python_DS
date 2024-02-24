"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    '''
    Use depth first search to create new node
    Start with any node and check if not exist in hashmap then 
    create copy node and add to hashmap.
    Finally run recursive iteration for all neigbours of the node 
    and also add that to neighbours of the copy node
    '''
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy=Node(node.val)
            oldToNew[node]=copy
        
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy 
    
        return dfs(node) if node else None
            