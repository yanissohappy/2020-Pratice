class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        ret_list = []
        for i in range(n):
            ret_list.append(nums[i])
            ret_list.append(nums[(len(nums) / 2) + i])
        
        return ret_list