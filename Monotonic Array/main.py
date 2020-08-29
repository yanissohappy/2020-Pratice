class Solution(object):
    def isMonotonic(self, A):
        if len(A) == 1:
            return True
        else:
            """
            if A[1] >= A[0]:
                return sorted(A) == A
            else:
                return sorted(A, reverse = True) == A
            """
            ascending = sorted(A)
            descending = sorted(A, reverse = True) 
            return ascending == A or descending == A