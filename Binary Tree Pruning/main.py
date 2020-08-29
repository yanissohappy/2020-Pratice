# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def DFS(self, root):
        if not root: # 走到最底
            return None
        
        root.left = self.DFS(root.left)
        root.right = self.DFS(root.right)
        
        if not root.left and not root.right and root.val == 0: # 同樣是走到最底，這點不要了
            return None
        else:
            return root
        
    def pruneTree(self, root):
        return self.DFS(root)