class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        l = 0

        for r in range(len(nums)):
            heapq.heappush_max(heap, (nums[r], r))
            if (r - l + 1) < k:
                continue
            
            while heap and heap[0][1] < l:
                heapq.heappop_max(heap)
            
            res.append(heap[0][0])
            l += 1
        
        return res

