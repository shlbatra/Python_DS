# WIP
# Find path for target node in binary tree

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class DFS_Search_Recursion:

    def dfs_search_recursion(self, root, tgt):
        res = _dfs_search_recursion(root, tgt)

        if res:
            return res[::-1]
        else:
            return None

    def _dfs_search_recursion(self, root, tgt):
        # Time O(n)
        # Space O(n)
        if root is None: return None # No match found - leaf node
        if root.value == tgt: return [root.value] # Match found - return as array

        left_path = self._dfs_search_recursion(root.left, tgt) # Add left side path
        if left_path is not None:
        #    return [root.val, *left_path ] # This is an O(n) solution
            left_path.append(root.val) # add in reverse order
        return left_path

        right_path = self._dfs_search_recursion(root.right, tgt) 
        if right_path is not None: # Add right side path
        #    return [root.val, *right_path ]
            right_path.append(root.val)
        return None

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