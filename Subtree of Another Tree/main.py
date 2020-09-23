# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkSubtree(self, s, t):
        if not s and not t:
            return True
        if (not s and t) or (s and not t):
            return False
        if s.val != t.val:
            return False
        return self.checkSubtree(s.left, t.left) and self.checkSubtree(s.right, t.right) 
        
    def DFSandCompare(self, s, t):
        if not s:
            return False
        if s.val == t.val and self.checkSubtree(s, t):
            return True
        
        ret1 = self.DFSandCompare(s.left, t)
        ret2 = self.DFSandCompare(s.right, t)
        
        return ret1 or ret2
            
    def isSubtree(self, s, t):
        return self.DFSandCompare(s, t)