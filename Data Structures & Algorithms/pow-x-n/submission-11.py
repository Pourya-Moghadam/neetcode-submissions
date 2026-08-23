class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def recursive(x, n):
            if n == 0:
                return 1
            
            if n == 1:
                return x
            
            tmp = recursive(x, n // 2)

            if n % 2 == 0:
                return tmp * tmp
            
            else:
                return (tmp * tmp) * x
        
        ans = recursive(x, abs(n))

        if n < 0:
            return 1 / ans
        
        if n == 0:
            return 1
        
        return ans