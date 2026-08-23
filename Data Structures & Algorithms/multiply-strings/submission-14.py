class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        l1 = len(num1)
        l2 = len(num2)
        l3 = l1 + l2
        res = [0] * l3

        for i in range(l1 - 1, -1, -1):
            carry = 0
            n1 = ord(num1[i]) - ord("0")
            for j in range(l2 - 1, -1, -1):
                n2 = ord(num2[j]) - ord("0")
                total = (n1 * n2) + res[i + j + 1]
                val = total % 10
                carry = total // 10
                res[i + j + 1] = val
                res[i + j] += carry
        
        ans = "".join(map(str, res)).lstrip("0")
        return ans if ans else "0"