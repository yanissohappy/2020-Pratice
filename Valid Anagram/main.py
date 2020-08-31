class Solution(object):
    def isAnagram(self, s, t):
        alphabet = {}
        for i, j in zip(range(1,27), "abcdefghijklmnopqrstuvwxyz"):
            alphabet[j] = 0
        for i in s:
            alphabet[i] += 1
        for i in t:
            alphabet[i] -= 1
        
        for i in alphabet:
            if alphabet[i] != 0:
                return False
        return True        