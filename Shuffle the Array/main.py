class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        middle = len(nums) / 2 - 1
        first_part = nums[: middle + 1]
        second_part = nums[middle + 1:]
        ret_list = []
        for i, j in zip(first_part, second_part):
            ret_list.append(i)
            ret_list.append(j)
        
        return ret_list