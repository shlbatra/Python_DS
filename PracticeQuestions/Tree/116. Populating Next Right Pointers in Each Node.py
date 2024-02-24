"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    '''
    Use BFS approach. Iterate left to root using queue
    Use 2 conditions -
    if child then, add left.next=right
    if node.next and node.right available, then node.right = node.next.left 
    '''
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root is None:
            return root
        
        current_node=root
        queue=[]
        results=[]
        queue.append(current_node)
        
        while len(queue)>0:
            current_node=queue.pop(0)
            if current_node.left is not None:
                current_node.left.next=current_node.right
                queue.append(current_node.left)
                queue.append(current_node.right)
            if current_node.next is not None and current_node.right is not None:
                current_node.right.next=current_node.next.left
                
        return root