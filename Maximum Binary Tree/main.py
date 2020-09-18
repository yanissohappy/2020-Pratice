# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryCreate(self, nums):
        if not nums:
            return None
        max_val_index = 0
        max_val = max(nums)
        for index, key in enumerate(nums):
            if key == max_val:
                max_val_index = index
        root = TreeNode(max_val)
        root.right = self.binaryCreate(nums[max_val_index + 1:])
        root.left = self.binaryCreate(nums[:max_val_index])
        
        return root
            
    def constructMaximumBinaryTree(self, nums):
        return self.binaryCreate(nums)