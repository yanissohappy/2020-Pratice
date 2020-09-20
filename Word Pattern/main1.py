class Solution(object):
    def otherHasSS(self, _list, index, ss):
        for i in range(len(_list)):
            if i == index:
                continue
            if _list[i] == ss:
                return True
        return False
    
    def wordPattern(self, pattern, s):        
        s_list = s.split(" ")
        str_map = [None for i in range(26)]
        if len(s_list) != len(pattern):
            return False
        
        for p, ss in zip(pattern, s_list):
            if self.otherHasSS(str_map, ord(p) - ord('a'), ss):
                return False
            
            if not str_map[ord(p) - ord('a')]:
                str_map[ord(p) - ord('a')] = ss
            else:
                if str_map[ord(p) - ord('a')] != ss:
                    return False
        return True