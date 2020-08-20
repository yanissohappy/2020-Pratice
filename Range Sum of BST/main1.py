# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R): 
        _sum = 0
        
        if not root:
            return 0
        if L <= root.val <= R:
            _sum += root.val
            if root.left: 
                _sum += self.rangeSumBST(root.left, L, R)
            if root.right: 
                _sum += self.rangeSumBST(root.right, L, R)    
        else:
            if root.val > R: # 右半部就不用找了
                _sum += self.rangeSumBST(root.left, L, R)
            if root.val < L: # 左半部就不用找了
                _sum += self.rangeSumBST(root.right, L, R)
        
        return _sum