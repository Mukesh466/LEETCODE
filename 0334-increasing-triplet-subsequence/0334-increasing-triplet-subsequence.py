class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        i=j=float('inf')
        for num in nums:
            if num <= i:
                i=num
            elif num <=j:
                j=num
            else:
                return True
        return False