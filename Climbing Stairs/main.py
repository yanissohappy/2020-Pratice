class Solution(object):
    def recursive(self, n, now_stair):
        if n < now_stair:
            return 0
        if n == now_stair:
            return 1
        if n > now_stair:
            return self.recursive(n, now_stair + 1) + self.recursive(n, now_stair + 2)
    def climbStairs(self, n):
        return self.recursive(n, 0)
        