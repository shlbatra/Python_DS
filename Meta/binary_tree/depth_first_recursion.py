# Using stack
# First In, First Out ex. A, B, D -> then D first, B and finally A
# Time and space complexity of O(n)
# check children exists before adding to stack


class DepthFirstBT:

    def depth_first_traversal(self, root):

        if root is None: return []
            
        return [ root.value, *self.depth_first_traversal(root.left), *self.depth_first_traversal(root.right)]


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

dfs = DepthFirstBT()
res = dfs.depth_first_traversal(a)
print(res)

a = None
res = dfs.depth_first_traversal(a)
print(res)