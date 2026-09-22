class Solution:
    def reverse(self, x: int) -> int:
        org = x
        x = abs(x)
        res = int(str(x)[::-1])

        if res > (2 ** 31) - 1 or res < -(2 ** 31):
            return 0
        
        return res if org > 0 else -res