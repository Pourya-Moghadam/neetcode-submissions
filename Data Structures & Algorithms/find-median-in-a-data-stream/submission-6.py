class MedianFinder:

    def __init__(self):
        self.minH, self.maxH = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.maxH, num)

        while self.minH and self.maxH and self.maxH[0] > self.minH[0]:
            val = heapq.heappop_max(self.maxH)
            heapq.heappush(self.minH, val)

        while len(self.minH) > len(self.maxH) + 1:
            val = heapq.heappop(self.minH)
            heapq.heappush_max(self.maxH, val)
        
        while len(self.maxH) > len(self.minH) + 1:
            val = heapq.heappop_max(self.maxH)
            heapq.heappush(self.minH, val)
        
    def findMedian(self) -> float:
        if len(self.minH) > len(self.maxH):
            return self.minH[0]
        
        if len(self.maxH) > len(self.minH):
            return self.maxH[0]
        
        return (self.maxH[0] + self.minH[0]) / 2
        