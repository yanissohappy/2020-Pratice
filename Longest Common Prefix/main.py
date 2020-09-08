class Solution(object):
    def longestCommonPrefix(self, strs):
        ret = ""
        if not strs:
            return ret
        for i in range(len(strs[0])):
            char = strs[0][i] 
            for j in range(len(strs)):
                if i < len(strs[j]) and strs[j][i] != char:
                    return ret
                if i >= len(strs[j]):
                    return ret
            ret += char
        return ret