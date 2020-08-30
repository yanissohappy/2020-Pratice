class Solution(object):
    def lastStoneWeight(self, stones):
        stones.sort()
        while stones:
            if len(stones) == 1:
                return stones[0]
            _max = stones.pop()
            _secondmax = stones.pop()
            # _secondmax <= _max
            if _max == _secondmax:
                continue
            else: # _max > _secondmax
                ash = _max - _secondmax
                index = 0
                for i in stones:
                    if ash < i:
                        break
                    index += 1
                stones.insert(index, ash)
                
        return 0 # no stones left