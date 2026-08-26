class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        count = len(nums1) + len(nums2)
        res = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            
            else:
                res.append(nums2[j])
                j += 1
        
        if i < len(nums1):
            res += nums1[i:]
        
        if j < len(nums2):
            res += nums2[j:]
        
        if count % 2 == 0:
            m = count // 2
            median = (res[m - 1] + res[m]) / 2
            return median
        
        else:
            m = count // 2
            return res[m]
