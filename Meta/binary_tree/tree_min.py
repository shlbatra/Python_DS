# Smallest value within the tree
# Assume tree is not empty
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeMin:

    def tree_min_dfs_recursive(self, root):
        
        if root is None: return float('inf') # base case - for null, return infinity -> as not going to be min compared to numbers in tree

        return min(root.value, self.tree_min_dfs_recursive(root.left), self.tree_min_dfs_recursive(root.right))

    def tree_min_bfs_traversal(self, root):
        # if root is None: return None; Assumption tree is not empty
        min_val = float('inf')
        q = deque()
        q.append(root)

        while len(q) > 0:
            curr_node = q.popleft() # check if this operation is O(1) or O(n)
            min_val = min(min_val, curr_node.value)

            if curr_node.left:
                q.append(curr_node.left)

            if curr_node.right:
                q.append(curr_node.right)
        return min_val

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(2)
e = Node(4)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

dfs = TreeMin()
res = dfs.tree_min_dfs_recursive(a)
print(res)

res = dfs.tree_min_bfs_traversal(a)
print(res)