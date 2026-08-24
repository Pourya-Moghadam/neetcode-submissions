class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = [1 for _ in range(n)]
        
        for i in range(n - 2, -1, -1):
            tmp = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    tmp = max(tmp, 1 + res[j])
            
            res[i] = tmp
        
        return max(res)

