class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxH = list(count.values())
        heapq.heapify_max(maxH)
        q = deque()
        time = 0

        while maxH or q:
            time += 1
            if maxH:
                task = heapq.heappop_max(maxH)
                if task - 1 > 0:
                    q.append((task - 1, time + n))
                
            if q:
                if q[0][1] <= time:
                    task2, time2 = q.popleft()
                    heapq.heappush_max(maxH, task2)
            
        
        return time

