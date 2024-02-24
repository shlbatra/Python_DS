# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))

    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        level=0
        queue = []
        queue.append(root)
        
        while len(queue) > 0:
            print(len(queue))
            for i in range(len(queue)):
                current_node = queue.pop(0)
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            level = level+1
        return level

