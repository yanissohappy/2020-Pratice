class Solution(object):
    def DFS(self, s, a_list, ret):
        if not s:
            ret.append(a_list[:])
            return
        
        i = 1
        while i < len(s) + 1:
            if s[:i][::-1] == s[:i]: # what we get now is palindrome
                a_list.append(s[:i])
                self.DFS(s[i:], a_list, ret)           
                a_list.pop()
            i += 1
            
    def partition(self, s):
        ret = []
        self.DFS(s, [], ret)
        return ret

            
            
