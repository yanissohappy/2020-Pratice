class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        
        min_diff = min([b - a for a, b in zip(arr, arr[1:])])
        return [[a,b] for a, b in zip(arr, arr[1:]) if min_diff == b - a]