class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def dfs(i):
            if i >= len(s):
                return True

            if i in cache:
                return cache[i]    

            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    if dfs(i + len(w)):
                        return True

            cache[i] = False
            return False
        
        return dfs(0)