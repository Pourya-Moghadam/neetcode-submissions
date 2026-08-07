class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        curSum = 0
        res = 0

        for r in range(len(arr)):
            curSum += arr[r]
            if r - l + 1 != k:
                continue
            
            if curSum / k >= threshold:
                res += 1
            
            curSum -= arr[l]
            l += 1

        return res