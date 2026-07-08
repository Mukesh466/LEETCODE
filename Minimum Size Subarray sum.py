class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        mini=float("inf")
        subsum=0
        for right in range(len(nums)):
            subsum += nums[right]
            while subsum >= target:
                mini=min(mini,right-left+1)
                subsum -= nums[left]
                left += 1
            right += 1
        return mini if mini != float("inf") else 0
