class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x):
            return math.sqrt((x[0]**2) + (x[1]**2))
        

        maxHeap = []
        for p in points:
            heapq.heappush_max(maxHeap, (distance(p), p))
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        
        res = []
        for item in maxHeap:
            res.append(item[1])
        
        return res