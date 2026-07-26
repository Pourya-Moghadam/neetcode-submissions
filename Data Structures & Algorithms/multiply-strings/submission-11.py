class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)

        for i in range(n2 - 1, -1, -1):
            for j in range(n1 - 1, -1, -1):
                position = i + j + 1
                tmp = (int(num2[i]) * int(num1[j])) + res[position]
                res[position] = tmp % 10
                res[position - 1] += tmp // 10
            
        ans = "".join(map(str, res)).lstrip("0")
        return ans if ans else "0"