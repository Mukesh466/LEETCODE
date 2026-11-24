class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        return nums[n//2]