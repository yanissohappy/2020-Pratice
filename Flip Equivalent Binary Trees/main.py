# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        if not root1 or not root2:
            return root1 == root2 == None
        if root1.val != root2.val:
            return False
        
        # non-flip case
        ans1 = self.flipEquiv(root1.left, root2.left) 
        ans2 = self.flipEquiv(root1.right, root2.right)
        # flip case
        ans3 = self.flipEquiv(root1.right, root2.left)
        ans4 = self.flipEquiv(root1.left, root2.right)
        
        return (ans1 & ans2) | (ans3 & ans4)
        