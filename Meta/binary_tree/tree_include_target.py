# Find target node in binary tree
# Approach for traversal -> BFS traversal or DFS with stack recursion
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BFS_Search:
    def bfs_search(self, root, tgt):
        if root is None: return False

        q = deque()
        q.append(root)

        while len(q) > 0:
            curr_node = q.popleft()
            if curr_node.value == tgt:
                return True
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
        return False
        

class DFS_Search_Recursion:
    def dfs_search_recursion(self, root, tgt):

        if root is None: return False # base case 1 for leaf nodes
        if root.value == tgt: return True # base case 2 for match

        return self.dfs_search_recursion(root.left, tgt) | self.dfs_search_recursion(root.right, tgt)

        # Match target -> recursive call True
        # For empty / null node -> False
        # Use logical OR at the top -> evaluate and combine
        
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

b = BFS_Search()
res = b.bfs_search(a, 'f')
print(res)
res = b.bfs_search(a, 'g')
print(res)

d = DFS_Search_Recursion()
res = d.dfs_search_recursion(a, 'f')
print(res)
res = d.dfs_search_recursion(a, 'g')
print(res)