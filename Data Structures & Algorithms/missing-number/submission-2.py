class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxN = len(nums)
        total = maxN * (maxN + 1) / 2
        return int(total - sum(nums))