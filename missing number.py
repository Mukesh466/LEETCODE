class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        tot=n*(n+1)//2
        return tot - sum(nums)
