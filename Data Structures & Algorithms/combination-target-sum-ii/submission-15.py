class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(i, curSum):
            if curSum == target:
                res.append(path[:])
                return
            
            if i >= len(candidates) or curSum > target:
                return
            
            path.append(candidates[i])
            dfs(i + 1, curSum + candidates[i])

            while i <= len(candidates) - 2 and candidates[i] == candidates[i + 1]:
                i += 1
            
            path.pop()
            dfs(i + 1, curSum)
        
        dfs(0, 0)

        return res