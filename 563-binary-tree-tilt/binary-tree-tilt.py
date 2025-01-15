# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def subtree_sum(node):
            """ Helper function to compute the sum of a node's subtree and update tilt. """
            if not node:
                return 0
            left_sum = subtree_sum(node.left)  # Recursive sum of left subtree
            right_sum = subtree_sum(node.right)  # Recursive sum of right subtree
            node_tilt = abs(left_sum - right_sum)  # Tilt for the current node
            self.total_tilt += node_tilt  # Accumulate tilt
            return node.val + left_sum + right_sum  # Total sum of the subtree rooted at node
        
        self.total_tilt = 0  # Initialize total tilt
        subtree_sum(root)  # Compute tilt by traversing the tree
        return self.total_tilt  # Return the total tilt
