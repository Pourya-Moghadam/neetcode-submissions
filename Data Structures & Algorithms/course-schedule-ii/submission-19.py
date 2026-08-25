class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[pre].append(crs)
        
        visited = set()
        visiting = set()
        res = []

        def dfs(crs):
            if crs in visited:
                return True
            
            if crs in visiting:
                return False
            
            visiting.add(crs)
            for nei in preMap[crs]:
                if nei in visited:
                    continue
                
                if dfs(nei) == False:
                    return False
            
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        
        return res[::-1]