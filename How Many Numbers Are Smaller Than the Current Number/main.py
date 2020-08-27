class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        return [sorted(nums).index(num) for num in nums]
        