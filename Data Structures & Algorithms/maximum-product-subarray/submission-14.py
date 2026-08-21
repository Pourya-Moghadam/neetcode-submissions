class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxN, minN = 1, 1
        res = float("-inf")

        for n in nums:
            tmp = maxN * n
            maxN = max(maxN * n, minN * n, n)
            minN = min(tmp, minN * n, n)
            res = max(res, maxN)
        
        return res