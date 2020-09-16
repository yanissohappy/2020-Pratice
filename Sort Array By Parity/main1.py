class Solution(object):
    def sortArrayByParity(self, A):
        left, right = 0, len(A) - 1
        
        while left < right:
            while A[left] & 1 == 0 and left < right:
                left += 1
            while A[right] & 1 == 1 and left < right:
                right -= 1
            A[right], A[left] = A[left], A[right]
        return A