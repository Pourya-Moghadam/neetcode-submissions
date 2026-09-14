class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, curSum):            
            if i == len(nums):
                if curSum == target:
                    return 1
                return 0
            
            if (i, curSum) in cache:
                return cache[(i, curSum)]

            add = dfs(i + 1, curSum + nums[i])
            subtract = dfs(i + 1, curSum - nums[i])
            cache[(i, curSum)] = add + subtract

            return add + subtract
        
        return dfs(0, 0)