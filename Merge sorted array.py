class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1.sort()
      #append the value of nums2 to nums1's 0 values and then sorting it in nums1 so array can be sorted

