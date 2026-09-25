class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = {}
        index = 0
        heap = []

        for q in sorted(queries):
            while index <= len(intervals) - 1 and intervals[index][0] <= q:
                heapq.heappush(heap, (intervals[index][1] - intervals[index][0] + 1, intervals[index][1]))
                index += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            res[q] = heap[0][0] if heap else -1

        return [res[q] for q in queries]
