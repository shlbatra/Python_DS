# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return 1+max(left,right)
        else:
            return 1+min(left,right)

    def minDepth_bfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue=[]
        result=1
        queue.append(root)
        while len(queue):
            for i in range(len(queue)):
                current_node = queue.pop(0)
                if current_node.left is None and current_node.right is None:
                    return result
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            result = result+1
        return -1