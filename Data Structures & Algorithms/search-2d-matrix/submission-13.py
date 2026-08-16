class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, (len(matrix) * len(matrix[0])) - 1

        while l <= r:
            m = (l + r) // 2
            mid = matrix[m//COLS][m%COLS]
            if target  == mid:
                return True
            
            elif target > mid:
                l = m + 1
            
            else:
                r = m - 1
        
        return False