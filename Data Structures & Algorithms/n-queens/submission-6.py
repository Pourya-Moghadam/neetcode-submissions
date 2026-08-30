class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posD, negD = set(), set(), set()
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        
        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r + c) in posD or (r - c) in negD:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                posD.add(r + c)
                negD.add(r - c)

                dfs(r + 1)

                cols.remove(c)
                posD.remove(r + c)
                negD.remove(r - c)
                board[r][c] = "."
            
        dfs(0)

        return res