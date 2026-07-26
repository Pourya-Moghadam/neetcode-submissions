class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        cache = {}

        def dfs(i, curSum):
            if curSum > target:
                return float("-inf")
            
            if curSum == target:
                return target
            
            if i >= len(stones):
                return curSum

            if (i, curSum) in cache:
                return cache[(i, curSum)]

            take = dfs(i + 1, curSum + stones[i])
            skip = dfs(i + 1, curSum)

            cache[(i, curSum)] = max(take, skip)
            return cache[(i, curSum)]
        
        return total - ( 2 * dfs(0, 0))