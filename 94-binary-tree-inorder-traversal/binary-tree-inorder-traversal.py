# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        
        # Helper function for recursion
        def inorder(node):
            if not node:
                return
            inorder(node.left)  # Traverse left subtree
            res.append(node.val)  # Visit current node
            inorder(node.right)  # Traverse right subtree
        
        inorder(root)
        return res