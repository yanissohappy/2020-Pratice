# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binarySearch(self, nums):
        if not nums:
            return 
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.binarySearch(nums[:mid])
        root.right = self.binarySearch(nums[mid + 1:])
        
        return root
        
    def sortedArrayToBST(self, nums):
        return self.binarySearch(nums)
        