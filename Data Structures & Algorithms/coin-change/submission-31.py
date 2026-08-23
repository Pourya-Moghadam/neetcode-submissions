class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(i, curSum):

            if curSum == amount:
                return 0
            
            if curSum > amount or i >= len(coins):
                return float("inf")
            
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            
            take = 1 + dfs(i, curSum + coins[i])
            skip = dfs(i + 1, curSum)
            cache[(i, curSum)] = min(take, skip)

            return cache[(i, curSum)]
        
        ans = dfs(0, 0)
        return ans if ans != float("inf") else -1
