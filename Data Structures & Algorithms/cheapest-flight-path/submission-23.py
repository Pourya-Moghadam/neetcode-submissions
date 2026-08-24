class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        shortest = {i: float("inf") for i in range(n)}
        shortest[src] = 0

        for i in range(k + 1):
            tmp = shortest.copy()

            for s, d, p in flights:
                if shortest[s] == float("inf"):
                    continue
                
                if shortest[s] + p < tmp[d]:
                    tmp[d] = shortest[s] + p
            
            shortest = tmp
        
        return shortest[dst] if shortest[dst] != float("inf") else -1