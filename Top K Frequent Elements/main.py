class Solution(object):
    def topKFrequent(self, nums, k):
        _dict = {}
        
        for i in nums: # O(n)
            if i not in _dict:
                _dict[i] = 1
            else:
                _dict[i] += 1
        n = len(nums) + 1 # index 0 won't be used
        
        freq = [[] for _ in range(n)]
        for key, value in _dict.items():
            freq[value].append(key) # higher value(freq) will be put in higher index(we can do this way becuz of "distinct num"!)
        
        ret, count, innercount = [], 0, 0    
        for i in range(n - 1, -1, -1):
            innercount = 0
            if freq[i] != None:
                while innercount <= len(freq[i]) - 1:
                    ret.append(freq[i][innercount])
                    innercount += 1
                    count += 1
            if count == k:
                break
        return ret
            