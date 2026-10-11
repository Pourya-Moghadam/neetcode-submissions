class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0 for _ in range(capacity + 1)] for _ in range(len(profit))]    

        for i in range(capacity + 1):
            if weight[0] <= i:
                dp[0][i] = profit[0]
        

        for item in range(len(profit)):
            for cap in range(capacity + 1):
                if weight[item] <= cap:
                    dp[item][cap] = max(profit[item] + dp[item - 1][cap - weight[item]], dp[item - 1][cap])
                else:
                    dp[item][cap] = dp[item - 1][cap]
        

        return dp[-1][-1]