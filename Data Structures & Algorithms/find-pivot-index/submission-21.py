class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        curSum = 0
        totalSum = sum(nums)

        for i in range(n):
            rightSum = totalSum - curSum - nums[i]
            if rightSum == curSum:
                return i
            curSum += nums[i]
        return -1
