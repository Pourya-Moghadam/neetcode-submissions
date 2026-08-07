class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        curSum, res = 0, 0

        for n in nums:
            curSum += n
            diff = curSum - k
            if diff in prefix:
                res += prefix[diff]
            
            prefix[curSum] = 1 + prefix.get(curSum, 0)

        
        return res
