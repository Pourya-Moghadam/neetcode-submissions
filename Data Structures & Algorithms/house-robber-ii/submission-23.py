class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        def solve(arr):
            n = len(arr)
            if n == 1:
                return arr[0]
            
            if n == 0:
                return 0
            
            dp = [arr[0], max(arr[0], arr[1])]
            for i in range(2, n):
                tmp = dp[1]
                dp[1] = max(dp[0] + arr[i], dp[1])
                dp[0] = tmp
            
            return dp[1]
        
        ans1 = solve(nums[:-1])
        ans2 = solve(nums[1:])

        return max(ans1, ans2)