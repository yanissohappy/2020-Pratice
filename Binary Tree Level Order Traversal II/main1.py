# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root, ret, level):
        if not root:
            return
        if len(ret) < level + 1:
            ret.append([])
        ret[level].append(root.val)
        self.levelOrder(root.left, ret, level + 1)
        self.levelOrder(root.right, ret, level + 1)        
    
    def levelOrderBottom(self, root):
        ret = []
        self.levelOrder(root, ret, 0)
        return ret[::-1]