# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        ret1, ret2 = 0, 0
        if root.left:
            ret1 = 1 + self.minDepth(root.left)
        if root.right:    
            ret2 = 1 + self.minDepth(root.right)
        
        if not ret1:
            return ret2
        if not ret2:
            return ret1
        if ret1 and ret2:
            return min(ret1, ret2)