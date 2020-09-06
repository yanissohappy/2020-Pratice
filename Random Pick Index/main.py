# import random
# import math
class Solution(object):

    def __init__(self, nums):
        self._index = {} 
        self._dict = {}
        for index, key in enumerate(nums):
            if key not in self._dict:
                self._dict[key] = [index]
                self._index[key] = 0 # To know now what index is
            else:
                self._dict[key].append(index)
        

    def pick(self, target):
        n = len(self._dict[target])
        if self._index[target] + 1 == n:
            ret = self._dict[target][self._index[target]]
            self._index[target] = 0
            return ret
        else:
            self._index[target] += 1
            return self._dict[target][self._index[target] - 1]
        
        """ 如果一個有很多個 index 的值在短時間內被快速呼叫，則被叫出值都會相同，所以此法不行
        ran = int(math.ceil(random.random()))
        return self._dict[target][ran * (n - 1)]
        """


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)