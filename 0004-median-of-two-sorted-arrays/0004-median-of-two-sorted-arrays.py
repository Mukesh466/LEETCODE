class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1=nums1+nums2
        nums1.sort()
        left,right=0,len(nums1)-1
        while left < right:
            left +=1
            right -=1
        if left == right:
            return nums1[left]*1.0
        else:
            res=nums1[left]+nums1[right]
            res*= 1.0
            return res/2
        