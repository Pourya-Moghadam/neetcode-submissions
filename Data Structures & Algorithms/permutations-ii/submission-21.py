class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = []
        path = []

        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for n in count:
                if count[n] > 0:
                    count[n] -= 1
                    path.append(n)
                    dfs()
                    path.pop()
                    count[n] += 1
        
        dfs()
        return res
