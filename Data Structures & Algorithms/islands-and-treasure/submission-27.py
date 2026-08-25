class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque()
        visited = set()
        m, n = len(grid), len(grid[0])

        def addCell(r, c, step):
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                (r, c) in visited or
                grid[r][c] != INF
            ):
                return
    
            q.append((r, c))
            grid[r][c] = step

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))

        distance = 0
        while q:
            distance += 1
            size = len(q)

            for i in range(size):
                r, c = q.popleft()
                if (r, c) in visited:
                    continue
                
                visited.add((r, c))
                addCell(r + 1, c, distance)
                addCell(r, c + 1, distance)
                addCell(r - 1, c, distance)
                addCell(r, c - 1, distance)
        


