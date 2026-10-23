class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 0
        prev = None
        res = 0

        while r < len(arr) - 1:

            if prev == "<" and arr[r] > arr[r + 1]:
                r += 1
                prev = ">"
                res = max(res, r - l + 1)
            
            elif prev == ">" and arr[r] < arr[r + 1]:
                r += 1
                prev = "<"
                res = max(res, r - l + 1)
            
            else:
                
                if arr[r] > arr[r + 1]:
                    prev = ">"
                    l = r
                    r += 1
                
                elif arr[r] < arr[r + 1]:
                    prev = "<"
                    l = r
                    r += 1
                
                else:
                    prev = None
                    r += 1
                    l = r
        res = max(res, r - l + 1)
        return res
