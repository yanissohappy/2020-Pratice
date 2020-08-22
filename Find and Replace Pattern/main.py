from collections import defaultdict
class Solution(object):
    def checkDict(self, _dict):
        for key, value in _dict.items():
            _set = set()
            for val in value:
                _set.add(val)
                if len(_set) > 1:
                    return False
        return True
    def findAndReplacePattern(self, words, pattern):
        ret = []
        for word in words:
            if len(word) != len(pattern):
                continue
            _dict1, _dict2 = defaultdict(str), defaultdict(str)
            for pattern_char, word_char in zip(pattern, word):
                _dict1[pattern_char] += word_char
                _dict2[word_char] += pattern_char
            can_add = True
            can_add &= self.checkDict(_dict1)
            can_add &= self.checkDict(_dict2)               
                
            # another_dict = dict((value, key) for key, value in _dict.items())
            if can_add == True:
                ret.append(word)
            
        return ret