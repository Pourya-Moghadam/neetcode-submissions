class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            tmp = 0
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    tmp = max(tmp, dp[j])
            dp[i] = tmp + 1
        
        return max(dp)