class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num=set(nums)
        if len(num)==len(nums):
            return False
        else:
            return True