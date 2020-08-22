# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val: # 因為 BST 等於是不可能的，特別區隔那種可能(其實寫 else 即可)
            root.left = self.insertIntoBST(root.left, val)
            
        return root
        