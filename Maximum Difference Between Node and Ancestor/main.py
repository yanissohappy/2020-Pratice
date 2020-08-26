# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def DFS_collect(self, root, ret, temp):
        if not root:
            if temp[:] not in ret:
                ret.append(temp)
            return 
        temp.append(root.val)
        self.DFS_collect(root.left, ret, temp[:])
        self.DFS_collect(root.right, ret, temp[:])
        
        return ret
        
    def maxAncestorDiff(self, root):
        all_value = self.DFS_collect(root, [], [])
        _max = 0
        for _list in all_value:
            _max = max(abs(max(_list) - min(_list)), _max)
        
        return _max
        