class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        ones = [0] * n
        ones[-1] = 1
        res = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            tmp = res[i + 1] + digits[i] + ones[i]
            res[i + 1] = tmp % 10
            res[i] = tmp // 10
        
        if res[0] == 0:
            return res[1:]
        
        return res
