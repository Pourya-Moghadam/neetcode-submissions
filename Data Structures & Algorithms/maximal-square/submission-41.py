class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def dfs(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                matrix[r][c] == "0"
            ):
                cache[(r, c)] = 0
                return 0
            
            if (r, c) in cache:
                return cache[(r, c)]

            right = dfs(r, c + 1)
            down = dfs(r + 1, c)
            diag = dfs(r + 1, c + 1)

            cache[(r, c)] = 1 + min(right, down, diag)
            return cache[(r, c)]
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
        
        return max(cache.values()) ** 2

        