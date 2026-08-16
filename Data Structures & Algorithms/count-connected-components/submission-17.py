class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        visited = set()

        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res