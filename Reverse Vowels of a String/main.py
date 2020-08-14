class Solution(object):
    def reverseVowels(self, s):
        i = len(s) - 1
        reversed_vowel = ""
        while i >= 0:
            if s[i] in "AEIOUaeiou":
                reversed_vowel += s[i]
            i -= 1
        j = 0
        ret = ""
        for index, char in enumerate(s):
            if char in "AEIOUaeiou":
                ret += reversed_vowel[j]
                j += 1
            else:
                ret += s[index]
        return ret
            
                
        