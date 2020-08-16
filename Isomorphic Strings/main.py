class Solution(object):
    def isIsomorphic(self, s, t):
        tuples = list(zip(s, t))
        set_tuples = set(tuples)
        set_s, set_t = [], []
        for item_s, item_t in set_tuples:
            set_s.append(item_s)
            set_t.append(item_t)
        return len(set_s) == len(set(s)) and len(set_t) == len(set(t))
