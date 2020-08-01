class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        left, right, max_len, last_set_len = 0, 0, 1, 0 #  last_set_len 紀錄上一次set最大的len
        while left < len(s):
            _set = set()
            _set.add(s[left])
            last_set_len = len(_set)
            right = left + 1
            while right < len(s):
                _set.add(s[right])
                if len(_set) == last_set_len:
                    break
                else: 
                    max_len = max(max_len,len(_set))
                    last_set_len = len(_set)
                right += 1
            left += 1
            
        return max_len
                    