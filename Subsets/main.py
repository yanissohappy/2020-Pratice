class Solution(object):
    def DFS(self, ret, temp, nums, index):
        ret.append(temp)
        for i in range(index, len(nums)):
            temp.append(nums[i])
            self.DFS(ret, temp[:], nums, i + 1)
            temp.pop()
        
    def subsets(self, nums):
        ret, temp = [], []
        self.DFS(ret, temp, nums, 0)
        return ret