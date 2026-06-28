class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        index = 0
        for i in nums:
            index ^= i
        return index
#^= is xor operator(eg. if both num are same then it is 0 or it gives 1 as return) 
        
