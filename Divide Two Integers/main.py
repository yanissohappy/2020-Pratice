class Solution(object):
    def divide(self, dividend, divisor):
        rev = int(float(dividend) / float(divisor)) # get truncated result
        if rev > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return rev
            