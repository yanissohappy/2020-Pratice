class Solution(object):
    def singleNumber(self, nums):
        nums.sort() # O(nlogn)
        for i in range(0, len(nums), 2):
            if i + 1 == len(nums):
                return nums[i]
            if nums[i] != nums[i + 1]:
                return nums[i]