class Solution(object):
    def maxChunksToSorted(self, arr):
        count, i, _max = 0, 0, 0
        
        while i < len(arr):
            _max = max(arr[i], _max)
            if _max == i:
                count += 1
            i += 1
        return count