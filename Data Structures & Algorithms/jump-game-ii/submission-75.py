class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            end = min(nums[i] + i, n - 1)
            if end == n - 1:
                dp[i] = 1
            elif nums[i] == 0:
                continue
            else:
                dp[i] = 1 + min(dp[i + 1 : end + 1])

        return dp[0]