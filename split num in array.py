class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            s=str(num)
            for ch in s:
                res.append(int(ch))
        return res
        
