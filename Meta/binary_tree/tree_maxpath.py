# Find maximum path from root to leaf node

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeMaxPath:

    def tree_max_path_root_leaf_dfs(self, root):

        if root is None: return -1
        # Get max path across sub tree
        return 1 + max(self.tree_max_path_root_leaf_dfs(root.left), self.tree_max_path_root_leaf_dfs(root.right))

    # def tree_max_path_root_bfs(self, root):

a = Node(5)
b = Node(11)
c = Node(4)
d = Node(2)
e = Node(3)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

dfs = TreeMaxPath()
res = dfs.tree_max_path_root_leaf_dfs(a)
print(res)