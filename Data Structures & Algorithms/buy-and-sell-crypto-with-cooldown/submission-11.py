class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(buying, i):
            if i >= len(prices):
                return 0

            if (buying, i) in cache:
                return cache[(buying, i)]    

            cooldown = dfs(buying, i + 1)
            if buying:
                buy = dfs(not buying, i + 1) - prices[i]
                cache[(buying, i)] = max(cooldown, buy)
                return max(cooldown, buy)

            if not buying:
                sell = dfs(not buying, i + 2) + prices[i]
                cache[(buying, i)] = max(cooldown, sell)
                return max(cooldown, sell)
            
        return dfs(True, 0)