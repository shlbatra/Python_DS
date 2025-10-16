# Using stack
# First In, First Out ex. A, B, D -> then D first, B and finally A
# Time and space complexity of O(n)
# check children exists before adding to queue
# recursive under the hood uses stack order
from collections import deque

class BreadthFirstBT:

    def breadth_first_traversal(self, root):

        if root is None: return []
        q = deque() # Optimal data structure with O(1) add and remove operations
        q.append(root)
        res = []

        while len(q) > 0:

            curr_node = q.popleft() # First in , First out
            # print(curr_node.value)
            res.append(curr_node.value)
        
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
            
        return res


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
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

dfs = BreadthFirstBT()
res = dfs.breadth_first_traversal(a)
print(res)

a = None
res = dfs.breadth_first_traversal(a)
print(res)