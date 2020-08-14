class Solution(object):
    def reverseVowels(self, s):
        reversed_vowel = []
        reversed_vowel_index = []
        vowel = {'a', 'e', 'i' ,'o','u', 'A', 'E', 'I' , 'O', 'U'}
        for index, char in enumerate(s):
            if char in vowel:
                reversed_vowel_index.append(index)
                reversed_vowel.append(char)
        ret, i = list(s), 0
        
        while i < len(reversed_vowel_index):
            ret[reversed_vowel_index[i]] = reversed_vowel.pop()
            i += 1
        
        return ''.join(ret)
            
                
        