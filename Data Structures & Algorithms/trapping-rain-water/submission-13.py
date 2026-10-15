class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        curL, curR = 0, 0

        for i in range(1, len(height)):
            curL = max(curL, height[i - 1])
            leftMax[i] = curL
        
        for j in range(len(height) - 2, -1, -1):
            curR = max(curR, height[j + 1])
            rightMax[j] = curR
        
        res = 0
        for i in range(len(height)):
            res += max(0, min(leftMax[i], rightMax[i]) - height[i])
        
        return res
        

        

