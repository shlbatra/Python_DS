# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif (p == None and q != None) or (q == None and p != None):
            print('b')
            print(p)
            print(q)
            return False
        elif p.val != q.val:
            print('a')
            print(p)
            print(q)
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)