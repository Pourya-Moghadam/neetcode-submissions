class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def dfs(i):
            if i >= len(s):
                return 1
            
            if s[i] == "0":
                return 0

            if i in cache:
                return cache[i]    

            res = 0
            if i <= len(s) - 1:
                res += dfs(i + 1)
            
            if i <= len(s) - 2:
                if s[i] == "1" or (s[i] == "2" and s[i + 1] < "7"):
                    res += dfs(i + 2)
            
            cache[i] = res
            return res

        return dfs(0)