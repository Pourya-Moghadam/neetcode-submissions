class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}

        def solve(i, j):
            if i >= len(s1) and j >= len(s2):
                return True

            if (i, j) in cache:
                return cache[(i, j)]    

            if i < len(s1) and s1[i] == s3[i + j]:
                if solve(i + 1, j):
                    return True

            if j < len(s2) and s2[j] == s3[i + j]:
                if solve(i, j + 1):
                    return True
            cache[(i, j)] = False
            return False

        return solve(0, 0)