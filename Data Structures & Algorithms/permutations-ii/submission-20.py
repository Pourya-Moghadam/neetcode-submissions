class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        res = []
        path = []

        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return
        
            for i in counter:
                if counter[i] > 0:
                    path.append(i)
                    counter[i] -= 1
                    dfs()
                    counter[i] += 1
                    path.pop()
            
        
        dfs()

        return res