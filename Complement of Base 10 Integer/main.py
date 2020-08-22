class Solution(object):
    def bitwiseComplement(self, N):
        if N == 0:
            return 1
        exp, max_pow_2 = 0, 1
        while True:
            max_pow_2 = pow(2, exp)
            if max_pow_2 > N:
                break
            exp += 1
        return (max_pow_2 - 1) - N