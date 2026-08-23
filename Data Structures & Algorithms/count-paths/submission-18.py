class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            
            if (r, c) in cache:
                return cache[(r, c)]

            if r >= m or c >= n:
                return 0
            
            right = dfs(r, c + 1)
            down = dfs(r + 1, c)
            cache[(r, c)] = right + down

            return right + down
        
        return dfs(0, 0)