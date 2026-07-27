class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                grid[r][c] == "0"
            ):
                return
            
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        
        return res