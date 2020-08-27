class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        if not A or not B:
            return False 
        if len(A) == 1:
            return False
        if len(A) == 2:
            if B[::-1] == A:
                return True
            else:
                return False
        if A == B and len(set(A)) < len(A): # if duplicate exists
            return True        
        if A == B and len(set(A)) == len(A):
            return False
        
        count, first, second = 0, None, None
        for a, b in zip(A, B): # check different word
            if a != b:
                if count == 0:
                    first = a
                    second = b
                count += 1
            if count == 2:
                if first != b or second != a:
                    return False
        
        if count == 2:
            return True
        