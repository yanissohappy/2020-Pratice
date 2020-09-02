class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        ret = []
        i, j = 0, 0
        while i < len(nums):
            ret.append(nums[i])
            _sum = nums[i]
            j = i + 1
            while j < len(nums):
                _sum += nums[j]
                ret.append(_sum)               
                j += 1
            i += 1
        ret.sort()
        return sum(ret[left - 1: right]) % 1000000007