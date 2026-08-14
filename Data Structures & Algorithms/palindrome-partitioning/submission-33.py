class Solution:
    def isPal(self,s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(s):
            if not s:
                res.append(path[:])
                return
            
            for i in range(len(s)):
                if self.isPal(s, 0, i):
                    path.append(s[:i + 1])
                    dfs(s[i + 1:])
                    path.pop()
            
        dfs(s)

        return res
            

