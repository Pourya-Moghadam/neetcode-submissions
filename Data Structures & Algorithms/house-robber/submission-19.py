class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])

        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, n):
            tmp = dp[1]
            dp[1] = max(dp[0] + nums[i], dp[1])
            dp[0] = tmp
        
        return dp[1]