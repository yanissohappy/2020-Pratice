class Solution(object):
    def uniqueMorseRepresentations(self, words):
        _set = set()
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
                        
        for word in words:
            temp = ""
            for char in word:
                temp += alphabet[ord(char)-97]
            _set.add(temp)
        
        return len(_set)
        