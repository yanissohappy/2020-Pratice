class Solution(object):
    def rotate(self, nums, k):
        times = k % len(nums)
        nums[:] = nums[-times:] + nums[:-times]