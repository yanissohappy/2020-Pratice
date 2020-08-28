class Solution(object):
    def findErrorNums(self, nums):
        should_sum = sum(range(1, len(nums) + 1))        
        real_sum_set = sum(set(nums))
        real_sum = sum(nums)
        
        lack = should_sum - real_sum_set
        twice = real_sum - real_sum_set
                         
        return [twice, lack]