class Solution(object):
    def findUnsortedSubarray(self, nums):
        left, right = 0, len(nums) - 1
        if len(nums) < 2:
            return 0
        
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                left += 1
            else:
                break
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] >= nums[i - 1]:
                right -= 1
            else:
                break
        
        if left == len(nums) - 1 or right == 0: # replacing or with and is also available
            return 0 # no need to be sorted
        not_sorted_max = max(nums[left : right + 1])
        not_sorted_min = min(nums[left : right + 1])
        
        
        while right < len(nums) - 1:
            if nums[right + 1] < not_sorted_max:
                right += 1
            else:
                break
        while left > 0:
            if nums[left - 1] > not_sorted_min:
                left -= 1        
            else:
                break
        return right - left + 1
            