class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        last_one = start + (n - 1) * 2
        if start % 4 < 2: # 起始開始就可以抓"搭配 +2"為一國的 因為 00 + 10 = 10 and 01 + 10 = 11 兩者 xor 完會是 2
            if n % 4 == 0:
                return 2 ^ 2
            elif n % 4 == 1:
                return 0 ^ last_one
            elif n % 4 == 2:
                return 2
            else: # == 3
                return 2 ^ last_one
        else: # 取下一個(start + 2) 為首，原先的 start 保留
            first_one = start
            n = n - 1 # 用後面的 n - 1 個當新的可能
            if n % 4 == 0:
                return 2 ^ 2 ^ first_one
            elif n % 4 == 1:
                return 0 ^ last_one ^ first_one
            elif n % 4 == 2:
                return 2 ^ first_one
            else: # == 3
                return 2 ^ last_one ^ first_one