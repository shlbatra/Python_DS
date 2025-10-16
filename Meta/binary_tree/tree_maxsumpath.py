# Find maximum path sum of values from root to leaf node

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeMaxPath:

    def tree_max_path_root_leaf_dfs(self, root):

        if root is None: return float('-inf')
        if (root.left is None) & (root.right is None): # for single node, return the node itself
            return root.value
        # Get max sub path for sub tree
        return root.value + max(self.tree_max_path_root_leaf_dfs(root.left), self.tree_max_path_root_leaf_dfs(root.right))

    # def tree_max_path_root_bfs(self, root):

a = Node(5)
b = Node(11)
c = Node(4)
d = Node(2)
e = Node(10)
f = Node(1)

    #       5
    #    11     4
    #  2   10     1    

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

dfs = TreeMaxPath()
res = dfs.tree_max_path_root_leaf_dfs(a)
print(res)