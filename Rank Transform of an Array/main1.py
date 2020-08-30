class Solution(object):
    def arrayRankTransform(self, arr):
        ret, _dict = [], {}
        sorted_arr = sorted(list(set(arr)))
        
        for index, value in enumerate(sorted_arr):
            if value not in _dict:
                _dict[value] = index
        
        for i in arr:
            ret.append(_dict[i] + 1)            
            
        return ret
            