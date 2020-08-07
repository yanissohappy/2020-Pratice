# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def DFS_sum(root, current_sum, needed_sum): # needed_sum represents question demand
    is_sum = False
    current_sum += root.val    
    if not root.left and not root.right: # is leaf
        return (current_sum == needed_sum) | is_sum
    if root.left:
        is_sum |= DFS_sum(root.left, current_sum, needed_sum)
        if is_sum: return True
    if root.right:
        is_sum |= DFS_sum(root.right, current_sum, needed_sum)
        if is_sum: return True
    return is_sum
    
class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        return DFS_sum(root, 0, sum)