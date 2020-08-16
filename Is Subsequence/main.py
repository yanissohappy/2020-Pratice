class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) > len(t):
            return False
        
        index, index_list = -1, []
        i = 0
        
        while i < len(s):
            index = t.find(s[i], index + 1)
            i += 1
            index_list.append(index) 
            if index == -1:
                break
                
        if not index_list or -1 in index_list: # can't find specific char
            return False
        
        if sorted(index_list) == index_list: # if ascending
            return True
        else:
            return False