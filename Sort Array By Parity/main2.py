class Solution(object):
    def sortArrayByParity(self, A):
        left, right = 0, len(A) - 1
        
        while left < right:
            if A[left] & 1 == 0:
                left += 1
            else:
                if A[right] & 1 == 1:
                    right -= 1
                else:
                    A[right], A[left] = A[left], A[right]
                    left += 1
                    right -= 1
        return A