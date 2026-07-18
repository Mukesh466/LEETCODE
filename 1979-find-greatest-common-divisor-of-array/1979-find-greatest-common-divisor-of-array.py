class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small=min(nums)
        large=max(nums)
        while large !=0:
            small,large=large,small % large
        return small