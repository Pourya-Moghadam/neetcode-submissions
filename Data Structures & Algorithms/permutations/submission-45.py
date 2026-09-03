class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return [[]]

        prem = self.permute(nums[1:])
        tmp = []
        for p in prem:
            for i in range(len(p) + 1):
                pCopy = p[:]
                pCopy.insert(i, nums[0])
                tmp.append(pCopy)
            
        return tmp

    