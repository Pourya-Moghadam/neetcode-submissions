class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (h, i)
        res = 0

        for i, h in enumerate(heights):
            start = i

            while stack and h < stack[-1][0]:
                height, index = stack.pop()
                res = max(res, (i - index) * height)
                start = index

            stack.append((h, start))
        
        for h, i in stack:
            res = max(res, (len(heights) - i) * h)
        return res