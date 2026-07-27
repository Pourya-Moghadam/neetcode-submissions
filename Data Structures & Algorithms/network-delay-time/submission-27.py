class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest = {}
        adj = defaultdict(list)
        for s, d, t in times:
            adj[s].append([d, t])
        
        minH = [(0, k)]

        while minH:
            t, node = heapq.heappop(minH)
            
            if node in shortest:
                continue
            
            shortest[node] = t

            for nei, t2 in adj[node]:
                if nei not in shortest:
                    heapq.heappush(minH, (t + t2, nei))
        
        return max(shortest.values()) if len(shortest) == n else -1