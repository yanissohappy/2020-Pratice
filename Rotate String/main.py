class Solution(object):
    def rotateString(self, A, B):
        new_A = A + A
        if not A and not B:
            return True
        for i in range(len(A)):
            if new_A[i: i + len(A)] == B:
                return True
        
        return False