class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        actualsum=0
        n=len(nums)
        for i in nums:
            actualsum +=i
        summ=n*(n+1)//2
        return summ-actualsum