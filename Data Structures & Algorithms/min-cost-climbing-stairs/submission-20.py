class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        
        if len(cost) == 1:
            return cost[0]
        
        dp = [0, 0]

        for i in range(2, len(cost) + 1):
            tmp = dp[1]
            dp[1] = min(dp[0] + cost[i - 2], dp[1] + cost[i - 1])
            dp[0] = tmp
        
        return dp[1]