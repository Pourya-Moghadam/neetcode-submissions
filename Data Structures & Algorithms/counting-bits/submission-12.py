class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]

        for number in range(1, n + 1):
            count = 0
            while number > 0:
                count += number & 1
                number = number >> 1
            res.append(count)
        
        return res