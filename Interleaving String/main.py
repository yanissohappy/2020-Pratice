def recursion(s1, s2, s3, index1, index2, index3, len_s1, len_s2, len_s3, check):
    ret = False
    if (index1, index2) in check:
        return check[index1, index2]
    if index3 == len_s3 and index2 == len_s2 and index1 == len_s1:
        return True      
    if index1 < len_s1 and index2 < len_s2:    
        if s1[index1] != s3[index3] and s2[index2] != s3[index3]:
            return False
    if index2 == len_s2 and index1 < len_s1 and s1[index1] != s3[index3]:
        return False
    if index1 == len_s1 and index2 < len_s2 and s2[index2] != s3[index3]:
        return False 
    
    if index3 < len_s3:
        if index1 < len_s1 and s1[index1] == s3[index3]:
            ret = ret or recursion(s1, s2, s3, index1 + 1, index2, index3 + 1, len_s1, len_s2, len_s3, check)
        if index2 < len_s2 and s2[index2] == s3[index3]:
            ret = ret or recursion(s1, s2, s3, index1, index2 + 1, index3 + 1, len_s1, len_s2, len_s3, check)
        check[index1, index2] = ret
    return ret
 
        
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)
        return recursion(s1, s2, s3, 0, 0, 0, len_s1, len_s2, len_s3, {})
        