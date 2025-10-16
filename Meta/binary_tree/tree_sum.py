# find sum of all nodes of Binary Tree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSum:

    def tree_sum_dfs_recursive(self, root):

        if root is None: # base case
            return 0

        return root.value + self.tree_sum_dfs_recursive(root.left) + self.tree_sum_dfs_recursive(root.right)

    def tree_sum_dfs_iterative(self, root):

        if root is None: return 0
        total = 0
        lst = [ root ]
        while len(lst) > 0:
            curr_node = lst.pop() # processing logic when node leaves the queue is much easier
            total += curr_node.value
            if curr_node.right:
                lst.append(curr_node.right)
            if curr_node.left:
                lst.append(curr_node.left)
        return total


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
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

dfs = TreeSum()
res = dfs.tree_sum_dfs_recursive(a)
print(res)

res = dfs.tree_sum_dfs_iterative(a)
print(res)
