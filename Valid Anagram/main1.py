class Solution(object):
    def isAnagram(self, s, t):
        s_sum, t_sum = 0, 0
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        for i, j in zip(s,t):
            s_sum += ord(i) - ord('a')  
            t_sum += ord(j) - ord('a')
        
        return s_sum == t_sum