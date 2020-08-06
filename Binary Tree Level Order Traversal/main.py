# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def BFS(ret, level, node):
    if (not node.right) and (not node.left):
        return
    if level + 1 not in ret: # root 是 level 0， 第 0 層有1個
        ret.update({level + 1 : 0})
    if node.right:
        ret[level + 1] += 1
        BFS(ret, level+1, node.right)        
    if node.left:
        ret[level + 1] += 1
        BFS(ret, level+1, node.left)
        
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        
        # null 的下面就不用再接了！所以 null 下面的　null 可以忽略
        ret = []
        queue = [root]
        level, max_in_level, iteration_times = 0, 0, 0 # max_in_level : 一層中最多有幾個
        dic = {0:1}
        BFS(dic, 0, root) # get node counts in a layer
                
        while queue:
            max_in_level = dic[level]
            iteration_times = 0
            temp = []
            while iteration_times < max_in_level:
                node = queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp.append(node.val)    
                iteration_times += 1                    
            level += 1
            ret.append(temp)
        return ret