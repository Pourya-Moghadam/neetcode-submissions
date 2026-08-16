class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [float("-inf"), float("-inf"), float("-inf")]

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            res = [max(t[0], res[0]), max(t[1], res[1]), max(t[2], res[2])]    

        return res == target
