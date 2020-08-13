class Solution(object):
    def numJewelsInStones(self, J, S):
        jewel_type = set(list(J))
        count = 0
        for stone in list(S):
            if stone in jewel_type:
                count += 1
        return count
        