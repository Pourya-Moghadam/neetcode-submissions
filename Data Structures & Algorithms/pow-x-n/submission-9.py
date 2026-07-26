class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def dfs(x, n):
            if x == 0:
                return 0
            
            if n == 0:
                return 1
            
            if n % 2 == 0:
                res = dfs(x, n // 2)
                return res * res
            
            else:
                res = dfs(x, n // 2)
                return x * res * res
            
        res = dfs(x, abs(n))

        if n < 0:
            return 1 / res
        
        return res