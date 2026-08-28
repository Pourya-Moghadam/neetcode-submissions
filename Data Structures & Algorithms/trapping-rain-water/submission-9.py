class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftM, rightM = [], [0] * n
        l, r = 0, n - 1
        curL, curR = 0, 0

        while l < n:
            curL = max(curL, height[l])
            leftM.append(curL)
            l += 1

            curR = max(curR, height[r])
            rightM[r] = curR
            r -= 1
        
        res = []
        for i in range(n):
            res.append(min(leftM[i], rightM[i]))
        

        water = 0
        for i in range(n):
            water += max(0, res[i] - height[i])
        
        return water
