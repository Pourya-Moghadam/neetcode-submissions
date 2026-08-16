class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        
        cost = 0
        heap = [(0, 0)] #dist, index
        visited = set()

        while len(visited) < len(points):
            d, p = heapq.heappop(heap)

            if p in visited:
                continue
                
            cost += d
            visited.add(p)

            for i in range(len(points)):
                if i not in visited:
                    heapq.heappush(heap, (manhattan(p, i), i))
            
        return cost
