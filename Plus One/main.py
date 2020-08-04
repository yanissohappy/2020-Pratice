class Solution(object):
    def plusOne(self, digits):
        weight = 1
        sum_pop = 0
        for _ in range(len(digits)):
            pop_thing = digits.pop()
            pop_thing *= weight
            sum_pop += pop_thing 
            weight *= 10
        sum_pop += 1
        
        ret = []
        while sum_pop != 0:
            ret.insert(0,sum_pop % 10)
            sum_pop /= 10
        return ret