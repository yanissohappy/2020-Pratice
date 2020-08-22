from collections import defaultdict
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        ret = []
        for word in words:
            if len(set(word)) == len(set(pattern)) == len(set(zip(word, pattern))):
                ret.append(word)
        return ret