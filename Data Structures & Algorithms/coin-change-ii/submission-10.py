class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, curSum):
            if curSum > amount:
                return 0
            
            if curSum == amount:
                return 1
            
            if i >= len(coins):
                return 0
            
            if (i, curSum) in cache:
                return cache[(i, curSum)]

            take = dfs(i, curSum + coins[i])
            skip = dfs(i + 1, curSum)
            cache[(i, curSum)] = take + skip

            return take + skip
        
        return dfs(0, 0)