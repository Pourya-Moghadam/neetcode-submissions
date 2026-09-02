class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i, n in enumerate(nums):
            heapq.heappush_max(heap, (n, i))
            if i >= k - 1:
                while heap and heap[0][1] <= i - k:
                    heapq.heappop_max(heap)
                res.append(heap[0][0])
        return res