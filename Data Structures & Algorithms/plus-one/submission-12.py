class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        res = [0] * (n + 1)
        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            val = total % 10
            carry = total // 10
            res[i + 1] = val
        
        res[0] = carry
        if res[0] == 0:
            res = res[1:]
        return res