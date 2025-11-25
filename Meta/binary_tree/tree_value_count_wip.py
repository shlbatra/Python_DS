# Binary tree
# Find number of times that the target occurs in the tree.

def tree_value_count(root, target):
    
    if root is None: return 0
    match = 1 if root.val == target: 1 else 0

    return match + tree_value_count(root.left, target) + tree_value_count(root.right, target)