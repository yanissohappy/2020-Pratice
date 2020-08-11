# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def DFS(self,layer, root, _set):
        layer += 1
        if not root.left and not root.right:
            _set.add(layer)
            return 
        if root.left:
            self.DFS(layer, root.left, _set)
        if root.right:
            self.DFS(layer, root.right, _set)
            
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        _set = set()
        self.DFS(0, root, _set)
        return max(_set)