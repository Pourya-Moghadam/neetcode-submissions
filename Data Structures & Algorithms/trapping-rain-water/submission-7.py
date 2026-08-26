class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL, maxR = [], [0] * n
        l, r = 0 , n - 1
        curL, curR = 0, 0

        while l < n:
            maxL.append(curL)
            curL = max(curL, height[l])
            l += 1

            maxR[r] = curR
            curR = max(curR, height[r])
            r -= 1
        
        res = []
        for i in range(n):
            res.append(min(maxL[i], maxR[i]))
        
        water = 0
        for i in range(n):
            water += max(0, res[i] - height[i])
        
        return water
