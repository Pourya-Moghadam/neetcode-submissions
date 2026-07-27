class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        visited = set()
        cycle = set()
        cycleStart = -1

        def dfs(i, par):
            nonlocal cycleStart

            if i in visited:
                cycleStart = i
                return True
            
            visited.add(i)

            for nei in adj[i]:
                if nei == par:
                    continue
                
                if dfs(nei, i):
                    cycle.add(i)

                    if i == cycleStart:
                        return False
                    
                    return True
                
            return False
        
        dfs(1, -1)

        for s, d in reversed(edges):
            if s in cycle and d in cycle:
                return [s, d]
