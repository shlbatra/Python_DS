# Insert value in Binary Search Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = Node(100)
b = Node(80)
c = Node(120)
d = Node(50)
e = Node(90)
f = Node(140)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

    #       100
    #    80     120
    #  50   90 **  140    

# Where add 108 -> ** ?

def binary_tree_insert_recursive(root, val):
    if root is None: # reached end goal at leaf level where to insert data
        head = Node(val)
        return head
    if root.value < val:
        root.right = binary_tree_insert_recursive(root.right, val) # add connections of left and right for BST
    else:
        root.left = binary_tree_insert_recursive(root.left, val)
    return root # return original root node

def tree_traversal(root):
    if root is None: return []
    return [ root.value, *tree_traversal(root.left), *tree_traversal(root.right)]

def tree_traversal_leaf(root): # print leaf nodes only
    if root is None: return
    if root.left is None and root.right is None: # leaf node
        print(root.value)
        return
    leaves = []
    if root.left is not None:
        tree_traversal_leaf(root.left) # keep traversing left path
    if root.right is not None:
        tree_traversal_leaf(root.right) # once left done, traverse right path

print(tree_traversal(a))
ans = binary_tree_insert_recursive(a, 108)
print(ans.value)
print(tree_traversal(ans))
tree_traversal_leaf(ans)