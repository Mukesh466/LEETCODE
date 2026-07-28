class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start=0
        zero=-1
        max_length=0
        for i in range(len(nums)):
            if nums[i]==0:
                start = zero+1
                zero = i
            max_length=max(max_length,i-start)
        return max_length