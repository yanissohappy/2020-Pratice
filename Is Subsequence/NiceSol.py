from collections import defaultdict
class Solution(object):
	def isSubsequence(self, s, t):
		idx = defaultdict(list)
		for i, c in enumerate(t):
			idx[c].append(i)
		prev = 0
		for i, c in enumerate(s):            
			j = bi.bisect_left(idx[c], prev)
			if j == len(idx[c]): return False
			prev = idx[c][j] + 1
		return True     