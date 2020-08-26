# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def DFS(self, root, _max, _min):
        if not root:
            return _max - _min
        _max = max(root.val, _max)
        _min = min(root.val, _min)
        max1 = self.DFS(root.left, _max, _min)        
        max2 = self.DFS(root.right, _max, _min)
        return max(max1, max2)
        
    def maxAncestorDiff(self, root):        
        return self.DFS(root, 0, 100000)
        