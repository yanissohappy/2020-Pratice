class Solution(object):
    def recursive(self, grid, i, j, m, n):
        if 0 <= i < m and 0 <= j < n:
            if grid[i][j] == 1:
                grid[i][j] = 0 # if reached, set 0 in order to avoid repeatedly computing
                return 1 + self.recursive(grid, i + 1, j, m, n) + self.recursive(grid, i - 1, j, m, n) + self.recursive(grid, i, j + 1, m, n) + self.recursive(grid, i, j - 1, m, n)
        return 0
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        _max = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                else: # == 1
                    _max = max(_max, self.recursive(grid, i, j, m, n))
        return _max