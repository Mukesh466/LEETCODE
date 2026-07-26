class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        index=0
        for i in nums:
            index ^= i
        return index

        