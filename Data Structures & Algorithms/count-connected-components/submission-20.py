class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        visited = set()

        def dfs(node, par):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                dfs(nei, node)
            
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i, -1)
        
        return res