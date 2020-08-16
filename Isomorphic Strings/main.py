class Solution(object):
    def isIsomorphic(self, s, t):
        tuples = list(zip(s, t))
        set_tuples = set(tuples)
        set_s = []
        for item, _ in set_tuples:
            set_s.append(item)
        return len(set_s) == len(set(s))