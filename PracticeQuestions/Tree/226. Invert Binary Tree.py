# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverseNodes(node):
            if node is None:
                return
            reverseNodes(node.left)
            reverseNodes(node.right)
            print(node)
            temp = node.left 
            node.left = node.right 
            node.right = temp
            print(node)
            
        reverseNodes(root)
        return root

    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        st = [root]
            while len(st) > 0:
                node = st.pop()
                print(node)
                if node != None:
                    hold = node.left 
                    node.left = node.right
                    node.right = hold 
                    st.append(node.left)
                    st.append(node.right)
            return root
        