# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
    
    def levelOrder(self, root, ret, level):
        if not root:
            return
        ret[level].append(root.val)
        self.levelOrder(root.left, ret, level - 1)
        self.levelOrder(root.right, ret, level - 1)        
    
    def levelOrderBottom(self, root):
        ret = [[] for i in range(self.depth(root))]
        self.levelOrder(root, ret, self.depth(root) - 1)
        return ret
