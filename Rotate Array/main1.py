class Solution(object):
    def rotate(self, nums, k):
        times = k % len(nums)
        count = 0
        while count < times:
            nums.insert(0, nums.pop())
            count += 1