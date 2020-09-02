class Solution(object):
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left_list = nums[:mid]
        right_list = nums[mid:]
        
        sorted_left = self.mergeSort(left_list)
        sorted_right = self.mergeSort(right_list)
        ret = []
        while sorted_left and sorted_right:
            if sorted_left[0] > sorted_right[0]:
                ret.append(sorted_right[0])
                del sorted_right[0]
            else:
                ret.append(sorted_left[0])
                del sorted_left[0]
        if sorted_left:
            ret.extend(sorted_left)
        if sorted_right:
            ret.extend(sorted_right)
        return ret[:]
            
        
    def sortArray(self, nums):
        return self.mergeSort(nums)