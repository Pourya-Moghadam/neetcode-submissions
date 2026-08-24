class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            hour = 0
            for p in piles:
                hour += math.ceil(p / k)
                if hour > h:
                    return False
            
            return True
        
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2

            if check(m):
                r = m
            
            else:
                l = m + 1
        
        return l
