class Solution(object):
    def isPowerOfFour(self, num):
        if num <= 0:
            return False
        if num == 1:
            return True
        count = 0
        copy_num = num

        while copy_num != 0:
            copy_num >>= 1
            count += 1
            
        ans_ref = 1        
        ans_ref <<= count - 1
        
        if ans_ref == num and count & 1 == 1:
            return True
        else:
            return False