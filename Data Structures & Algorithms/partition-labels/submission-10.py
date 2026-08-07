class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        res = []
        for i in range(len(s)):
            count[s[i]] = i
        
        farthest = 0
        l = 0
        for i in range(len(s)):
            farthest = max(farthest, count[s[i]])
            if farthest == i:
                res.append(i - l + 1)
                l = i + 1
        
        return res

