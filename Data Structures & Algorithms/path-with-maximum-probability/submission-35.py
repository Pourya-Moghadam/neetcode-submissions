class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for (s, d), p in zip(edges, succProb):
            adj[s].append((d, p))
            adj[d].append((s, p))

        shortest = {}
        maxH = [(1, start_node)]

        while maxH:
            prob1, n1 = heapq.heappop_max(maxH)
            if n1 in shortest:
                continue
            
            shortest[n1] = prob1
            
            for n2, prob2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush_max(maxH, (prob1 * prob2, n2))
            
        if end_node not in shortest:
            return 0
        
        return shortest[end_node]
