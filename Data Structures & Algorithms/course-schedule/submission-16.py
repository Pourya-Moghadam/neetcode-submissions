class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visiting = set()
        visited = set()

        def dfs(crs):
            if crs in visited:
                return True
            
            if crs in visiting:
                return False
            
            visiting.add(crs)

            for nei in adj[crs]:
                if dfs(nei) == False:
                    return False
            
            visiting.remove(crs)
            visited.add(crs)

            return True
        
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        
        return True