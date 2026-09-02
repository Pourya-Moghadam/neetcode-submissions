class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        res = 0
        heap = [(0, 0)]
        shortest = {}
        while len(shortest) != len(points):
            d, p = heapq.heappop(heap)
            if p in shortest:
                continue
            shortest[p] = d
            res += d
            for nei in range(len(points)):
                if nei in shortest:
                    continue
                heapq.heappush(heap, (distance(p, nei), nei))

        return res
        