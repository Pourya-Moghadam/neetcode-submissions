class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}

        def dfs(i, curSum):
            
            if i >= len(profit):
                return 0
            
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            
            skip = dfs(i + 1, curSum)

            take = 0
            if weight[i] + curSum <= capacity:
                take = profit[i] + dfs(i + 1, curSum + weight[i])

            cache[(i, curSum)] = max(take, skip)
            return cache[(i, curSum)]
        
        return dfs(0, 0)