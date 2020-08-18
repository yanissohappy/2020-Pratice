class Solution(object):
    def integerReplacement(self, n):
        step = 0
        
        while True:
            while n % 2 == 0: # 是偶數就先除以 2 到底為止
                n = n / 2
                print(n)
                step += 1   
            if n == 1:
                return step
            if n == 3:
                return step + 2
            
            # 此時 n 為奇數
            if (n + 1) % 4 == 0: # 若 n + 1 為 4 的 倍數
                step += 1
                n = (n + 1)
                continue
            elif (n - 1) % 4 == 0:
                step += 1
                n = (n - 1)
                continue
                
            """
            i = 1 # 此時 n 為奇數
            while True:
                if (2 ** i) > n:
                    break
                i += 1

            if (2 ** i) - n >= n - (2 ** (i - 1)): # 找最近的 2 的指數
                n -= 1 # (2 ** (i - 1))
                step += 1 
            else:
                n += 1
                step += 1 
                print(n)
            """

            