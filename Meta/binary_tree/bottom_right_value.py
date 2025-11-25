# Binary tree
# Return right most value in bottom most level of tree
from collections import Deque

def tree_value_count(root):
    # BFS traversal with left to right - last node bottom one
    queue = deque([ root ])

    curr = None
    while len(queue) > 0:
        curr = queue.pop()
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return curr.val
