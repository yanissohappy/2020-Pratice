class Solution(object):
    def wordPattern(self, pattern, s):        
        s_list = s.split(" ")
        return len(set(zip(s_list, pattern))) == len(set(s_list)) == len(set(pattern)) and len(s_list) == len(pattern)