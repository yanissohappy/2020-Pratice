class Solution(object):
    def thirdMax(self, nums):
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if first < num:
                first = num
        
        for num in nums:
            if num < first and second < num: # < max and > others
                second = num
                
        for num in nums:
            if num < second and third < num:
                third = num
        if third == float('-inf'):
            return first
        else:
            return third