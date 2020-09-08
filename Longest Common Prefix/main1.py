class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        max_index = len(strs[0])
        for _str in strs:
            while _str[:max_index] != strs[0][:max_index]:
                max_index -= 1
                if max_index == 0:
                    return ""
        return strs[0][:max_index]
                           
                