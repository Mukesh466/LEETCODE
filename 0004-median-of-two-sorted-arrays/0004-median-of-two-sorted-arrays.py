class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        merge.sort()
        tot=len(merge)
        if tot % 2 == 1:
            return float(merge[tot//2])
        else:
            mid1=merge[tot//2 -1]
            mid2=merge[tot//2]
            return (float(mid1)+float(mid2)) / 2.0