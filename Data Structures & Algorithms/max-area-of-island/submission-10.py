class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                grid[r][c] != 1
            ):
                return 0
            
            visited.add((r, c))
            res = 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)

            return res
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited:
                    res = max(res, dfs(r, c))
        
        return res
