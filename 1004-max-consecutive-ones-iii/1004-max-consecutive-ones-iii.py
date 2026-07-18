class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        maxi=0
        zeros=0
        for r in range(len(nums)):
            if nums[r]==0:
                zeros +=1
            while zeros > k:
                if nums[left]==0:
                    zeros -=1
                left +=1
            maxi=max(maxi,r-left+1)
        return maxi