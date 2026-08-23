class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            if i in cache:
                return cache[i]
            
            end = min(len(nums) - 1, nums[i] + i)
            if end == len(nums) - 1:
                return 1

            tmp = float("inf")
            for j in range(i + 1, end + 1):
                tmp = min(tmp, 1 + dfs(j))
            
            cache[i] = tmp
            return tmp
        
        return dfs(0)