# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def mergeTrees(self, root1, root2):
        '''
        Use  DFS here - Get the two nodes from both trees
        Check if node values are None then return None
        else create new node based on sum of both nodes
        Then loop again first going left and then going right 
        and make sure to pass None if left or right of the node 
        doesnt exist
        Time and Space Complexity - O(n+m)
        '''
        def merge(node1,node2):
            
            if not node1 and not node2:
                return None
        
            v1=node1.val if node1 else 0
            v2=node2.val if node2 else 0 
            result=TreeNode(v1+v2)
        
            result.left=merge(node1.left if node1 else None,node2.left if node2 else None)
            result.right=merge(node1.right if node1 else None,node2.right if node2 else None)
            return result
        
        result = merge(root1,root2)
        
        return result 