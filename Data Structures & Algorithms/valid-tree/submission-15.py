class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        visited = set()

        def dfs(node, par):
            if node in visited:
                return False
            
            visited.add(node)

            for nei in adj[node]:
                if nei == par:
                    continue
                
                if dfs(nei, node) == False:
                    return False
                
            return True
        
        return dfs(0, -1) and len(visited) == n and len(edges) == n - 1