class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close, path):
            if open == close == n:
                res.append(path)
                return
            
            if open < close or open > n or close > n:
                return
            
            else:
                dfs(open + 1, close, path + "(")
                dfs(open, close + 1, path + ")")
            
            
        dfs(0, 0, "")

        return res