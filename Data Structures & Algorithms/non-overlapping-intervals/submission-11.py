class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        intervals.sort()
        count = 0

        for i in intervals:
            if res and res[-1][1] > i[0]:
                res[-1] = [min(res[-1][0], i[0]), min(res[-1][1], i[1])]
                count += 1
            else:
                res.append(i)
        
        return count