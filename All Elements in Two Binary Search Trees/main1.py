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
        
    def getAllElements(self, root1, root2):
        list1 = self.DFS(root1, [])
        list2 = self.DFS(root2, [])
        ret = []
        
        if list1:
            ret.extend(list1)
        if list2:
            ret.extend(list2)
        
        return sorted(ret)