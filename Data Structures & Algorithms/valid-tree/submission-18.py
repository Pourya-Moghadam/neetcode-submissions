class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        visited = set()

        def dfs(i, par):
            if i in visited:
                return False
            
            visited.add(i)
            for nei in adj[i]:
                if nei == par:
                    continue
                
                if dfs(nei, i) == False:
                    return False
                
            return True
        
        dfs(0, -1)

        if len(visited) == n and len(edges) == n - 1:
            return True
        
        return False