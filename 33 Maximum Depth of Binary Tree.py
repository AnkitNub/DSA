# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root): 
        if not root: # If the node is None, return 0
            return 0
        
        left_depth = self.maxDepth(root.left) # Recursively find the depth of the left subtree
        right_depth = self.maxDepth(root.right) # Recursively find the depth of the right subtree
        return max(left_depth, right_depth) + 1 # Add 1 for the current node