# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def DFS(self, root, ret):
        if not root:
            return
        self.DFS(root.left, ret)
        ret.append(root.val)
        self.DFS(root.right, ret)
        return ret
    
    def makeBFS(self, _list):
        if len(_list) == 0:
            return None
        mid = len(_list) // 2
        ret = TreeNode(_list[mid])
        ret.left = self.makeBFS(_list[:mid])
        ret.right = self.makeBFS(_list[mid + 1:])
        
        return ret
    
    def balanceBST(self, root):
        if not root:
            return None
        
        _list = self.DFS(root, [])
        return self.makeBFS(_list)

        