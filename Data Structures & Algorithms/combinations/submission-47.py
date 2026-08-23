class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):
            if len(path) == k:
                res.append(path[:])
                return
            
            if i > n:
                return
            
            path.append(i)
            dfs(i + 1)
            path.pop()
            dfs(i + 1)
        
        dfs(1)
        return res