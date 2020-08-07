# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def DFS(ref_list, root): # from left to right
    ref_list.append(root.val)
    if root.left:
        DFS(ref_list, root.left)
    else:
        ref_list.append(None)
        
    if root.right:
        DFS(ref_list, root.right)
    else:
        ref_list.append(None)
    if (not root.right) and (not root.left):
        return
def rev_DFS(ref_list, root): # from right to left
    ref_list.append(root.val)
    if root.right:
        rev_DFS(ref_list, root.right)
    else:
        ref_list.append(None)    
    if root.left:
        rev_DFS(ref_list, root.left)
    else:
        ref_list.append(None)
    if (not root.right) and (not root.left):
        return
    
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        if (not root.right) and (not root.left):
            return True
        if (not root.right) or (not root.left):
            return False
        ref, rev_ref = [], []
        DFS(ref, root.left)
        rev_DFS(rev_ref, root.right)
        return ref == rev_ref
        