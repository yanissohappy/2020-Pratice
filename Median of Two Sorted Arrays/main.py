class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        total_len = len(nums1) + len(nums2)
        grab_num = total_len // 2
        first_part_max = 0

        while grab_num != 0:
            if nums1 and nums2:
                if nums1[0] > nums2[0] :
                    first_part_max = nums2[0]
                    del nums2[0]
                else:
                    first_part_max = nums1[0]
                    del nums1[0]
            elif (nums2): # still sth in nums2
                first_part_max = nums2[0]
                del nums2[0]
            elif (nums1): # still sth in nums1
                first_part_max = nums1[0]
                del nums1[0]                         
            grab_num -= 1

        if total_len % 2 == 1: # odd
            if len(nums1) >= 1 and len(nums2) >= 1:
                return float(min(nums1[0], nums2[0]))
            elif len(nums1) >= 1 and len(nums2) < 1:
                return nums1[0]
            elif len(nums1) < 1 and len(nums2) >= 1:
                return nums2[0]        
        else: # even
            if len(nums1) >= 1 and len(nums2) >= 1:
                return (float(first_part_max) + float(min(nums1[0], nums2[0])))/2
            elif len(nums1) >= 1 and len(nums2) < 1:
                return (float(first_part_max) + float(nums1[0]))/2
            elif len(nums1) < 1 and len(nums2) >= 1:
                return (float(first_part_max) + float(nums2[0]))/2