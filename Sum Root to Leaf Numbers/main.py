# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def DFS(self, root, keep_num, total_list):
        keep_num *= 10    
        keep_num += root.val 
        if root.left:
            self.DFS(root.left, keep_num, total_list)
        if root.right:
            self.DFS(root.right, keep_num, total_list)
        
        if not root.left and not root.right:
            total_list.append(keep_num)
            return            
    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        total_list = []
        self.DFS(root, 0, total_list)
        return sum(total_list)