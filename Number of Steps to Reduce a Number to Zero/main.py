class Solution(object):
    def numberOfSteps (self, num):
        count = 0
        while num != 0:
            if num & 1 == 1:
                num = num - 1
                count += 1
            else: # even
                num >>= 1
                count += 1
        return count
            